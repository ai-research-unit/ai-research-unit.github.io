
# __Cyclic Homology__

## Introduction

The Hochschild complex of an algebra $A$ carries a symmetry that the homology forgets: the $n$-chains are tensors $a_0\otimes a_1\otimes\cdots\otimes a_n$ on which the cyclic group of order $n+1$ acts by cyclically permuting the factors with a sign, and the permutation commutes with the Hochschild boundary only up to that sign. The **cyclic homology** $HC_{\bullet}(A)$ is the homology of a bicomplex built from this action, and it is a different invariant from the Hochschild homology, neither a quotient nor a subgroup of it in any naive sense. It is the natural home of two constructions: the **Connes boundary** $B$, which is not a differential of the Hochschild complex but intertwines it with the cyclic one, and the periodic complex, in which $B$ and the Hochschild boundary $b$ are placed together and the whole becomes $\mathbb{Z}/2$-graded. The result is a long exact sequence — the **Connes sequence**, or $SBI$ sequence — relating the Hochschild and cyclic homologies of $A$, and a second, the change from cyclic to periodic cyclic homology.

This article develops the cyclic category and cyclic modules, the cyclic and periodic cyclic complexes, the Connes boundary and the $SBI$ exact sequence, the computation for smooth commutative algebras in terms of differential forms and the de Rham cohomology, the comparison with Hochschild homology, the Morita invariance, and the trace maps from algebraic K-theory that motivate the theory. It follows *Hochschild Homology*, *K-Theory of Rings* and *Derived Categories*, and it preparesand the higher structures of the category.

Two distinctions must be stated at the outset. First, **cyclic cohomology is a different invariant despite the name**: it belongs to Part III, where it is treated, and it is built from the same cyclic object by taking the dual, with the additional structure of a topological vector space on which the theory of Part III operates; nothing in the present article depends on it, and the present article supplies its algebraic input. Second, the ground ring is commutative and the algebra is discrete; the analytic completions, the traces on operator algebras and the cyclic cohomology of Fréchet algebras all belong to Part III and are not used.

Throughout, $k$ is a commutative ring with $1\neq0$, $A$ is an associative $k$-algebra with unit, and tensors are over $k$; the Hochschild complex, the Kähler differentials $\Omega^p_{A/k}$ and the enveloping algebra $A^{\mathrm{e}}$ are those of *Hochschild Homology*. No distance, norm, open set or completion occurs. A trace means a $k$-linear functional annihilating the commutators, as in *K-Theory of Rings*.

## The Cyclic Category and Cyclic Modules

### The Cyclic Category

**Definition.** The **cyclic category** $\Lambda$ has as objects the finite sets $[n]=\{0,1,\dots,n\}$ for $n\ge0$, and as morphisms the maps that are compositions of the **coface** maps $\delta_i:[n-1]\to[n]$, the **codegeneracy** maps $\sigma_i:[n+1]\to[n]$ and the **cyclic** maps $\tau_n:[n]\to[n]$, subject to the cosimplicial relations together with

$$
\tau_n\delta_i=\delta_{i-1}\tau_{n-1}\ (1\le i\le n), \qquad \tau_n\delta_0=\delta_n, \qquad \tau_n\sigma_i=\sigma_{i-1}\tau_{n+1}\ (1\le i\le n), \qquad \tau_n\sigma_0=\sigma_n\tau_{n+1}^2, \qquad \tau_n^{n+1}=\operatorname{id}.
$$

A **cyclic module** is a contravariant functor from $\Lambda$ to the category of $k$-modules; a **cyclic object** in a category $\mathcal{C}$ is a covariant functor from $\Lambda^{\mathrm{op}}$ to $\mathcal{C}$. A cyclic module is thus a simplicial module, from the coface and codegeneracy data, together with the extra **cyclic operators** $t_n$ coming from $\tau_n$, and a simplicial module is cyclic exactly when it carries operators $t_n$ of order dividing $n+1$ satisfying the compatibility relations.

**Proposition (cyclic nerve).** For a $k$-algebra $A$ the assignment $[n]\mapsto A^{\otimes(n+1)}$ extends to a cyclic module, with the simplicial structure

$$
\partial_i(a_0\otimes\cdots\otimes a_n)=a_0\otimes\cdots\otimes a_ia_{i+1}\otimes\cdots\otimes a_n \quad (0\le i\le n-1),
$$

$$
\partial_n(a_0\otimes\cdots\otimes a_n)=a_na_0\otimes a_1\otimes\cdots\otimes a_{n-1},
$$

$$
s_j(a_0\otimes\cdots\otimes a_n)=a_0\otimes\cdots\otimes a_j\otimes1\otimes a_{j+1}\otimes\cdots\otimes a_n,
$$

and the cyclic operators $t_n(a_0\otimes\cdots\otimes a_n)=(-1)^n a_n\otimes a_0\otimes\cdots\otimes a_{n-1}$. The $k$-module $C_n(A)=A^{\otimes(n+1)}$ with the Hochschild boundary $b=\sum_i(-1)^i\partial_i$ is the **Hochschild complex**, and the operators $t_n$ satisfy $t_n^{n+1}=\operatorname{id}$ together with the compatibility relations with the face and degeneracy maps that define the cyclic category. This is the **cyclic nerve** of $A$, and the sign $(-1)^n$ in $t_n$ is the Koszul sign of moving $a_n$ past the $n$ preceding factors.

*Proof.* The simplicial identities are the standard ones for the tensor algebra, verified by direct computation with the two cases of $\partial_i$. The compatibility relations of the cyclic category are checked from the definitions; the relation $t_n^{n+1}=\operatorname{id}$ is the statement that a cyclic permutation of $n+1$ factors returns to the start, with Koszul sign $(-1)^{n(n+1)}=1$. $\square$

### The Cyclic and Periodic Complexes

**Definition.** The **cyclic bicomplex** $CC_{p,q}(A)=C_q(A)$ for $p,q\ge0$ has vertical differential $b:C_q\to C_{q-1}$ and horizontal differential $1-t$ for $p$ even and $N=1+t+\cdots+t^q$ for $p$ odd, the signs being chosen so that the horizontal and vertical differentials anticommute. The **cyclic homology** $HC_{\bullet}(A)$ is the homology of the total complex of this bicomplex:

$$
HC_n(A)=H_n\bigl(\operatorname{Tot}CC_{\bullet\bullet}(A)\bigr).
$$

**Remark.** The quotient complex $(C_{\bullet}(A)/\operatorname{im}(1-t),\,b)$ is **not** in general a complex whose homology is the cyclic homology of $A$: for $A=k$ it would give the wrong answer in degree $2$. The total complex of the bicomplex, which retains the column of $N$ as well as the column of $1-t$, is the object whose homology is $HC_{\bullet}(A)$; the failure of the naive quotient is the reason the theory is genuinely larger than the Hochschild homology rather than a quotient of it.

**Definition.** The **Connes boundary** $B:C_n(A)\to C_{n+1}(A)$ is

$$
B=(1-t)s_0N, \qquad N=1+t+t^2+\cdots+t^n \text{ on degree } n,
$$

where $s_0$ is the degeneracy inserting the unit and $N$ is the summation operator, called the norm operator in the cyclic literature (it is an operator on the cyclic complex, not a norm on a module).

**Proposition.** The operators satisfy $b^2=0$, $B^2=0$ and $bB+Bb=0$ on $C_\bullet(A)$; hence $(C_\bullet(A),b,B)$ is a **mixed complex**, and the cyclic bicomplex is its associated double complex.

*Proof.* $b^2=0$ is the simplicial identity. $B^2=0$ follows from the relations among $s_0$, $N$ and $t$, together with $t^{n+1}=\operatorname{id}$. The anticommutation $bB+Bb=0$ is the compatibility of the simplicial and cyclic structures, computed directly from the definitions. $\square$

**Definition.** The **periodic cyclic complex** is the product of infinitely many columns,

$$
CC^{\mathrm{per}}_n=\prod_{p\ge0}C_{n-2p}(A)
$$

with the total differential $b+B$, and **periodic cyclic homology** is $HP_n(A)=H_n(CC^{\mathrm{per}}_\bullet(A))$. The periodic theory is $\mathbb{Z}/2$-periodic, $HP_n\cong HP_{n+2}$.

**Definition.** In the $SBI$ sequence, the **$S$ operator** is the map $HC_n\to HC_{n-2}$ induced by the projection of the total complex of the cyclic bicomplex onto its first column, the **$I$ operator** is the map $HH_n\to HC_n$ induced by the inclusion of the Hochschild complex as the zeroth column, and the **$B$ operator** is the map $HC_{n}\to HH_{n+1}$ induced by the Connes boundary.

**Theorem (Connes, $SBI$ sequence).** For every $k$-algebra $A$ there is a long exact sequence

$$
\cdots\xrightarrow{\ B\ }HH_n(A)\xrightarrow{\ I\ }HC_n(A)\xrightarrow{\ S\ }HC_{n-2}(A)\xrightarrow{\ B\ }HH_{n-1}(A)\to\cdots
$$

natural in $A$, where $HH_n=HH_n(A,A)$ and $HC_n=HC_n(A)$; the sequence is periodic in the sense that the same three operators repeat every two degrees. There is also an exact sequence comparing cyclic and periodic homology,

$$
\cdots\to HC_{n-1}(A)\xrightarrow{\ S\ }HC_{n-3}(A)\to HP_{n}(A)\to HC_n(A)\xrightarrow{\ S\ }HC_{n-2}(A)\to\cdots
$$

obtained by taking the inverse limit of the $S$ maps, and when the $S$ maps are eventually isomorphisms the periodic homology is the direct sum of two copies of the cyclic homology in the limit.

*Proof (in outline).* The cyclic bicomplex has two spectral sequences, one filtering by columns and computing $HC$, the other filtering by rows and computing $HH$; the exact sequence of a double complex with a first-quadrant shape, together with the identification of the $E^2$-terms of the two filtrations, produces the $SBI$ sequence. The periodic sequence is the long exact sequence of the colimit of the cyclic complexes along $S$, and the final statement is the exactness of the resulting Milnor sequence. $\square$

**Example.** If $A$ is a field $k$, then $C_n(k)=k$ for all $n$, the cyclic operator in degree $n$ is multiplication by $(-1)^n$, and the Hochschild boundary in degree $n$ is multiplication by $1-1+1-\cdots+(-1)^n$, which is $1$ for $n$ even and $0$ for $n$ odd. Hence $HH_0(k)=k$ and $HH_n(k)=0$ for $n\ge1$. The $SBI$ sequence with these values gives, inductively from $HC_{-1}=HC_{-2}=0$,
$$
HC_0(k)\cong k,\qquad HC_{2m}(k)\cong k\ (m\ge1),\qquad HC_{2m+1}(k)=0,
$$
and correspondingly $HP_0(k)\cong k$ and $HP_1(k)=0$. In particular $HC_2(k)$ is one-dimensional, which the naive quotient complex $C_{\bullet}(k)/\operatorname{im}(1-t)$ does not see; this is the example behind the remark above.

## Comparison with Hochschild Homology

### Consequences of the $SBI$ Sequence

**Theorem.** The $I$ operator induces an isomorphism $HC_0(A)\cong HH_0(A)=A/[A,A]$, and the $SBI$ sequence in low degrees gives an exact sequence

$$
HH_0(A)\xrightarrow{\ B\ }HH_1(A)\xrightarrow{\ I\ }HC_1(A)\to0.
$$

Hence $HC_1(A)\cong HH_1(A)/B(HH_0(A))$, the cokernel of the Connes boundary in degree zero. More generally the Connes boundary gives an exact sequence

$$
HH_2(A)\xrightarrow{\ I\ }HC_2(A)\xrightarrow{\ S\ }HC_0(A)\xrightarrow{\ B\ }HH_1(A)\xrightarrow{\ I\ }HC_1(A)\to0.
$$

In general the kernel of $S:HC_n\to HC_{n-2}$ is the image of $HH_n$ and the cokernel of $B:HH_n\to HC_{n+1}$ is the image of $S:HC_{n+1}\to HC_{n-1}$; the successive quotients of the filtration by the image of $S$ are the Hochschild homologies.

*Proof.* The $SBI$ sequence in low degrees, with the known vanishing $HC_{-1}=HC_{-2}=0$, gives the displayed sequence; $HC_0\cong HH_0$ is the statement that the zeroth column of the cyclic bicomplex is the Hochschild complex, and the identification of $HC_1$ follows from the four-term sequence. $\square$

**Corollary.** If the Connes boundary vanishes identically, $B=0$ on $HH_n(A)$ for all $n$, then the mixed complex splits and

$$
HC_n(A)\cong\bigoplus_{j\ge0}HH_{n-2j}(A).
$$

This is the case for $A=k$, where $HH_n(k)=0$ for $n\ge1$, and it gives $HC_{2m}(k)\cong k$, $HC_{2m+1}(k)=0$ again.

### The Smooth Commutative Case

**Theorem.** Let $A$ be a commutative $k$-algebra smooth over $k$ and let $d:\Omega^p_{A/k}\to\Omega^{p+1}_{A/k}$ be the exterior derivative of *Hochschild Homology*. Then

$$
HC_n(A)\cong\frac{\Omega^n_{A/k}}{d\Omega^{n-1}_{A/k}}\ \oplus\ H^{n-2}_{dR}(A)\ \oplus\ H^{n-4}_{dR}(A)\oplus\cdots,
$$

where $H^p_{dR}(A)=H^p(\Omega^{\bullet}_{A/k},d)$ is the de Rham cohomology of the algebra, the sum being finite in each degree when $A$ has finite dimension, and the corresponding periodic cyclic homology is the product of the de Rham cohomologies of one parity: $HP_n(A)\cong\prod_{p\equiv n (2)}H^p_{dR}(A)$.

*Proof (in outline).* Under the Hochschild–Kostant–Rosenberg theorem the Hochschild complex is the complex of differential forms with the de Rham differential, and the Connes boundary $B:\Omega^n_{A/k}\to\Omega^{n+1}_{A/k}$ corresponds to the exterior derivative $d$, so the $(b,B)$-bicomplex becomes the bicomplex whose columns are the de Rham complex, with $b=0$ and $B=d$; its spectral sequence has $E^1$-page the de Rham complex and $E^2$-page the de Rham cohomology, and its two filtrations give the displayed direct sum decomposition, the first summand being the cokernel of $d$ in degree $n$ and the further summands the de Rham cohomologies in degrees $n-2,n-4,\dots$. $\square$

**Example.** For $A=k[x_1,\dots,x_m]$ the de Rham cohomology is $k$ in degree zero and zero in positive degrees, and the map $d:\Omega^{n-1}\to\Omega^n$ has image the closed $n$-forms for $n\ge1$, so $\Omega^n/d\Omega^{n-1}=0$ for $n\ge1$ while $\Omega^0/d\Omega^{-1}=A$. The theorem therefore gives

$$
HC_0(A)\cong A,\qquad HC_{2m}(A)\cong k\ (m\ge1),\qquad HC_{2m+1}(A)=0,
$$

and $HP_{\mathrm{even}}(A)\cong k$, $HP_{\mathrm{odd}}(A)=0$. The Hochschild homology is the free module of forms, $HH_n\cong\Omega^n$ of rank $\binom{m}{n}$, so the cyclic homology is very much smaller than the Hochschild homology of the same degree; in particular $HC_1(A)=0$ while $HH_1(A)$ is free of rank $m$.

## Traces, the Chern Character and K-Theory

### The Dennis Trace

**Definition.** Let $R$ be a ring. For a finitely generated projective $R$-module $P$ and an endomorphism $f:P\to P$, the **trace** is the element $\operatorname{tr}(f)\in R/[R,R]$ obtained from a matrix of $f$ with respect to a finite free complement; it is independent of the choices because the trace of a commutator lies in $[R,R]$. The **Dennis trace** is the natural map

$$
\operatorname{tr}:K_n(R)\to HH_n(R)
$$

from the algebraic K-theory of *K-Theory of Rings* to the Hochschild homology, whose degree-zero case assigns to the class of $(P,f)$ the class of the trace $\operatorname{tr}(f)$, and which composes with the map $I:HH_n\to HC_n$ to give $K_n(R)\to HC_n(R)$. The map is natural and multiplicative.

**Proposition.** The Dennis trace is Morita invariant. In degree zero it is the **Hattori–Stallings trace**, and for a commutative ring $R$ it identifies with the rank: the trace of an idempotent matrix over a connected commutative ring is a rank, an integer, and the class it defines in $R/[R,R]$ is that integer times the class of the identity.

*Proof.* A Morita equivalence is realised by a finitely generated projective bimodule, and the trace of an endomorphism is unchanged by the equivalence because it is computed in the common module category; this gives the invariance. For the degree-zero statement, an idempotent $e$ in $M_n(R)$ has trace equal to the rank of the image of $e$, and the class of a scalar matrix in $R/[R,R]$ is the scalar times the class of $1$. $\square$

### The Chern Character

**Theorem (Chern character).** For a smooth commutative algebra $A$ the Dennis trace and the de Rham isomorphism assemble into the **Chern character**

$$
\operatorname{ch}:K_0(A)\to HP_{\mathrm{even}}(A)\cong\prod_{p\ge0}H^{2p}_{dR}(A),
$$

which is a ring homomorphism for the tensor product on the left and the cup product on the right, and which is an isomorphism after tensoring with $\mathbb{Q}$ when $A$ is smooth and of finite type over a field of characteristic zero.

*Proof (in outline).* The trace of an idempotent representing a projective module gives a cyclic cycle whose de Rham classes are the Chern classes; naturality and multiplicativity are checked on matrices, and the isomorphism statement is the rational comparison theorem, which uses the degeneration of the Atiyah–Hirzebruch-type spectral sequence of the mixed complex in the smooth case. $\square$

**Remark.** The full statement of the comparison between algebraic K-theory and cyclic homology, and the corresponding rational isomorphism for the higher groups, is the subject of and the rational homotopy theory of the K-theory spaces; only the elementary trace and its low-degree form are used here. The topological Chern character, which takes values in the cohomology of a space, belongs to Part II, where it is treated.

## Morita Invariance and Base Change

**Theorem.** Cyclic homology and periodic cyclic homology are Morita invariant: if $A$ and $A'$ are Morita equivalent $k$-algebras then $HC_{\bullet}(A)\cong HC_{\bullet}(A')$ and $HP_{\bullet}(A)\cong HP_{\bullet}(A')$, compatibly with the $SBI$ sequences.

*Proof.* The Hochschild homology is Morita invariant by *Hochschild Homology*, and the $SBI$ sequence is natural; the functoriality of the sequence in the algebra then identifies the cyclic homologies inductively from the Hochschild ones, starting from $HC_0=HH_0$. The periodic version follows by the same induction on the periodic sequence. $\square$

**Example.** For the matrix algebra $M_n(k)$ one has $HC_0\cong k$, $HC_n\cong k$ for $n$ even and $0$ for $n$ odd, agreeing with $HC_{\bullet}(k)$.

**Proposition.** If $k\to k'$ is a flat commutative ring homomorphism and $A$ is flat over $k$, then $HC_n(A\otimes_kk')\cong HC_n(A)\otimes_kk'$ and $HP_n(A\otimes_kk')\cong HP_n(A)\otimes_kk'$, the isomorphisms respecting the operators $S$, $B$, $I$.

*Proof.* The Hochschild complex is flat over $k$ in each degree, so the cyclic and periodic complexes commute with flat base change, and the homology of the base-changed complex is the base change of the homology because $k'$ is flat. $\square$

## Summary

The cyclic category $\Lambda$ is the simplicial category with an extra cyclic operator of order $n+1$ in degree $n$; a cyclic module is a simplicial module with compatible cyclic operators, and the tensor algebra $A^{\otimes(n+1)}$ is the fundamental example, its cyclic operator cyclically permuting the factors with sign $(-1)^n$. The total complex of the cyclic bicomplex, whose columns carry the operators $1-t$ and $N$ over the Hochschild boundary $b$, has homology the cyclic homology $HC_{\bullet}(A)$; the Connes boundary $B=(1-t)s_0N$ anticommutes with $b$, so the two operators form a mixed complex, and taking $B$ into account periodically gives the periodic cyclic homology $HP_{\bullet}(A)$, which is $2$-periodic.

The Connes $SBI$ sequence relates the two theories: $HH_n\to HC_n\to HC_{n-2}\to HH_{n-1}$ is exact in every degree, so the cyclic homology is built from the Hochschild homology of both parities. For a smooth commutative algebra the cyclic homology is the direct sum of the differential forms modulo exact forms and the de Rham cohomology shifted by even degrees; for the polynomial algebra it is $A$ in degree zero, $k$ in the positive even degrees and $0$ in the odd degrees. Cyclic homology is Morita invariant and commutes with flat base change, and it receives the Dennis trace from the algebraic K-theory of *K-Theory of Rings*, whose rational form is the Chern character comparing K-theory with de Rham cohomology.

The cyclic homology of this article is the algebraic invariant of a discrete algebra, computed by the cyclic complex and the $SBI$ sequence. The **cyclic cohomology** of a topological algebra is a different object, despite the shared name, and belongs to Part III, where it is treated ; the analytic traces, the dense subalgebras and the topological tensor products of that theory are not available in Part I and are not used here.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\Lambda$ | the cyclic category, objects $[n]$, $n\ge0$ |
| $t_n$ | cyclic operator on degree $n$, of order dividing $n+1$ |
| $\partial_i$, $s_j$ | face and degeneracy maps of the cyclic module |
| $C_n(A)=A^{\otimes(n+1)}$ | Hochschild chains, a cyclic module |
| $b$, $B$ | Hochschild boundary and Connes boundary |
| $N=1+t+\cdots+t^n$ | summation operator in degree $n$ |
| $HC_n(A)$ | cyclic homology, homology of the total complex of $CC$ |
| $CC_{p,q}=C_q(A)$ | cyclic bicomplex with differentials $b$ and $1-t$, $N$ |
| $HP_n(A)$ | periodic cyclic homology, $2$-periodic |
| $S$, $I$, $B$ | operators of the Connes $SBI$ sequence |
| $\Omega^p_{A/k}$, $H^p_{dR}$ | Kähler differentials and de Rham cohomology |
| $\operatorname{tr}:K_n(R)\to HH_n(R)$ | Dennis trace |
| $\operatorname{ch}$ | Chern character |
| $[A,A]$ | commutator submodule, so $A/[A,A]$ is the trace space |





## Further Reading

- Alain Connes, "Noncommutative differential geometry", *Publications Mathématiques de l'IHÉS* 62 (1985), 257–360, for the cyclic complex, the operator $B$ and the $SBI$ sequence.
- Alain Connes, *Noncommutative Geometry* (Academic Press, 1994), for the cyclic category, the Chern character and the comparison with K-theory.
- Boris Feigin and Boris Tsygan, "Additive K-theory", in *K-Theory, Arithmetic and Geometry* (Springer Lecture Notes in Mathematics 1289, 1987), for the additive structure and the Chern character.
- Thomas G. Goodwillie, "Cyclic homology, derivations, and the free loop space", *Topology* 24 (1985), 187–215, for the relation of cyclic homology to derivations and the free loop space.
- Christian Kassel, "Cyclic homology, comodules, and mixed complexes", *Journal of Algebra* 107 (1987), 195–216, for the mixed-complex formalism used here.
- Jean-Louis Loday, *Cyclic Homology*, 2nd ed. (Springer, 1998), for the cyclic category, the $SBI$ sequence and the computations.
- Jean-Louis Loday and Daniel Quillen, "Cyclic homology and the Lie algebra homology of matrices", *Commentarii Mathematici Helvetici* 59 (1984), 565–591, for the computation via the Lie algebra of matrices.
- Boris L. Tsygan, "Homology of matrix Lie algebras over rings and the Hochschild homology", *Russian Mathematical Surveys* 38 (1983), 198–199, for the additive cyclic structure and the comparison with K-theory.
