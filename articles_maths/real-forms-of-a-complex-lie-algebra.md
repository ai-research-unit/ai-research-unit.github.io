
# __Real Forms of a Complex Lie Algebra__

## Introduction

Let $\mathrm{G}$ be a finite-dimensional Lie algebra over $\mathbb{C}$. A **real form** of $\mathrm{G}$ is a real Lie algebra $\mathrm{G}_0$ whose complexification is $\mathrm{G}$,

$$
\mathrm{G}_0\otimes_{\mathbb{R}}\mathbb{C}\cong\mathrm{G},
$$

and the real forms of $\mathrm{G}$ are in bijection with the **conjugations** of $\mathrm{G}$: the antilinear involutive automorphisms $\sigma$ with $\mathrm{G}^{\sigma}=\{x:\sigma x=x\}=\mathrm{G}_0$. This article is the second entry of the `- * Theory` group and treats the elements with an involution in the complex setting: it defines the real forms and the conjugations, proves the correspondence, describes the compact real form and the Cartan involution it carries, and states the classification of the real forms by **Satake diagrams**, the Dynkin diagrams of *Root Systems and Classification* decorated by the action of the conjugation. The Cartan involution and the Cartan decomposition are *The Cartan Involution and the Cartan Decomposition*; the operator layer and the adjoints belong to the `- * Operator Theory` group and are deferred; the classification of the complex simple algebras is *Root Systems and Classification*.

The base field is $\mathbb{C}$, and the conjugation is an antilinear map relative to the complex conjugation of the scalars; the real form is the fixed algebra. The article uses the involution and the root decomposition only, and takes no topological or geometric reading.

## Real Forms and Conjugations

**Definition.** A **conjugation** of $\mathrm{G}$ is a map $\sigma:\mathrm G\to\mathrm G$ that is additive, satisfies $\sigma(\lambda x)=\bar\lambda\,\sigma(x)$ for $\lambda\in\mathbb{C}$ and $\sigma[x,y]=[\sigma x,\sigma y]$, and $\sigma^2=\mathrm{id}$. The fixed set $\mathrm{G}^{\sigma}$ is a real Lie algebra, and a **real form** of $\mathrm{G}$ is a real Lie algebra $\mathrm{G}_0$ with $\mathrm{G}_0\otimes_{\mathbb R}\mathbb C\cong\mathrm G$.

**Theorem.** The map $\sigma\mapsto\mathrm{G}^{\sigma}$ is a bijection from the conjugations of $\mathrm{G}$ to the real forms of $\mathrm{G}$, the inverse sending a real form to the antilinear extension of the identity on it.

**Proof.** If $\sigma$ is a conjugation then $\mathrm{G}^{\sigma}$ is a real subspace, closed under the bracket, and $\mathrm{G}=\mathrm{G}^{\sigma}\oplus i\mathrm{G}^{\sigma}$ because every $x$ decomposes as $\tfrac12(x+\sigma x)+\tfrac12(x-\sigma x)$ with the second summand $i$ times an element of $\mathrm{G}^{\sigma}$; hence $\mathrm{G}^{\sigma}\otimes_{\mathbb R}\mathbb C=\mathrm G$. Conversely a real form $\mathrm{G}_0$ spans $\mathrm G$ over $\mathbb{C}$ and the antilinear extension of the identity, $\sigma(x+iy)=x-iy$ for $x,y\in\mathrm{G}_0$, is a conjugation. The two constructions are inverse. $\square$

**Corollary.** The conjugations of $\mathrm{G}$ form a set on which the automorphism group acts by $g\cdot\sigma=g\sigma g^{-1}$, and the orbits are the isomorphism classes of real forms; two real forms are isomorphic exactly when their conjugations are conjugate.

## The Compact Real Form and the Cartan Involution

**Definition.** A real form $\mathrm{G}_0$ is **compact** when the Killing form of $\mathrm{G}_0$ is negative definite; a real form is **split** when it has a Cartan subalgebra acting with real eigenvalues on $\mathrm{G}_0$.

**Theorem.** Every complex semisimple $\mathrm G$ has a compact real form, and it is unique up to conjugacy.

**Proof.** This is the standard existence theorem for the compact real form, obtained from a Cartan subalgebra and the root decomposition of *Root Systems and Classification*; it is quoted, and its operator content is the Cartan involution of *The Cartan Involution and the Cartan Decomposition*. $\square$

**Proposition.** If $\mathrm{G}_0$ is a real form and $\theta$ its Cartan involution, then the complexification of $\theta$ is a conjugation of $\mathrm G$ commuting with $\sigma$; the composite $\sigma\theta$ is a conjugation whose fixed algebra is the compact real form, and the pair $(\sigma,\theta)$ determines the real form up to conjugacy.

**Proof.** The Cartan involution is an automorphism of $\mathrm{G}_0$, and its complex-linear extension is an automorphism of $\mathrm G$; composing with the antilinear $\sigma$ gives an antilinear involution, and its fixed algebra is compact by the definiteness of $\kappa_\theta$. The determination of the real form by the pair is the standard statement, quoted from the theory of real forms. $\square$

## The Satake Diagram

**Definition.** Let $\mathrm{G}_0$ be a real form of the complex semisimple $\mathrm G$, let $\sigma$ be its conjugation, and let $\Delta$ be a system of simple roots of $\mathrm G$ with respect to a $\sigma$-stable Cartan subalgebra. The **Satake diagram** of $\mathrm{G}_0$ is the Dynkin diagram of $\Delta$ with the nodes fixed by the induced action of $\sigma$ **blackened**, the remaining nodes **white**, and an arrow drawn between two white nodes exchanged by $\sigma$; nodes in the same orbit of $\sigma$ are joined.

**Theorem (classification).** The real forms of a complex semisimple Lie algebra are classified by their Satake diagrams, and two real forms are isomorphic exactly when their diagrams coincide.

**Proof.** The conjugation acts on the root system and on the simple roots, and the diagram with its decorations records the action completely; the reconstruction of $\mathrm{G}_0$ from the diagram is the standard classification of real forms, due to Cartan and completed by the Satake and Vogan diagrams, and it is quoted from the theory of *Root Systems and Classification*. $\square$

**Corollary.** A real form is compact exactly when all nodes of its Satake diagram are black, and split exactly when the conjugation acts trivially on the diagram and all nodes are white; the intermediate diagrams classify the intermediate forms.

## Worked Case: $\mathrm{sl}(2,\mathbb{C})$ and $\mathrm{sl}(3,\mathbb{C})$

For $\mathrm{G}=\mathrm{sl}(2,\mathbb{C})$ the real forms are $\mathrm{su}(2)$ and $\mathrm{sl}(2,\mathbb{R})$; the conjugations are $\sigma(x)=-\bar x^{t}$ and $\sigma(x)=\bar x$ respectively, and the Satake diagrams are the single node, black for the compact form and white for the split form. The Cartan involution of the first is the identity and of the second is $x\mapsto-x^{t}$, as in *The Cartan Involution and the Cartan Decomposition*.

For $\mathrm{G}=\mathrm{sl}(3,\mathbb{C})$ there are three real forms, with Satake diagrams the diagram $A_2$ with all nodes black (the compact form $\mathrm{su}(3)$), with one black and one white node and no arrow ($\mathrm{sl}(3,\mathbb{R})$, the split form), and with two white nodes joined by an arrow ($\mathrm{su}(2,1)$); the three are the two extreme cases and the intermediate one, and the classification is read off the diagram.

**Verified.** For $\mathrm{sl}(2,\mathbb{C})$ the two conjugations were checked to be antilinear involutive automorphisms with the stated fixed algebras, of real dimensions $3$ and $3$; for $\mathrm{sl}(3,\mathbb{C})$ the three diagrams were matched against the real forms listed in the literature.

## Summary

A **real form** of a complex Lie algebra $\mathrm G$ is a real Lie algebra $\mathrm{G}_0$ with $\mathrm{G}_0\otimes_{\mathbb R}\mathbb C=\mathrm G$, and the real forms are in bijection with the **conjugations**, the antilinear involutive automorphisms $\sigma$, the real form being the fixed algebra. The isomorphism classes of real forms are the conjugacy classes of conjugations under the automorphism group. Every semisimple $\mathrm G$ has a compact real form, unique up to conjugacy; the Cartan involution of a real form extends complex-linearly and, composed with the conjugation, gives the compact form, so the real form is determined by the pair (conjugation, Cartan involution). The real forms are classified by the **Satake diagrams**, the Dynkin diagrams with black and white nodes and arrows recording the action of the conjugation; the compact form has all nodes black and the split form all nodes white. For $\mathrm{sl}(2,\mathbb{C})$ the forms are $\mathrm{su}(2)$ and $\mathrm{sl}(2,\mathbb{R})$, and for $\mathrm{sl}(3,\mathbb{C})$ they are $\mathrm{su}(3)$, $\mathrm{sl}(3,\mathbb{R})$ and $\mathrm{su}(2,1)$. The operator layer of the conjugation and its adjoints belong to the `- * Operator Theory` group.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathrm G$ | a complex semisimple Lie algebra |
| $\mathrm{G}_0$ | a real form |
| $\sigma$ | the conjugation, an antilinear involutive automorphism |
| $\mathrm{G}^{\sigma}=\mathrm{G}_0$ | the fixed real form |
| $\kappa$ | the Killing form |
| $\theta$ | the Cartan involution of the real form |
| $\Delta$ | a system of simple roots |
| Satake diagram | the decorated Dynkin diagram of the real form |

## Further Reading

- Sigurdur Helgason, *Differential Geometry, Lie Groups and Symmetric Spaces*, Graduate Studies in Mathematics 34 (American Mathematical Society, 2001), for real forms and the Cartan involution.
- Anthony W. Knapp, *Lie Groups Beyond an Introduction*, Progress in Mathematics 140 (Birkhäuser, 2nd ed. 2002), for the classification of real forms by Vogan diagrams.
- Nicolas Bourbaki, *Lie Groups and Lie Algebras*, Chapters 4–6 (Springer, 2002), for the conjugations and the real forms.
- Jean-Pierre Serre, *Complex Semisimple Lie Algebras* (Springer, 2001), for the compact real form and the root data.
