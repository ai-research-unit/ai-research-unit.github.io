# __The Hermitian Modules and the Hyperbolic Witt Group over the Split-Complex Ring__

## Introduction

A Hermitian module over the split-complex ring is a pair of real vector spaces with a pairing between them, and every non-degenerate such module is hyperbolic. That is the classification, and it is a short one: the isometry class is a single integer, the realified signature is always balanced, and the Witt group is trivial. This article proves the three statements and separates the true count from the count the product structure suggests.

The claim is that the naive answer is wrong. Since $\mathbb{C}_{\mathrm{spl}}=\mathbb{R}\times\mathbb{R}$, the guess is that a Hermitian module is a pair of real Hermitian modules and that the Witt group is $\mathbb{Z}\oplus\mathbb{Z}$, one copy for each idempotent. **The guess fails**, and the reason is one line: the conjugation exchanges the two components. A form's two components are therefore transposes of one another and cannot be chosen independently, so a form is one real matrix rather than two, and its isometry class is its rank.

The involution is *The Involutions, the Subspaces and the Idempotent Lines of the Split-Complex Space*; the modules are *Modules over the Split-Complex Ring*; the rank-one case is the form $H$ of *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*; the general theory of forms over a ring with involution is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*, and the metabolic case there is the special case proved here.

## The Hermitian Modules

### The Definition

**Definition.** A **Hermitian module** over $(\mathbb{C}_{\mathrm{spl}},\bar\cdot)$ is a finitely generated module $M$ with a map $\Phi:M\times M\to\mathbb{C}_{\mathrm{spl}}$, linear in the first slot, conjugate-linear in the second, with $\Phi(x,y)=\overline{\Phi(y,x)}$.

The form $H(A,C)=A\bar C$ on the ring as a module over itself is the basic example, and it is the one of *The Two Forms and the Two Algebraic Norms of the Split-Complex Space*.

### The Conjugation Exchanges the Two Components

**Proposition.** $\overline{\Pi_+}=\Pi_-$ and $\overline{\Pi_-}=\Pi_+$; the conjugation exchanges the two components of every element, $Q_+\mapsto Q_-$.

**Proof.** $\bar j=-j$, so $\overline{\Pi_+}=\tfrac12(1-j)=\Pi_-$, and the conjugation is $\mathbb{R}$-linear and involutive.

So the conjugation is not the identity on either component and does not act inside a component: it is the exchange. This is the fact that decides everything below, and it is where the product structure of the ring stops being a product of two independent halves.

### A Module Is a Pair and a Form Is a Pairing

**Theorem.** A Hermitian form on $M=(V_+,V_-)$ is a real bilinear pairing $\beta:V_+\times V_-\to\mathbb{R}$, its two components being

$$
\Phi_+(x,y)=x_+^{\mathsf T}\beta\, y_-, \qquad \Phi_-(x,y)=x_-^{\mathsf T}\beta^{\mathsf T}y_+ .
$$

**Proof.** Write the form as a pair of real-valued forms, $\Phi=(\Phi_+,\Phi_-)$. Conjugate-linearity in the second slot with the scalar $\lambda\Pi_+$ gives $\Phi(x,\lambda\Pi_+y)=(0,\lambda\Phi_-(x,y))$, so $\Phi_+$ vanishes on the $+$-component of its second argument and pairs $V_+$ with $V_-$; the conjugate-symmetry $\Phi_+(x,y)=\Phi_-(y,x)$ identifies $\Phi_-$ as the transpose.

The form is therefore not a pair of forms on the two components but a single pairing between them. The description "a pair of real forms" names the pair $(\beta,\beta^{\mathsf T})$, and the two members of that pair are one datum.

## The Form as One Real Matrix

### The Two Components Are Transposes

A consequence of the proposition is that a Hermitian form has no freedom at the second component once the first is fixed. The pair $(\Phi_+,\Phi_-)$ is $(\beta,\beta^{\mathsf T})$, and a signature of one is a signature of the other. The two components of an isometry act on the two sides of $\beta$, so the isometry class of the form is the equivalence class of $\beta$ under

$$
\beta\ \longmapsto\ P_+^{\mathsf T}\beta\,P_-, \qquad P_\pm\ \text{real and invertible},
$$

the two-sided equivalence of real matrices.

### The Classification by Rank

**Theorem.** Two Hermitian forms on free modules are isometric exactly when their pairings have the same rank. In particular every non-degenerate form of rank $n$ is isometric to the standard one, $\beta=I_n$.

**Proof.** Two real matrices are two-sidedly equivalent exactly when they have the same rank, by row and column reduction; and the isometry condition is exactly the two-sided equivalence displayed.

The classification of the Hermitian modules over the split ring is therefore by one integer per module, the rank of the pairing, and the modules with a non-degenerate form are those with $\dim V_+=\dim V_-=n$ and $\beta$ invertible.

### Why the Pair of Signs Collapses

Over a field the classification is by the signature, an integer, and over a product of two fields with the identity involution it would be by a pair of integers. Here it is by one integer and not by a pair, because the two components are transposes and a transpose has the same rank. The pair of signs that the product structure suggests is a pair $(s,s)$ of equal entries at best, and even that is not an invariant, since a form of rank $n$ may be carried to any form of rank $n$.

## The Signature

### The Realified Signature

**Theorem.** Regard $M$ as a real vector space of dimension $2n$ and $\operatorname{Re}\Phi$ as a real symmetric form. Its signature is $(n,n)$ for every non-degenerate form.

**Proof.** Each component is totally isotropic, since $V_+$ pairs with $V_-$ and not with itself, and both have dimension $n$. A non-degenerate real form on a space of dimension $2n$ with two complementary totally isotropic subspaces of dimension $n$ is hyperbolic, so its signature is $(n,n)$.

**Corollary.** No non-degenerate Hermitian form over $\mathbb{C}_{\mathrm{spl}}$ is definite, and every one is hyperbolic in the sense of admitting a Lagrangian submodule of half the dimension.

This is the module-level form of the statement of *The Hermitian Form, the Double Cone and the Reversed Cauchy-Schwarz Inequality*: the form on the free module of rank one has signature $(1,1)$ and the two null lines are its two Lagrangians.

### The Refutation of the Pair of Signs

| | the naive count | the true count |
|---|---|---|
| the invariant | a pair $(s_+,s_-)$ of signatures | the rank $n$ |
| the realified signature | $(p_+,q_+;p_-,q_-)$ independent | always $(n,n)$ |
| the Witt group | $\mathbb{Z}\oplus\mathbb{Z}$ | $0$ |

The naive column is what a product of two fields with the identity involution gives. The true column is what the exchange involution gives, and the exchange is forced: the conjugation of the algebra is $j\mapsto-j$, and it swaps the idempotents. A form over $\mathbb{C}_{\mathrm{spl}}$ does not see two independent real forms; it sees one real matrix.

## The Hyperbolic Forms

### The Standard Form Is Metabolic

**Theorem.** The standard form on the free module of rank one, $\Phi(A,C)=A\bar C$, is metabolic: the submodule $S_+=\mathbb{R}\Pi_+$ is totally isotropic and of real dimension one, half of the dimension two.

**Proof.** $H(\lambda\Pi_+,\mu\Pi_+)=\lambda\mu\Pi_+\Pi_-=0$, so $S_+$ is totally isotropic, and its real dimension is one, which is half of $2$.

A **metabolic** form is one with a totally isotropic submodule of half the dimension; a **hyperbolic** form is one isometric to a sum of the standard forms. By the classification the two notions coincide here, and every non-degenerate form is hyperbolic.

### Every Form Is a Sum of Standard Ones

**Theorem.** Every non-degenerate Hermitian module of rank $n$ is isometric to the orthogonal sum of $n$ copies of the standard form.

**Proof.** $\beta=I_n$ is the orthogonal sum of $n$ copies of $\beta=(1)$, and the classification carries every non-degenerate $\beta$ to $I_n$.

So the monoid of isometry classes of non-degenerate Hermitian modules is the monoid $\mathbb{N}$ of ranks, and its addition is the addition of integers.

## The Witt Group

### The Grothendieck Group

The Witt group is the Grothendieck group of the monoid of isometry classes of non-degenerate forms under orthogonal sum, with the metabolic forms set to zero. Two forms are equal in the Witt group when each becomes isometric to the other after the addition of a suitable metabolic form.

**Theorem.** The Witt group of $(\mathbb{C}_{\mathrm{spl}},\bar\cdot)$ is trivial.

**Proof.** Every class is $n\cdot[\,\langle1\rangle\,]$ by the previous section, and $\langle1\rangle$ is metabolic, so its class is zero; hence every class is zero.

The triviality is the extreme case of the Witt cancellation: the metabolic forms are all the forms, so the cancellation has nothing left to distinguish. The statement is not that forms are uninteresting but that the form alone carries no information beyond the rank, and the rank is killed by the metabolic identification.

### What the Trivial Group Says

Three statements are equivalent for non-degenerate Hermitian modules over the split ring: they are all hyperbolic, their classes in the Witt group all vanish, and the signature invariant is trivial. The three are the module-level shadow of the two isotropic lines of the form: the lines are the Lagrangian of every form, and a form with a Lagrangian carries no Witt class.

## The Comparison with the Complex Case

### The Single $\mathbb{Z}$ There

Over $\mathbb{C}$ with its conjugation the Hermitian forms are classified by the signature $(p,q)$ and the Witt group is $\mathbb{Z}$, by $p-q$. Every form has a diagonal form with $p$ ones and $q$ minus ones, the metabolic forms are the ones with $p=q$, and the anisotropic residue is the definite part.

### The Two Collapses

Over $\mathbb{C}_{\mathrm{spl}}$ the same computation gives no residue: the minus signs can be absorbed, because a form of rank $n$ is isometric to the standard one whatever its realified signature looked like in a particular basis. The complex field keeps a signature because its conjugation is not an exchange of two components; the split ring loses it because its conjugation is exactly that exchange.

### The Number of the Components

The comparison in one line: over $\mathbb{C}$ one integer survives, over $\mathbb{C}_{\mathrm{spl}}$ none does, and over a product of two real fields with the identity involution two integers would survive. The three cases are the three involutions: the conjugation, the exchange, and the identity.

## Summary

A Hermitian module over the split ring is a pair of real spaces with a real pairing $\beta:V_+\times V_-\to\mathbb{R}$; the conjugation exchanges the components, so the form's two components are $\beta$ and its transpose and are one datum. The isometry class is the rank of $\beta$, and every non-degenerate form of rank $n$ has realified signature $(n,n)$ and is isometric to the sum of $n$ copies of the standard form $H(A,C)=A\bar C$.

The standard form is metabolic, with the Lagrangian $S_+$; every form is metabolic; and the Witt group is trivial. The naive count $\mathbb{Z}\oplus\mathbb{Z}$, one copy to each idempotent, would be right for the identity involution on $\mathbb{R}\times\mathbb{R}$ and is wrong here, because the exchange ties the two components together.

Over $\mathbb{C}$ the signature survives and the Witt group is $\mathbb{Z}$; over the split ring nothing survives and the group is trivial; over the product with the identity involution two copies of $\mathbb{Z}$ survive. The three answers are the three involutions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Phi(x,y)=\overline{\Phi(y,x)}$ | A Hermitian form over the split ring |
| $\beta:V_+\times V_-\to\mathbb{R}$ | The real pairing, the whole of the form |
| $(\beta,\beta^{\mathsf T})$ | The two components of the form |
| $\beta\mapsto P_+^{\mathsf T}\beta P_-$ | The isometry, two-sided equivalence |
| $n=\mathrm{rank}\,\beta$ | The complete invariant |
| $(n,n)$ | The realified signature of every non-degenerate form |
| $S_+=\mathbb{R}\Pi_+$ | A Lagrangian, the isotropic submodule |
| $\langle1\rangle$ | The standard form $H(A,C)=A\bar C$, metabolic |
| $W(\mathbb{C}_{\mathrm{spl}},\bar\cdot)=0$ | The Witt group |

## Further Reading

- Max-Albert Knus, *Quadratic and Hermitian Forms over Rings* (Springer, Grundlehren der mathematischen Wissenschaften 294, 1991), for forms over a ring with involution, metabolic forms and the Witt group of a ring.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, Grundlehren der mathematischen Wissenschaften 270, 1985), for the Witt group, hyperbolic forms and the metabolic identification.
- C. T. C. Wall, "On the axiomatic foundations of the theory of Hermitian forms", *Mathematical Proceedings of the Cambridge Philosophical Society* 67 (1970), 243-250, for the Witt group of a ring with involution.
- Richard S. Pierce, *Associative Algebras* (Springer, Graduate Texts in Mathematics 88, 1982), for the exchange involution on a product of two algebras and its forms.
- T. Y. Lam, *Introduction to Quadratic Forms over Fields* (American Mathematical Society, 2005), for the real case, the signature and the Witt group $\mathbb{Z}$ of the real field.
