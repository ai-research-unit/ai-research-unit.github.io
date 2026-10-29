# __The Incomplete Definitions of the Spin of an Algebra__

## Introduction

**The test.** The biquaternion sector has three observed spin values: $0$ for the scalar, $\tfrac12$ for the fermion, and $1$ for the vector. Since $\mathbb{B}\cong M_2(\mathbb{C})$, a definition is pertinent for the sector only if, applied to $M_2(\mathbb{C})$ alone, it produces exactly
$$
\{0,\ \tfrac12,\ 1\}.
$$
The companion article, *Possible General Definitions of the Spin of an Algebra*, presents the five definitions that pass. This article presents the methods that fail. They are not worthless: each captures a part of the structure. They are incomplete as definitions of the spin list.

**The failure modes.** A method can fail in five ways.

1. **Wrong value:** it returns a number outside the experimental set.
2. **Incomplete:** it returns a proper subset of the experimental set.
3. **Overcomplete:** it returns an infinite set, or a set with extra values.
4. **Normalization:** it returns the coefficient of a generator, not a spin.
5. **Extra structure:** it needs data beyond the algebra.

**The six algebras.** The test cases are $\mathbb{C}$, the split-complex numbers $\mathbb{D}$, the quaternions $\mathbb{H}$, and the matrix algebras $M_2(\mathbb{C})$, $M_3(\mathbb{C})$, $M_5(\mathbb{C})$. The field is stated in every table.

**Conventions.** The field is $\mathbb{R}$ or $\mathbb{C}$ as stated. The indexing is $1$-based. Matrix notation is used only for the matrix algebras. No Clifford algebra is used. The biquaternion is $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$.

## 1. The Failure Table

**The audit.** The table applies every incomplete method to $M_2(\mathbb{C})$ and compares the result with $\{0,\tfrac12,1\}$.

| method | result on $M_2(\mathbb{C})$ | failure | what it captures |
|---|---|---|---|
| dimension over $\mathbb{C}$ | $\{\tfrac12\}$ | incomplete | carrier size |
| dimension over $\mathbb{R}$ | $\{\tfrac32\}$ | wrong value | real carrier size |
| ladder list | $\{0,\tfrac12\}$ | incomplete | Jordan chain |
| regular spin | $\tfrac12$ | incomplete | maximal chain |
| Peirce chain | $\{0,\tfrac12\}$ | incomplete | corner chain |
| quiver | $\{0\}$ | wrong value | Morita class |
| spectral count | $\{0,\tfrac12\}$ | incomplete | eigenvalue count |
| adjoint alone | $\{0,1\}$ | incomplete | spin-$1$ carrier |
| half-angle | $\tfrac12$ and $1$ | normalization | rotor parameter |
| unrestricted highest weight | all $j\ge0$ | overcomplete | representation label |
| unrestricted Casimir | all $j\ge0$ | overcomplete | representation label |
| unrestricted coadjoint | all $j\ge0$ | overcomplete | orbit label |
| circle weight | $0$ or $\{0,\tfrac12\}$ mod $1$ | incomplete | parity |
| ribbon twist | $0$ | wrong value | topological spin |

**The reading.** The methods fall into four families: those that read one carrier (dimension, adjoint), those that read one chain (ladder, Peirce), those that read a coarse invariant (quiver, spectral, circle, ribbon), and those that read a representation label without a bound (highest weight, Casimir, coadjoint). The half-angle is a coordinate of the rotor; its coefficient is a normalization of the generator. The circle weight and the ribbon twist also need extra structure: a circle action or a ribbon category. §2 to §10 give each definition, its table on the six algebras, and the reason for its failure.

## 2. Dimension of a Simple Module

**Definition.** Let $A$ be a finite-dimensional $k$-algebra and $V$ a simple left $A$-module. The **dimension spin** is
$$
j=\frac{\dim_k V-1}{2}.
$$
The **left list** is the set over the simple modules. The definition uses no nilpotent, no grading, and no triple.

**The six algebras.** The table gives the value over the base field and the value after complexification of the module.

| algebra | over $k$ | after complexification |
|---|---|---|
| $\mathbb{C}$ | $\tfrac12$ | $0$ |
| $\mathbb{D}$ | $0$ | $0$ |
| $\mathbb{H}$ | $\tfrac32$ | $\tfrac12$ |
| $M_2(\mathbb{C})$ | $\tfrac12$ | $\tfrac12$ |
| $M_3(\mathbb{C})$ | $1$ | $1$ |
| $M_5(\mathbb{C})$ | $2$ | $2$ |

**Why it fails on $M_2(\mathbb{C})$.** Over $\mathbb{C}$ the only simple module is $\mathbb{C}^2$, and the formula gives $\tfrac12$; it misses $0$ and $1$. Viewed over $\mathbb{R}$, the same module has real dimension $4$, and the formula gives $\tfrac32$; that is a wrong value. A single carrier cannot produce a list of three.

**The quaternion row.** Over $\mathbb{R}$ the simple module is $\mathbb{H}$ itself, of real dimension $4$, and the formula gives $\tfrac32$. The spin-$\tfrac12$ carrier is $\mathbb{H}$ as a left $\mathbb{H}$-module; after complexification it is two copies of the complex irreducible of dimension $2$, and the formula gives $\tfrac12$. The real dimension counts two copies, so the formula doubles the spin and adds one half.

**What it captures.** The size of the carrier. It gives the defining spin $(n-1)/2$ of $M_n$, and it is the right count of states. It is not the spin of the algebra.

**Verdict.** Incomplete: a proper subset over $\mathbb{C}$, a wrong value over $\mathbb{R}$.

## 3. The Nilpotent Ladder

**Definition.** Let $u\in A$ be nilpotent and let
$$
\operatorname{ind}(u)=\min\{m:u^m=0\}
$$
be the nilpotency index. The **ladder spin** is
$$
j=\frac{\operatorname{ind}(u)-1}{2}.
$$
The **ladder list** is the set over all nilpotent $u\in A$. The **regular spin** is the maximum of the list.

**The six algebras.**

| algebra | indices | ladder list | regular spin |
|---|---|---|---|
| $\mathbb{C}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $\mathbb{D}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $\mathbb{H}$ | $\{1\}$ | $\{0\}$ | $0$ |
| $M_2(\mathbb{C})$ | $\{1,2\}$ | $\{0,\tfrac12\}$ | $\tfrac12$ |
| $M_3(\mathbb{C})$ | $\{1,2,3\}$ | $\{0,\tfrac12,1\}$ | $1$ |
| $M_5(\mathbb{C})$ | $\{1,\ldots,5\}$ | $\{0,\tfrac12,1,\tfrac32,2\}$ | $2$ |

**Why it fails on $M_2(\mathbb{C})$.** The list is $\{0,\tfrac12\}$; it misses $1$. The ladder reads the Jordan chain of a nilpotent. The adjoint spin $1$ is a semisimple weight, not a nilpotent index. The regular spin is $\tfrac12$, so the single-value reading is also incomplete.

**The quaternion row.** The ladder definition gives $0$ for $\mathbb{H}$. $\mathbb{H}$ is a division algebra, so the only nilpotent is $0$. The spin-$\tfrac12$ of the quaternion is not a ladder in $\mathbb{H}$; the ladder lives in the complexification $\mathbb{B}$.

**What it captures.** The Jordan chain of $M_n$. Its maximum equals the defining spin $(n-1)/2$ of the principal triple, and it is the right notion for the regular nilpotent. It cannot see a spectral label without a nilpotent.

**Verdict.** Incomplete: misses the adjoint spin.

## 4. The Peirce Chain

**Definition.** A **Peirce chain** is a sequence of nonzero orthogonal idempotents $e_1,\ldots,e_\ell$ in $A$,
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
The **Peirce list** is the set over all chains; the maximum is $0$ when no chain of length $2$ exists.

**The six algebras.**

| algebra | longest chain | Peirce list |
|---|---|---|
| $\mathbb{C}$ | $1$ | $\{0\}$ |
| $\mathbb{D}$ | $1$ | $\{0\}$ |
| $\mathbb{H}$ | $1$ | $\{0\}$ |
| $M_2(\mathbb{C})$ | $2$ | $\{0,\tfrac12\}$ |
| $M_3(\mathbb{C})$ | $3$ | $\{0,\tfrac12,1\}$ |
| $M_5(\mathbb{C})$ | $5$ | $\{0,\tfrac12,1,\tfrac32,2\}$ |

**Why it fails on $M_2(\mathbb{C})$.** The list is $\{0,\tfrac12\}$; it misses $1$. The Peirce chain reads the corner $e_iAe_{i+1}$. The adjoint spin is not a corner chain.

**The split-complex row.** $\mathbb{D}$ has four idempotents, including $e_+$ and $e_-$, but it is commutative. The corner is
$$
e_+\mathbb{D}e_-=0,
$$
because every product is symmetric. The two idempotents do not make a chain; the length is $1$ and the spin is $0$. The same algebra has the spectral label $\tfrac12$ from $S=(1,-1)$, but no chain of length $2$ and no ladder. The idempotents alone are not a spin.

**The chirality caution.** The $\pm$ of $e_\pm$ is a copy index. It is not the chirality of the biquaternion. The chirality is the nontrivial central involution of the complexification, $\chi=ij$ with $i$ and $j$ the two commuting imaginary units, $\chi^2=1$; it is central and outside the real biquaternion, equivalently the grading $S\oplus S^{\mathrm c}$. A Peirce pair is not that grading.

**What it captures.** The corner chain of $M_n$. It sees the matrix units and the nonzero corners. It is blind to division algebras and to commutative algebras.

**Verdict.** Incomplete: misses the adjoint spin; it is the combinatorial shadow of the ladder.

## 5. The Quiver

**Definition.** Let $A$ be finite-dimensional over a field. Its **Ext quiver** has one vertex for each simple module and one arrow for each basis element of $\operatorname{Ext}^1$ between two simple modules. When the field is algebraically closed, Gabriel's theorem identifies the basic algebra Morita equivalent to $A$ with $kQ/I$, with $Q$ a finite quiver and $I$ an admissible ideal. Let $\ell_Q$ be one plus the maximum number of arrows in a nonzero path of $kQ/I$. The **quiver spin** is
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

**Why it fails on $M_2(\mathbb{C})$.** The quiver gives $0$. It is Morita invariant, so it must give the same value to $M_2(\mathbb{C})$ and $\mathbb{C}$. The matrix size and the multiplicity of the simple module are invisible.

**What it captures.** The Morita class and the representation type. It is the right invariant for the category of modules, not for the spin.

**Verdict.** Wrong value: the Morita shadow.

## 6. The Spectral Level Count

**Definition.** Let $S\in A$ be semisimple over the algebraic closure, and let $L_S$ be left multiplication by $S$ on $A$. Suppose the distinct eigenvalues of $L_S$ are
$$
jd,\ (j-1)d,\ \ldots,\ -jd
$$
for some $j\in\tfrac12\mathbb{Z}_{\ge0}$ and some nonzero $d$ in the algebraic closure of $k$. The **spectral spin** is the number of levels minus one over two,
$$
j=\frac{r-1}{2},
$$
where $r=2j+1$ is the number of distinct eigenvalues. The **spectral list** is the set over all such $S$.

**The six algebras.**

| algebra | spectral list | witness |
|---|---|---|
| $\mathbb{C}$ | $\{0\}$ | $S=z$, one eigenvalue |
| $\mathbb{D}$ | $\{0,\tfrac12\}$ | $S=(1,-1)$, eigenvalues $\pm1$ |
| $\mathbb{H}$ | $\{0,\tfrac12\}$ | $S=i$, eigenvalues $\pm i$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12\}$ | $S=\operatorname{diag}(\tfrac12,-\tfrac12)$ |
| $M_3(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $S=\operatorname{diag}(1,0,-1)$ |
| $M_5(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2\}$ | $S=\operatorname{diag}(2,1,0,-1,-2)$ |

**Why it fails on $M_2(\mathbb{C})$.** The spectral list is $\{0,\tfrac12\}$; it misses $1$. The level count reads the semisimple spectrum on the left regular module. The adjoint spin $1$ is a weight on the adjoint carrier, not a level count on the left regular module.

**The split-complex row.** $S=(1,-1)$ has two eigenvalues $\pm1$, a full string with $d=2$, and the spin $\tfrac12$. There is no nilpotent and no triple. The value is a **grading label**, not a physical spin.

**What it captures.** The number of spectral levels of a semisimple element. It is scale-free and gives $\tfrac12$ to $\mathbb{H}$ and $\mathbb{D}$. It is the right notion for a grading.

**Verdict.** Incomplete: misses the adjoint spin.

## 7. The Adjoint Alone

**Definition.** Let $(S,U,V)$ be a spin triple and let $A$ act on itself by the adjoint action. The weights of $\operatorname{ad}_S$ are the differences $\lambda_i-\lambda_j$ of the weights of $S$. The **adjoint spin** is the top weight
$$
j_{\mathrm{ad}}=2j_{\mathrm{def}},
$$
where $j_{\mathrm{def}}$ is the defining spin. The **adjoint list** is the set over all triples.

**The six algebras.**

| algebra | adjoint spin | adjoint content |
|---|---|---|
| $\mathbb{C}$ | $0$ | $\{0\}$ |
| $\mathbb{D}$ | $0$ | $\{0\}$ |
| $\mathbb{H}$ | $1$ in $\mathbb{B}$ | $\{0,1\}$ |
| $M_2(\mathbb{C})$ | $1$ | $\{0,1\}$ |
| $M_3(\mathbb{C})$ | $2$ | $\{0,1,2\}$ |
| $M_5(\mathbb{C})$ | $4$ | $\{0,1,2,3,4\}$ |

**Why it fails on $M_2(\mathbb{C})$.** The adjoint content is $\{0,1\}$; it misses $\tfrac12$. The adjoint carrier is the spin-$1$ carrier. Read alone, it is not the whole list.

**The material sector.** For $\mathbb{H}$, the adjoint action on the vector part $\operatorname{Im}\mathbb{H}$ is the spin-$1$ representation. The Hermitian generator is $J_k=\tfrac12\operatorname{ad}_{ie_k}$, whose eigenvalues are $0,\pm1$. The raw derivation $\operatorname{ad}_{ie_k}$ has eigenvalues $0,\pm2$, so the factor $\tfrac12$ is the normalization that turns the derivation into the physical generator; the spin is $1$, not $2$. This is the construction of *Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form*.

**The caution for $n\ge3$.** The adjoint of $\mathfrak{gl}_n$ is reducible under the principal $\mathfrak{sl}_2$: it decomposes as $W_0\oplus W_1\oplus\cdots\oplus W_{n-1}$. The centre is $W_0$; the traceless part is $W_1\oplus\cdots\oplus W_{n-1}$. The top component has spin $n-1$, but the physical gauge field in the adjoint has spin $1$. The integer $n-1$ is the $\mathfrak{sl}_2$ content, not the $\mathfrak{su}(n)$ spin.

**What it captures.** The spin-$1$ carrier and the integer-spin sector. It is the right notion for the material sector, and one of the three carriers of the biquaternion.

**Verdict.** Incomplete: misses the defining spin $\tfrac12$.

## 8. The Half-Angle and the Polar Operators

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
with the half-angle. The coefficient $\tfrac12$ is the top eigenvalue of the generator $\sigma_z/2$ in the fundamental representation. For the spin-$1$ adjoint of $\mathfrak{su}(2)$ the generator $J_z$ has eigenvalues $1,0,-1$, and the rotor is $\exp(i\theta J_z)$, with the full angle. The coefficient is not the spin; it is the normalization of the generator in the chosen carrier.

**The six algebras.**

| algebra | defining coefficient | adjoint top coefficient |
|---|---|---|
| $\mathbb{C}$ | undefined | undefined |
| $\mathbb{D}$ | undefined | undefined |
| $\mathbb{H}$ | $\tfrac12$ | $1$ |
| $M_2(\mathbb{C})$ | $\tfrac12$ | $1$ |
| $M_3(\mathbb{C})$ | $\tfrac12$ | $2$ |
| $M_5(\mathbb{C})$ | $\tfrac12$ | $4$ |

**Why it fails on $M_2(\mathbb{C})$.** It gives $\tfrac12$ on the defining carrier and $1$ on the adjoint. That is a coefficient per carrier, not a list. It does not produce $0$.

**What it captures.** The parameter of the rotor and the normalization of the generator. It is the right notion for the polar decomposition.

**Verdict.** A coordinate of the rotor, not a definition of the spin.

## 9. The Unrestricted Representation Labels

**Highest weight.** Let $\mathfrak{g}$ be a reductive Lie algebra acting on $V$, choose a Cartan and a positive system, and let $\lambda$ be the highest weight. The **highest-weight spin** is $\lambda$; a number requires a chosen $\mathfrak{sl}_2$. For $\mathfrak{sl}_2$ with $\mathfrak{h}=\langle H\rangle$, the spin is $j=\lambda(H)/2$.

**Casimir.** Let $\mathfrak{g}$ be semisimple with an invariant form and Casimir $C$, and let $C|_V=c_V I$. For $\mathfrak{sl}_2$ the **Casimir spin** is
$$
j=\frac{-1+\sqrt{1+4c_V}}{2}.
$$
The formula uses the Casimir of the chosen $\mathfrak{sl}_2$, not the Casimir of the full algebra.

**Coadjoint orbit.** Let $f\in\mathfrak{g}^*$ and $O_f$ the coadjoint orbit with the Kirillov–Kostant–Souriau form. For $\mathfrak{su}(2)$, with the normalization in which the unit sphere has area $4\pi$, the **orbit spin** is $j=\operatorname{Area}(O_f)/(4\pi)$.

**The six algebras.** The table gives the unrestricted range, that is, the values over all representations of the chosen algebra.

| algebra | highest weight | Casimir | coadjoint |
|---|---|---|---|
| $\mathbb{C}$ | $0$ | $0$ | $0$ |
| $\mathbb{D}$ | $0$ | $0$ | $0$ |
| $\mathbb{H}$ | all $j\ge0$ | all $j\ge0$ | all $j\ge0$ |
| $M_2(\mathbb{C})$ | all $j\ge0$ | all $j\ge0$ | all $j\ge0$ |
| $M_3(\mathbb{C})$ | all $j$ after a choice of $\mathfrak{sl}_2$ | non-half-integers | flag variety |
| $M_5(\mathbb{C})$ | all $j$ after a choice of $\mathfrak{sl}_2$ | non-half-integers | flag variety |

**Why it fails on $M_2(\mathbb{C})$.** Over all representations, every $j\ge0$ occurs. The set is infinite; it does not produce the finite experimental list. The restricted versions, read on the natural family, are in the general article.

**On $M_3$ and $M_5$.** The highest weight of $\mathfrak{sl}_n$ is a vector, not a single number. The Casimir of the full algebra on the defining module gives $0.758$ and $1.128$, which are not half-integers. The coadjoint orbit is a flag variety, and the area formula does not produce a single spin. The definitions are $A_1$ definitions; they need a chosen $\mathfrak{sl}_2$ and a chosen representation.

**What they capture.** The labels of a representation: its highest weight, its Casimir, its orbit. They are the right notions for representation theory, not for the algebra's own list.

**Verdict.** Overcomplete: infinite unless restricted.

## 10. The Circle Weight and the Ribbon Twist

**Circle weight.** Let a circle $T\cong U(1)$ act on $V$, and let $\rho(e^{it})=e^{ijt}$ on the highest-weight space. The **weight** is $j\in\mathbb{R}/\mathbb{Z}$, and the **$2\pi$ sign** is $(-1)^{2j}$. Only $j$ modulo $1$ is defined; the integer part requires a lift.

**Ribbon twist.** Let $\mathcal{C}$ be a ribbon category, $X$ a simple object, and $\theta_X$ its twist. Write $\theta_X=e^{2\pi ih_X}$ with $h_X\in\mathbb{Q}/\mathbb{Z}$; $h_X$ is the **topological spin**.

**The six algebras.**

| algebra | circle weight | ribbon twist |
|---|---|---|
| $\mathbb{C}$ | $0$ | $0$ |
| $\mathbb{D}$ | $0$ | $0$ |
| $\mathbb{H}$ | $0,\tfrac12$ | $0$ or $\tfrac12$ |
| $M_2(\mathbb{C})$ | $0$ or $\tfrac12$ (mod $1$) | $0$ |
| $M_3(\mathbb{C})$ | $0$ (mod $1$) | $0$ |
| $M_5(\mathbb{C})$ | $0$ (mod $1$) | $0$ |

**Why it fails on $M_2(\mathbb{C})$.** The circle weight gives $0$ with the trivial action and $\tfrac12$ modulo $1$ with the natural action. The ribbon twist gives $0$. Both miss $1$. The methods see the parity of the spin, not the integer part.

**What they capture.** The parity and the topological spin. They are the right notions for a ribbon category, not for the algebra's own list. The definition requires a ribbon structure; it is extra data.

**Verdict.** Coarse: the parity shadow.

## 11. What Each Method Captures

| method | invariant | where it is the right tool |
|---|---|---|
| dimension | size of the carrier | counting states |
| ladder | Jordan chain | Jordan chains of $M_n$ |
| Peirce | corner chain | matrix units and idempotents |
| quiver | Morita class | representation type |
| spectral | eigenvalue count | gradings |
| adjoint | spin-$1$ carrier | the material sector |
| half-angle | rotor parameter | polar decomposition |
| highest weight | top weight | representation theory of $\mathfrak{sl}_2$ |
| Casimir | quadratic Casimir | representation theory of $\mathfrak{sl}_2$ |
| coadjoint | orbit area | geometric quantization of $SU(2)$ |
| circle weight | parity | $2\pi$ spin |
| ribbon twist | topological spin | ribbon categories |

**The common pattern.** Each method is the right tool for its own object. None of them is the spin list of the algebra.

## 12. Why They Were Mistaken for Definitions

**One carrier instead of three.** The dimension reads the defining module; the adjoint reads the adjoint module. Each gives one value, and the biquaternion needs three. The error is to take the value of one carrier for the list.

**One chain instead of the spectrum.** The ladder reads the Jordan chain of a nilpotent; the Peirce chain reads a chain of idempotents. Both are chains in $M_n$. The adjoint spin is a semisimple weight, not a chain. The error is to take the chain for the whole list.

**One coarse invariant instead of the spin.** The quiver is Morita invariant, the spectral count is a grading label, and the circle weight and the ribbon twist see only the parity. The error is to take an invariant that is constant on the interesting part.

**One representation instead of the algebra.** The highest weight, the Casimir, and the coadjoint orbit are labels of a chosen representation. Over all representations they are infinite; on the natural family they are finite, and the restricted versions are in the general article.

**One normalization instead of the spin.** The half-angle is the coordinate of the rotor; the coefficient in the exponent is the normalization of the generator on the fundamental carrier. The error is to take the coefficient for the eigenvalue.

**The test.** The $M_2(\mathbb{C})$ test separates the five pertinent definitions from these. A method that cannot produce $0$, $\tfrac12$, and $1$ on $M_2(\mathbb{C})$ is not a definition of the biquaternion's spin list.

## 13. Summary

**These methods fail the test.** On $M_2(\mathbb{C})$ they give a proper subset, a wrong value, an infinite set, or a coefficient. They are incomplete as definitions of the spin list.

**They are not useless.** Each captures a part: the carrier size, the Jordan chain, the corner chain, the Morita class, the eigenvalue count, the spin-$1$ carrier, the rotor parameter, a representation label, or the parity. §11 records the right use of each.

**The five pertinent definitions are elsewhere.** The triple, the module list, the Casimir list, the highest-weight list, and the orbit list with the cut are in *Possible General Definitions of the Spin of an Algebra*. They produce $\{0,\tfrac12,1\}$ on $M_2(\mathbb{C})$.

**The list.** The non-pertinent methods are: dimension over $\mathbb{C}$; dimension over $\mathbb{R}$; the ladder list; the regular spin; the Peirce chain; the quiver; the spectral count; the adjoint alone; the half-angle; the unrestricted highest weight; the unrestricted Casimir; the unrestricted coadjoint; the circle weight; the ribbon twist.

## Further Reading

- [Possible General Definitions of the Spin of an Algebra](the-general-definitions-of-the-spin-of-an-algebra.html), for the five definitions that pass the $M_2(\mathbb{C})$ test.
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
