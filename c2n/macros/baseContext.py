
import c2n.dsl

def dealWithComponent(anReMatch) :
  if not anReMatch : return
  subContextPath = anReMatch.group(1)
  c2n.dsl.parse(subContextPath+'.tex')

c2n.dsl.registerMacro(
  'component',
  '\\\\component\s+(\S+)\s*',
  dealWithComponent
)