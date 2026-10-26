# __The Defective Sector of the Dual-Number Algebra__

## Introduction

The preceding article, *Spectral Regularity and Degeneracy in the Dual-Number Algebra*, proved that every element of the dual-number algebra $\mathbb{D}'_R=R[\varepsilon]/(\varepsilon^2)$ is spectrally degenerate: for $Q=a+b\varepsilon$, the characteristic polynomial of left multiplication is $(X-a)^2$ and the spectrum is the singleton $\{a\}$. The repetition of the eigenvalue is universal. The failure of an eigenbasis is not. This article studies the second phenomenon. The **defective sector** is the set of elements whose minimal polynomial has a repeated factor, equivalently the set of elements whose left multiplication is not diagonalisable, equivalently the set of elements for which no basis of eigenvectors exists. The main theorem identifies it:

$$
D = \{Q = a + b\varepsilon : b\neq0\} = \mathbb{D}'_R\setminus R\cdot1.
$$

The real axis $R\cdot1$, where $b=0$, is the semisimple stratum. The maximal ideal $\mathrm{M}=\{a=0\}$ is not the defective sector: it is the union of the real point $0$, which is semisimple, and the nilpotent stratum $D_0=\mathrm{M}\setminus\{0\}$, which is defective. The defect is carried by the nilpotent part $Q-a=b\varepsilon$; the defective sector is the preimage of $\mathrm{M}\setminus\{0\}$ under the projection $Q\mapsto Q-\operatorname{Re}Q$, and not the maximal ideal itself. This distinction is the subject of the first section and the reason the article separates three strata rather than two.

**Notation.** The algebra is $\mathbb{D}'_R$ over a real closed field $R$, with the geometric case $R=\mathbb{R}$; a general element is $Q=a+b\varepsilon$ with $a=\operatorname{Re}Q$ and $b=\operatorname{Inf}Q$. The norm is $\langle Q\rangle=Q\bar Q=a^2$, dual conjugation is $\bar Q=a-b\varepsilon$, and $\mathrm{M}=(\varepsilon)=\{a=0\}$. In the prime notation of *Dual-Numbers Algebra* the element is $Q=q+\varepsilon q'$, with $a=q$ and $b=q'$. The matrix-element representation $\mathsf{M}_2(Q)=\begin{pmatrix}a&b\\0&a\end{pmatrix}$ and the regular representation $[L_Q]_{(1,\varepsilon)}=\begin{pmatrix}a&0\\b&a\end{pmatrix}$ are those of *Dual-Numbers Matrix Element Representation* and *Dual-Numbers Element Representations*. The polar decomposition is *Dual-Numbers Polar Decomposition*, the module theory is *Modules over $k[x]$ and the Jordan Form*, and the biquaternion comparison is *The Spectrum*.

## The Defective Set

**Semisimplicity is the squarefreeness of the minimal polynomial; in the dual algebra that is a single condition on the infinitesimal part.**

**Definition (semisimple, defective).** An element $Q\in\mathbb{D}'_R$ is **semisimple** if its minimal polynomial $m_Q$ is squarefree, equivalently if $L_Q$ is diagonalisable over $R$. It is **defective** if it is not semisimple, equivalently if $m_Q$ has a repeated factor, equivalently if the geometric multiplicity of its eigenvalue is strictly less than its algebraic multiplicity. The **defective set** is

$$
D = \{Q\in\mathbb{D}'_R : Q \text{ is defective}\}.
$$

**Definition (eigenbasis).** An **eigenbasis** of $Q$ is a basis of $\mathbb{D}'_R$ consisting of eigenvectors of $L_Q$.

**Lemma (the minimal polynomial).** For $Q=a+b\varepsilon$,

$$
m_Q(X) = \begin{cases} X-a, & b=0, \\ (X-a)^2, & b\neq0. \end{cases}
$$

*Proof.* This is the dichotomy of *Spectral Regularity and Degeneracy in the Dual-Number Algebra*, §*The Minimal Polynomial Dichotomy*: $Q-a=b\varepsilon$ has square zero, is zero exactly when $b=0$, and no linear polynomial other than $X-a$ can annihilate $Q$ when $Q-a\neq0$.

**Theorem (the defective set).** The defective set is the complement of the real axis:

$$
D = \{a+b\varepsilon : b\neq0\} = \mathbb{D}'_R\setminus R\cdot1.
$$

*Proof.* By the lemma, $m_Q=X-a$ is squarefree when $b=0$, so $Q$ is semisimple. When $b\neq0$, $m_Q=(X-a)^2$ has the repeated factor $X-a$, so $Q$ is defective. The real axis is exactly the set $b=0$.

**Remark (the maximal ideal is not the defective set).** The maximal ideal $\mathrm{M}=\{a=0\}$ contains the origin, which is semisimple, and the punctured line $\mathrm{M}\setminus\{0\}=\{b\varepsilon:b\neq0\}$, which is defective. It does not contain the defective units $a+b\varepsilon$ with $a\neq0$ and $b\neq0$. The correct statement is that the defect is carried by the nilpotent part: the map

$$
\nu : \mathbb{D}'_R\longrightarrow \mathrm{M}, \qquad \nu(Q) = Q-\operatorname{Re}Q = b\varepsilon,
$$

is the projection onto $\mathrm{M}$ along the real axis, and

$$
D = \nu^{-1}(\mathrm{M}\setminus\{0\}).
$$

So $\mathrm{M}\setminus\{0\}$ is the set of possible non-zero nilpotent parts, and the defective set is the union of the fibres of $\nu$ over that punctured line. This is the precise sense in which the defect lives in the maximal ideal: it lives in the nilpotent part, not in the real part.

## The Semisimple Stratum

**The real axis is the whole semisimple locus, and it is a field sitting inside the local ring.**

**Theorem (the semisimple stratum).** The semisimple locus of $\mathbb{D}'_R$ is the real axis

$$
S = R\cdot1 = \{a : a\in R\},
$$

a subalgebra isomorphic to $R$. Its units are $R^\times$, and its only non-unit is the origin. The algebra is the disjoint union

$$
\mathbb{D}'_R = S \sqcup D,
$$

of the semisimple stratum and the defective sector.

*Proof.* The semisimple locus is $\{b=0\}$ by the theorem of the preceding section, and that is $R\cdot1$. It is closed under addition and multiplication and contains $1$, so it is a subalgebra isomorphic to $R$. Its unit group is $R^\times$ because $a$ is invertible in $R$ exactly when $a\neq0$, and the only element that is not a unit is $0$. The disjoint-union statement is the partition into $b=0$ and $b\neq0$.

**Corollary (the two defective strata).** The defective sector splits into two strata:

$$
D_0 = D\cap\mathrm{M} = \mathrm{M}\setminus\{0\} = \{b\varepsilon : b\neq0\},
\qquad
D_1 = D\cap(\mathbb{D}'_R)^\times = \{a+b\varepsilon : a\neq0,\ b\neq0\}.
$$

The stratum $D_0$ is the **nilpotent stratum**; its elements are the non-zero nilpotents, they are non-units and zero divisors, and they satisfy $Q^2=0$. The stratum $D_1$ is the **unipotent stratum**; its elements are units, and each is $Q=a(1+s\varepsilon)$ with $s=b/a\neq0$, where $1+s\varepsilon$ is a unipotent element with $(1+s\varepsilon-1)^2=0$.

*Proof.* The intersection of $D$ with $\mathrm{M}$ is $\{a=0,b\neq0\}$; these are exactly the non-zero elements of the maximal ideal, and they square to zero. The intersection with the unit group is $\{a\neq0,b\neq0\}$, since the units are $a\neq0$; dividing by $a$ gives the unipotent form, and $(s\varepsilon)^2=0$.

**The three strata.**

| stratum | condition | form | $Q^2$ | $m_Q$ | Jordan type | unit |
|---|---|---|---|---|---|---|
| semisimple $S$ | $b=0$ | $a$ | $a^2$ | $X-a$ | $aI$ | iff $a\neq0$ |
| nilpotent $D_0$ | $a=0$, $b\neq0$ | $b\varepsilon$ | $0$ | $X^2$ | $J_2(0)$ | no |
| unipotent $D_1$ | $a\neq0$, $b\neq0$ | $a(1+s\varepsilon)$ | $a^2+2ab\varepsilon$ | $(X-a)^2$ | $J_2(a)$ | yes |

**Corollary (the origin).** The origin is the unique semisimple non-unit. It is the vertex of the maximal ideal, the point at which the nilpotent stratum is punctured, and it is not defective. The defect of the maximal ideal is therefore $\mathrm{M}\setminus\{0\}$, not $\mathrm{M}$.

*Proof.* The semisimple elements are $a$ with $b=0$, and such an element is a non-unit exactly when $a=0$. The remaining statements are the definitions of $D_0$ and of the origin.

## The Jordan Type and the Non-Uniqueness of the Eigenbasis

**Off the real axis there is one eigenvector line and one Jordan chain; the line is canonical, the chain is not.**

**Theorem (the Jordan form).** Let $Q=a+b\varepsilon$ with $b\neq0$. In the basis $(\varepsilon,b^{-1})$ the matrix of $L_Q$ is

$$
[L_Q]_{(\varepsilon,b^{-1})} = \begin{pmatrix} a & 1 \\ 0 & a \end{pmatrix} = J_2(a).
$$

The eigenspace is $E_a=R\varepsilon$, of dimension one; the generalized eigenspace is all of $\mathbb{D}'_R$; and the Jordan type is the single block $(2)$. On the real axis the matrix is $aI$ in every basis, and the Jordan type is $(1,1)$.

*Proof.* The computation is that of *Spectral Regularity and Degeneracy in the Dual-Number Algebra*, §*The Jordan Form*:

$$
L_Q(\varepsilon)=a\varepsilon, \qquad
L_Q(b^{-1})=a b^{-1}+\varepsilon.
$$

The generalized eigenspace is $\ker(L_Q-a)^2$, and $(L_Q-a)^2=b^2L_\varepsilon^2=0$; so it is everything. The eigenspace is $\ker(bL_\varepsilon)=R\varepsilon$.

**Corollary (no eigenbasis).** For $b\neq0$ the geometric multiplicity of $a$ is one and the algebraic multiplicity is two, so there is no eigenbasis. The defect is exactly the gap between the two multiplicities.

*Proof.* The geometric multiplicity is $\dim E_a=1$; the algebraic multiplicity is the multiplicity of the root in $p_Q=(X-a)^2$, namely two. An eigenbasis would require the geometric multiplicity to equal the dimension of the space, which is two.

**Remark (the non-uniqueness of the Jordan basis).** The eigenvector is not unique: every non-zero element of $R\varepsilon$ is an eigenvector, so it is determined only up to a non-zero scalar. The cyclic vector is determined only up to adding an eigenvector. For every $\lambda\in R^\times$ and every $\mu\in R$,

$$
v_1=\lambda\varepsilon, \qquad v_2=\lambda b^{-1}+\mu\varepsilon,
$$

is a Jordan basis, because $(L_Q-a)v_1=0$ and

$$
(L_Q-a)v_2 = bL_\varepsilon(\lambda b^{-1}+\mu\varepsilon)=\lambda\varepsilon=v_1.
$$

The pair is a Jordan basis for every choice of $\lambda$ and $\mu$; the normalized choice $\lambda=1$, $\mu=0$ gives the basis of the theorem. Thus the eigenvector line is unique, the Jordan chain is not, and the matrix in any Jordan basis is the same $J_2(a)$. The non-uniqueness is not an ambiguity of the Jordan form; it is the freedom of choosing a splitting of the projection onto the quotient by the eigenvector line, and that splitting is not canonical. There is no eigenbasis because no splitting by eigenvectors exists.

## The Module Picture

**The defect is the non-splitting of a short exact sequence of $R[X]$-modules.**

Let $A=R[X]$ and let $M_Q$ be the abelian group $\mathbb{D}'_R$ with the $A$-module structure

$$
X\cdot v = Qv.
$$

**Theorem (the module structure).**

1. If $b=0$, then $M_Q\cong R[X]/(X-a)\oplus R[X]/(X-a)$; the module is a direct sum of two copies of the simple module $R[X]/(X-a)$, and it is semisimple.
2. If $b\neq0$, then $M_Q\cong R[X]/((X-a)^2)$; the module is indecomposable of length two, with a unique simple submodule $R\varepsilon$ and quotient $\mathbb{D}'_R/R\varepsilon\cong R$.

*Proof.* The evaluation map $A\to\mathbb{D}'_R$, $f\mapsto f(Q)$, has kernel $(m_Q)$ and image $R[Q]$. If $b=0$, $Q=a$ and the image is $R\cdot1$; the module is the regular module of $R$, that is, two copies of $R[X]/(X-a)$. If $b\neq0$, then $Q-a=b\varepsilon$ is a non-zero element of $\mathbb{D}'_R$, so $1$ and $Q-a$ generate $\mathbb{D}'_R$ over $R$; hence $R[Q]=\mathbb{D}'_R$, and the evaluation map induces an isomorphism $R[X]/((X-a)^2)\to\mathbb{D}'_R$. The submodule $R\varepsilon$ is simple because $X$ acts on it as $a$, and the quotient is $R$ with $X$ acting as $a$; both are isomorphic to $R[X]/(X-a)$.

**Corollary (the non-split extension).** For $b\neq0$ there is a short exact sequence of $A$-modules

$$
0 \longrightarrow R\varepsilon \longrightarrow M_Q \longrightarrow \mathbb{D}'_R/R\varepsilon \longrightarrow 0,
$$

both ends isomorphic to $R[X]/(X-a)$, which does not split. The defect is the non-splitting.

*Proof.* A splitting would give a submodule $S$ complementary to $R\varepsilon$, hence a one-dimensional $R$-subspace $S=Rv$ with $v\notin R\varepsilon$ and $Qv=av$. But $\ker(L_Q-a)=R\varepsilon$, so no such $v$ exists. Hence the sequence does not split, and $M_Q$ is not semisimple.

## Relation to the Polar Decomposition

**The polar decomposition of a unit separates its scale and sign, which are blind to the defect, from its parabolic angle, which is the defect coordinate.**

**Theorem (the polar form).** Every unit $Q=a+b\varepsilon$, with $a\neq0$, has a unique representation

$$
Q = r\,u\,\exp(s\varepsilon), \qquad r=|a|>0, \quad u=\operatorname{sgn}(a)\in\{\pm1\}, \quad s=\frac{b}{a},
$$

where $\exp(s\varepsilon)=1+s\varepsilon$. This is the polar decomposition of *Dual-Numbers Polar Decomposition*.

**Proposition (the defect is the parabolic angle).** For a unit $Q$ the following are equivalent:

1. $Q$ is semisimple;
2. $Q$ lies on the real axis;
3. $s=0$;
4. the shear factor $\exp(s\varepsilon)$ is the identity.

The unit is defective exactly when $s\neq0$, that is, exactly when its unipotent factor is not the identity. The shear factor $1+s\varepsilon$ has minimal polynomial $X-1$ when $s=0$ and $(X-1)^2$ when $s\neq0$.

*Proof.* The equivalences are the definition $s=b/a$ with $a\neq0$ and the semisimple criterion $b=0$. The minimal polynomial of $1+s\varepsilon$ is computed from $(1+s\varepsilon)-1=s\varepsilon$, which is zero exactly when $s=0$ and has square zero in every case.

**Corollary (the modulus and the sign are defect-blind).** The modulus $r=|a|$ and the sign $u=\operatorname{sgn}(a)$ depend only on the real part; they are constant along each line $a+\mathrm{M}$, on which the defect varies, so they do not detect it. The parabolic angle $s=b/a$ is the only polar coordinate that detects the defect.

*Proof.* The formulae for $r$ and $u$ involve only $a$; along a line $a+\mathrm{M}$ the real part is fixed and $b$ varies, so $r$ and $u$ are constant while $s$ varies. The single coordinate that vanishes exactly on the real axis is $s$.

## Contrast with the Defect on the Biquaternion Nilpotent Cone

**The dual algebra is the two-dimensional local model of one Jordan block of the biquaternion defect.**

In the biquaternion algebra $\mathbb{B}$, the spectral-degenerate cone is

$$
\mathcal S=\{B^2=0\}, \qquad B^2=Q_x^2+Q_y^2+Q_z^2,
$$

and it splits into three strata, exactly as in *The Spectrum*:

| stratum of $\mathcal S$ | condition | minimal polynomial | Jordan type | defect |
|---|---|---|---|---|
| scalar | $\vec Q=0$ | $X-Q_t$ | $(1,1,1,1)$ | semisimple |
| nilpotent | $Q_t=0$, $\vec Q\neq0$ | $X^2$ | $(2,2)$ | defective |
| unipotent | $Q_t\neq0$, $\vec Q\neq0$ | $(X-Q_t)^2$ | $(2,2)$ | defective |

**The nilpotent cone.** The nilpotent cone in the strict sense is

$$
\mathcal N_0=\{Q_t=0,\ B^2=0\}=\{\tilde Q : \vec Q^2=0\}.
$$

It contains the origin, which is scalar and semisimple, and the non-zero nilpotents, which are defective. The defect is therefore not the whole nilpotent cone: it is the cone with its vertex removed. The same statement holds in the dual algebra, where the maximal ideal $\mathrm{M}$ contains the semisimple origin and the defective punctured line $\mathrm{M}\setminus\{0\}$. The vertex is the one point at which the defect disappears.

**The unipotent stratum.** The defect in $\mathbb{B}$ is not confined to the nilpotent cone. The unipotent stratum $Q_t\neq0$, $\vec Q\neq0$ consists of units, and every element of it is defective. The same is true in $\mathbb{D}'$: the stratum $D_1$ consists of units and every element of it is defective. In both algebras the defect has the same two parts, a nilpotent one and a unipotent one, separated by the scalar part.

**The correspondence.** The table records the matching.

| $\mathbb{B}$ | $\mathbb{D}'$ |
|---|---|
| centre $\mathbb{C}e_t$, scalar stratum $\vec Q=0$ | real axis $R\cdot1$, semisimple stratum $b=0$ |
| nilpotent stratum $Q_t=0$, $\vec Q\neq0$ | nilpotent stratum $a=0$, $b\neq0$ |
| unipotent stratum $Q_t\neq0$, $\vec Q\neq0$ | unipotent stratum $a\neq0$, $b\neq0$ |
| spectral-degenerate cone $\mathcal S$, complex dimension $3$ | defective sector $D$, real dimension $2$ |
| eigenspace complex dimension $2$ | eigenspace real dimension $1$ |
| Jordan type $(2,2)$ | Jordan type $(2)$ |
| algebra generated: $\mathbb{C}[\vec Q]\cong\mathbb{C}[X]/(X^2)$ | algebra generated: $\mathbb{D}'_R\cong R[X]/(X^2)$ |

**The differences.** Three differences are differences of dimension. The biquaternion defect sits inside the proper hypersurface $\mathcal S$ of a four-complex-dimensional algebra, and there are spectrally regular biquaternions off $\mathcal S$; the dual defect is the complement of a real line in a two-real-dimensional algebra, and there are no spectrally regular elements. The biquaternion defect has Jordan type $(2,2)$ on a four-dimensional space with a two-dimensional eigenspace; the dual defect has type $(2)$ on a two-dimensional space with a one-dimensional eigenspace. The semisimple stratum in $\mathbb{B}$ is the centre $\mathbb{C}e_t$; in $\mathbb{D}'$ it is the real axis $R\cdot1$, which is not the centre because the algebra is commutative. What the cases share is the local structure: the algebra generated at a defective dual point is $R[Q]=R[X]/(X^2)$, with $Q-a=b\varepsilon$ nilpotent and non-zero, and at a defective biquaternion point it is $\mathbb{C}[\vec Q]=\mathbb{C}[X]/(X^2)$ on each of the two blocks; the defect is the single Jordan block of that local algebra.

*Proof.* The biquaternion strata and Jordan types are *The Spectrum*, §*The Degenerate Case: The Cone*; the dual strata and types are the theorems of this article. The dimension counts are those of $\mathcal S$ (one complex equation in four complex coordinates) and of $D$ (the complement of a real line in the real plane).

## Summary

The defective sector of the dual-number algebra is $D=\{a+b\varepsilon:b\neq0\}=\mathbb{D}'\setminus R\cdot1$, not the maximal ideal. The maximal ideal $\mathrm{M}$ contains the semisimple origin and the defective nilpotent stratum $\mathrm{M}\setminus\{0\}$; the defect is carried by the nilpotent part $b\varepsilon$, and $D$ is its preimage under $Q\mapsto b\varepsilon$. The semisimple stratum is the real axis $R\cdot1$, a subalgebra isomorphic to $R$ whose only non-unit is the origin. The defective sector splits into the nilpotent stratum $D_0=\mathrm{M}\setminus\{0\}$, with $Q^2=0$, $m_Q=X^2$ and Jordan type $J_2(0)$, and the unipotent stratum $D_1=\{a\neq0,b\neq0\}$, with $Q=a(1+s\varepsilon)$, $s=b/a\neq0$, $m_Q=(X-a)^2$ and Jordan type $J_2(a)$.

Off the real axis the eigenspace is the line $R\varepsilon$, the generalized eigenspace is everything, and the operator is the single block $J_2(a)$ in the basis $(\varepsilon,b^{-1})$. There is no eigenbasis; the eigenvector line is canonical but the Jordan chain is not, the general basis being $(\lambda\varepsilon,\lambda b^{-1}+\mu\varepsilon)$ with $\lambda\neq0$. In the module picture, $M_Q$ is $R[X]/(X-a)\oplus R[X]/(X-a)$ when $b=0$ and the indecomposable $R[X]/((X-a)^2)$ when $b\neq0$; the defect is the non-splitting of $0\to R\varepsilon\to M_Q\to\mathbb{D}'/R\varepsilon\to0$.

The polar decomposition $Q=ru\exp(s\varepsilon)$ exposes the defect as the parabolic angle: $r=|a|$ and $u=\operatorname{sgn}(a)$ are blind to it, and $Q$ is defective exactly when $s\neq0$; it is defined on the unit group and fails on the nilpotent stratum, where the scale vanishes. The biquaternion cone has the same three strata, with the origin of its nilpotent cone as the semisimple vertex; the dual algebra is the two-dimensional local model of one Jordan block, with type $(2)$ in place of $(2,2)$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{D}'_R=R[\varepsilon]/(\varepsilon^2)$ | the dual-number algebra over $R$ |
| $Q=a+b\varepsilon$ | a general element, equal to $q+\varepsilon q'$ in the prime notation |
| $a=\operatorname{Re}Q$, $b=\operatorname{Inf}Q$ | real and infinitesimal parts |
| $\langle Q\rangle=a^2$ | the norm, the dual norm |
| $\mathrm{M}=(\varepsilon)=\{a=0\}$ | the maximal ideal |
| $m_Q$ | the minimal polynomial: $X-a$ if $b=0$, $(X-a)^2$ if $b\neq0$ |
| $D$ | the defective sector $\{b\neq0\}$ |
| $S=R\cdot1$ | the semisimple stratum $\{b=0\}$ |
| $D_0=\mathrm{M}\setminus\{0\}$ | the nilpotent stratum $\{a=0,b\neq0\}$ |
| $D_1=\{a\neq0,b\neq0\}$ | the unipotent stratum |
| $\nu(Q)=Q-\operatorname{Re}Q=b\varepsilon$ | the nilpotent part, the projection onto $\mathrm{M}$ |
| $L_Q$ | left multiplication, $L_Q(v)=Qv$ |
| $J_2(a)=\begin{pmatrix}a&1\\0&a\end{pmatrix}$ | the Jordan block of the defective sector |
| $M_Q$ | $\mathbb{D}'_R$ as an $R[X]$-module with $X\cdot v=Qv$ |
| $r=\lvert a\rvert$, $u=\operatorname{sgn}(a)$, $s=b/a$ | the polar data of a unit |

## Further Reading

- [Dual-Numbers Algebra](dual-numbers-algebra.html), for the algebra, the maximal ideal and the two conjugations.
- [Dual-Numbers Norm and Invertibility](dual-numbers-norm-and-invertibility.html), for the norm, the unit criterion and the Euclidean form.
- [Dual-Numbers Zero Divisors](dual-numbers-zero-divisors.html), for the nilpotent stratum and the zero-divisor set.
- [Dual-Numbers Polar Decomposition](dual-numbers-polar-decomposition.html), for the decomposition $Q=ru\exp(s\varepsilon)$ and the parabolic angle.
- [Shears and Parabolic Rotations](shears-and-parabolic-rotations.html), for the shear group $1+\mathrm{M}$ and its parametrisation.
- [Dual-Numbers Matrix Element Representation](dual-numbers-matrix-element-representation.html), for the matrix model and the Jordan form of the nilpotent.
- [Dual-Numbers Element Representations](dual-numbers-element-representations.html), for the regular representation.
- [Spectral Regularity and Degeneracy in the Dual-Number Algebra](spectral-regularity-and-degeneracy-in-the-dual-number-algebra.html), for the characteristic polynomial, the minimal polynomial dichotomy and the one-term decomposition.
- [Relations between the Dual Norm and Spectral Degeneracy](relations-between-the-dual-norm-and-spectral-degeneracy.html), for the comparison of the norm and the defect.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the three strata of the biquaternion spectral-degenerate cone.
- [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for semisimplicity, defect and the additive decomposition.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html), for the structure theorem behind the module picture.
- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (2nd edition, Cambridge University Press, 2013), for the Jordan form and the geometric multiplicity.
- Nicholas Bourbaki, *Algebra I* (Springer, Berlin, 1989), for semisimple modules and the Jordan–Chevalley decomposition.
