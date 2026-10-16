p = '/home/hp/Documents/1_Doc/Projects/ai-research/ai-research-unit/articles_maths/the-specificities-of-the-quaternion-algebra.md'
t = open(p, encoding='utf-8').read()

# 1. introduction
i = t.index('This article collects what singles out')
j = t.index('\n', i)
new_intro = ("This article collects what is specific to the quaternion algebra among the algebras the space "
             "$\\mathbb{R}^4$ carries, and with it the classes of element that an associative division algebra "
             "makes empty. Those classes are read in the first section. The remaining sections give the centre, the "
             "tensor products, the Frobenius theorem and the place of $\\mathbb{H}$ among the real division "
             "algebras. The product itself is defined in *Introduction to the Quaternion Algebra*, above this "
             "article in this category; the norm and the invertibility criterion are *Norm and Invertibility in the "
             "Quaternion Algebra*, above this article in this category; the ideal-theoretic reading of the same "
             "facts is *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category; and "
             "the four element-theory articles *Zero Divisors of the Quaternion Algebra*, *Annihilators of the "
             "Quaternion Algebra*, *Square Roots of One and the Idempotents of the Quaternion Algebra*, *Square "
             "Roots of Zero and the Nilpotents of the Quaternion Algebra* and *Square Roots of a General Element in "
             "the Quaternion Algebra*, above this article in this category, carry the classes in full. The "
             "companion products the same space carries belong to the *Quaternioid Algebraic Structures* category "
             "and are cited there rather than here.")
t = t[:i] + new_intro + t[j:]

# 2. the comparative theorem block
i = t.index('**Theorem.** Of the six products')
j = t.index('## The Centre', i)
new_block = ("**Theorem.** The quaternion product is the only product the space $\\mathbb{R}^4$ carries that is "
             "associative with a two-sided unit, and the only one with the division property. The companion "
             "products, and the reading of these properties on each of them, are the subject of the *Quaternioid "
             "Algebraic Structures* category; no companion product is re-derived here.\n\n")
t = t[:i] + new_block + t[j:]

# 3. drop the isolation section
i = t.index('## The Isolation among the Six')
j = t.index('## Summary', i)
t = t[:i] + t[j:]

# 4. summary sentence
t = t.replace('The quaternion product is the only one of the six products of the quaternion space that is associative',
              'The quaternion product is the only product the space carries that is associative') \
     .replace('The plain product is the only one of the six products of the quaternion space that is associative',
              'The quaternion product is the only product the space carries that is associative')
open(p, 'w', encoding='utf-8').write(t)
print('ok')
