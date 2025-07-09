def standard_args(arg):
    print(arg)

def pos_only_arg(arg,/): # no matter what , respect the position , don't use params
    print(arg)

def kwd_only_arg(*,arg): # explicitly call arg as a keyword to reach  it
    print(arg)

def combined_exemple(pos_only,/,standard,*,kwd_only):
    print(pos_only,standard,kwd_only)

standard_args('ahh')
combined_exemple('joe',4,kwd_only='toto')