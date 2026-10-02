function open_homework(number)
%OPEN_HOMEWORK Open one preserved homework model without running it.
% From the repository folder: addpath('scripts'); open_homework(1)
    validateattributes(number, {'numeric'}, {'scalar', 'integer', '>=', 1, '<=', 6});
    repository_root = fileparts(fileparts(mfilename('fullpath')));
    names = {'Adaptive', 'HW2', 'HW3', 'HW4', 'HW5', 'HW6'};
    model_file = fullfile(repository_root, 'homeworks', sprintf('hw-%02d', number), ...
                          'matlab', [names{number} '.slx']);
    if ~isfile(model_file)
        error('open_homework:MissingModel', 'Model file is missing: %s', model_file);
    end
    open_system(model_file);
end
