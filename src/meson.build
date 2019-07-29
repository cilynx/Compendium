compendium_sources = [
  'main.vala',
  'window.vala',
  'tabs/finance.vala',
  'tabs/house.vala',
  'tabs/pool.vala',
  'tabs/vehicle.vala',
  'tabs/wishlist.vala',
]

compendium_deps = [
  dependency('gio-2.0', version: '>= 2.50'),
  dependency('gtk+-3.0', version: '>= 3.22'),
]

gnome = import('gnome')

compendium_sources += gnome.compile_resources('compendium-resources',
  'compendium.gresource.xml',
  c_name: 'compendium'
)

executable('compendium', compendium_sources,
  vala_args: '--target-glib=2.50',  dependencies: compendium_deps,
  install: true,
)
