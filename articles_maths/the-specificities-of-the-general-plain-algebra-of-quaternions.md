# __The Specificities of the General Plain Algebra__

## Introduction

This article collects what singles out the general plain product among the six products of the quaternion space, and with it the classes of element that an associative division algebra makes empty. The empty classes are folded here on purpose: the quaternion chapter has no article on the zero divisors, none on the nilpotents and none on the idempotents, because over the plain product there is nothing in those classes but $0$ and $e_0$, and the folding is the content of the first two sections. The remaining sections give the centre, the tensor products, the Frobenius theorem and the isolation of the block among the six. The product itself is defined in *Introduction to the General Plain Algebra of Quaternions*, above this article in this category; the norm and the invertibility criterion are *Norm and Invertibility in the General Plain Algebra*, above this article in this category; the ideal-theoretic reading of the same facts is *Ideals and Simplicity of the General Plain Algebra*, below this article in this category; and the six products are owned by *The 6 Products of the Quaternion Real Space* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category, and are cited here rather than derived.

## The Classes of Element

**Theorem (the folded classes).** Over the plain product the classes of element are

| Class | Condition | Set in $\mathbb{H}$ |
|---|---|---|
| zero divisors | $\tilde p\tilde q=0$, both non-zero | none |
| non-zero nilpotents | $\tilde a^2=0$, $\tilde a\neq0$ | none |
| idempotents | $\tilde a^2=\tilde a$ | $\{0,e_0\}$ |
| roots of $-1$ | $\tilde\xi^2=-e_0$ | the unit sphere of the vector subspace $V$, a two-dimensional family |
| roots of $+1$ | $\tilde\xi^2=e_0$ | $\{\pm e_0\}$ |
| roots of $0$ | $\tilde\xi^2=0$ | $\{0\}$ |

*Proof.* Every non-zero element is invertible by *Norm and Invertibility in the General Plain Algebra*, above this article in this category, with $\tilde q^{-1}=\tilde q^{\natural}/\tilde q\tilde q^{\natural}$; a vanishing product with a non-zero factor therefore forces the other factor to vanish, so there is no zero divisor, and a non-zero nilpotent would be a zero divisor with itself. For the idempotents, $\tilde a(\tilde a-e_0)=0$ forces $\tilde a=0$ or $\tilde a=e_0$. The three root sets are the cases $q_0=-1,0,1$ of the classification of *Square Roots of a General Element in the General Plain Algebra*, above this article in this category.

**Remark (the contrast with the biquaternion case).** The same three classes are non-empty over the complex coefficient field: the biquaternion plain product has the null cone as its zero-divisor set, non-zero nilpotents in the isotropic cone of the vector part, and the idempotent pair $\tfrac12(e_0\pm e_3i)$ of its Peirce decomposition. The three empty rows above are exactly the three classes whose article slots the quaternion chapter has pruned, and the pruned slots are the difference between the quaternion and the biquaternion chapter. The biquaternion facts are owned by the biquaternion chapter and are cited for the contrast alone.

## Associativity, the Unit and the Division Property

The three properties that isolate the block are:

- **Associativity**, $(\tilde p\tilde q)\tilde r=\tilde p(\tilde q\tilde r)$, proved on the generators $e_1,e_2$ in *Introduction to the General Plain Algebra of Quaternions*, above this article in this category;
- the **two-sided unit** $e_0$, $e_0\tilde q=\tilde qe_0=\tilde q$;
- the **division property**, every non-zero element invertible, equivalently the equation $\tilde a\tilde x=\tilde b$ uniquely solvable for $\tilde x$ whenever $\tilde a\neq0$.

**Theorem.** Of the six products of the quaternion space, the general plain product is the only one that is associative with a two-sided unit, and the only one with the division property.

*Proof.* The other five are read off from *The 6 Products of the Quaternion Real Space* and *The 6 Algebraic Structures over the Quaternion $\mathbb{R}$ Space*, above this article in this category: the general quaternionic product has the unit on the left alone and is not associative; the symmetric plain product is commutative and unital but not associative; the antisymmetric plain product is alternating, hence has no unit and every element is square-zero; the symmetric quaternionic product is scalar valued and has no unit; the antisymmetric quaternionic product is alternating and fails the Jacobi identity. No property is re-derived here.

**Corollary.** The division property fails for each of the other five: in the symmetric plain product two pure quaternions that anticommute multiply to $0$, and every element of each of the two antisymmetric products is square-zero; the quaternionic and the symmetric quaternionic products have no two-sided unit at all, so the equation $\tilde a\tilde x=\tilde b$ is not the equation of a multiplication by $a$ with a two-sided identity.

## The Centre

**Theorem.** The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}e_0$, and the centre of the group of units is $\mathbb{R}^{\times}e_0$.

*Proof.* Commuting with $e_1$ and with $e_2$ forces the vector part to vanish; the scalars commute. For the units, an element commuting with every quaternion lies in the centre, and a non-zero scalar is a unit.

The centrality of the scalar line is what makes $N(\tilde q)$ a scalar and what makes the polar split of the units a direct product; both readings are in *Norm and Invertibility in the General Plain Algebra*, above this article in this category.

## Tensor Products and the Complexification

**Theorem.** For the tensor products of $\mathbb{H}$ with the complex field and with its own opposite algebra,

$$
\mathbb{H}\otimes_\mathbb{R}\mathbb{C}\cong M_2(\mathbb{C}),\qquad \mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}\cong \operatorname{End}_\mathbb{R}(\mathbb{H})\cong M_4(\mathbb{R}).
$$

*Proof.* The first is the complexification of the algebra, treated in *The Complexification and the Effect of the Change of Scalars on the Quaternions*, above this article in this category. For the second, the sandwich map $\tilde p\otimes\tilde q^{\mathrm{op}}\mapsto(\tilde r\mapsto\tilde p\tilde r\tilde q)$ is an $\mathbb{R}$-algebra homomorphism of a $16$-dimensional algebra onto $\operatorname{End}_\mathbb{R}(\mathbb{H})$, of dimension $16$; it is injective because $\mathbb{H}$ is central simple over $\mathbb{R}$, and the enveloping algebra and the operator basis are *The Enveloping Operator Algebra of the General Plain Algebra and the Bi-module Structure*, below this article in this category.

Thus the algebra is a division algebra over $\mathbb{R}$ and becomes a full matrix algebra as soon as the scalars are extended to $\mathbb{C}$: the two tensor products display the split case as the complexification of the division case.

## The Frobenius Theorem and the Real Division Algebras

**Theorem (Frobenius).** Every finite-dimensional associative division algebra over $\mathbb{R}$ is isomorphic to $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$.

*Proof.* Quoted as standard; the proof belongs to the structure theory of real algebras and is not reproduced here. The dimension count is $1,2,4$, and $\mathbb{H}$ is the largest-dimensional associative one.

**Theorem (Hurwitz).** Every finite-dimensional real composition algebra is isomorphic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or the octonions; in dimensions $1,2,4,8$.

*Proof.* Quoted as standard. The two theorems are cited, not proved, and they are the reason the quaternion algebra is a distinguished rung: it is the top of the associative part of both classifications.

## The Isolation among the Six

The six products are generated from two seeds, the plain product $\tilde p\tilde q$ and the twisted product $\tilde p^{\natural}\tilde q$, taken with the three combinators of a bilinear form, the form itself, its symmetric part and its antisymmetric part. The two seeds and the three combinators give

| Product | Formula | Character |
|---|---|---|
| general plain | $\tilde p\tilde q$ | associative, two-sided unit $e_0$, division |
| general quaternionic | $\tilde p^{\natural}\tilde q$ | non-associative, left unit only, no division |
| symmetric plain | $\tfrac12(\tilde p\tilde q+\tilde q\tilde p)$ | commutative, unital, Jordan, not associative, zero divisors |
| antisymmetric plain | $\tfrac12(\tilde p\tilde q-\tilde q\tilde p)$ | alternating, Lie, no unit |
| symmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q+\tilde q^{\natural}\tilde p)$ | commutative, scalar valued, no unit |
| antisymmetric quaternionic | $\tfrac12(\tilde p^{\natural}\tilde q-\tilde q^{\natural}\tilde p)$ | alternating, Jacobi fails, no unit |

Only the first row carries the associative-unital theory, and it carries all of it: the division property, the two-sided unit, the simplicity, the free module category and the enveloping algebra. Over $\mathbb{R}$ the bar is the identity and the star coincides with the natural sign, so of the two slot operations only the natural one is available, and the six products above are all the products the block has. The conjugation in the first slot is the operation that the complex coefficient field splits into a conjugation and an involution; over $\mathbb{R}$ no such split exists, and this is the sense in which the block is one rung below the biquaternion one.

## Summary

The plain product is the only one of the six products of the quaternion space that is associative with a two-sided unit and has the division property; every non-zero quaternion is invertible. Consequently the zero divisors, the non-zero nilpotents and the nontrivial idempotents are all absent, and the classes of element reduce to the table: no zero divisor, no non-zero nilpotent, idempotents $0$ and $e_0$, roots of $-1$ the unit sphere of the vector subspace, roots of $+1$ the pair $\pm e_0$, roots of $0$ the origin. The centre is the scalar line $\mathbb{R}e_0$; the complexification is $M_2(\mathbb{C})$ and the enveloping algebra is $M_4(\mathbb{R})$; by Frobenius the algebra is one of the three real associative division algebras, and by Hurwitz one of the four real composition algebras.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, the block's division algebra |
| $e_0$ | Two-sided unit |
| $V=\mathbb{R}e_1+\mathbb{R}e_2+\mathbb{R}e_3$ | Vector subspace |
| $\mathbb{H}^{\mathrm{op}}$ | Opposite algebra |
| $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{op}}$ | Enveloping algebra, $\cong M_4(\mathbb{R})$ |
| $M_2(\mathbb{C})$ | Complexification $\mathbb{H}\otimes_\mathbb{R}\mathbb{C}$ |

## Further Reading

- Ferdinand Georg Frobenius, "Über lineare Substitutionen und bilineare Formen", *Journal für die reine und angewandte Mathematik* **84** (1878) 1–63, for the classification of the real associative division algebras.
- Adolf Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variablen", *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1898) 309–316, for the composition algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the centre, the tensor products and the structure theory.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the four real composition algebras and their classes of element.
