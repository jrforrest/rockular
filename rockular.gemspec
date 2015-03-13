Gem::Specification.new do |s|
  s.name = "rockular"
  s.version = "0.0.1"
  s.author = "Jack Forrest"
  s.email = "jack@jrforrest.net"
  s.homepage = "https://github.com/jrforrest/rockular"
  s.files = Dir["{bin,lib}/**/*"]
  s.description = "Image correctness verification for tests"
  s.summary = "Provides some MiniTest assertions for checking "\
    "image correctness during image processing tests"
  s.license = 'WTFPL'

  s.require_paths = ['lib']
  
  s.add_dependency('phashion', '~> 1')
  s.add_development_dependency('rake', '~> 10')
  s.add_development_dependency('minitest', '~> 5')
  s.add_development_dependency('pry', '~> 0.10')
end
