import type { Plugin } from 'unified';
import type { Root, Element, Text } from 'hast';
import { visit } from 'unist-util-visit';

const CALLOUT_TYPES = ['pros', 'cons', 'eco'] as const;
type CalloutType = typeof CALLOUT_TYPES[number];

function getCalloutType(node: Element): CalloutType | null {
  const firstChild = node.children[0];
  if (!firstChild || firstChild.type !== 'element') return null;

  const para = firstChild as Element;
  if (para.tagName !== 'p') return null;

  const textNode = para.children[0];
  if (!textNode || textNode.type !== 'text') return null;

  const text = (textNode as Text).value.trim();
  for (const type of CALLOUT_TYPES) {
    if (text === `[!${type}]`) return type;
  }
  return null;
}

export const rehypeCallouts: Plugin<[], Root> = () => {
  return (tree: Root) => {
    visit(tree, 'element', (node: Element, index, parent) => {
      if (node.tagName !== 'blockquote') return;
      if (index === undefined || !parent) return;

      const calloutType = getCalloutType(node);
      if (!calloutType) return;

      const remainingChildren = node.children.slice(1);

      const replacement: Element = {
        type: 'element',
        tagName: 'div',
        properties: { className: [`callout-${calloutType}`] },
        children: remainingChildren,
      };

      parent.children.splice(index, 1, replacement);
    });
  };
};
