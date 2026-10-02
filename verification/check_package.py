"""Static archive, source-text, and documentation checks; no MATLAB execution."""
from pathlib import Path
import hashlib
import json
import re
import zipfile
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
WORD = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'

def main():
    manifest = json.loads((ROOT/'verification/original-file-manifest.json').read_text(encoding='utf-8'))
    for item in manifest:
        data = (ROOT/item['file']).read_bytes()
        assert len(data) == item['bytes'], item['file']
        assert hashlib.sha256(data).hexdigest() == item['sha256'], item['file']
    models = json.loads((ROOT/'verification/model-inventory.json').read_text(encoding='utf-8'))
    xml_count = 0
    for item in models:
        with zipfile.ZipFile(ROOT/item['file']) as z:
            assert z.testzip() is None
            for name in z.namelist():
                if name.endswith('.xml'):
                    ET.fromstring(z.read(name))
                    xml_count += 1
            metadata = ET.fromstring(z.read('metadata/mwcoreProperties.xml'))
            releases = [n.text for n in metadata.iter() if n.tag.rsplit('}',1)[-1]=='matlabRelease']
            assert releases == [item['release']]
            configs = [ET.fromstring(z.read(name)) for name in z.namelist() if re.match(r'simulink/configSet\d*\.xml$', name)]
            assert configs
            settings = {p.get('Name'):p.text for c in configs for p in c.iter('P')}
            for field in ['StartTime','StopTime','SolverName','RelTol']:
                assert settings[field] == item['configuration'][field]
    folder = ROOT/'homeworks/hw-06/matlab'
    with zipfile.ZipFile(folder/'HW6.mlx') as z:
        assert z.testzip() is None
        doc = ET.fromstring(z.read('matlab/document.xml'))
    code = []
    for p in doc.iter(WORD+'p'):
        style = p.find('.//'+WORD+'pStyle')
        if style is not None and style.get(WORD+'val')=='code':
            text = ''.join(n.text or '' for n in p.iter(WORD+'t'))
            if text.strip():code.append(text)
    provenance = json.loads((folder/'export-provenance.json').read_text())
    assert len(code) == provenance['code_cell_count']
    assert [hashlib.sha256(c.encode()).hexdigest() for c in code] == provenance['code_cell_sha256']
    exported = (folder/'HW6_code_export.m').read_text(encoding='utf-8')
    position = 0
    for cell in code:
        found = exported.find(cell,position)
        assert found >= 0, 'Code section changed or missing from export'
        position = found+len(cell)
    links = 0
    for p in ROOT.rglob('*.md'):
        for target in re.findall(r'!?\[[^\]]*\]\(([^)]+)\)',p.read_text(encoding='utf-8')):
            if '://' in target or target.startswith('#'):continue
            assert (p.parent/target.split('#')[0]).exists(), f'Broken link: {p.relative_to(ROOT)} -> {target}'
            links += 1
    print(json.dumps({'preserved_file_copies_verified':len(manifest),'simulink_archives_checked':len(models),
                      'simulink_xml_documents_parsed':xml_count,'live_script_code_sections_verified':len(code),
                      'local_markdown_links_checked':links,'scope':'Static packaging checks, not MATLAB simulation'},indent=2))

if __name__ == '__main__':
    main()
