pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'compendium')
gnome = import('gnome')

gnome.compile_resources('compendium',
  'compendium.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

conf = configuration_data()
conf.set('PYTHON', python.find_installation().path())
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'compendium.in',
  output: 'compendium',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

compendium_sources = [
  '__init__.py',
  'main.py',
  'window.py',
  'finance/finance_tab.py',
  'finance/account.py'
]

install_data(compendium_sources, install_dir: moduledir)
