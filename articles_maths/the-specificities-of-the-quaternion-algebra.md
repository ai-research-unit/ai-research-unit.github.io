# __The Specificities of the Quaternion Algebra__

## Introduction

This article collects what is specific to the quaternion algebra among the algebras the space $\mathbb{R}^4$ carries, and with it the classes of element that an associative division algebra makes empty. Those classes are read in the first section. The remaining sections give the centre, the tensor products, the Frobenius theorem and the place of $\mathbb{H}$ among the real division algebras. The product itself is defined in *Introduction to the Quaternion Algebra*, above this article in this category; the norm and the invertibility criterion are *Norm and Invertibility in the Quaternion Algebra*, above this article in this category; the ideal-theoretic reading of the same facts is *Ideals and Simplicity of the Quaternion Algebra*, below this article in this category; and the four element-theory articles *Zero Divisors of the Quaternion Algebra*, *Annihilators of the Quaternion Algebra*, *Square Roots of One and the Idempotents of the Quaternion Algebra*, *Square Roots of Zero and the Nilpotents of the Quaternion Algebra* and *Square Roots of a General Element in the Quaternion Algebra*, above this article in this category, carry the classes in full.

## The Classes of Element

**Theorem (the folded classes).** Over the quaternion product the classes of element are

| Class | Condition | Set in $\mathbb{H}$ |
|---|---|---|
| zero divisors | $\tilde q_1\tilde q_2=0$, both non-zero | none |
| non-zero nilpotents | $\tilde q^2=0$, $\tilde q\neq0$ | none |
| idempotents | $\tilde q^2=\tilde q$ | $\{0,e_t\}$ |
| roots of $-1$ | $\tilde\xi^2=-e_t$ | the unit sphere of the vector subspace $V$, a two-dimensional family |
| roots of $+1$ | $\tilde\xi^2=e_t$ | $\{\pm e_t\}$ |
| roots of $0$ | $\tilde\xi^2=0$ | $\{0\}$ |

*Proof.* Every non-zero element is invertible by *Norm and Invertibility in the Quaternion Algebra*, above this article in this category, with $\tilde q^{-1}=\tilde q^{\natural}/\tilde q\tilde q^{\natural}$; a vanishing product with a non-zero factor therefore forces the other factor to vanish, so there is no zero divisor, and a non-zero nilpotent would be a zero divisor with itself. For the idempotents, $\tilde q(\tilde q-e_t)=0$ forces $\tilde q=0$ or $\tilde q=e_t$. The three root sets are the cases $q_t=-1,0,1$ of the classification of *Square Roots of a General Element in the Quaternion Algebra*, above this article in this category.

## Associativity, the Unit and the Division Property

The three properties that isolate the block are:

- **Associativity**, $(\tilde q_1\tilde q_2)\tilde q_3=\tilde q_1(\tilde q_2\tilde q_3)$, proved on the generators $\vec e_x,\vec e_y$ in *Introduction to the Quaternion Algebra*, above this article in this category;
- the **two-sided unit** $e_t$, $e_t\tilde q=\tilde qe_t=\tilde q$;
- the **division property**, every non-zero element invertible, equivalently the equation $\tilde q_1\tilde q_2=\tilde q_3$ uniquely solvable for $\tilde q_2$ whenever $\tilde q_1\neq0$.

**Theorem.** The quaternion product is associative with a two-sided unit and has the division property.

## The Centre

**Theorem.** The centre of $\mathbb{H}$ is the scalar line $\mathbb{R}e_t$, and the centre of the group of units is $\mathbb{R}^{\times}e_t$.

*Proof.* Commuting with $\vec e_x$ and with $\vec e_y$ forces the vector part to vanish; the scalars commute. For the units, an element commuting with every quaternion lies in the centre, and a non-zero scalar is a unit.

The centrality of the scalar line is what makes $\langle\tilde q\rangle_{\natural}$ a scalar and what makes the polar split of the units a direct product; both readings are in *Norm and Invertibility in the Quaternion Algebra*, above this article in this category.

## The Tensor Product with the Opposite Algebra

**Theorem.** For the tensor product of $\mathbb{H}$ with its own opposite algebra,

$$
\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{opp}}\cong \operatorname{End}_\mathbb{R}(\mathbb{H})\cong M_4(\mathbb{R}).
$$

*Proof.* The sandwich map $\tilde q_1\otimes\tilde q_2^{\mathrm{opp}}\mapsto(\tilde q_3\mapsto\tilde q_1\tilde q_3\tilde q_2)$ is an $\mathbb{R}$-algebra homomorphism of a $16$-dimensional algebra onto $\operatorname{End}_\mathbb{R}(\mathbb{H})$, of dimension $16$; it is injective because $\mathbb{H}$ is central simple over $\mathbb{R}$, and the enveloping algebra and the operator basis are *The Enveloping Operator Algebra of the Quaternion Algebra and the Bi-module Structure*, below this article in this category.

Thus the algebra is a division algebra over $\mathbb{R}$ and its enveloping tensor product is the full endomorphism algebra.

## The Frobenius Theorem and the Real Division Algebras

**Theorem (Frobenius).** Every finite-dimensional associative division algebra over $\mathbb{R}$ is isomorphic to $\mathbb{R}$, $\mathbb{C}$ or $\mathbb{H}$.

*Proof.* Quoted as standard; the proof belongs to the structure theory of real algebras and is not reproduced here. The dimension count is $1,2,4$, and $\mathbb{H}$ is the largest-dimensional associative one.

**Theorem (Hurwitz).** Every finite-dimensional real composition algebra is isomorphic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{H}$ or the octonions; in dimensions $1,2,4,8$.

*Proof.* Quoted as standard. The two theorems are cited, not proved, and they are the reason the quaternion algebra is a distinguished rung: it is the top of the associative part of both classifications.

## Summary

The quaternion product is the only product the space carries that is associative with a two-sided unit and has the division property; every non-zero quaternion is invertible. Consequently the zero divisors, the non-zero nilpotents and the nontrivial idempotents are all absent, and the classes of element reduce to the table: no zero divisor, no non-zero nilpotent, idempotents $0$ and $e_t$, roots of $-1$ the unit sphere of the vector subspace, roots of $+1$ the pair $\pm e_t$, roots of $0$ the origin. The centre is the scalar line $\mathbb{R}e_t$; the enveloping algebra is $M_4(\mathbb{R})$; by Frobenius the algebra is one of the three real associative division algebras, and by Hurwitz one of the four real composition algebras.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}$ | The quaternion algebra, the block's division algebra |
| $e_t$ | Two-sided unit |
| $V=\mathbb{R}\vec e_x+\mathbb{R}\vec e_y+\mathbb{R}\vec e_z$ | Vector subspace |
| $\mathbb{H}^{\mathrm{opp}}$ | Opposite algebra |
| $\mathbb{H}^{\mathrm{e}}=\mathbb{H}\otimes_\mathbb{R}\mathbb{H}^{\mathrm{opp}}$ | Enveloping algebra, $\cong M_4(\mathbb{R})$ |

## Further Reading

- Ferdinand Georg Frobenius, "Über lineare Substitutionen und bilineare Formen", *Journal für die reine und angewandte Mathematik* **84** (1878) 1–63, for the classification of the real associative division algebras.
- Adolf Hurwitz, "Über die Composition der quadratischen Formen von beliebig vielen Variablen", *Nachrichten von der Königlichen Gesellschaft der Wissenschaften zu Göttingen* (1898) 309–316, for the composition algebras.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for the centre, the tensor products and the structure theory.
- John H. Conway and Derek A. Smith, *On Quaternions and Octonions* (A K Peters, 2003), for the four real composition algebras and their classes of element.
