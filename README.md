# BaseHangul

[![PyPI Version](https://badge.fury.io/py/basehangul.svg)](http://badge.fury.io/py/basehangul)
[![Build Status](https://travis-ci.org/ssut/basehangul.svg?branch=master)](https://travis-ci.org/ssut/basehangul)

Human-readable binary encoding, [BaseHangul](https://github.com/koreapyj/basehangul) for Python.

BaseHangul is an binary encoder using hangul. You can see [the specification](http://api.dcmys.jp/basehangul/) of it.

## Installation

To install it just run pip as usual:

``` sh
$ pip install basehangul
```

## Usage

``` python
import basehangul

basehangul.encode('This is an encoded string')
# => '넥라똔먈늴멥갯놓궂뗐밸뮤뉴뗐뀄굡덜멂똑뚤'

basehangul.decode(u'넥라똔먈늴멥갯놓궂뗐밸뮤뉴뗐뀄굡덜멂똑뚤')
# => 'This is an encoded string'
```

## Testing

For running the tests, you need the standard unittest module, shipped with Python.

To run them, use either py.test, unittest or trial.

To run the tests:

```sh
$ nosetests
```

## Contributing

1. Fork it (https://github.com/ssut/basehangul/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request

## License

Copyright &copy; SuHun Han. See [LICENSE.txt](LICENSE.txt) for further details.
