# __The Hermitian Form and the Positivity of the Complex Algebra__

## Introduction

The sesquilinear product $A\bar C$ has a second reading, and it is the reading of the article: the Hermitian form $H(A,C)=A\bar C$ on the complex space and its regular module. On $\mathbb{C}$ the reading is the whole form theory, because the algebra is one-dimensional and its regular module is the algebra itself; the consequences are that the form is definite, that its cone is a ray, that its modules are classified by rank alone, and that its Witt group is the integers with the signature as invariant. This is the base case of the Hermitian layer of the corpus.

The article assumes the form is the general plain sesquilinear form and does not define it twice: the form and the product it comes from are *The Sesquilinear Product of the Complex Space*, above this article. It does not treat the topological norm, the modulus or the topology of the cone: those are *Complex Norm and Invertibility*, and the article only names them where the algebra-level statement ends. The general theory is *Positivity and the Positive Cone of a Hermitian Form*, *Hermitian Modules over a Hermitian Algebra with Hermitian Adjoint* and *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Interpretation and notation.** The element is $A=a+ia'$; the base involution is the bar $\bar A=a-ia'$ and ${}^{*}=\bar{\cdot}$. The letters $B$, $N$, $H$, $K$ name the four forms, and $B=N=AC$, $H=K=A\bar C$ on the complex space; they are never elements. The Hermitian form is written $H(A,C)$, its diagonal $H(A)=H(A,A)$; the algebraic norm $A\bar A$ is the same diagonal and is written $A\bar A$ in the algebraic statements. The brackets $[\,,\,]$ and the dot product are the commutator and the symmetrised product of *The Sesquilinear Product of the Complex Space*, above this article.

## The Hermitian Form

**Definition.** The **Hermitian form** of the complex space is

$$
H(A,C)=A\bar C .
$$

**Proposition (sesquilinearity and conjugate symmetry).** For complex $\lambda,\mu$,

$$
H(\lambda A+\mu C,D)=\lambda H(A,D)+\mu H(C,D), \qquad H(A,\lambda C+\mu D)=\bar\lambda H(A,C)+\bar\mu H(A,D),
$$

so that $H$ is $\mathbb{C}$-linear in the first argument and conjugate-linear in the second; and

$$
H(A,C)=\overline{H(C,A)} .
$$

**Proof.** The first two displays are the parities of the product $A\bar C$; the third is $\overline{C\bar A}=\bar C A=A\bar C$ by the commutativity of the field.

**Proposition (the Gram matrix and non-degeneracy).** In the basis $1$ of the complex space the Gram matrix of $H$ is the one-entry matrix $[1]$; the form is non-degenerate, and its radical is $\{0\}$.

**Proof.** $H(1,1)=1\cdot\bar 1=1$, so the Gram matrix is the $1\times1$ identity; for $A\neq0$ the linear functional $C\mapsto H(A,C)=A\bar C$ is not the zero functional, so the left radical is $\{0\}$, and the same on the right by conjugate symmetry.

**Definition.** The **associated quadratic form** is the diagonal

$$
H(A)=H(A,A)=A\bar A=a^{2}+a'^{2},
$$

a real value $\ge0$; the **polarisation** is

$$
H(A,C)+H(C,A)=2\operatorname{Re}(A\bar C),
$$

and the difference $H(A,C)-H(C,A)$ is the commutator $[A,C]=2i\operatorname{Im}(A\bar C)$ of the sesquilinear product.

**Proposition (the polarisation recovers the form).** The form is recovered from its diagonal and its commutator: $H(A,C)=\tfrac12\bigl(H(A,C)+H(C,A)\bigr)+\tfrac12\bigl(H(A,C)-H(C,A)\bigr)$.

**Proof.** Immediate from the two displays; the two halves are the symmetrised product and the commutator of *The Sesquilinear Product of the Complex Space*.

## The Two Inequalities as Statements of the Form

**Theorem (the Cauchy–Schwarz statement is an identity here).** For all $A,C$,

$$
H(A,C)\overline{H(A,C)}=H(A)\,H(C).
$$

The Cauchy–Schwarz inequality is therefore an equality on the complex space, and it is so because the space is one-dimensional over its own algebra: the regular module has rank one, and the inequality degenerates to the identity.

**Proof.** $H(A,C)\overline{H(A,C)}=A\bar C\,\overline{A\bar C}=A\bar C\bar A C=A\bar A\,C\bar C=H(A)H(C)$.

**Theorem (the triangle statement).** For all $A,C$,

$$
H(A+C)=H(A)+H(C)+H(A,C)+H(C,A)=H(A)+H(C)+2\operatorname{Re}H(A,C).
$$

The two identities are the algebraic content from which the triangle statement of the norm is read, the second being applied to $\operatorname{Re}H(A,C)$; the inequality itself belongs to the norm, and is *Complex Norm and Invertibility*.

**Proof.** The form is additive in the second argument and conjugate-linear in the first, and $H(A,C)+H(C,A)$ is the symmetrised product of the sesquilinear structure.

## Positivity and the Hermitian Cone

**Definition.** The form is **positive definite**: $H(A)\ge0$ for every $A$, with $H(A)=0$ exactly at $A=0$.

**Proof.** $H(A)=a^{2}+a'^{2}$ with $a,a'$ real, a sum of two squares.

**Definition.** The **Hermitian cone** is the set of the values of the diagonal,

$$
P=\{A\bar A: A\in\mathbb{C}\}=\mathbb{R}_{\ge0},
$$

the ray of the non-negative reals.

**Proposition.** The cone $P$ is a closed, convex, pointed, generating cone of real dimension one; it contains $0$; it is closed under addition and under multiplication by non-negative real scalars; and its interior is the ray of the positive reals, the diagonal $H(A)=A\bar A$ lying in $P^{\circ}$ exactly for $A\neq0$.

**Proof.** $\mathbb{R}_{\ge0}$ is closed, convex, pointed and generating in $\mathbb{R}$, and the images $A\bar A$ fill it. The last statement is the positive definiteness.

**Definition.** The **order** defined by the cone is the relation on the self-adjoint elements $\mathbb{R}$ given by $x\le y$ when $y-x\in P$; it is the usual order of the real line. On the whole algebra no order compatible with the multiplication exists, by the non-orderability of $\mathbb{C}$ cited in *The Specificities of the Complex Algebra*.

**Remark (the Hilbert algebra of rank one).** The algebra, read with the involution ${}^{*}$ and the definite form $H$, satisfies the adjointness axiom

$$
H(A C,D)=H(C,A^{*}D),
$$

since $H(AC,D)=AC\bar D$ and $H(C,A^{*}D)=C\overline{A^{*}D}=C\overline{\bar A D}=CA\bar D$, equal to the first by commutativity. The algebra is therefore a Hilbert algebra, and because it is one-dimensional over itself it is the **Hilbert algebra of rank one**. The completeness of the order of $\mathbb{R}$, which upgrades the algebra to a Hilbert space and the algebra to a $C^{*}$-algebra, is a topological property and is *Complex Norm and Invertibility*; the algebraic statements stop at the cone and the order above.

## The Hermitian Modules

**Definition.** A **Hermitian module** over $(\mathbb{C},\bar{\cdot})$ is a left $\mathbb{C}$-module $M$ with a form $h:M\times M\to\mathbb{C}$, conjugate-linear in the first argument, $\mathbb{C}$-linear in the second, and conjugate-symmetric, $h(x,y)=\overline{h(y,x)}$; the module is **definite** when $h(x,x)\ge0$ with equality only at $x=0$. This is the slot convention of the modules articles, conjugate-linear in the first; it is the transpose of the convention of $H$ above, where the first slot is the linear one, and the two conventions differ only by the exchange of the two slots, so that $h$ is the form $H$ read with its arguments in the other order and conjugated.

**Theorem.** Every Hermitian module over $\mathbb{C}$ is free, and the definite ones are classified by their rank alone: a definite Hermitian module of rank $n$ is isometric to the free module $\mathbb{C}^{n}$ with the standard form

$$
h_{\mathrm{st}}(x,y)=\sum_{k=1}^{n}\bar x_{k}y_{k}.
$$

**Proof.** A module over a field is free, and the rank is well defined, as in *The Classes of Element of the Complex Algebra*, §*The Modules*. For definiteness, the Gram matrix of $h$ in a basis of the free module is a Hermitian matrix with all principal minors positive; its diagonalisation by the congruence $S^{*}hS$ puts it in the form $\mathrm{I}_{n}$, and the change of basis is the isometry. The congruence and the inertia are *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Definition.** The **group of linear maps preserving the form** of rank $n$ is

$$
U(n)=\{T\in GL(n,\mathbb{C}): h_{\mathrm{st}}(Tx,Ty)=h_{\mathrm{st}}(x,y)\ \text{for all}\ x,y\},
$$

whose matrix condition is $T^{*}T=\mathrm{I}_{n}$, where $T^{*}$ is the conjugate transpose; in rank one it is $U(1)=\{\lambda\in\mathbb{C}:\lambda\bar\lambda=1\}$, the algebraic condition $\lambda\bar\lambda=1$ replacing the modulus.

**Remark.** The regular module of the algebra is the rank-one definite Hermitian module, with $h(x,y)=H(y,x)$ the form $H$ read with its arguments exchanged; its group of linear maps preserving the form is $U(1)$.

## The Classification and the Witt Group

**Definition.** A Hermitian form on $\mathbb{C}^{n}$ has **inertia** $(p,q)$ when a basis puts its Gram matrix in the normal form $\mathrm{diag}(1_{p},-1_{q})$, with $p+q=n$.

**Theorem (Sylvester).** Every Hermitian form on $\mathbb{C}^{n}$ has an inertia, the pair $(p,q)$ is independent of the basis, and two forms are isometric exactly when they have the same inertia. The **signature** is $\sigma=p-q$.

**Proof.** The diagonalisation is by the congruence $S^{*}hS$ with $S$ invertible, and the inertia is the invariant of the congruence, the hermitian analogue of Sylvester's law for real symmetric forms; the theory is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint*.

**Remark (the classification over the reals).** Under the realification the two rules are as follows. A Hermitian form of signature $(p,q)$ on $\mathbb{C}^{n}$ realifies to a real symmetric bilinear form on $\mathbb{R}^{2n}$ of signature $(2p,2q)$: the inertia doubles. A real symmetric bilinear form that is $\mathbb{C}$-bilinear for the complex structure realifies with the split signature $(n,n)$. The two rules are the realification dictionary, and the two-dimensional case is *The Realification and the Effect of the Change of Scalars*, above this article in this category.

**Definition and theorem (the Witt group of the definite forms).** The **Witt group** $W(\mathbb{C},\bar{\cdot})$ is the group of the isometry classes of non-degenerate Hermitian forms under orthogonal sum, modulo the hyperbolic forms. It is

$$
W(\mathbb{C},\bar{\cdot})\cong\mathbb{Z},
$$

with the signature $\sigma$ as invariant; the definite forms are the classes $\pm n[H]$, $n\ge0$, generated by the rank-one form $H$ and its negative, and they generate the whole group. The group is $\mathbb{Z}$ and not $\mathbb{Z}/2$ because the involution is the real one, that is, its fixed space $\mathbb{R}_{\mathbb{C}}$ is a real form of the complex space, so that scaling by $i$ does not collapse the classification and the signature and not only the rank parity is the invariant. The general theory is *Hermitian Forms over an Involution Ring and the Unitary Witt Group with Hermitian Adjoint* and *The Witt Group and the Grothendieck–Witt Ring*.

**Proof.** Every non-degenerate Hermitian form is Witt-equivalent to its normal form, which is determined by the signature; the orthogonal sum adds the signatures; the hyperbolic plane has signature $0$ and is the null class. The rank-one form $H$ has signature $1$, its negative has signature $-1$, and every form is an orthogonal sum of copies of the two, so the definite classes generate the group and the signature is an isomorphism onto $\mathbb{Z}$.

## Summary

The Hermitian form of the complex space is $H(A,C)=A\bar C$, $\mathbb{C}$-linear in the first argument and conjugate-linear in the second, conjugate-symmetric, with Gram matrix the unit in the basis $1$ and radical $\{0\}$. Its diagonal is $A\bar A=a^{2}+a'^{2}$, non-negative and zero only at the origin, so the form is positive definite and the Hermitian cone is the ray $\mathbb{R}_{\ge0}$ with the usual order; the algebra is the Hilbert algebra of rank one. The Cauchy–Schwarz statement is an identity, $H(A,C)\overline{H(A,C)}=H(A)H(C)$, and the triangle statement is the identity $H(A+C)=H(A)+H(C)+2\operatorname{Re}H(A,C)$; the inequalities themselves are the norm, deferred. The definite Hermitian modules are free and classified by rank alone, the group of linear maps preserving the rank-$n$ form being the group with $T^{*}T=\mathrm{I}_{n}$; the Hermitian forms are classified by inertia and signature, and the Witt group of the definite forms is $\mathbb{Z}$, generated by the rank-one form.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $H(A,C)=A\bar C$ | the Hermitian form, the general plain sesquilinear form (and $H=K$ on $\mathbb{C}$) |
| $H(A)=H(A,A)=A\bar A$ | the associated quadratic form, the definite algebraic norm |
| $A\odot C$, $[A,C]$ | the symmetrised product $2\operatorname{Re}H$ and the commutator $2i\operatorname{Im}H$ |
| $P=\mathbb{R}_{\ge0}$ | the Hermitian cone, the ray of the non-negative reals |
| $h_{\mathrm{st}}$ | the standard definite form on $\mathbb{C}^{n}$, $\sum_{k}\bar x_{k}y_{k}$ |
| $U(n)$, $U(1)$ | the group of linear maps preserving the form, $T^{*}T=\mathrm{I}_{n}$; $\lambda\bar\lambda=1$ in rank one |
| $(p,q)$, $\sigma=p-q$ | the inertia and the signature of a Hermitian form |
| $W(\mathbb{C},\bar{\cdot})\cong\mathbb{Z}$ | the Witt group, with the signature as invariant |

## Further Reading

- Vladimir I. Arnold, *On Teaching Mathematics* (1997), for the reading of a form by its cone and its group, in the tradition the article follows.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998), for Hermitian forms over an algebra with involution, their inertia and their Witt group.
- Tsit-Yuen Lam, *Introduction to Quadratic Forms over Fields*, Graduate Studies in Mathematics 67 (American Mathematical Society, 2005), for the Witt group, the hyperbolic plane and the signature invariant.
- Jacques Faraut and Adam Korányi, *Analysis on Symmetric Cones* (Oxford University Press, 1994), for the cone of a definite form, the order it defines and the rank-one case.
- Richard V. Kadison and John R. Ringrose, *Fundamentals of the Theory of Operator Algebras*, Volume I (Academic Press, 1983), for Hilbert algebras, the adjointness axiom and the passage to the $C^{*}$-case.
