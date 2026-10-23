# __The Hermitian Form and the Positivity of the Complexoid Algebra__

## Introduction

The sesquilinear product $Q_1\bar Q_2$ has a second reading, and it is the reading of the article: the Hermitian form $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ on the complex space and its regular module. On $\mathbb{C}$ the reading is the whole form theory, because the algebra is one-dimensional and its regular module is the algebra itself; the consequences are that the form is definite, that its cone is a ray, that its modules are classified by rank alone, and that its Witt group is the integers with the signature as invariant. This is the base case of the Hermitian layer of the corpus.

The article assumes the form is the general plain sesquilinear form and does not define it twice: the form and the product it comes from are *The Sesquilinear Product of the Complexoid Space*, above this article. It does not treat the topological norm, the modulus or the topology of the cone: those are *Complex Norm and Invertibility*, and the article only names them where the algebra-level statement ends. The general theory is *Positivity and the Positive Cone of a Hermitian Form*, *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Interpretation and notation.** The element is $Q=q+iq'$; the base involution is the bar $\bar Q=q-iq'$ and ${}^{*}=\bar{\cdot}$. The letters $\langle\cdot,\cdot\rangle$, $\langle\cdot,\cdot\rangle_{\natural}$, $\langle\cdot,\cdot\rangle_{*}$, $\langle\cdot,\cdot\rangle_{\natural*}$ name the four forms, and $\langle\cdot,\cdot\rangle=\langle\cdot,\cdot\rangle_{\natural}=Q_1Q_2$, $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}=Q_1\bar Q_2$ on the complex space; they are never elements. The Hermitian form is written $\langle Q_1,Q_2\rangle_{*}$, its diagonal $\langle Q\rangle_{*}=\langle Q,Q\rangle_{*}$; the algebraic norm $Q\bar Q$ is the same diagonal and is written $Q\bar Q$ in the algebraic statements. The brackets $[\,,\,]$ and the dot product are the commutator and the symmetrised product of *The Sesquilinear Product of the Complexoid Space*, above this article.

## The Hermitian Form

**Definition.** The **Hermitian form** of the complex space is

$$
\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2 .
$$

**Proposition (sesquilinearity and conjugate symmetry).** For complex $\lambda,\mu$,

$$
\langle \lambda Q_1+\mu Q_2,Q_3\rangle_{*}=\lambda \langle Q_1,Q_3\rangle_{*}+\mu \langle Q_2,Q_3\rangle_{*}, \qquad \langle Q_1,\lambda Q_2+\mu Q_3\rangle_{*}=\bar\lambda \langle Q_1,Q_2\rangle_{*}+\bar\mu \langle Q_1,Q_3\rangle_{*},
$$

so that $\langle\cdot,\cdot\rangle_{*}$ is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second; and

$$
\langle Q_1,Q_2\rangle_{*}=\overline{\langle Q_2,Q_1\rangle_{*}} .
$$

**Proof.** The first two displays are the parities of the product $Q_1\bar Q_2$; the third is $\overline{Q_2\bar Q_1}=\bar Q_2 Q_1=Q_1\bar Q_2$ by the commutativity of the field.

**Proposition (the Gram matrix and non-degeneracy).** In the basis $1$ of the complex space the Gram matrix of $\langle\cdot,\cdot\rangle_{*}$ is the one-entry matrix $[1]$; the form is non-degenerate, and its radical is $\{0\}$.

**Proof.** $\langle 1,1\rangle_{*}=1\cdot\bar 1=1$, so the Gram matrix is the $1\times1$ identity; for $Q_1\neq0$ the conjugate-linear functional $Q_2\mapsto \langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ is not the zero functional, so the left radical is $\{0\}$, and the same on the right by conjugate symmetry.

**Definition.** The **associated quadratic form** is the diagonal

$$
\langle Q\rangle_{*}=\langle Q,Q\rangle_{*}=Q\bar Q=q^{2}+q'^{2},
$$

a real value $\ge0$; the **polarisation** is

$$
\langle Q_1,Q_2\rangle_{*}+\langle Q_2,Q_1\rangle_{*}=2\operatorname{Re}(Q_1\bar Q_2),
$$

and the difference $\langle Q_1,Q_2\rangle_{*}-\langle Q_2,Q_1\rangle_{*}$ is the commutator $[Q_1,Q_2]=2i\operatorname{Im}(Q_1\bar Q_2)$ of the sesquilinear product.

**Proposition (the polarisation recovers the form).** The form is recovered from its diagonal and its commutator: $\langle Q_1,Q_2\rangle_{*}=\tfrac12\bigl(\langle Q_1,Q_2\rangle_{*}+\langle Q_2,Q_1\rangle_{*}\bigr)+\tfrac12\bigl(\langle Q_1,Q_2\rangle_{*}-\langle Q_2,Q_1\rangle_{*}\bigr)$.

**Proof.** Immediate from the two displays; the two halves are the symmetrised product and the commutator of *The Sesquilinear Product of the Complexoid Space*.

## The Two Inequalities as Statements of the Form

**Theorem (the Cauchy–Schwarz statement is an identity here).** For all $Q_1,Q_2$,

$$
\boxed{\;\langle Q_1,Q_2\rangle_{*}\overline{\langle Q_1,Q_2\rangle_{*}}=\langle Q_1\rangle_{*}\,\langle Q_2\rangle_{*}\;}.
$$

The Cauchy–Schwarz inequality is therefore an equality on the complex space, and it is so because the space is one-dimensional over its own algebra: the regular module has rank one, and the inequality degenerates to the identity.

**Proof.** $\langle Q_1,Q_2\rangle_{*}\overline{\langle Q_1,Q_2\rangle_{*}}=Q_1\bar Q_2\,\overline{Q_1\bar Q_2}=Q_1\bar Q_2\bar Q_1 Q_2=Q_1\bar Q_1\,Q_2\bar Q_2=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$.

**Theorem (the triangle statement).** For all $Q_1,Q_2$,

$$
\boxed{\;\langle Q_1+Q_2\rangle_{*}=\langle Q_1\rangle_{*}+\langle Q_2\rangle_{*}+\langle Q_1,Q_2\rangle_{*}+\langle Q_2,Q_1\rangle_{*}=\langle Q_1\rangle_{*}+\langle Q_2\rangle_{*}+2\operatorname{Re}\langle Q_1,Q_2\rangle_{*}\;}.
$$

The two identities are the algebraic content from which the triangle statement of the norm is read, the second being applied to $\operatorname{Re}\langle Q_1,Q_2\rangle_{*}$; the inequality itself belongs to the norm, and is *Complex Norm and Invertibility*.

**Proof.** The form is additive in the second argument and conjugate-linear in the first, and $\langle Q_1,Q_2\rangle_{*}+\langle Q_2,Q_1\rangle_{*}$ is the symmetrised product of the sesquilinear structure.

## Positivity and the Hermitian Cone

**Definition.** The form is **positive definite**: $\langle Q\rangle_{*}\ge0$ for every $Q$, with $\langle Q\rangle_{*}=0$ exactly at $Q=0$.

**Proof.** $\langle Q\rangle_{*}=q^{2}+q'^{2}$ with $q,q'$ real, a sum of two squares.

**Definition.** The **Hermitian cone** is the set of the values of the diagonal,

$$
P=\{Q\bar Q: Q\in\mathbb{C}\}=\mathbb{R}_{\ge0},
$$

the ray of the non-negative reals.

**Proposition.** The cone $P$ is a closed, convex, pointed, generating cone of real dimension one; it contains $0$; it is closed under addition and under multiplication by non-negative real scalars; and its interior is the ray of the positive reals, the diagonal $\langle Q\rangle_{*}=Q\bar Q$ lying in $P^{\circ}$ exactly for $Q\neq0$.

**Proof.** $\mathbb{R}_{\ge0}$ is closed, convex, pointed and generating in $\mathbb{R}$, and the images $Q\bar Q$ fill it. The last statement is the positive definiteness.

**Definition.** The **order** defined by the cone is the relation on the self-adjoint elements $\mathbb{R}$ given by $x\le y$ when $y-x\in P$; it is the usual order of the real line. On the whole algebra no order compatible with the multiplication exists, by the non-orderability of $\mathbb{C}$ cited in *The Specificities of the Complex Algebra*.

**Remark (the Hilbert algebra of rank one).** The algebra, read with the involution ${}^{*}$ and the definite form $\langle\cdot,\cdot\rangle_{*}$, satisfies the adjointness axiom

$$
\langle Q_1 Q_2,Q_3\rangle_{*}=\langle Q_2,Q_1^{*}Q_3\rangle_{*},
$$

since $\langle Q_1Q_2,Q_3\rangle_{*}=Q_1Q_2\bar Q_3$ and $\langle Q_2,Q_1^{*}Q_3\rangle_{*}=Q_2\overline{Q_1^{*}Q_3}=Q_2\overline{\bar Q_1 Q_3}=Q_2Q_1\bar Q_3$, equal to the first by commutativity. The algebra is therefore a Hilbert algebra, and because it is one-dimensional over itself it is the **Hilbert algebra of rank one**. The completeness of the order of $\mathbb{R}$, which upgrades the algebra to a Hilbert space and the algebra to a $C^{*}$-algebra, is a topological property and is *Complex Norm and Invertibility*; the algebraic statements stop at the cone and the order above.

## The Hermitian Modules

**Definition.** A **Hermitian module** over $(\mathbb{C},\bar{\cdot})$ is a left $\mathbb{C}$-module $M$ with a form $h:M\times M\to\mathbb{C}$, conjugate-linear in the first argument, $\mathbb{C}$-linear in the second, and conjugate-symmetric, $h(x,y)=\overline{h(y,x)}$; the module is **definite** when $h(x,x)\ge0$ with equality only at $x=0$. This is the slot convention of the modules articles, conjugate-linear in the first; it is the transpose of the convention of $\langle\cdot,\cdot\rangle_{*}$ above, where the first slot is the linear one, and the two conventions differ only by the exchange of the two slots, so that $h$ is the form $\langle\cdot,\cdot\rangle_{*}$ read with its arguments in the other order and conjugated.

**Theorem.** Every Hermitian module over $\mathbb{C}$ is free, and the definite ones are classified by their rank alone: a definite Hermitian module of rank $n$ is isometric to the free module $\mathbb{C}^{n}$ with the standard form

$$
h_{\mathrm{st}}(x,y)=\sum_{k=1}^{n}\bar x_{k}y_{k}.
$$

**Proof.** A module over a field is free, and the rank is well defined, as in *The Classes of Element of the Complex Algebra*, §*The Modules*. For definiteness, the Gram matrix of $h$ in a basis of the free module is a Hermitian matrix with all principal minors positive; its diagonalisation by the congruence $S^{*}hS$ puts it in the form $\mathrm{I}_{n}$, and the change of basis is the isometry. The congruence and the inertia are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Definition.** The **group of linear maps preserving the form** of rank $n$ is

$$
\mathrm{U}(n)=\{T\in GL(n,\mathbb{C}): h_{\mathrm{st}}(Tx,Ty)=h_{\mathrm{st}}(x,y)\ \text{for all}\ x,y\},
$$

whose matrix condition is $T^{*}T=\mathrm{I}_{n}$, where $T^{*}$ is the conjugate transpose; in rank one it is $\mathrm{U}(1)=\{\lambda\in\mathbb{C}:\lambda\bar\lambda=1\}$, the algebraic condition $\lambda\bar\lambda=1$ replacing the modulus.

**Remark.** The regular module of the algebra is the rank-one definite Hermitian module, with $h(x,y)=\langle y,x\rangle_{*}$ the form $\langle\cdot,\cdot\rangle_{*}$ read with its arguments exchanged; its group of linear maps preserving the form is $\mathrm{U}(1)$.

## The Classification and the Witt Group

**Definition.** A Hermitian form on $\mathbb{C}^{n}$ has **inertia** $(n,m)$ when a basis puts its Gram matrix in the normal form $\mathrm{diag}(1_{n},-1_{m})$, with $n+m=N$.

**Theorem (Sylvester).** Every Hermitian form on $\mathbb{C}^{n}$ has an inertia, the pair $(n,m)$ is independent of the basis, and two forms are isometric exactly when they have the same inertia. The **signature** is $\sigma=n-m$.

**Proof.** The diagonalisation is by the congruence $S^{*}hS$ with $S$ invertible, and the inertia is the invariant of the congruence, the hermitian analogue of Sylvester's law for real symmetric forms; the theory is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Remark (the classification over the reals).** Under the realification the two rules are as follows. A Hermitian form of signature $(n,m)$ on $\mathbb{C}^{n+m}$ realifies to a real symmetric bilinear form on $\mathbb{R}^{2(n+m)}$ of signature $(2n,2m)$: the inertia doubles. A real symmetric bilinear form that is $\mathbb{C}$-bilinear for the complex structure realifies with the split signature $(n,n)$. The two rules are the realification dictionary, and the two-dimensional case is *The Realification and the Effect of the Change of Scalars*, above this article in this category.

**Definition and theorem (the Witt group of the definite forms).** The **Witt group** $W(\mathbb{C},\bar{\cdot})$ is the group of the isometry classes of non-degenerate Hermitian forms under orthogonal sum, modulo the hyperbolic forms. It is

$$
\boxed{\;W(\mathbb{C},\bar{\cdot})\cong\mathbb{Z}\;},
$$

with the signature $\sigma$ as invariant; the definite forms are the classes $\pm n[H]$, $n\ge0$, generated by the rank-one form $\langle\cdot,\cdot\rangle_{*}$ and its negative, and they generate the whole group. The group is $\mathbb{Z}$ and not $\mathbb{Z}/2$ because the involution is the real one, that is, its fixed space $\mathbb{R}_{\mathbb{C}}$ is a real form of the complex space, so that scaling by $i$ does not collapse the classification and the signature and not only the rank parity is the invariant. The general theory is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *The Witt Group and the Grothendieck–Witt Ring*.

**Proof.** Every non-degenerate Hermitian form is Witt-equivalent to its normal form, which is determined by the signature; the orthogonal sum adds the signatures; the hyperbolic plane has signature $0$ and is the null class. The rank-one form $\langle\cdot,\cdot\rangle_{*}$ has signature $1$, its negative has signature $-1$, and every form is an orthogonal sum of copies of the two, so the definite classes generate the group and the signature is an isomorphism onto $\mathbb{Z}$.

## Summary

The Hermitian form of the complex space is $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second, conjugate-symmetric, with Gram matrix the unit in the basis $1$ and radical $\{0\}$. Its diagonal is $Q\bar Q=q^{2}+q'^{2}$, non-negative and zero only at the origin, so the form is positive definite and the Hermitian cone is the ray $\mathbb{R}_{\ge0}$ with the usual order; the algebra is the Hilbert algebra of rank one. The Cauchy–Schwarz statement is an identity, $\langle Q_1,Q_2\rangle_{*}\overline{\langle Q_1,Q_2\rangle_{*}}=\langle Q_1\rangle_{*}\langle Q_2\rangle_{*}$, and the triangle statement is the identity $\langle Q_1+Q_2\rangle_{*}=\langle Q_1\rangle_{*}+\langle Q_2\rangle_{*}+2\operatorname{Re}\langle Q_1,Q_2\rangle_{*}$; the inequalities themselves are the norm, deferred. The definite Hermitian modules are free and classified by rank alone, the group of linear maps preserving the rank-$n$ form being the group with $T^{*}T=\mathrm{I}_{n}$; the Hermitian forms are classified by inertia and signature, and the Witt group of the definite forms is $\mathbb{Z}$, generated by the rank-one form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle Q_1,Q_2\rangle_{*}=Q_1\bar Q_2$ | the Hermitian form, the general plain sesquilinear form (and $\langle\cdot,\cdot\rangle_{*}=\langle\cdot,\cdot\rangle_{\natural*}$ on $\mathbb{C}$) |
| $\langle Q\rangle_{*}=\langle Q,Q\rangle_{*}=Q\bar Q$ | the associated quadratic form, the definite algebraic norm |
| $Q_1\odot Q_2$, $[Q_1,Q_2]$ | the symmetrised product $2\operatorname{Re}(Q_1\bar Q_2)$ and the commutator $2i\operatorname{Im}(Q_1\bar Q_2)$ |
| $P=\mathbb{R}_{\ge0}$ | the Hermitian cone, the ray of the non-negative reals |
| $h_{\mathrm{st}}$ | the standard definite form on $\mathbb{C}^{n}$, $\sum_{k}\bar x_{k}y_{k}$ |
| $\mathrm{U}(n)$, $\mathrm{U}(1)$ | the group of linear maps preserving the form, $T^{*}T=\mathrm{I}_{n}$; $\lambda\bar\lambda=1$ in rank one |
| $(n,m)$, $\sigma=n-m$ | the inertia and the signature of a Hermitian form |
| $W(\mathbb{C},\bar{\cdot})\cong\mathbb{Z}$ | the Witt group, with the signature as invariant |

## Further Reading

- Vladimir I. Arnold, *On Teaching Mathematics* (1997), for the reading of a form by its cone and its group, in the tradition the article follows.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for Hermitian forms over an algebra with involution, their inertia and their Witt group.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the Witt group, the hyperbolic plane and the signature invariant.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford University Press, 1994), for the cone of a definite form, the order it defines and the rank-one case.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Volume I (Academic Press, 1983), for Hilbert algebras, the adjointness axiom and the passage to the $C^{*}$-case.
