# __The Derivations and the Automorphisms of $M_4(\mathbb{C})$__

## Introduction

A **derivation** of $M_4(\mathbb{C})$ is a linear map $D$ with the Leibniz rule

$$
D(AB)=D(A)B+AD(B).
$$

An **automorphism** is an invertible linear map preserving the product. For the full matrix algebra both structures are as small as they can be: every derivation is inner, $D=\operatorname{ad}_X$ for some $X$, and every automorphism is inner, $A\mapsto UAU^{-1}$ for some invertible $U$. The two statements are the theorems of Wedderburn and Skolem–Noether, and they give

$$
\operatorname{Der}(M_4)=\operatorname{ad}\mathfrak{sl}_4\cong\mathfrak{sl}_4,\qquad
\operatorname{Aut}(M_4)=PGL_4(\mathbb{C}),
$$

both of dimension $15$. There are no outer derivations and no outer automorphisms.

This article states the two theorems, the kernel of the adjoint map, the $*$-structures, the complex-antilinear automorphisms, and the comparison with the biquaternion algebra, whose derivations are only three-dimensional. The Lie algebra itself is *The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$*; the inner automorphisms as a group are *The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$*; the operators of the Peirce decomposition are *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*.

## Derivations

**Definition.** Let $\operatorname{Der}(M_4)$ be the vector space of derivations of $M_4(\mathbb{C})$, with the bracket $[D_1,D_2]=D_1D_2-D_2D_1$.

**Proposition.** $\operatorname{Der}(M_4)$ is a Lie algebra, and for every $X\in M_4$ the map

$$
\operatorname{ad}_X(Y)=[X,Y]
$$

is a derivation.

**Proof.** The Jacobi identity gives

$$
\operatorname{ad}_X(YZ)=[X,YZ]=[X,Y]Z+Y[X,Z]=\operatorname{ad}_X(Y)Z+Y\operatorname{ad}_X(Z).
$$

The bracket of two derivations is a derivation because the commutator of two endomorphisms satisfying the Leibniz rule satisfies it as well.

**Proposition.** The kernel of $\operatorname{ad}:\mathfrak{gl}_4\to\operatorname{Der}(M_4)$ is the centre $\mathbb{C}I$, and the image is $\operatorname{ad}\mathfrak{sl}_4$, of dimension $15$.

**Proof.** $\operatorname{ad}_X=0$ exactly when $X$ commutes with every matrix, that is, when $X$ is scalar. The image of $\operatorname{ad}$ is isomorphic to $\mathfrak{gl}_4/\mathbb{C}I\cong\mathfrak{sl}_4$, of dimension $15$.

**Theorem (Wedderburn).** Every derivation of $M_4(\mathbb{C})$ is inner:

$$
\operatorname{Der}(M_4)=\operatorname{ad}\mathfrak{sl}_4,\qquad
\dim\operatorname{Der}(M_4)=15.
$$

**Proof.** The theorem is the case $n=4$ of Wedderburn's theorem: every derivation of a central simple algebra over a field is inner. The elementary proof reconstructs $X$ from the images of the matrix units. Fix the units $E_{ij}$ and a derivation $D$. The relation $E_{ij}E_{kl}=\delta_{jk}E_{il}$ forces the entries of $D(E_{ij})$ to be the entries of a single matrix $X$: the entry $(1,k)$ of $D(E_{1j})$ is $X_{jk}$ for $k\ne j$, the entry $(1,j)$ of $D(E_{1j})$ is $X_{jj}-X_{11}$, and the entries of $D(E_{ij})$ in the other positions are the remaining entries of $X$ and $-X$; the consistency of these readings is the Leibniz rule applied to the three-factor identities $E_{ij}E_{jk}E_{ki}=E_{ii}$. With $X$ so reconstructed and normalised by $X_{11}=0$, the map $D-\operatorname{ad}_X$ is a derivation vanishing on every $E_{1j}$, hence on every matrix unit, hence everywhere. So $D=\operatorname{ad}_X$.

**The inner derivations.** The map $\operatorname{ad}$ is an isomorphism $\mathfrak{sl}_4\to\operatorname{Der}(M_4)$, and the derivation $\operatorname{ad}_X$ depends only on the traceless part of $X$. The fifteen-dimensional space of derivations is therefore a copy of $\mathfrak{sl}_4$, and the scalar matrices act trivially.

**The grading.** The derivations act on the Peirce blocks of an idempotent by the rule of *The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$*: $\operatorname{ad}_X$ carries $A_{rs}$ to $A_{rs}$ for the diagonal blocks and mixes the off-diagonal blocks according to the entries of $X$. The derivation is determined by its values on the four blocks.

## Automorphisms

**Definition.** An automorphism of $M_4(\mathbb{C})$ is an invertible linear map $\varphi$ with $\varphi(AB)=\varphi(A)\varphi(B)$ for all $A,B$.

**Proposition.** For every $U\in GL_4(\mathbb{C})$ the map $\operatorname{Inn}_U(A)=UAU^{-1}$ is an automorphism, and $\operatorname{Inn}_U=\operatorname{Inn}_V$ exactly when $V=\lambda U$ for some $\lambda\in\mathbb{C}^{\times}$.

**Proof.** Conjugation preserves products and is invertible. If $UAU^{-1}=VAV^{-1}$ for all $A$, then $V^{-1}U$ commutes with every $A$, hence is scalar.

**Theorem (Skolem–Noether).** Every automorphism of $M_4(\mathbb{C})$ is inner:

$$
\operatorname{Aut}(M_4)=PGL_4(\mathbb{C})=GL_4(\mathbb{C})/\mathbb{C}^{\times}I,
$$

of dimension $15$. In particular there is no outer automorphism.

**Proof.** The theorem is the case $n=4$ of the Skolem–Noether theorem: every isomorphism of central simple algebras is conjugation by an invertible element. The elementary proof uses the module: an automorphism $\varphi$ makes $\mathbb{C}^{4}$ into a second module for $M_4$ by $A\cdot v=\varphi(A)v$, and the two modules are isomorphic because $M_4$ has a unique irreducible module up to isomorphism; an intertwiner $U$ satisfies $\varphi(A)U=UA$, that is, $\varphi(A)=UAU^{-1}$.

**The centre.** The scalar matrices act trivially, so the automorphism group is the quotient $PGL_4$, not $GL_4$. The determinant of $A$ is preserved by every inner automorphism, but the group is not reduced to $SL_4$: conjugation by $U$ and by $\lambda U$ agree for every $\lambda\ne0$, and the correct statement is $PGL_4\cong SL_4/\mu_4$, where $\mu_4$ is the group of fourth roots of unity acting by scalars.

**The Lie algebra.** The Lie algebra of $\operatorname{Aut}(M_4)$ is $\operatorname{Der}(M_4)=\mathfrak{sl}_4$, and the exponential of a derivation is an automorphism: $\exp(\operatorname{ad}_X)(A)=e^{X}Ae^{-X}$. The exponential map of $PGL_4$ is the exponential of $\mathfrak{sl}_4$ modulo the kernel of the adjoint representation.

## The $*$-Structures

**Definition.** A $*$-derivation is a derivation $D$ with $D(A^{*})=D(A)^{*}$ for all $A$. A $*$-automorphism is an automorphism $\varphi$ with $\varphi(A^{*})=\varphi(A)^{*}$.

**Proposition.** A derivation $\operatorname{ad}_X$ is a $*$-derivation exactly when $X$ is skew-Hermitian, $X^{*}=-X$. The $*$-derivations form the real Lie algebra $\mathfrak{u}(4)$ modulo its centre, isomorphic to $\mathfrak{su}(4)$, of real dimension $15$.

**Proof.** For $Y$ arbitrary,

$$
\operatorname{ad}_X(Y)^{*}=[Y,X]^{*}=[X^{*},Y^{*}]=-\operatorname{ad}_{X^{*}}(Y^{*}).
$$

The condition $\operatorname{ad}_X(Y^{*})=\operatorname{ad}_X(Y)^{*}$ for all $Y$ is therefore $\operatorname{ad}_X=\operatorname{ad}_{-X^{*}}$, that is, $X+X^{*}$ is scalar. The scalar part acts trivially, so the condition is that the traceless part of $X$ is skew-Hermitian; the skew-Hermitian matrices form $\mathfrak{u}(4)$ of real dimension $16$, and the scalars $i\theta I$ act trivially, leaving $\mathfrak{su}(4)$ of dimension $15$.

**The $*$-automorphisms.** The automorphism $\operatorname{Inn}_U$ is a $*$-automorphism exactly when $U$ is unitary:

$$
(UAU^{-1})^{*}=UAU^{-1}\quad\text{for all }A
\iff
U^{*}U\in\mathbb{C}^{\times}I.
$$

The group of $*$-automorphisms is therefore $PU(4)=U(4)/U(1)$, of real dimension $15$, the compact real form of $PGL_4$.

**The real structure.** For the real form $M_4(\mathbb{R})$ the derivations are $\operatorname{ad}\mathfrak{sl}_4(\mathbb{R})$, of real dimension $15$, and the automorphisms are $PGL_4(\mathbb{R})$. For the quaternionic form $M_2(\mathbb{H})$ the derivations are $\operatorname{ad}\mathfrak{sl}_2(\mathbb{H})$, and the automorphisms are $PGL_2(\mathbb{H})$; the two real forms are *The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$*.

## The Antilinear Automorphisms

**Definition.** A **complex-antilinear automorphism** is a bijective map $\varphi$ with

$$
\varphi(A+B)=\varphi(A)+\varphi(B),\qquad
\varphi(\lambda A)=\bar\lambda\,\varphi(A),\qquad
\varphi(AB)=\varphi(A)\varphi(B).
$$

**Proposition.** Every antilinear automorphism is of the form

$$
\varphi(A)=U\bar A U^{-1}
$$

for some $U\in GL_4(\mathbb{C})$, and two matrices $U,V$ give the same map exactly when $V=\lambda U$ with $\lambda\in\mathbb{C}^{\times}$.

**Proof.** Composing $\varphi$ with the conjugation $\bar A$ gives a complex-linear automorphism $A\mapsto \varphi(\bar A)$, which is inner by Skolem–Noether: $\varphi(\bar A)=UAU^{-1}$, hence $\varphi(A)=U\bar A U^{-1}$. The ambiguity is the scalar, as for the linear case.

**The group.** The antilinear automorphisms form the coset $PGL_4\cdot\bar{\phantom{A}}$, and

$$
\operatorname{Aut}_\mathbb{R}(M_4)=PGL_4(\mathbb{C})\rtimes\mathbb{Z}/2,
$$

where the nontrivial element acts by $\bar{\phantom{A}}$. The subgroup of complex-linear automorphisms has index two, and the coset is the set of antilinear ones.

**The real forms again.** An antilinear automorphism of order two is a **real structure** on the algebra; its fixed algebra is a real form. The two possibilities, $\varphi^{2}=\mathrm{id}$ and $\varphi^{2}$ an inner automorphism of order two, correspond to the real and quaternionic structures. The classification is *The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$*; the point here is that the antilinear automorphisms are a single coset, and the real forms are the fixed algebras of its involutions.

## The Biquaternion Comparison

**The derivations of $\mathbb{B}$.** The biquaternion algebra $\mathbb{B}\cong M_2(\mathbb{C})$ has derivations

$$
\operatorname{Der}(\mathbb{B})=\operatorname{ad}\mathbb{B}\cong\mathfrak{sl}_2(\mathbb{C}),
$$

of complex dimension $3$, and automorphisms $PGL_2(\mathbb{C})$, of dimension $3$. The inner derivation $\operatorname{ad}_u$ for $u\in\mathbb{B}$ is the infinitesimal rotation of the biquaternion algebra; the three-dimensional algebra is the one generated by the three imaginary units.

**The embedding.** The left factor of the Kronecker decomposition gives an inclusion

$$
\mathfrak{sl}_2(\mathbb{C})\cong\operatorname{ad}(\mathbb{B}\otimes I)\subset\operatorname{ad}\mathfrak{sl}_4=\operatorname{Der}(M_4),
$$

and the right factor gives a second, commuting copy. The two copies are the two factors of *The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$*, and their sum is a six-dimensional subalgebra of the fifteen derivations. The remaining nine derivations mix the two factors: they are the ones that do not preserve the tensor decomposition.

**The physical interpretation.** The derivations of $\mathbb{B}$ are the gauge rotations of the biquaternion algebra, of dimension three; the derivations of $M_4$ are the gauge rotations of the algebra of two-sided operators, of dimension fifteen. The difference of twelve is the price of the passage from the four-dimensional algebra to its sixteen-dimensional endomorphism algebra, and it is the same difference that separates the biquaternion frame from the gamma frame of *The Gamma Frame and the Complexified Dirac Algebra of $M_4(\mathbb{C})$*.

## Summary

Every derivation of $M_4(\mathbb{C})$ is inner, $\operatorname{Der}(M_4)=\operatorname{ad}\mathfrak{sl}_4\cong\mathfrak{sl}_4$ of dimension $15$, with kernel $\mathbb{C}I$; every automorphism is inner, $\operatorname{Aut}(M_4)=PGL_4(\mathbb{C})$ of dimension $15$, with no outer automorphisms. The $*$-derivations are the skew-Hermitian ones, forming $\mathfrak{su}(4)$, and the $*$-automorphisms are $PU(4)$; the antilinear automorphisms form the coset $PGL_4\rtimes\mathbb{Z}/2$. The biquaternion algebra has only a three-dimensional derivation algebra, embedded twice in the fifteen, and the remaining nine derivations mix the two Kronecker factors.

| Quantity | Value |
|---|---|
| $\dim\operatorname{Der}(M_4)$ | $15$ |
| $\operatorname{Der}(M_4)$ | $\operatorname{ad}\mathfrak{sl}_4$ |
| Kernel of $\operatorname{ad}$ | $\mathbb{C}I$ |
| $\dim\operatorname{Aut}(M_4)$ | $15$ |
| $\operatorname{Aut}(M_4)$ | $PGL_4(\mathbb{C})$ |
| Outer automorphisms | none |
| $*$-derivations | $\mathfrak{su}(4)$, dimension $15$ |
| $*$-automorphisms | $PU(4)$, dimension $15$ |
| Antilinear automorphisms | $PGL_4\rtimes\mathbb{Z}/2$ |
| $\dim\operatorname{Der}(\mathbb{B})$ | $3$ |

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\operatorname{Der}(M_4)$ | the Lie algebra of derivations |
| $\operatorname{ad}_X$ | the inner derivation $Y\mapsto [X,Y]$ |
| $\operatorname{Inn}_U$ | the inner automorphism $A\mapsto UAU^{-1}$ |
| $PGL_4$ | $GL_4/\mathbb{C}^{\times}I$, the automorphism group |
| $PU(4)$ | $U(4)/U(1)$, the $*$-automorphism group |
| $\operatorname{Aut}_\mathbb{R}$ | the group of linear and antilinear automorphisms |
| $\mu_4$ | the fourth roots of unity, the kernel of $SL_4\to PGL_4$ |

## Further Reading

- [The Lie Algebra $\mathfrak{gl}_4(\mathbb{C})$ and $\mathfrak{sl}_4(\mathbb{C})$ of $M_4(\mathbb{C})$](the-lie-algebra-gl4-and-sl4-of-m4c.html), for $\mathfrak{sl}_4$ and its root decomposition.
- [The Operators of the Peirce Decomposition of $M_4(\mathbb{C})$](the-operators-of-the-peirce-decomposition-of-m4c.html), for the derivations on the Peirce blocks.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), for the action of $PGL_4$.
- [The Kronecker Factorisation $M_4(\mathbb{C})\cong M_2(\mathbb{C})\otimes M_2(\mathbb{C})$](the-kronecker-factorisation-of-m4c.html), for the two commuting $\mathfrak{sl}_2$'s.
- [The Quaternionic Structure and the Real Forms of $M_4(\mathbb{C})$](the-real-forms-of-m4c.html), for the real and quaternionic structures.
- [The Involution and the Hermitian Structure of $M_4(\mathbb{C})$](the-involution-and-the-hermitian-structure-of-m4c.html), for the $*$-structures.
- Richard S. Pierce, *Associative Algebras* (Springer, 1982), for Wedderburn's and Skolem–Noether's theorems.
- Nathan Jacobson, *Lie Algebras* (Dover, 1979), for the derivations of matrix algebras.
