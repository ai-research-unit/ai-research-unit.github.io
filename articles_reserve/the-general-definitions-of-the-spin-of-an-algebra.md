# __Possible General Definitions of the Spin of an Algebra__

## Introduction

**The test of usefulness.** The biquaternion sector has three observed spin values: $0$ for the scalar, $\tfrac12$ for the fermion, and $1$ for the vector. Since $\mathbb{B}\cong M_2(\mathbb{C})$, a definition is pertinent for the sector only if, applied to $M_2(\mathbb{C})$ alone, it produces exactly
$$
\{0,\ \tfrac12,\ 1\}.
$$
A definition that misses a value, adds a value, or gives a different value is non-pertinent for the sector, whatever its interest elsewhere. This article presents the five definitions that pass. The companion article, *The Incomplete Definitions of the Spin of an Algebra*, presents the methods that fail, with the reason for each.

**An algebra alone has a finite list of possible spins.** The list is finite because every definition that uses only the algebra is bounded by its dimension. The list is not canonical: different definitions select different subsets of the same range. The five definitions below are different computations; they agree at $M_2(\mathbb{C})$ and diverge above it.

**What the list is not.** It is not a single number and not a single formula. The top weight of a chosen carrier, the dimension of a carrier, the Casimir eigenvalue, the orbit area, and the top of a chain give different numbers for the same algebra. The article keeps them apart, states what data each one needs, and records where each one generalizes.

**The corpus's approaches.** The polar-operator articles read the coefficient of the half-angle in the exponential. The integer-spin article reads the top weight of the adjoint action on the material sector. The principal-pair articles read the top weight of the triple. The articles on the individual algebras read the presence or absence of a ladder or a triple. These are different readings, and they do not agree on every algebra. The five definitions below are the ones that agree on the biquaternion.

**The cases.** The real line $\mathbb{R}$; the complex numbers over $\mathbb{R}$ and over $\mathbb{C}$; the split-complex numbers $\mathbb{D}$; the dual numbers $\mathbb{D}'$; the reduced biquaternions $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$; the quaternions over $\mathbb{R}$ and over $\mathbb{C}$; the split quaternions $\mathbb{H}_{\mathrm s}\cong M_2(\mathbb{R})$; the biquaternions $\mathbb{B}\cong M_2(\mathbb{C})$; the split biquaternions $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$; and the matrix algebras $M_n(\mathbb{C})$ for $n=2,\ldots,6$. The field is stated in every table, because the dimension of $\mathbb{C}$ is $2$ over $\mathbb{R}$ and $1$ over $\mathbb{C}$, and the dimension of $\mathbb{H}$ is $4$ over $\mathbb{R}$ and $2$ over $\mathbb{C}$.

**The finite range.** Let $A$ be a finite-dimensional unital $k$-algebra and $d=\dim_k A$. The definitions in §§3–7 read only $A$, its modules of dimension at most $d$, and the complexification when required. There are finitely many isomorphism classes of such modules, and each definition returns a set determined by them. The spin values of the triple, the module list, the highest-weight list, and the orbit list lie in
$$
\left\{0,\ \tfrac12,\ 1,\ \tfrac32,\ \ldots,\ d-1\right\}.
$$
The bound is $d-1$: a carrier has dimension at most $d$, so a defining spin is at most $(d-1)/2$, and the adjoint top of a triple is at most $d-1$. The Casimir list is finite in the same sense, but its values need not be half-integers; it is a spin only when the semisimple part is $\mathfrak{sl}_2$.

**What is excluded.** A definition that quantifies over all representations of an external Lie algebra, or that uses an unnormalized continuous scale, can produce infinitely many values. The highest weight over all representations of $\mathfrak{su}(2)$ is the standard example: every $j\ge0$ occurs. Such a definition is a definition of a representation, not of the algebra's own list. Those definitions are in the companion article.

The conventions are those of the corpus. The field is $\mathbb{R}$ or $\mathbb{C}$ as stated. The indexing is $1$-based. Matrix notation is used only for the matrix algebras. No Clifford algebra is used. The biquaternion is $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$.

## 1. The Test and the Cases

**The algebras.** The complex numbers are $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$. The split-complex numbers are $\mathbb{D}=\mathbb{R}[j]/(j^2-1)\cong\mathbb{R}\times\mathbb{R}$. The dual numbers are $\mathbb{D}'=\mathbb{R}[\varepsilon]/(\varepsilon^2)$, with $\varepsilon$ nilpotent of index $2$. The reduced biquaternions are $\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$. The quaternions are $\mathbb{H}=\mathbb{R}\{1,e_x,e_y,e_z\}$ with $e_x^2=e_y^2=e_z^2=-1$ and $e_xe_y=e_z$, cyclically. The split quaternions are $\mathbb{H}_{\mathrm s}\cong\mathrm{Cl}_{1,1}\cong M_2(\mathbb{R})$. The split biquaternions are $\mathbb{H}_{\mathbb D}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\times\mathbb{H}$. The matrix algebras are $M_n=M_n(\mathbb{C})$.

**The basic invariants.** The table records the field, the dimension, the simple modules, the nilpotents, the idempotents, and whether a spin triple exists in the algebra itself.

| algebra | field | $\dim_k A$ | simple modules | nilpotents | idempotents | triple in $A$ |
|---|---|---|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $1$ | $\mathbb{R}$ of dimension $1$ | none | $0,1$ | no |
| $\mathbb{C}$ | $\mathbb{R}$ | $2$ | $\mathbb{C}$ of dimension $2$ | none | $0,1$ | no |
| $\mathbb{C}$ | $\mathbb{C}$ | $1$ | $\mathbb{C}$ of dimension $1$ | none | $0,1$ | no |
| $\mathbb{D}$ | $\mathbb{R}$ | $2$ | $\mathbb{R},\mathbb{R}$ of dimension $1$ | none | $0,1,e_+,e_-$ | no |
| $\mathbb{D}'$ | $\mathbb{R}$ | $2$ | $\mathbb{R}$ of dimension $1$ | index $2$ | $0,1$ | no |
| $\mathbb{B}_{\mathrm{r}}$ | $\mathbb{C}$ | $2$ | $\mathbb{C}_+,\mathbb{C}_-$ of dimension $1$ | none | $0,1,\Pi_+,\Pi_-$ | no |
| $\mathbb{H}$ | $\mathbb{R}$ | $4$ | $\mathbb{H}$ of dimension $4$ | none | $0,1$ | no |
| $\mathbb{H}$ | $\mathbb{C}$ | $2$ | $\mathbb{C}^2$ of dimension $2$ | index $2$ | many | yes |
| $\mathbb{H}_{\mathrm{s}}$ | $\mathbb{R}$ | $4$ | $\mathbb{R}^2$ of dimension $2$ | index $2$ | many | yes |
| $\mathbb{B}$ | $\mathbb{C}$ | $2$ | $\mathbb{C}^2$ of dimension $2$ | index $2$ | matrix units | yes |
| $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{R}$ | $8$ | $\mathbb{H}_+,\mathbb{H}_-$ of dimension $4$ | none | $0,1,\Pi_+,\Pi_-$ | no |
| $M_2(\mathbb{C})$ | $\mathbb{C}$ | $2$ | $\mathbb{C}^2$ of dimension $2$ | index $2$ | matrix units | yes |
| $M_3(\mathbb{C})$ | $\mathbb{C}$ | $3$ | $\mathbb{C}^3$ of dimension $3$ | index $3$ | matrix units | yes |
| $M_4(\mathbb{C})$ | $\mathbb{C}$ | $4$ | $\mathbb{C}^4$ of dimension $4$ | index $4$ | matrix units | yes |
| $M_5(\mathbb{C})$ | $\mathbb{C}$ | $5$ | $\mathbb{C}^5$ of dimension $5$ | index $5$ | matrix units | yes |
| $M_6(\mathbb{C})$ | $\mathbb{C}$ | $6$ | $\mathbb{C}^6$ of dimension $6$ | index $6$ | matrix units | yes |
| $M_n(\mathbb{C})$ | $\mathbb{C}$ | $n$ | $\mathbb{C}^n$ of dimension $n$ | index $n$ | matrix units | yes |

**The commutative algebras.** $\mathbb{C}$ over $\mathbb{R}$ and over $\mathbb{C}$ is a field: every nonzero element is invertible, the only idempotents are $0$ and $1$, and every bracket vanishes. $\mathbb{D}$ is not a field: it has the idempotents $e_\pm=\tfrac12(1\pm j)$ and the zero divisors $1\pm j$. The dual numbers $\mathbb{D}'$ have the nilpotent $\varepsilon$ and the maximal ideal $(\varepsilon)$, and only the idempotents $0,1$. The reduced biquaternions $\mathbb{B}_{\mathrm r}$ have the two central idempotents $\Pi_\pm=\tfrac12(1\pm j)$ and two non-isomorphic simple modules $\mathbb{C}_\pm$. All of them are commutative, so every bracket vanishes and every element is central; none has a spin triple.

**The quaternions.** $\mathbb{H}$ over $\mathbb{R}$ is a division algebra. Its only nilpotent is $0$ and its only idempotents are $0$ and $1$. It has no spin triple in itself: for every $S\in\mathbb{H}$ the eigenvalues of $\operatorname{ad}_S$ are $0$ and $\pm2i\lvert s\rvert$, where $s$ is the imaginary part, and the value $1$ never occurs, so $[S,U]=U$ has no nonzero real solution. The triple exists in the complexification $\mathbb{B}$. The split biquaternions $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$ are a product of two division algebras, so they have no nilpotent and no spin triple either; their complexification is $\mathbb{B}\times\mathbb{B}$.

**The matrix algebras.** $M_n$ has the principal triple
$$
S=\operatorname{diag}\left(\tfrac{n-1}{2},\tfrac{n-3}{2},\ldots,-\tfrac{n-1}{2}\right),\qquad
U=\sum_{i=1}^{n-1}E_{i,i+1},\qquad
V=\sum_{i=1}^{n-1}i(n-i)E_{i+1,i}.
$$
The defining module $\mathbb{C}^n$ has weights $\tfrac{n-1}{2},\ldots,-\tfrac{n-1}{2}$. The adjoint module has weights the differences of those numbers, from $-(n-1)$ to $n-1$.

**The biquaternion carriers.** At $M_2(\mathbb{C})$ the three carriers are the centre $\mathbb{C}I$, the defining module $\mathbb{C}^2$, and the traceless part $\mathfrak{sl}_2$. Their dimensions are $1,2,3$. The observed set $0,\tfrac12,1$ is the set of their spins. Every definition below reads this family in a different way.

## 2. The Natural Carrier Family

**The family.** Let $A$ be a finite-dimensional unital algebra. The **natural family** is
$$
\mathcal{F}(A)=\{W:\ W\ \text{is an irreducible constituent of }A\text{ as a left }A\text{-module}\}\ \cup\ \{W:\ W\ \text{is an irreducible constituent of }A\text{ under the adjoint action}\}.
$$
When $k$ is not algebraically closed the family is taken after complexification.

**Why this family.** The left regular module and the adjoint module are the two modules that every unital algebra carries without extra structure, so the family is intrinsic. It is not the family of all simple modules: for $M_n$ that is only $\mathbb{C}^n$. It is not the family of all triples either: a triple quantifies over nilpotents and produces a chain that need not be a constituent of $A$ (see §3).

**The cases.** The table lists both sources, the deduplicated family, and its size. Multiplicities are dropped, because the family is a set of isomorphism classes: the left regular module of $M_n$ is $n$ copies of $\mathbb{C}^n$ and contributes that class once.

| algebra | left regular | adjoint | $\mathcal{F}(A)$ (dimension) | size |
|---|---|---|---|---|
| $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}$ | $\mathbb{R}(1)$ | $1$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\mathbb{C}$ | $\mathbb{R}$ | $\mathbb{C}(2)$, $\mathbb{R}(1)$ | $2$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\mathbb{C}$ | $\mathbb{C}$ | $\mathbb{C}(1)$ | $1$ |
| $\mathbb{D}$ | $L_+\oplus L_-$ | $\mathbb{R}$ | $L_+(1)$, $L_-(1)$, $\mathbb{R}(1)$ | $3$ |
| $\mathbb{D}'$ | $\mathbb{R}[\varepsilon]$ | $\mathbb{R}$ | $\mathbb{R}(1)$ | $1$ |
| $\mathbb{B}_{\mathrm{r}}$ | $\mathbb{C}_+\oplus\mathbb{C}_-$ | $\mathbb{C}_{\mathrm{diag}}$ | $\mathbb{C}_+(1)$, $\mathbb{C}_-(1)$, $\mathbb{C}_{\mathrm{diag}}(1)$ | $3$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\mathbb{H}$ | $\mathbb{R}\oplus\operatorname{Im}\mathbb{H}$ | $\mathbb{H}(4)$, $\mathbb{R}(1)$, $\operatorname{Im}\mathbb{H}(3)$ | $3$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $2\mathbb{C}^2$ | $\mathbb{C}\oplus\mathfrak{sl}_2$ | $\mathbb{C}^2(2)$, $\mathbb{C}(1)$, $\mathfrak{sl}_2(3)$ | $3$ |
| $\mathbb{H}_{\mathrm{s}}$ | $2\mathbb{R}^2$ | $\mathbb{R}\oplus\mathfrak{sl}_2(\mathbb{R})$ | $\mathbb{R}^2(2)$, $\mathbb{R}(1)$, $\mathfrak{sl}_2(\mathbb{R})(3)$ | $3$ |
| $\mathbb{B}$ | $2\mathbb{C}^2$ | $\mathbb{C}I\oplus\mathfrak{sl}_2(\mathbb{C})$ | $\mathbb{C}^2(2)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_2(\mathbb{C})(3)$ | $3$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\mathbb{H}_+\oplus\mathbb{H}_-$ | $\mathbb{R}_+\oplus\mathbb{R}_-\oplus\operatorname{Im}\mathbb{H}_+\oplus\operatorname{Im}\mathbb{H}_-$ | $\mathbb{H}_+(4)$, $\mathbb{H}_-(4)$, $\mathbb{R}_+(1)$, $\mathbb{R}_-(1)$, $\operatorname{Im}\mathbb{H}_+(3)$, $\operatorname{Im}\mathbb{H}_-(3)$ | $6$ |
| $M_2(\mathbb{C})$ | $2\mathbb{C}^2$ | $\mathbb{C}I\oplus\mathfrak{sl}_2$ | $\mathbb{C}^2(2)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_2(3)$ | $3$ |
| $M_3(\mathbb{C})$ | $3\mathbb{C}^3$ | $\mathbb{C}I\oplus\mathfrak{sl}_3$ | $\mathbb{C}^3(3)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_3(8)$ | $3$ |
| $M_4(\mathbb{C})$ | $4\mathbb{C}^4$ | $\mathbb{C}I\oplus\mathfrak{sl}_4$ | $\mathbb{C}^4(4)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_4(15)$ | $3$ |
| $M_5(\mathbb{C})$ | $5\mathbb{C}^5$ | $\mathbb{C}I\oplus\mathfrak{sl}_5$ | $\mathbb{C}^5(5)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_5(24)$ | $3$ |
| $M_6(\mathbb{C})$ | $6\mathbb{C}^6$ | $\mathbb{C}I\oplus\mathfrak{sl}_6$ | $\mathbb{C}^6(6)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_6(35)$ | $3$ |
| $M_n(\mathbb{C})$ | $n\mathbb{C}^n$ | $\mathbb{C}I\oplus\mathfrak{sl}_n$ | $\mathbb{C}^n(n)$, $\mathbb{C}I(1)$, $\mathfrak{sl}_n(n^2-1)$ | $3$ |

**The small size.** The family has at most six classes in the cases above. It has three classes for $\mathbb{D}$, $\mathbb{B}_{\mathrm r}$, $\mathbb{H}$ over $\mathbb{R}$ and over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $M_n$: one or two simple modules, and an adjoint that splits into the centre and the traceless part. It has two classes for $\mathbb{C}$ over $\mathbb{R}$. It has one class for $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, and $\mathbb{D}'$, whose regular module has a unique simple constituent. It has six classes for $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$, because each factor contributes a simple module, a centre line, and a traceless part. An algebra with more simple modules has a larger family; these cases do not.

**At $M_2(\mathbb{C})$.** The family is the centre $\mathbb{C}I$, the defining module $\mathbb{C}^2$, and the traceless part $\mathfrak{sl}_2$. These are exactly the three carriers of the biquaternion.

## 3. The Triple

**Definition.** A **spin triple** in $A$ is a triple $(S,U,V)$ with
$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S.
$$
On an irreducible carrier, the eigenvalues of $S$ are $j,j-1,\ldots,-j$; the **triple spin** is $j$. Equivalently, a **spin datum** is a pair $(S,u)$ with $S$ semisimple, $u$ nilpotent, $[S,u]=u$, and the spectrum of $S$ on the chain generated by $u$ equal to $j,j-1,\ldots,-j$. The third element is determined on the chain by the relations; the pair $(S,u)$ is the minimal data. The **triple list** is the set over all triples in $A$.

**The cases.**

| algebra | principal list | all-triple list |
|---|---|---|
| $\mathbb{R}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm{r}}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\{0\}$ | $\{0\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,1,2\}$ | $\{0,\tfrac12,1,2\}$ |
| $M_4(\mathbb{C})$ | $\{0,\tfrac32,3\}$ | $\{0,\tfrac12,1,\tfrac32,2,3\}$ |
| $M_5(\mathbb{C})$ | $\{0,2,4\}$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ |
| $M_6(\mathbb{C})$ | $\{0,\tfrac52,5\}$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,4,5\}$ |
| $M_n(\mathbb{C})$ | $\{0,\tfrac{n-1}{2},n-1\}$ | $\{0,\tfrac12,\ldots,\tfrac{n-1}{2}\}\cup\{0,1,\ldots,n-1\}$ |

**The matrix lists.** For $M_n$ with the principal triple, the defining spin is $(n-1)/2$ and the adjoint top is $n-1$; the elementary list is
$$
\left\{0,\ \frac{n-1}{2},\ n-1\right\}.
$$
Over all triples, a nilpotent of index $\ell\le n$ gives the defining spin $(\ell-1)/2$ and the adjoint top $\ell-1$. The union is
$$
\left\{0,\tfrac12,\ldots,\tfrac{n-1}{2}\right\}\cup\{0,1,\ldots,n-1\}.
$$
For $n=5$ this is $\{0,\tfrac12,1,\tfrac32,2,3,4\}$; the values $\tfrac52$ and $\tfrac72$ are absent because the defining carrier has at most five levels and the adjoint top is an integer.

**The quaternion rows.** $\mathbb{H}$ over $\mathbb{R}$ has no triple in itself. The triple exists in $\mathbb{B}$, where the carrier $\mathbb{H}$ (as a left module) has spin $\tfrac12$ and the adjoint has content $0,1$. The list $\{0,\tfrac12,1\}$ is a list of $\mathbb{B}$, not of $\mathbb{H}$ alone. The split biquaternions $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$ also have no triple, for the same reason: no nonzero nilpotent. Their complexification is $\mathbb{B}\times\mathbb{B}$.

**What the definition does.** It is finite and intrinsic for $M_n$. It gives the corpus's elementary list and the adjoint content. It is the definition used in the principal-pair articles and in the biquaternion articles. It is not intrinsic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{B}_{\mathrm r}$, $\mathbb{H}$, or $\mathbb{H}_{\mathbb D}$: those algebras have no nonzero triple, so the list collapses to $\{0\}$ (or to the list of the complexification).

**Verdict.** The physical definition for $M_n$ and for $\mathbb{B}$. On $M_2(\mathbb{C})$ it gives $\{0,\tfrac12,1\}$, the experimental set. It is one of the five definitions that pass, and it is the one that generalizes to all $M_n$.

## 4. The Module List

**Definition.** The **module list** is
$$
\Sigma_{\mathrm{mod}}(A)=\left\{\frac{\dim_k W-1}{2}:\ W\in\mathcal{F}(A)\right\}.
$$
It returns a set, and it needs no triple and no chosen carrier.

**The cases.**

| algebra | module list |
|---|---|
| $\mathbb{R}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0,\tfrac12\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm{r}}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0,1,\tfrac32\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\{0,1,\tfrac32\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,1,\tfrac72\}$ |
| $M_4(\mathbb{C})$ | $\{0,\tfrac32,7\}$ |
| $M_5(\mathbb{C})$ | $\{0,2,\tfrac{23}{2}\}$ |
| $M_6(\mathbb{C})$ | $\{0,\tfrac52,17\}$ |
| $M_n(\mathbb{C})$ | $\{0,\tfrac{n-1}{2},\tfrac{n^2-2}{2}\}$ |

**What it gives.** At $M_2(\mathbb{C})$ the list is $\{0,\tfrac12,1\}$, the experimental set. At $M_n$ it is $0$, $(n-1)/2$, $(n^2-2)/2$: the defining value and the adjoint-dimension value. It coincides with the elementary list $0,(n-1)/2,n-1$ only at $n=2$, because $\dim\mathfrak{sl}_2=3$. At $n\ge3$ it reads the dimension of the adjoint, not its spin.

**Verdict.** Passes the $M_2(\mathbb{C})$ test; does not generalize above $n=2$.

## 5. The Casimir List

**Definition.** Let $C$ be the Casimir of the semisimple part of the algebra. For each $W\in\mathcal{F}(A)$ let $C|_W=c_W I$. The **Casimir list** is
$$
\Sigma_C(A)=\left\{\frac{-1+\sqrt{1+4c_W}}{2}:\ W\in\mathcal{F}(A)\right\}.
$$
Write $j(c)=(-1+\sqrt{1+4c})/2$ for the entry of a Casimir eigenvalue $c$.

**The cases.**

| algebra | Casimir list |
|---|---|
| $\mathbb{R}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm{r}}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,0.758,1.303\}$ |
| $M_4(\mathbb{C})$ | $\{0,0.958,1.561\}$ |
| $M_5(\mathbb{C})$ | $\{0,1.128,1.791\}$ |
| $M_6(\mathbb{C})$ | $\{0,1.279,2\}$ |
| $M_n(\mathbb{C})$ | $\{0,j(\tfrac{n^2-1}{2n}),j(n)\}$ |

**What it gives.** It is exact on $M_2(\mathbb{C})$: the Casimirs of the centre, the defining module, and the adjoint are $0$, $\tfrac34$, and $2$, which give $0$, $\tfrac12$, and $1$. It fails on $M_n$ for $n\ge3$: the defining module of $\mathfrak{sl}_3$ has $c=\tfrac43$, which gives $0.758$, not $1$; the adjoint has $c=3$, which gives $1.303$, not $2$. For $M_4$ the values are $0.958$ and $1.561$; for $M_6$ they are $1.279$ and $2$. The formula is an $\mathfrak{su}(2)$ formula, and it computes the spin only when the semisimple part is $\mathfrak{sl}_2$. That is the case for $\mathbb{H}$ over $\mathbb{R}$, $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, and $\mathbb{B}$, where it gives $\{0,\tfrac12,1\}$, and for $\mathbb{H}_{\mathbb D}$, where each semisimple factor is $\mathfrak{su}(2)$ and it gives the same list.

**Verdict.** Passes the $M_2(\mathbb{C})$ test because the semisimple part is $\mathfrak{sl}_2$; fails above $n=2$.

## 6. The Highest-Weight List

**Definition.** Choose a Cartan subalgebra, a positive system, and a principal $\mathfrak{sl}_2$ with coroot $H$. For $W\in\mathcal{F}(A)$ let $\lambda_W$ be the highest weight. The **highest-weight list** is
$$
\Sigma_{\mathrm{hw}}(A)=\left\{\frac{\lambda_W(H)}{2}:\ W\in\mathcal{F}(A)\right\}.
$$

**The cases.**

| algebra | highest-weight list |
|---|---|
| $\mathbb{R}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm{r}}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,1,2\}$ |
| $M_4(\mathbb{C})$ | $\{0,\tfrac32,3\}$ |
| $M_5(\mathbb{C})$ | $\{0,2,4\}$ |
| $M_6(\mathbb{C})$ | $\{0,\tfrac52,5\}$ |
| $M_n(\mathbb{C})$ | $\{0,\tfrac{n-1}{2},n-1\}$ |

**What it gives.** It is exact on $M_2(\mathbb{C})$ and on the principal family of $M_n$. The value is a weight, so a unit step is part of the definition; the list is the set of top weights of the natural family.

**Verdict.** Passes the $M_2(\mathbb{C})$ test and generalizes to the principal family of $M_n$. It needs a choice of principal $\mathfrak{sl}_2$, but no triple.

## 7. The Orbit List

**Definition.** Choose a principal $\mathfrak{sl}_2$ in the semisimple part. Let $O_f$ be a coadjoint orbit of that $\mathfrak{sl}_2$, normalized so that the unit sphere of $\mathfrak{su}(2)$ has area $4\pi$. The orbit method gives $j\in\tfrac12\mathbb{Z}_{\ge0}$. The **orbit list** cuts this set at the largest constituent:
$$
\Sigma_{\mathrm{orb}}(A)=\left\{j\in\tfrac12\mathbb{Z}_{\ge0}:\ 2j+1\le\max_{W\in\mathcal{F}(A)}\dim_k W\right\}.
$$

**The cases.**

| algebra | largest constituent | orbit list |
|---|---|---|
| $\mathbb{R}$ | $1$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $2$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $1$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{D}$ | $1$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{D}'$ | $1$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{B}_{\mathrm{r}}$ | $1$ (no $\mathfrak{sl}_2$) | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $4$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $3$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm{s}}$ | $3$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $3$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb{D}}$ | $4$ | $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $3$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $8$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,\tfrac72\}$ |
| $M_4(\mathbb{C})$ | $15$ | $\{0,\tfrac12,\ldots,7\}$ |
| $M_5(\mathbb{C})$ | $24$ | $\{0,\tfrac12,\ldots,\tfrac{23}{2}\}$ |
| $M_6(\mathbb{C})$ | $35$ | $\{0,\tfrac12,\ldots,17\}$ |
| $M_n(\mathbb{C})$ | $n^2-1$ | $\{0,\tfrac12,\ldots,\tfrac{n^2-2}{2}\}$ |

**The rows without a semisimple part.** $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, and $\mathbb{B}_{\mathrm r}$ have no semisimple part, so they have no $\mathfrak{sl}_2$ orbits; their list is $\{0\}$ even when the cut would allow more. The same remark applies to the Casimir and highest-weight lists.

**What it gives.** It is exact at $M_2(\mathbb{C})$ because $\dim\mathfrak{sl}_2=3$ gives the cut $j\le1$. For $M_n$ with $n\ge3$ the list uses the principal $\mathfrak{sl}_2$; the cut is the adjoint dimension. It is overcomplete for $n\ge3$: the adjoint of $\mathfrak{sl}_3$ has dimension $8$, and the cut admits spins up to $\tfrac72$; at $M_6$ the cut admits spins up to $17$. The cut is not intrinsic to the orbit; it uses the module dimensions.

**Verdict.** Passes the $M_2(\mathbb{C})$ test with the cut; overcomplete above $n=2$. The cut is extra data.

## 8. The Five Agree on $M_2(\mathbb{C})$

**The table.** The five definitions and the carrier each reads.

| definition | what it reads | result on $M_2(\mathbb{C})$ |
|---|---|---|
| triple | the brackets on all carriers | $\{0,\tfrac12,1\}$ |
| module list | dimensions of the natural family | $\{0,\tfrac12,1\}$ |
| Casimir list | Casimir eigenvalues on the natural family | $\{0,\tfrac12,1\}$ |
| highest-weight list | top weights on the natural family | $\{0,\tfrac12,1\}$ |
| orbit list | orbits with $2j+1\le3$ | $\{0,\tfrac12,1\}$ |

**The three values are the three carriers.** The centre gives $0$; the defining module gives $\tfrac12$; the traceless part of the adjoint gives $1$. The five definitions read the same three carriers.

**They are not restatements.** The triple reads the brackets. The module list reads the dimensions. The Casimir list reads the quadratic Casimir. The highest-weight list reads the top weight. The orbit list reads the coadjoint orbit. The formulas are different and the data are different. They agree at $M_2(\mathbb{C})$ because the natural family is exactly the three carriers.

## 9. The Five Diverge Above $M_2(\mathbb{C})$

**The table.**

| definition | $M_3(\mathbb{C})$ | $M_4(\mathbb{C})$ | $M_5(\mathbb{C})$ | $M_6(\mathbb{C})$ |
|---|---|---|---|---|
| triple, all | $\{0,\tfrac12,1,2\}$ | $\{0,\tfrac12,1,\tfrac32,2,3\}$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,4,5\}$ |
| triple, principal | $\{0,1,2\}$ | $\{0,\tfrac32,3\}$ | $\{0,2,4\}$ | $\{0,\tfrac52,5\}$ |
| module list | $\{0,1,\tfrac72\}$ | $\{0,\tfrac32,7\}$ | $\{0,2,\tfrac{23}{2}\}$ | $\{0,\tfrac52,17\}$ |
| Casimir list | $\{0,0.758,1.303\}$ | $\{0,0.958,1.561\}$ | $\{0,1.128,1.791\}$ | $\{0,1.279,2\}$ |
| highest-weight list | $\{0,1,2\}$ | $\{0,\tfrac32,3\}$ | $\{0,2,4\}$ | $\{0,\tfrac52,5\}$ |
| orbit list | $\{0,\ldots,\tfrac72\}$ | $\{0,\ldots,7\}$ | $\{0,\ldots,\tfrac{23}{2}\}$ | $\{0,\ldots,17\}$ |

**Which generalize.** The all-triple list and the highest-weight list give half-integer spins on $M_n$. The module list gives the adjoint-dimension value, which is $\tfrac72$ or $\tfrac{23}{2}$, not the adjoint spin. The Casimir list gives non-half-integers. The orbit list is overcomplete. Only the triple and the highest-weight list are general definitions of the spin of the principal family of $M_n$; the other three are exact only at $n=2$.

**The physical reading.** For the biquaternion, the five agree. For $M_n$ above $n=2$, the physical list is the triple's. The module list, the Casimir list, and the orbit list are diagnostics of the defining representation, not general definitions. The $M_2(\mathbb{C})$ test is necessary for the biquaternion; it is not sufficient for a general definition. The companion article records the methods that fail even the necessary test.

## 10. Checks

**The triple.** With $S=\operatorname{diag}(\tfrac12,-\tfrac12)$, $U=E_{12}$, $V=E_{21}$,
$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S.
$$
The defining module has weights $\pm\tfrac12$; the adjoint has weights $0,\pm1$; the centre has weight $0$.

**The left multiplication.** $L_S$ on $M_2(\mathbb{C})$ has eigenvalues $\pm\tfrac12$, each of multiplicity $2$. These are the weights of the defining module; its top weight is $\tfrac12$.

**The adjoint.** $\operatorname{ad}_S$ has eigenvalues $0$ of multiplicity $2$ and $\pm1$. These are the adjoint weights $0,\pm1$; the adjoint spin is $1$.

**The Casimirs.** The centre, the defining module, and the adjoint have Casimirs $0$, $\tfrac34$, and $2$. The formula gives $0$, $\tfrac12$, and $1$.

**The orbit cut.** The largest constituent has dimension $3$, so $2j+1\le3$ gives $j\le1$.

**The quaternion check.** $\operatorname{ad}_i$ has eigenvalues $0$ of multiplicity $2$ and $\pm2i$; the normalized generator $J_3=\tfrac12\operatorname{ad}_{ie_3}$ has $0$ of multiplicity $2$ and $\pm1$. This is the spin-$1$ content of the adjoint carrier in $\mathbb{B}$.

| check | computation | result |
|---|---|---|
| $M_2$ triple | brackets with $S,U,V$ | $\mathfrak{sl}_2$ |
| $M_2$ defining | weights $\pm\tfrac12$ | $j=\tfrac12$ |
| $M_2$ adjoint | weights $0,\pm1$ | $j=1$ |
| $M_2$ centre | fixed | $j=0$ |
| $M_2$ left multiplication | eigenvalues $\pm\tfrac12$, multiplicity $2$ | weights $\pm\tfrac12$ |
| $M_2$ adjoint spectrum | $0$ (multiplicity $2$), $\pm1$ | weights $0,\pm1$ |
| $M_2$ Casimirs | $0,\tfrac34,2$ | $0,\tfrac12,1$ |
| $M_2$ orbit cut | $2j+1\le3$ | $j\le1$ |
| $\mathbb{H}$ adjoint | $0$ (multiplicity $2$), $\pm2i$ | normalized $0,\pm1$ |

## 11. The Five Methods in All Cases

**The table.** One row per case, one column per method. The base field is the one stated in §1.

| algebra | triple | module | Casimir | highest weight | orbit |
|---|---|---|---|---|---|
| $\mathbb{R}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0\}$ | $\{0,\tfrac12\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm r}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0\}$ | $\{0,1,\tfrac32\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm s}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb D}$ | $\{0\}$ | $\{0,1,\tfrac32\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,\tfrac12,1,2\}$ | $\{0,1,\tfrac72\}$ | $\{0,0.758,1.303\}$ | $\{0,1,2\}$ | $\{0,\tfrac12,\ldots,\tfrac72\}$ |
| $M_4(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,3\}$ | $\{0,\tfrac32,7\}$ | $\{0,0.958,1.561\}$ | $\{0,\tfrac32,3\}$ | $\{0,\tfrac12,\ldots,7\}$ |
| $M_5(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ | $\{0,2,\tfrac{23}{2}\}$ | $\{0,1.128,1.791\}$ | $\{0,2,4\}$ | $\{0,\tfrac12,\ldots,\tfrac{23}{2}\}$ |
| $M_6(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,4,5\}$ | $\{0,\tfrac52,17\}$ | $\{0,1.279,2\}$ | $\{0,\tfrac52,5\}$ | $\{0,\tfrac12,\ldots,17\}$ |
| $M_n(\mathbb{C})$ | $\{0,\tfrac12,\ldots,\tfrac{n-1}{2}\}\cup\{0,1,\ldots,n-1\}$ | $\{0,\tfrac{n-1}{2},\tfrac{n^2-2}{2}\}$ | $\{0,j(\tfrac{n^2-1}{2n}),j(n)\}$ | $\{0,\tfrac{n-1}{2},n-1\}$ | $\{0,\tfrac12,\ldots,\tfrac{n^2-2}{2}\}$ |

**The agreements.** On $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, and $\mathbb{B}_{\mathrm r}$ all five give $\{0\}$. On $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $M_2(\mathbb{C})$ all five give $\{0,\tfrac12,1\}$; this is the biquaternion list. $\mathbb{C}$ over $\mathbb{R}$ is the one commutative case where the module list separates: it gives $\{0,\tfrac12\}$ from the real dimension of $\mathbb{C}$, while the other four give $\{0\}$.

**The scope.** The rows are the finite-dimensional algebras over $\mathbb{R}$ or $\mathbb{C}$ that Part VI treats as categories. The categories *Complexoid*, *Split-Complexoid*, *Quaternioid*, and *Biquaternion Algebraic Structures* are not separate algebras: they carry extra products, forms, and subspaces on $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$, and $\mathbb{B}$, which are already rows. *Structural Comparison around Biquaternions* compares the rows and adds no algebra. The Booleans, $\mathbb{N}$, and $\mathbb{Z}$ are not finite-dimensional algebras over a field, and $\mathbb{Q}$ is excluded by the convention that the base field is $\mathbb{R}$ or $\mathbb{C}$; the five definitions do not apply to them.

**Two real forms do not agree.** On $\mathbb{H}$ over $\mathbb{R}$ and on $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$ the triple gives only $\{0\}$, because neither algebra has a nonzero nilpotent. The module list gives $\{0,1,\tfrac32\}$, because the simple module has real dimension $4$. The Casimir, highest-weight, and orbit lists give $\{0,\tfrac12,1\}$, because each semisimple factor is $\mathfrak{su}(2)$ and the carrier is its fundamental representation. A spin-$\tfrac12$ carrier can exist without a triple.

**The reduced biquaternion.** The row uses the complex base field of the corpus. Over $\mathbb{R}$ the two simple modules have real dimension $2$ and the module list gains $\tfrac12$; the other four lists remain $\{0\}$, because the algebra is commutative and has no nilpotent.

**Above $M_2(\mathbb{C})$ the five diverge.** At $M_3$ the module list reads the adjoint dimension $8$, the Casimir list returns $0.758$ and $1.303$, the highest-weight list returns $1$ and $2$, and the orbit list returns every half-integer up to $\tfrac72$. The divergence grows with $n$: at $M_6$ the module list returns $17$, the Casimir list returns $1.279$ and $2$, the highest-weight list returns $\tfrac52$ and $5$, and the orbit list returns every half-integer up to $17$.

**What the table selects.** The $M_2(\mathbb{C})$ test is passed by all five because the natural family there is exactly the centre, the defining module, and the traceless part, of dimensions $1,2,3$. The test does not separate them. The separation is the behavior on $M_n$ for $n\ge3$ and on the compact real forms.

## Summary

**Five definitions pass the biquaternion test.** They are the triple, the module list, the Casimir list, the highest-weight list, and the orbit list with the cut. On $M_2(\mathbb{C})$ all five give $\{0,\tfrac12,1\}$, the experimental set.

**They agree on the biquaternion and on its split and complex forms.** They give $\{0,\tfrac12,1\}$ on $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $M_2(\mathbb{C})$. They give $\{0\}$ on the commutative cases with one-dimensional simples, and $\{0\}$ from all methods except the module list on $\mathbb{C}$ over $\mathbb{R}$. On the compact real forms $\mathbb{H}$ and $\mathbb{H}_{\mathbb D}$ the triple gives only $\{0\}$: a spin-$\tfrac12$ carrier exists, but no nilpotent, so no triple.

**They diverge above $M_2(\mathbb{C})$.** The triple and the highest-weight list generalize to the principal family of $M_n$. The module list gives the adjoint-dimension value. The Casimir list gives non-half-integers. The orbit list is overcomplete. The $M_2(\mathbb{C})$ test selects the pertinent definitions; the behavior on $M_n$ selects the general ones.

**The incomplete methods are elsewhere.** The methods that fail the $M_2(\mathbb{C})$ test — dimension, ladder, Peirce, quiver, spectral, the adjoint alone, the half-angle, the unrestricted representation labels, the circle weight, and the ribbon twist — are in *The Incomplete Definitions of the Spin of an Algebra*. Each of them captures a part; none of them is a definition of the list.

## Further Reading

- [The Incomplete Definitions of the Spin of an Algebra](the-incomplete-definitions-of-the-spin-of-an-algebra.html), for the methods that fail the test and the part each one captures.
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
- [Split-Quaternion Algebra](../articles_maths/split-quaternion-algebra.html), for $\mathbb{H}_{\mathrm s}\cong M_2(\mathbb{R})$.
- [Reduced Biquaternion Space](../articles_maths/reduced-biquaternion-space.html), for $\mathbb{B}_{\mathrm r}\cong\mathbb{C}\times\mathbb{C}$.
- [Dual-Numbers Algebra](../articles_maths/dual-numbers-algebra.html), for the nilpotent $\varepsilon$ and the maximal ideal.
- [Split-Biquaternion Algebra](../articles_maths/split-biquaternion-algebra.html), for $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$.
- [The Matrix Algebra $M_4(\mathbb{C})$](../articles_maths/the-matrix-algebra-m4c.html), for the case $n=4$.
- [The Matrix Algebra $M_6(\mathbb{C})$](../articles_maths/the-matrix-algebra-m6c.html), for the case $n=6$.
- [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html), for the grading that is not a spin.
