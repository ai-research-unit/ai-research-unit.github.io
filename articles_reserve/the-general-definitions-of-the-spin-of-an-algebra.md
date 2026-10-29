# __Possible General Definitions of the Spin of an Algebra__

## Introduction

**An algebra alone has a finite list of possible spins.** The list is finite because every definition that uses only the algebra is bounded by its dimension. The list is not canonical: different definitions select different subsets of the same range. This article states the definitions independently, computes their lists on six algebras, and compares the answers. It does not adopt one definition as the definition.

**What the list is not.** It is not a single number and not a single formula. The top weight of a chosen carrier, the top weight of the adjoint carrier, the length of a Jordan ladder, the number of spectral levels, and the path length of a quiver give different numbers for the same algebra. The article keeps them apart, states what data each one needs, and records where each one fails.

**The corpus's approaches.** The polar-operator articles read the coefficient of the half-angle in the exponential. The integer-spin article reads the top weight of the adjoint action on the material sector. The principal-pair articles read the top weight of the triple. The articles on the individual algebras read the presence or absence of a ladder or a triple. These are four different readings, and they do not agree on every algebra. The article treats each independently and compares them in §12.

**The criterion of usefulness.** A definition is not an end in itself. The biquaternion sector has three observed spin values: $0$, $\tfrac12$, $1$. Since $\mathbb{B}\cong M_2(\mathbb{C})$, a definition is pertinent for this sector only if, applied to $M_2(\mathbb{C})$, it produces exactly these three values. A definition that misses one, adds one, or gives a different one is non-pertinent for the sector, whatever its interest elsewhere. §14 applies this test to every definition in the article.

**The six algebras.** The test cases are the complex numbers $\mathbb{C}$, the split-complex numbers $\mathbb{D}$, the quaternions $\mathbb{H}$, and the matrix algebras $M_2(\mathbb{C})$, $M_3(\mathbb{C})$, $M_5(\mathbb{C})$. The first three are real algebras; the last three are complex algebras. The field is stated in every table, because the dimension of $\mathbb{C}$ is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$.

**The finite range.** Let $A$ be a finite-dimensional unital $k$-algebra and $d=\dim_k A$. Every definition in §§2–8 that uses only $A$, its modules of dimension at most $d$, and the complexification when the definition requires it, produces a subset of
$$
\left\{0,\ \tfrac12,\ 1,\ \tfrac32,\ \ldots,\ d-1\right\}.
$$
The union over those definitions is therefore finite. The proof is a bound in each case: a simple module has dimension at most $d$; a nilpotent has index at most $d$; a Peirce chain has length at most $d$; a quiver path has length at most $d$; a semisimple element has at most $d$ distinct eigenvalues; a spin triple has a carrier of dimension at most $d$, so its defining spin is at most $(d-1)/2$ and its adjoint top is at most $d-1$. This is the precise sense in which the algebra alone has a finite list.

**What is excluded from the list.** A definition that quantifies over all representations of an external Lie algebra, or that uses an unnormalized continuous scale, can produce infinitely many values. The highest weight over all representations of $\mathfrak{su}(2)$ is the standard example: every $j\ge0$ occurs. Such a definition is a definition of a representation, not of the algebra's own list. The article marks those cases.

The conventions are those of the corpus. The field is $\mathbb{R}$ or $\mathbb{C}$ as stated. The indexing is $1$-based. Matrix notation is used only for the matrix algebras. No Clifford algebra is used. The biquaternion is $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$.

## 1. The Six Algebras

**The algebras.** The complex numbers are $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$. The split-complex numbers are $\mathbb{D}=\mathbb{R}[j]/(j^2-1)\cong\mathbb{R}\times\mathbb{R}$. The quaternions are $\mathbb{H}=\mathbb{R}\{1,e_x,e_y,e_z\}$ with $e_x^2=e_y^2=e_z^2=-1$ and $e_xe_y=e_z$, cyclically. The matrix algebras are $M_n=M_n(\mathbb{C})$.

**The basic invariants.** The table records the field, the dimension, the simple modules, the nilpotents, the idempotents, and whether a spin triple exists in the algebra itself.

| algebra | field | $\dim_k A$ | simple modules | nilpotents | idempotents | triple in $A$ |
|---|---|---|---|---|---|---|
| $\mathbb{C}$ | $\mathbb{R}$ | $2$ | $\mathbb{C}$ of dimension $2$ | none | $0,1$ | no |
| $\mathbb{D}$ | $\mathbb{R}$ | $2$ | $\mathbb{R},\mathbb{R}$ of dimension $1$ | none | $0,1,e_+,e_-$ | no |
| $\mathbb{H}$ | $\mathbb{R}$ | $4$ | $\mathbb{H}$ of dimension $4$ | none | $0,1$ | no |
| $M_2(\mathbb{C})$ | $\mathbb{C}$ | $4$ | $\mathbb{C}^2$ of dimension $2$ | index $2$ | matrix units | yes |
| $M_3(\mathbb{C})$ | $\mathbb{C}$ | $9$ | $\mathbb{C}^3$ of dimension $3$ | index $3$ | matrix units | yes |
| $M_5(\mathbb{C})$ | $\mathbb{C}$ | $25$ | $\mathbb{C}^5$ of dimension $5$ | index $5$ | matrix units | yes |

**The two commutative algebras.** $\mathbb{C}$ is a field: every nonzero element is invertible, the only idempotents are $0$ and $1$, and every bracket vanishes. $\mathbb{D}$ is not a field: it has the idempotents $e_\pm=\tfrac12(1\pm j)$ and the zero divisors $1\pm j$. It is still commutative, so every bracket vanishes and every element is central.

**The quaternions.** $\mathbb{H}$ is a division algebra. Its only nilpotent is $0$ and its only idempotents are $0$ and $1$. It has no spin triple in itself: for every $S\in\mathbb{H}$ the eigenvalues of $\operatorname{ad}_S$ are $0$ and $\pm2i\lvert s\rvert$, where $s$ is the imaginary part, and the value $1$ never occurs, so $[S,U]=U$ has no nonzero real solution. The triple exists in the complexification $\mathbb{B}$.

**The matrix algebras.** $M_n$ has the principal triple
$$
S=\operatorname{diag}\left(\tfrac{n-1}{2},\tfrac{n-3}{2},\ldots,-\tfrac{n-1}{2}\right),\qquad
U=\sum_{i=1}^{n-1}E_{i,i+1},\qquad
V=\sum_{i=1}^{n-1}i(n-i)E_{i+1,i}.
$$
The defining module $\mathbb{C}^n$ has weights $\tfrac{n-1}{2},\ldots,-\tfrac{n-1}{2}$. The adjoint module has weights the differences of those numbers, from $-(n-1)$ to $n-1$.

## 2. Dimension of a Simple Module

**Definition (general case).** Let $A$ be a finite-dimensional $k$-algebra and $V$ a simple left $A$-module. The **dimension spin** is
$$
j=\frac{\dim_k V-1}{2}.
$$
The **left list** is the set of these numbers over the simple modules. The definition uses no nilpotent, no grading, and no triple.

**The six algebras.** The table gives the value over the base field and the value after complexification of the module.

| algebra | over $k$ | after complexification |
|---|---|---|
| $\mathbb{C}$ | $\tfrac12$ | $0$ |
| $\mathbb{D}$ | $0$ | $0$ |
| $\mathbb{H}$ | $\tfrac32$ | $\tfrac12$ |
| $M_2(\mathbb{C})$ | $\tfrac12$ | $\tfrac12$ |
| $M_3(\mathbb{C})$ | $1$ | $1$ |
| $M_5(\mathbb{C})$ | $2$ | $2$ |

**The quaternion row.** Over $\mathbb{R}$ the simple module is $\mathbb{H}$ itself, of real dimension $4$, and the formula gives $\tfrac32$. That is not the spin of the quaternion. The spin-$\tfrac12$ carrier is $\mathbb{H}$ as a left $\mathbb{H}$-module; after complexification it is two copies of the complex irreducible $W_{1/2}$ of dimension $2$, and the formula gives $\tfrac12$. The real dimension counts two copies, so the formula doubles the spin and adds one half. The complexified column is the correct one for the spin. The same correction applies to $\mathbb{C}$: over $\mathbb{R}$ the formula gives $\tfrac12$, over $\mathbb{C}$ it gives $0$.

**What the definition does.** It is finite, intrinsic, and always defined. It gives the defining spin $(n-1)/2$ of $M_n$. It fails on $\mathbb{H}$ over $\mathbb{R}$ and on $\mathbb{C}$ over $\mathbb{R}$: in both cases the real dimension is not the dimension of the complex irreducible. The failure is not a small error; it changes the value from $\tfrac12$ to $\tfrac32$ for $\mathbb{H}$.

**Verdict.** A dimension, not a spin. It coincides with the spin when the carrier is the complex irreducible of a spin triple. It reads only the dimension, so it cannot distinguish the real $4$-dimensional carrier of $\mathbb{H}$, which is two copies of spin $\tfrac12$, from the real $4$-dimensional adjoint, whose content is $0,1$.

## 3. The Nilpotent Ladder

**Definition (general case).** Let $u\in A$ be nilpotent and let
$$
\operatorname{ind}(u)=\min\{m:u^m=0\}
$$
be the nilpotency index. The **ladder spin** is
$$
j=\frac{\operatorname{ind}(u)-1}{2}.
$$
The **ladder list** is the set over all nilpotent $u\in A$. The **regular spin** is the maximum of the list. The definition uses only the algebra and one nilpotent.

**The six algebras.** The table gives the possible indices, the ladder list, and the regular spin.

| algebra | indices | ladder list | regular spin |
|---|---|---|---|
| $\mathbb{C}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $\mathbb{D}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $\mathbb{H}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $M_2(\mathbb{C})$ | $\{1,2\}$ | $\{0,\tfrac12\}$ | $\tfrac12$ |
| $M_3(\mathbb{C})$ | $\{1,2,3\}$ | $\{0,\tfrac12,1\}$ | $1$ |
| $M_5(\mathbb{C})$ | $\{1,\ldots,5\}$ | $\{0,\tfrac12,1,\tfrac32,2\}$ | $2$ |

**The quaternion row.** The ladder definition gives $0$ for $\mathbb{H}$. This is not an accident: $\mathbb{H}$ is a division algebra, so the only nilpotent is $0$. The spin-$\tfrac12$ of the quaternion is not a ladder in $\mathbb{H}$. It is the left multiplication on $\mathbb{H}$ as a carrier, and its ladder lives in the complexification: with $S=\tfrac{i}{2}e_z$ and $U=\tfrac{i}{2}e_x-\tfrac12e_y$, the triple is in $\mathbb{B}$, not in $\mathbb{H}$. The definition on $\mathbb{H}$ itself cannot see it.

**What the definition does.** It is finite, intrinsic, and gives the Jordan chain of $M_n$. It gives the same values as the defining spin for the principal triple of $M_n$. It gives $0$ to every division algebra and to every reduced commutative algebra. It cannot see a spectral label without a nilpotent.

**Verdict.** The physical ladder spin for $M_n$; not the spin of $\mathbb{H}$ in $\mathbb{H}$; not a nonzero spin for $\mathbb{C}$ or $\mathbb{D}$.

## 4. The Peirce Chain

**Definition (general case).** A **Peirce chain** is a sequence of nonzero orthogonal idempotents $e_1,\ldots,e_\ell$ in $A$,
$$
e_ie_j=\delta_{ij}e_i,
$$
such that the off-diagonal corner is nonzero:
$$
e_iAe_{i+1}\neq0,\qquad i=1,\ldots,\ell-1.
$$
The **chain spin** is
$$
j=\frac{\ell-1}{2}.
$$
The **Peirce list** is the set over all chains; the maximum spin is $0$ when no chain of length $2$ exists.

**The six algebras.**

| algebra | longest chain | spin |
|---|---|---|
| $\mathbb{C}$ | $1$ | $0$ |
| $\mathbb{D}$ | $1$ | $0$ |
| $\mathbb{H}$ | $1$ | $0$ |
| $M_2(\mathbb{C})$ | $2$ | $\tfrac12$ |
| $M_3(\mathbb{C})$ | $3$ | $1$ |
| $M_5(\mathbb{C})$ | $5$ | $2$ |

**The split-complex row.** $\mathbb{D}$ has four idempotents, including $e_+$ and $e_-$, but it is commutative. The corner is
$$
e_+\mathbb{D}e_-=0,
$$
because every product is symmetric. The two idempotents do not make a chain; the length is $1$ and the spin is $0$. This is the sharpest contrast with the spectral definition: the same algebra has the spectral label $\tfrac12$ from $S=(1,-1)$, but no Peirce chain and no ladder. The idempotents alone are not a spin.

**What the definition does.** It is finite and intrinsic. It sees the matrix chain of $M_n$ and the nonzero corners. It is blind to division algebras and to commutative algebras, including the split-complex numbers. It is not Morita invariant.

**Verdict.** The combinatorial shadow of the ladder; the same list as the ladder on these six; not a general definition of the quaternion spin.

## 5. The Quiver

**Definition (general case).** Let $A$ be finite-dimensional over a field. Its **Ext quiver** has one vertex for each simple module and one arrow for each basis element of $\operatorname{Ext}^1$ between two simple modules. When the field is algebraically closed, Gabriel's theorem identifies the basic algebra Morita equivalent to $A$ with $kQ/I$, with $Q$ a finite quiver and $I$ an admissible ideal. Let $\ell_Q$ be one plus the maximum number of arrows in a nonzero path of $kQ/I$. The **quiver spin** is
$$
j_Q=\frac{\ell_Q-1}{2}.
$$

**The six algebras.**

| algebra | quiver | $\ell_Q$ | spin |
|---|---|---|---|
| $\mathbb{C}$ | one vertex, no arrows | $1$ | $0$ |
| $\mathbb{D}$ | two vertices, no arrows | $1$ | $0$ |
| $\mathbb{H}$ | one vertex, no arrows | $1$ | $0$ |
| $M_2(\mathbb{C})$ | one vertex, no arrows | $1$ | $0$ |
| $M_3(\mathbb{C})$ | one vertex, no arrows | $1$ | $0$ |
| $M_5(\mathbb{C})$ | one vertex, no arrows | $1$ | $0$ |

**What the definition does.** It is finite, intrinsic, and Morita invariant. That is exactly why it is blind to the spin: $M_n$ is Morita equivalent to $\mathbb{C}$, so it must give the same value, and it gives $0$ for both. The matrix size and the multiplicity of the simple module are invisible. The split-complex algebra has two vertices but no arrows, so it also gives $0$, even though it has two simple modules.

**Verdict.** The Morita shadow. It shows that a Morita-invariant definition must give the same value to $M_n$ and $\mathbb{C}$, so it cannot reproduce the physical spin. It is a useful invariant, but it is not a spin.

## 6. The Spectral Level Count

**Definition (general case).** Let $S\in A$ be semisimple over the algebraic closure, and let $L_S$ be left multiplication by $S$ on $A$. Suppose the distinct eigenvalues of $L_S$ are
$$
jd,\ (j-1)d,\ \ldots,\ -jd
$$
for some $j\in\tfrac12\mathbb{Z}_{\ge0}$ and some nonzero $d$ in the algebraic closure of $k$. The **spectral spin** is the number of levels minus one over two,
$$
j=\frac{r-1}{2},
$$
where $r=2j+1$ is the number of distinct eigenvalues. The **top weight** is $jd$. The **spectral list** is the set over all such $S$.

**The scale is not the spin.** The step $d$ is a choice of unit. The level count is invariant under rescaling $S$. The top weight is not: it scales with $d$. For $S=i$ in $\mathbb{H}$ the eigenvalues are $+i$ and $-i$, so $d=2i$, $r=2$, and the spin is $\tfrac12$; the top weight is $i$, which is imaginary. The level count is real and equal to the spin; the top weight is a normalization. This is the precise sense in which a weight is not a spin; the half-angle is a normalization of the same kind.

**The six algebras.**

| algebra | spectral list | witness |
|---|---|---|
| $\mathbb{C}$ | $\{0\}$ | $S=z$, one eigenvalue |
| $\mathbb{D}$ | $\{0,\tfrac12\}$ | $S=(1,-1)$, eigenvalues $\pm1$ |
| $\mathbb{H}$ | $\{0,\tfrac12\}$ | $S=i$, eigenvalues $\pm i$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12\}$ | $S=\operatorname{diag}(\tfrac12,-\tfrac12)$ |
| $M_3(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $S=\operatorname{diag}(1,0,-1)$ |
| $M_5(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2\}$ | $S=\operatorname{diag}(2,1,0,-1,-2)$ |

**The split-complex row.** $S=(1,-1)$ has the two eigenvalues $\pm1$, a full string with $d=2$, and the spin $\tfrac12$. There is no nilpotent and no triple. The value is a **grading label**, not a physical spin. It answers the question "how many spectral levels does this element have?", not "what is the spin of a carrier?".

**What the definition does.** It is finite, intrinsic, and gives a list on all six, nonzero except for $\mathbb{C}$. It gives $\tfrac12$ to $\mathbb{H}$ without complexifying the algebra, because $i$ is an element of $\mathbb{H}$ and the eigenvalues of $L_i$ are complex. It gives the defining list $0,\tfrac12,\ldots,(n-1)/2$ to $M_n$. It gives $\tfrac12$ to $\mathbb{D}$, which the ladder and Peirce definitions do not.

**Verdict.** The most general intrinsic definition in this article. It is not sufficient for physics, because it does not require a nilpotent ladder. It produces labels, some of which are not spins of any carrier.

## 7. The Triple and the Top Weight

**Definition (general case).** A **spin triple** in $A$ is a triple $(S,U,V)$ with
$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S.
$$
On an irreducible carrier, the eigenvalues of $S$ are $j,j-1,\ldots,-j$; the **triple spin** is $j$. Equivalently, a **spin datum** is a pair $(S,u)$ with $S$ semisimple, $u$ nilpotent, $[S,u]=u$, and the spectrum of $S$ on the chain generated by $u$ equal to $j,j-1,\ldots,-j$. The third element is determined on the chain by the relations; the pair $(S,u)$ is the minimal data. The **triple list** is the set over all triples in $A$.

**The six algebras.**

| algebra | principal list | all-triple list |
|---|---|---|
| $\mathbb{C}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{H}$ | $\{0\}$ in $\mathbb{H}$; $\{0,\tfrac12,1\}$ in $\mathbb{B}$ | $\{0\}$ in $\mathbb{H}$; $\{0,\tfrac12,1\}$ in $\mathbb{B}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,1,2\}$ | $\{0,\tfrac12,1,2\}$ |
| $M_5(\mathbb{C})$ | $\{0,2,4\}$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ |

**The matrix lists.** For $M_n$ with the principal triple, the defining spin is $(n-1)/2$ and the adjoint top is $n-1$; the elementary list is
$$
\left\{0,\ \frac{n-1}{2},\ n-1\right\}.
$$
Over all triples, a nilpotent of index $\ell\le n$ gives the defining spin $(\ell-1)/2$ and the adjoint top $\ell-1$. The union is
$$
\left\{0,\tfrac12,\ldots,\tfrac{n-1}{2}\right\}\cup\{0,1,\ldots,n-1\}.
$$
For $n=5$ this is $\{0,\tfrac12,1,\tfrac32,2,3,4\}$; the values $\tfrac52$ and $\tfrac72$ are absent because the defining carrier has at most five levels and the adjoint top is an integer.

**The quaternion row.** $\mathbb{H}$ has no triple in itself. The triple exists in $\mathbb{B}$, where the carrier $\mathbb{H}$ (as a left module) has spin $\tfrac12$ and the adjoint has content $0,1$. The list $\{0,\tfrac12,1\}$ is a list of $\mathbb{B}$, not of $\mathbb{H}$ alone.

**What the definition does.** It is finite and intrinsic for $M_n$. It gives the corpus's elementary list and the adjoint content. It is the definition used in the principal-pair articles and in the biquaternion articles. It is not intrinsic to $\mathbb{C}$, $\mathbb{D}$, or $\mathbb{H}$: those algebras have no nonzero triple, so the list collapses to $\{0\}$ (or to the list of the complexification).

**Verdict.** The corpus's definition. It is the physical one for $M_n$ and for $\mathbb{B}$. It is not the only definition, and it is not available on every algebra without a complexification.

## 8. The Adjoint and Integer Spin

**Definition (general case).** Let $(S,U,V)$ be a spin triple and let $A$ act on itself by the adjoint action. The weights of $\operatorname{ad}_S$ are the differences $\lambda_i-\lambda_j$ of the weights of $S$. The **adjoint spin** is the top weight
$$
j_{\mathrm{ad}}=2j_{\mathrm{def}},
$$
where $j_{\mathrm{def}}$ is the defining spin. The **adjoint list** is the set over all triples. For the principal triple, the same number is the level spin of the derivation $\operatorname{ad}_S$: its spectrum has $4j+1=2j_{\mathrm{ad}}+1$ levels, so $(\text{levels}-1)/2=j_{\mathrm{ad}}$.

**The six algebras.**

| algebra | adjoint spin | adjoint content |
|---|---|---|
| $\mathbb{C}$ | $0$ | $\{0\}$ |
| $\mathbb{D}$ | $0$ | $\{0\}$ |
| $\mathbb{H}$ | $1$ in $\mathbb{B}$ | $\{0,1\}$ |
| $M_2(\mathbb{C})$ | $1$ | $\{0,1\}$ |
| $M_3(\mathbb{C})$ | $2$ | $\{0,1,2\}$ |
| $M_5(\mathbb{C})$ | $4$ | $\{0,1,2,3,4\}$ |

**The factor of two.** The adjoint weights are differences of the defining weights. For the principal triple of $M_n$, the defining top is $(n-1)/2$ and the adjoint top is $n-1$. The factor $2$ is not a half-angle and not a second definition of the same spin: it is the doubling of the weights on a different carrier. The defining carrier has spin $(n-1)/2$; the adjoint carrier has spin $n-1$. Both are spins, of different carriers.

**The material sector.** For $\mathbb{H}$, the adjoint action on the vector part $\operatorname{Im}\mathbb{H}$ is the spin-$1$ representation. The Hermitian generator is $J_k=\tfrac12\operatorname{ad}_{ie_k}$, whose eigenvalues are $0,\pm1$. The raw derivation $\operatorname{ad}_{ie_k}$ has eigenvalues $0,\pm2$, so the factor $\tfrac12$ is the normalization that turns the derivation into the physical generator; the spin is $1$, not $2$. The material sector therefore carries the integer spin $1$, while the defining carrier carries $\tfrac12$. This is the construction of *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*: the vector part of $\mathbb{M}_-$ is the spin-$1$ triplet, and the adjoint action supplies the representation.

**The caution for $n\ge3$.** The adjoint of $\mathfrak{sl}_n$ is reducible under the principal $\mathfrak{sl}_2$: it decomposes as $W_0\oplus W_1\oplus\cdots\oplus W_{n-1}$. The top component has spin $n-1$, but the physical gauge field in the adjoint has spin $1$. The integer $n-1$ is the $\mathfrak{sl}_2$ content, not the $\mathfrak{su}(n)$ spin. The corpus's statement "the spin of $\mathfrak{sl}_3$ is $2$" means the top principal $\mathfrak{sl}_2$ component; the gluon has spin $1$. Both statements are correct about different groups.

**Verdict.** A carrier-dependent integer list. It is numerically twice the defining spin for the principal triple, but it is the spin of a different carrier, not a second definition of the same spin. It is the right notion for the material sector.

## 9. The Half-Angle and the Polar Operators

**The polar decomposition.** A nonzero quaternion has the polar form
$$
q=\rho\left(\cos\frac{\theta}{2}+n\sin\frac{\theta}{2}\right),
$$
with $\rho>0$ and $n$ a unit imaginary quaternion. The half-angle is the parameter of the double cover $SU(2)\to SO(3)$. It is a property of the quaternion group, not of the spin quantum number.

**Why the half-angle is not the spin.** The spin-$1$ rotation about the $z$-axis is
$$
R_z(\theta)=\begin{pmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{pmatrix},
$$
with the full angle. The spin-$\tfrac12$ rotor is
$$
\exp\left(-\frac{i\theta\sigma_z}{2}\right)
=\begin{pmatrix}e^{-i\theta/2}&0\\0&e^{i\theta/2}\end{pmatrix},
$$
with the half-angle. The coefficient $\tfrac12$ is the eigenvalue of the generator $\sigma_z/2$ in the fundamental representation. For the spin-$1$ adjoint of $\mathfrak{su}(2)$ the generator $J_z$ has eigenvalues $1,0,-1$, and the rotor is $\exp(i\theta J_z)$, with the full angle. The coefficient is not the spin; it is the normalization of the generator in the chosen carrier. The half-angle appears only for the spin-$\tfrac12$ carrier.

**The six algebras.** The table gives the coefficient for the defining carrier and for the top adjoint component.

| algebra | defining coefficient | adjoint top coefficient |
|---|---|---|
| $\mathbb{C}$ | undefined | undefined |
| $\mathbb{D}$ | undefined | undefined |
| $\mathbb{H}$ | $\tfrac12$ | $1$ |
| $M_2(\mathbb{C})$ | $\tfrac12$ | $1$ |
| $M_3(\mathbb{C})$ | $\tfrac12$ | $2$ |
| $M_5(\mathbb{C})$ | $\tfrac12$ | $4$ |

**What the definition does.** The coefficient is the top eigenvalue of the generator: $\tfrac12$ for the fundamental, and $n-1$ for the top adjoint component of $M_n$. It is not a new invariant; it is the weight of the carrier. The half-angle is the special case of the fundamental. The polar-operator articles, for example *The Polarisation Operator*, identify the half-angle with the spin because they work in the biquaternion, whose defining module is the spin-$\tfrac12$ carrier. The half-angle is the parameter of the double cover, and it is $\tfrac12$ only on the fundamental carrier; that identification is a special case, not a general definition.

**Verdict.** A normalization, not a definition. It cannot distinguish the spin of a carrier from the normalization of its generator.

## 10. Representation Labels: Highest Weight, Casimir, Coadjoint Orbit

**Highest weight.** Let $\mathfrak{g}$ be a reductive Lie algebra acting on $V$, choose a Cartan and a positive system, and let $\lambda$ be the highest weight. The **highest-weight spin** is $\lambda$; a number requires a chosen $\mathfrak{sl}_2$. For $\mathfrak{sl}_2$ with $\mathfrak{h}=\langle H\rangle$, the spin is $j=\lambda(H)/2$. On $\mathbb{H}$, the rotation algebra is $\mathfrak{su}(2)$; the defining carrier has $j=\tfrac12$ and the adjoint has $j=1$. On $M_n$, the algebra $\mathfrak{sl}_n$ has a highest weight vector, not a single number; the principal $\mathfrak{sl}_2$ subalgebra gives the triple list of §7. Without that choice, the definition does not produce a spin for $M_3$ or $M_5$.

**Casimir.** Let $\mathfrak{g}$ be semisimple with an invariant form and Casimir $C$, and let $C|_V=c_V I$. For $\mathfrak{sl}_2$ the **Casimir spin** is
$$
j=\frac{-1+\sqrt{1+4c_V}}{2}.
$$
The formula uses the Casimir of the chosen $\mathfrak{sl}_2$, not the Casimir of the full algebra. On $M_2$ the defining Casimir is $\tfrac34$ and gives $\tfrac12$; the adjoint Casimir is $2$ and gives $1$. On $M_3$ the full $\mathfrak{sl}_3$ Casimir of the defining module is $\tfrac43$, which gives $0.758\ldots$, not a half-integer. On $M_5$ it is $\tfrac{12}{5}$, which gives $1.128\ldots$, not a half-integer. The principal $\mathfrak{sl}_2$ Casimir gives the correct values, $1$ and $2$ on $M_3$ and $2$ and $4$ on $M_5$; the full algebra Casimir does not.

**Coadjoint orbit.** Let $f\in\mathfrak{g}^*$ and $O_f$ the coadjoint orbit with the Kirillov–Kostant–Souriau form. For $\mathfrak{su}(2)$, with the normalization in which the unit sphere has area $4\pi$, the **orbit spin** is $j=\operatorname{Area}(O_f)/(4\pi)$. On $\mathbb{H}$ the orbits give $0,\tfrac12,1,\ldots$; on $M_n$ the orbit is a flag variety, and the area formula does not produce a single spin. The definition is an $A_1$ definition.

**The six algebras.** The table gives the values that the representation labels produce when a principal $\mathfrak{sl}_2$ is chosen. The entries marked "principal" use that subalgebra; the entries marked "$\mathfrak{sl}_3$" or "$\mathfrak{sl}_5$" are the full-algebra Casimirs and are not spins.

| algebra | highest weight | Casimir | coadjoint |
|---|---|---|---|
| $\mathbb{C}$ | $0$ | $0$ | $0$ |
| $\mathbb{D}$ | $0$ | $0$ | $0$ |
| $\mathbb{H}$ | $\tfrac12,1$ | $\tfrac12,1$ | $0,\tfrac12,1,\ldots$ |
| $M_2(\mathbb{C})$ | $\tfrac12,1$ | $\tfrac12,1$ | $A_1$ orbit |
| $M_3(\mathbb{C})$ | $\{0,1,2\}$ with principal $\mathfrak{sl}_2$ | $0.758$ with $\mathfrak{sl}_3$ | flag variety |
| $M_5(\mathbb{C})$ | $\{0,2,4\}$ with principal $\mathfrak{sl}_2$; content $0,\ldots,4$ | $1.128$ with $\mathfrak{sl}_5$ | flag variety |

**What the definition does.** The highest weight is a vector; a number requires a chosen $\mathfrak{sl}_2$. The Casimir is a number, but the formula is an $\mathfrak{sl}_2$ formula. The coadjoint orbit is an $A_1$ formula. None of them is a general definition of the spin of an algebra; each is a definition of a label of a chosen representation.

**Verdict.** Carrier-dependent labels. They reproduce the triple list when the principal $\mathfrak{sl}_2$ is chosen, and they fail on $M_3$ and $M_5$ when the full algebra is used.

## 11. Topological Labels: Circle Weight and Ribbon Twist

**Circle weight.** Let a circle $T\cong U(1)$ act on $V$, and let $\rho(e^{it})=e^{ijt}$ on the highest-weight space. The **weight** is $j\in\mathbb{R}/\mathbb{Z}$, and the **$2\pi$ sign** is $(-1)^{2j}$. Only $j$ modulo $1$ is defined; the integer part requires a lift. On $\mathbb{C}$, $\mathbb{D}$, and $M_n$ the module category is semisimple with a trivial circle action, so the weight is $0$. On $\mathbb{H}$ the defining carrier has $j=\tfrac12$ and the adjoint has $j=1$, so the values modulo $1$ are $0$ and $\tfrac12$.

**Ribbon twist.** Let $\mathcal{C}$ be a ribbon category, $X$ a simple object, and $\theta_X$ its twist. Write $\theta_X=e^{2\pi ih_X}$ with $h_X\in\mathbb{Q}/\mathbb{Z}$; $h_X$ is the **topological spin**. For the semisimple module categories of $\mathbb{C}$, $\mathbb{D}$, and $M_n$, the twist is trivial on each simple object and $h=0$. For the module category of $\mathbb{H}$ as a Hopf algebra, the twist gives $h=0$ or $\tfrac12$. The definition requires a ribbon structure; it is extra data, not a property of the algebra alone.

**Verdict.** Finite but coarse. The circle weight and the ribbon twist see the parity of the spin, not the integer part. They are shadows, not the algebraic spin.

## 12. Comparison

### The Values

The table collects the lists. A dash means that the definition does not apply without extra data. A set means the list over all admissible data.

| definition | $\mathbb{C}$ | $\mathbb{D}$ | $\mathbb{H}$ | $M_2$ | $M_3$ | $M_5$ |
|---|---|---|---|---|---|---|
| dimension over $k$ | $\tfrac12$ | $0$ | $\tfrac32$ | $\tfrac12$ | $1$ | $2$ |
| dimension over $\mathbb{C}$ | $0$ | $0$ | $\tfrac12$ | $\tfrac12$ | $1$ | $2$ |
| regular index | $0$ | $0$ | $0$ | $\tfrac12$ | $1$ | $2$ |
| ladder list | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0,\tfrac12\}$ | $\{0,\tfrac12,1\}$ | $\{0,\ldots,2\}$ |
| Peirce | $0$ | $0$ | $0$ | $\tfrac12$ | $1$ | $2$ |
| quiver | $0$ | $0$ | $0$ | $0$ | $0$ | $0$ |
| spectral | $\{0\}$ | $\{0,\tfrac12\}$ | $\{0,\tfrac12\}$ | $\{0,\tfrac12\}$ | $\{0,\tfrac12,1\}$ | $\{0,\ldots,2\}$ |
| triple, principal | $\{0\}$ | $\{0\}$ | $\{0\}$ in $\mathbb{H}$; $\{0,\tfrac12,1\}$ in $\mathbb{B}$ | $\{0,\tfrac12,1\}$ | $\{0,1,2\}$ | $\{0,2,4\}$ |
| triple, all | $\{0\}$ | $\{0\}$ | $\{0\}$ in $\mathbb{H}$; $\{0,\tfrac12,1\}$ in $\mathbb{B}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1,2\}$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ |
| adjoint top | $0$ | $0$ | $1$ in $\mathbb{B}$ | $1$ | $2$ | $4$ |
| half-angle | — | — | $\tfrac12$; $1$ | $\tfrac12$; $1$ | $\tfrac12$; $2$ | $\tfrac12$; $4$ |
| circle weight | $0$ | $0$ | $0,\tfrac12$ | $0$ | $0$ | $0$ |
| Casimir | $0$ | $0$ | $\tfrac12,1$ | $\tfrac12,1$ | $0.758$ | $1.128$ |
| coadjoint | $0$ | $0$ | $0,\tfrac12,1,\ldots$ | $0,\tfrac12,1,\ldots$ | flag | flag |

### The Coverage

The question is whether a definition computes the list on all six. The table answers it.

| definition | all six? | $M_2(\mathbb{C})$ exact? | gives $\mathbb{H}=\tfrac12$? | gives $M_n=(n-1)/2$? | intrinsic? |
|---|---|---|---|---|---|
| dimension over $k$ | yes | no, $\{\tfrac12\}$ | no, $\tfrac32$ | yes | yes |
| dimension over $\mathbb{C}$ | yes | no, $\{\tfrac12\}$ | yes | yes | after complexification |
| ladder | yes | no, $\{0,\tfrac12\}$ | no, $0$ | yes | yes |
| Peirce | yes | no, $\{0,\tfrac12\}$ | no, $0$ | yes | yes |
| quiver | yes | no, $\{0\}$ | no, $0$ | no, $0$ | yes |
| spectral | yes | no, $\{0,\tfrac12\}$ | yes | yes | yes |
| triple | no | yes, $\{0,\tfrac12,1\}$ | yes in $\mathbb{B}$ | yes | for $M_n$ |
| adjoint | no | no, $\{0,1\}$ | no, $1$ in $\mathbb{B}$ | $n-1$ | with triple |
| half-angle | no | no, normalization | constant | constant | no |
| highest weight | no | no, all $j$ unrestricted | yes with $A_1$ | with principal $A_1$ | no |
| Casimir | no | no, all $j$ unrestricted | yes with $A_1$ | full algebra fails | no |
| coadjoint | no | no, all $j$ | yes with $A_1$ | fails | no |
| circle, ribbon | yes | no, $\{0,\tfrac12\}$ mod $1$ | modulo $1$ | $0$ | extra structure |

**The answer.** No, not every definition computes all six, and only one computes the experimental set on $M_2(\mathbb{C})$. The intrinsic definitions that give a finite list on all six are: dimension, ladder, Peirce, quiver, and spectral. On $M_2(\mathbb{C})$ the ladder, Peirce, and spectral give $\{0,\tfrac12\}$, the dimension gives $\{\tfrac12\}$, and the quiver gives $\{0\}$; none gives $1$. The adjoint gives $\{0,1\}$ and misses $\tfrac12$. Only the triple gives $\{0,\tfrac12,1\}$ exactly; §14 audits every method against this set. On $\mathbb{H}$ the ladder and Peirce give $0$, the dimension gives $\tfrac32$ over $\mathbb{R}$, and the spectral gives $\{0,\tfrac12\}$; the triple gives $\{0,\tfrac12,1\}$ in $\mathbb{B}$. On $M_n$ the all-triple list is $\{0,\tfrac12,\ldots,(n-1)/2\}\cup\{0,1,\ldots,n-1\}$.

### The Finite List of Each Algebra

The union of the definitions of §§2–8, with the complexification where required, gives the following lists.

| algebra | possible spins | comment |
|---|---|---|
| $\mathbb{C}$ | $\{0,\tfrac12\}$ | $\tfrac12$ is the real dimension; over $\mathbb{C}$ the list is $\{0\}$ |
| $\mathbb{D}$ | $\{0,\tfrac12\}$ | $\tfrac12$ is spectral; the ladder and Peirce lists are $\{0\}$ |
| $\mathbb{H}$ | $\{0,\tfrac12,1,\tfrac32\}$ | $\tfrac32$ is the real dimension; the physical list is $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | only the triple gives this list exactly; see §14 |
| $M_3(\mathbb{C})$ | $\{0,\tfrac12,1,2\}$ | non-principal triples give $\tfrac12$ |
| $M_5(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ | no $\tfrac52$ or $\tfrac72$ |

The table is a union, not a method. On $M_2(\mathbb{C})$ the union coincides with the triple list; no other single method gives it.

**The two levels of the answer.** The **possible** list is the union over the definitions; it contains labels that are not physical. The **physical** values are the spins of the triple on the chosen carriers. The possible list contains them; it can be strictly larger, as it is for $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$, and for $M_n$ above the defining spin.

### The Four Notions in the Corpus

The corpus uses four distinct notions, and the confusion between them is the source of the apparent contradictions.

1. **Weight spin.** The top weight of a chosen carrier, with unit step. This is the triple spin $j$ of §7. It is the defining spin $(n-1)/2$ for $M_n$ and $\tfrac12$ for the spinor of $\mathbb{H}$.
2. **Adjoint spin.** The top weight of the adjoint carrier, $2j$. This is the integer spin of §8. It is $1$ for the vector part of $\mathbb{H}$ and $n-1$ for the adjoint of $M_n$. It is a different carrier, not a doubling of the same spin.
3. **Ladder spin.** The length of the Jordan chain, $(\ell-1)/2$. This is intrinsic to $M_n$ and gives the same values as the defining weight for the principal triple. It fails on division algebras.
4. **Level spin.** The number of spectral levels, $(r-1)/2$. This is scale-free, gives $\tfrac12$ to $\mathbb{H}$ and $\mathbb{D}$, and gives the defining list to $M_n$. It is the most general intrinsic definition, but it does not require a ladder.

On $M_2(\mathbb{C})$ the four notions are not equivalent. Adjoint spin gives $\{0,1\}$ and misses $\tfrac12$. Ladder spin gives $\{0,\tfrac12\}$ and misses $1$. Level spin gives $\{0,\tfrac12\}$ and misses $1$. Only the triple, read on the trivial, defining, and adjoint carriers, reproduces $\{0,\tfrac12,1\}$; §14 records the audit.

The half-angle of the polar operators is not a fifth notion. It is the normalization of the generator of the spin-$\tfrac12$ carrier. The integer spin of the adjoint is numerically twice the defining spin for the principal triple, but it is the spin of the adjoint carrier; it is not a redefinition of the defining spin. The quiver and the ribbon twist are shadows.

## 13. Checks

**The quaternion adjoint.** With $S=i$, the derivation $\operatorname{ad}_i$ acts on the basis $1,e_x,e_y,e_z$ by
$$
\operatorname{ad}_i(1)=0,\quad
\operatorname{ad}_i(e_x)=2e_y,\quad
\operatorname{ad}_i(e_y)=-2e_x,\quad
\operatorname{ad}_i(e_z)=0.
$$
The eigenvalues are $0,0,\pm2i$; the level spin is $1$. The Hermitian generator $J_z=\tfrac12\operatorname{ad}_{ie_z}$ has eigenvalues $0,\pm1$; the spin is $1$.

**The quaternion spectral label.** With $S=i$, the eigenvalues are $\pm i$; $r=2$, $d=2i$, and the level spin is $\tfrac12$. The top weight is $i$. The two numbers $\tfrac12$ and $i$ are different objects; only the first is the spin.

**The split-complex corner.** With $e_\pm=\tfrac12(1\pm j)$, every product is commutative, so $e_+\mathbb{D}e_-=0$. The longest Peirce chain has length $1$; the spin is $0$. The spectral element $S=(1,-1)$ has eigenvalues $\pm1$ and spin $\tfrac12$; the two definitions answer different questions.

**The matrix content.** For $M_n$ with the principal triple, the adjoint decomposes as
$$
\mathfrak{gl}_n=W_0\oplus W_1\oplus\cdots\oplus W_{n-1},
\qquad
\dim W_k=2k+1,
\qquad
\sum_{k=0}^{n-1}(2k+1)=n^2.
$$
For $n=2$ the content is $0,1$; for $n=3$ it is $0,1,2$; for $n=5$ it is $0,1,2,3,4$. The defining carrier has spin $(n-1)/2$; the adjoint top is $n-1$.

**The lists.** The spectral list of $M_n$ is $0,\tfrac12,\ldots,(n-1)/2$, realized by $\operatorname{diag}(j,j-1,\ldots,-j)$ with repeated eigenvalues. The all-triple list is the union of that list with $0,1,\ldots,n-1$, realized by a nilpotent of index $\ell$ on a block of size $\ell$ and a scalar on the rest.

## 14. The Audit on $M_2(\mathbb{C})$

**The criterion.** The biquaternion sector has three observed spin values: $0$ for the scalar, $\tfrac12$ for the fermion, and $1$ for the vector. Since $\mathbb{B}\cong M_2(\mathbb{C})$, a method is pertinent for the sector only if, applied to $M_2(\mathbb{C})$, it produces exactly
$$
\{0,\ \tfrac12,\ 1\}.
$$
A method that misses a value, adds a value, or gives a different value is non-pertinent, however interesting it is elsewhere. This is the test of usefulness, not of generality.

**The recheck.** The table applies every method of §§2–11 to $M_2(\mathbb{C})$. The column "exact?" compares the result with the experimental set.

| method | result on $M_2(\mathbb{C})$ | exact? | reason |
|---|---|---|---|
| dimension over $\mathbb{C}$ | $\{\tfrac12\}$ | no | misses $0,1$ |
| dimension over $\mathbb{R}$ | $\{\tfrac32\}$ | no | wrong value |
| regular index | $\{\tfrac12\}$ | no | misses $0,1$ |
| ladder | $\{0,\tfrac12\}$ | no | misses $1$ |
| Peirce | $\{0,\tfrac12\}$ | no | misses $1$ |
| quiver | $\{0\}$ | no | wrong value |
| spectral on $A$ | $\{0,\tfrac12\}$ | no | misses $1$ |
| triple, principal | $\{0,\tfrac12,1\}$ | yes | — |
| triple, all | $\{0,\tfrac12,1\}$ | yes | — |
| adjoint only | $\{0,1\}$ | no | misses $\tfrac12$ |
| half-angle | $\{0,\tfrac12,1\}$ on three carriers | no | normalization, not a list |
| highest weight | all $j\ge0$ unrestricted | no | overcomplete |
| Casimir | all $j\ge0$ unrestricted | no | overcomplete |
| coadjoint | all $j\ge0$ | no | overcomplete |
| circle weight | $\{0,\tfrac12\}$ mod $1$ | no | misses $1$ |
| ribbon twist | $\{0,\tfrac12\}$ | no | misses $1$ |

**The non-pertinent methods.** The list is the result.

- **Wrong value.** The quiver gives $0$, because $M_2(\mathbb{C})$ is Morita equivalent to $\mathbb{C}$. The dimension over $\mathbb{R}$ gives $\tfrac32$, because the real dimension of $\mathbb{C}^2$ is $4$. The circle weight and the ribbon twist see only $0$ and $\tfrac12$ modulo $1$; the value $1$ is invisible.
- **Incomplete.** The dimension over $\mathbb{C}$ gives only $\tfrac12$. The regular index gives only $\tfrac12$. The ladder and the Peirce chain give $\{0,\tfrac12\}$. The spectral level count on $A$ gives $\{0,\tfrac12\}$. The adjoint gives $\{0,1\}$. Each misses at least one experimental value.
- **Overcomplete.** The coadjoint orbit, and the highest weight and Casimir taken over all representations, give every $j\ge0$. They do not produce a finite experimental list.
- **Disguised triple.** The highest weight and the Casimir give $\{0,\tfrac12,1\}$ only when they are evaluated on the three carriers, trivial, defining, and adjoint, that the triple supplies. The spectral count and the dimension also give the set when they are applied to those three carriers. In each case the carriers are the triple's, so the method is a restatement, not an independent definition.
- **Normalization.** The half-angle gives the coefficient of the angle, not the spin. It equals $\tfrac12$ on the defining carrier and $1$ on the adjoint; the set is read from the carriers, not produced by the half-angle.

**The only pertinent method.** On $M_2(\mathbb{C})$, the triple is the only method that produces exactly $\{0,\tfrac12,1\}$ from the algebra and its modules. The all-triple definition is the intrinsic one; the principal triple coincides with it at $n=2$. The three values are the three carriers: the centre gives $0$, the defining module gives $\tfrac12$, and the adjoint gives $1$.

**What the corpus should take from this.** The ladder, the Peirce chain, the spectral count, the dimension, and the adjoint are descriptions of parts of the biquaternion. They are not definitions of its spin list. The triple is. The polar half-angle is a parametrization of the spin-$\tfrac12$ rotor, not a definition. The integer-spin article's adjoint action is the spin-$1$ carrier, not the whole list. The apparent disagreements between the corpus's articles are the projections of one triple onto different carriers.

## Summary

**There is no single general definition of the spin of an algebra.** There are definitions, each with its data and its range. The algebra alone has a finite list of possible spins, bounded by its dimension; the definitions select subsets of that list. The most general intrinsic definition is the spectral level count; the corpus's physical reading is the triple, which requires a carrier and a ladder. The half-angle is a normalization of the spin-$\tfrac12$ carrier, not the spin. The adjoint spin is the spin of a different carrier, numerically twice the defining spin for the principal triple; it is not a redefinition of the defining spin. The quiver and the ribbon twist are shadows.

**The six algebras.** The lists are: $\mathbb{C}$ $\{0\}$ or $\{0,\tfrac12\}$; $\mathbb{D}$ $\{0,\tfrac12\}$; $\mathbb{H}$ $\{0,\tfrac12,1\}$ (or $\{0,\tfrac12,1,\tfrac32\}$ with the real dimension); $M_2$ $\{0,\tfrac12,1\}$; $M_3$ $\{0,\tfrac12,1,2\}$; $M_5$ $\{0,\tfrac12,1,\tfrac32,2,3,4\}$. The physical values are the triple spins on the chosen carriers. On $M_2(\mathbb{C})$ they are $0,\tfrac12,1$, the experimental set.

**The audit is decisive for the biquaternion.** On $M_2(\mathbb{C})$ only the triple gives exactly $\{0,\tfrac12,1\}$. The ladder, the Peirce chain, the spectral count, the dimension, and the adjoint each miss a value or give a wrong one. The highest weight and the Casimir are overcomplete unless they are restricted to the triple's carriers. §14 lists the non-pertinent methods and the reason for each.

## Further Reading

- [The General Definition of Spin](../articles_maths/the-general-definition-of-spin.html), for the triple definition and the original table of cases.
- [The Approaches to Spin: Weight, Half-Angle, Ladder and Adjoint](../articles_maths/the-approaches-to-spin-weight-half-angle-ladder-and-adjoint.html), for the four notions in the corpus.
- [The Polarisation Operator](../articles_maths/the-polarisation-operator.html), for the polar decomposition and the half-angle.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the frame pair and the spin-$\tfrac12$ carrier.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the adjoint spin $1$ of the material sector.
- [The Spin of the Complex Numbers: The Absence of a Pair](../articles_reserve/the-spin-of-the-complex-numbers-the-absence-of-a-pair.html), for the triple list $\{0\}$.
- [The Spin of the Split-Complex Numbers: A Root Without a Ladder](../articles_reserve/the-spin-of-the-split-complex-numbers-a-root-without-a-ladder.html), for the gap between the spectral label and the ladder.
- [The Spin of the Quaternion Algebra: A Worked Computation](../articles_reserve/the-spin-of-the-quaternion-algebra-a-worked-computation.html), for the complexification and the real dimension.
- [The Spin of the Principal Pair of $M_2(\mathbb{C})$: A Worked Computation](../articles_reserve/the-principal-pair-of-m2c-a-worked-computation.html), for the list $\{0,\tfrac12,1\}$.
- [The Spin of the Principal Pair of $M_3(\mathbb{C})$: A Worked Computation](../articles_reserve/the-principal-pair-of-m3c-a-worked-computation.html), for the list $\{0,1,2\}$.
- [The Spin of the Principal Pair of $M_5(\mathbb{C})$: A Worked Computation](../articles_reserve/the-principal-pair-of-m5c-a-worked-computation.html), for the list $\{0,2,4\}$ and the content $0,\ldots,4$.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](../articles_maths/the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the general adjoint content.
- [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html), for the grading that is not a spin.
