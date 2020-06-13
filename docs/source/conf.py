import os
import sys

import _building

sys.path.insert(0, os.path.abspath('../..'))


(project,
 pkg,
 release,
 author,
 copyright,

 extensions,
 templates_path,
 exclude_patterns,
 master_doc,
 html_theme,
 html_static_path,
 ) = _building.sphinx_confs("this-package")
