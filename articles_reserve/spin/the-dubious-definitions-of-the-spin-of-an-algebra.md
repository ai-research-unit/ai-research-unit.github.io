# __The Dubious Definitions of the Spin of an Algebra__

## Introduction

**This file is a quarantine.** It records a programme that the corpus built on a false premise, and it records it so that the premise cannot return unnoticed. The premise was: *the spin of a particle is the highest weight of a representation of an $\mathfrak{sl}_2$ triple inside an algebra.* That is not a definition of spin. It is a computation of a weight, and it is valid only when the triple is the rotation triple and the carrier is the rest-frame one-particle space. The programme dropped both conditions, fitted its output to the three values observed at $M_2(\mathbb{C})$, and called the fit a definition.

**The correct definition.** Spin is the intrinsic angular momentum of a particle. In the rest frame the one-particle states satisfy

$$
\vec S^{\,2}\lvert s,m_s\rangle=\hbar^2 s(s+1)\lvert s,m_s\rangle,\qquad
S_z\lvert s,m_s\rangle=\hbar\,m_s\lvert s,m_s\rangle,
$$

with $s\in\{0,\tfrac12,1,\tfrac32,2,\dots\}$ and $m_s=-s,-s+1,\dots,s$. The multiplicity is $2s+1$, and the operator satisfies $[S_i,S_j]=i\hbar\,\epsilon_{ijk}S_k$. Relativistically, $s$ is the label of the little-group $SU(2)$ representation carried by the time-like unitary irreducible representation of the Poincaré group; mass and spin label the particle. For a massless particle the Lorentz-invariant label is helicity, $\lambda=\hat p\cdot\vec J=\pm s$. Integer $s$ is bosonic and half-integer $s$ is fermionic.

**A weight is not a definition.** The number $j=\lambda_{\max}(\rho(H))/2$ is a theorem about a carrier of a triple. It becomes the spin when $H=2S_z/\hbar$, when $\rho$ is the rotation action, and when the carrier is the rest-frame one-particle space. None of those conditions is algebraic. They are physical, and the programme never stated them.

**What this file contains.** Part I records the methods that the programme rejected as incomplete. Part II records the four methods that it accepted as general definitions. Part III states the verdict. The tables are kept because many of them are correct computations of weights, dimensions and orbit labels. They are not computations of spin.

**The rule for the reader.** Do not cite any formula in this file as a definition of spin. Cite it, if at all, as a statement about the representation theory of $\mathfrak{sl}_2$ or of $M_n(\mathbb{C})$. The physical definition is the one above, and the physics corpus states it in *Spin and the Three Elementary Carriers* and in *The Spin–Statistics Theorem in Biquaternionic Form*.

**The four halves, kept apart.** The symbol $\tfrac12$ occurs in four different roles in the material below, and conflating them is the source of most of the error. They are: the weight-to-spin conversion $j=\lambda_{\max}/2$; the antisymmetrisation $S=\tfrac12[U,V]$; the half-angle $\theta/2$ of the rotor; and the Hermitian normalisation $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$. Only the first is a conversion to a spin label, and only under the physical conditions above.

## Part I — The Incomplete Definitions

**The programme's test.** The biquaternion sector has three observed spin values: $0$ for the scalar, $\tfrac12$ for the fermion, and $1$ for the vector. Since $\mathbb{B}\cong M_2(\mathbb{C})$, the programme asked a definition to produce exactly

$$
\{0,\ \tfrac12,\ 1\}
$$

on $M_2(\mathbb{C})$. This test is recorded here, not endorsed: it selects by the answer and it ignores the physics. Part II records the four methods that passed it. Part I records the methods that failed it, and one method that passed it and was still rejected, the Casimir list. The failing methods are not worthless: each captures a part of the structure. None is a definition of spin.

**The verdicts.** A method fails in one of five ways, or it is dubious.

1. **Wrong value:** it returns a number outside the experimental set.
2. **Incomplete:** it returns a proper subset of the experimental set.
3. **Overcomplete:** it returns an infinite set, or a set with extra values.
4. **Normalization:** it returns the coefficient of a generator, not a spin.
5. **Extra structure:** it needs data beyond the algebra.
6. **Dubious:** it passes the test on $M_2(\mathbb{C})$, but its values on larger algebras are not spins.

**The six algebras.** The test cases are $\mathbb{C}$, the split-complex numbers $\mathbb{D}$, the quaternions $\mathbb{H}$, and the matrix algebras $M_2(\mathbb{C})$, $M_3(\mathbb{C})$, $M_5(\mathbb{C})$. The field is stated in every table.

**Conventions.** The field is $\mathbb{R}$ or $\mathbb{C}$ as stated. The indexing is $1$-based. Matrix notation is used only for the matrix algebras. No Clifford algebra is used. The biquaternion is $\mathbb{B}=\mathbb{H}\otimes_{\mathbb{R}}\mathbb{C}\cong M_2(\mathbb{C})$.

## 1. The Failure Table

**The audit.** The table applies every incomplete or dubious method to $M_2(\mathbb{C})$ and compares the result with $\{0,\tfrac12,1\}$.

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
| Casimir list, natural family | $\{0,\tfrac12,1\}$ | dubious | $\mathfrak{su}(2)$ formula |

**The reading.** The methods fall into four families: those that read one carrier (dimension, adjoint), those that read one chain (ladder, Peirce), those that read a coarse invariant (quiver, spectral, circle, ribbon), and those that read a representation label (highest weight, Casimir, coadjoint). The half-angle is a coordinate of the rotor; its coefficient is a normalization of the generator. The circle weight and the ribbon twist also need extra structure: a circle action or a ribbon category. §2 to §10 give each failing definition, its table on the six algebras, and the reason for its failure. §13 treats the one method that passes the test and is still rejected.

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
| Casimir, restricted | quadratic Casimir | representation theory of $\mathfrak{su}(2)$ |
| coadjoint | orbit area | geometric quantization of $SU(2)$ |
| circle weight | parity | $2\pi$ spin |
| ribbon twist | topological spin | ribbon categories |

**The common pattern.** Each method is the right tool for its own object. None of them is the spin list of the algebra.

## 12. Why They Were Mistaken for Definitions

**One carrier instead of three.** The dimension reads the defining module; the adjoint reads the adjoint module. Each gives one value, and the biquaternion needs three. The error is to take the value of one carrier for the list.

**One chain instead of the spectrum.** The ladder reads the Jordan chain of a nilpotent; the Peirce chain reads a chain of idempotents. Both are chains in $M_n$. The adjoint spin is a semisimple weight, not a chain. The error is to take the chain for the whole list.

**One coarse invariant instead of the spin.** The quiver is Morita invariant, the spectral count is a grading label, and the circle weight and the ribbon twist see only the parity. The error is to take an invariant that is constant on the interesting part.

**One representation instead of the algebra.** The highest weight, the Casimir, and the coadjoint orbit are labels of a chosen representation. Over all representations they are infinite; on the natural family they are finite. The restricted highest-weight and orbit lists are in the general article. The restricted Casimir list passes the test but is rejected in §13, because its formula is valid only for $\mathfrak{sl}_2$.

**One normalization instead of the spin.** The half-angle is the coordinate of the rotor; the coefficient in the exponent is the normalization of the generator on the fundamental carrier. The error is to take the coefficient for the eigenvalue.

**The test.** The $M_2(\mathbb{C})$ test separates the four pertinent definitions from these. A method that cannot produce $0$, $\tfrac12$, and $1$ on $M_2(\mathbb{C})$ is not a definition of the biquaternion's spin list. The test is necessary, not sufficient: the Casimir list passes it and is still rejected in §13.

## 13. Dubious Methods

**The category.** A method is **dubious** when it passes the $M_2(\mathbb{C})$ test and is still not a definition of the spin list. The test is necessary; it is not sufficient. Passing it can be an accident of the smallest case.

**The Casimir list.** Let $C$ be the quadratic Casimir of the semisimple part of $A$. For $W\in\mathcal{F}(A)$ let $C|_W=c_WI$. This is the Casimir of the full semisimple part, not the Casimir of a chosen $\mathfrak{sl}_2$; §9 already named that difference. The **Casimir list** is
$$
\Sigma_C(A)=\left\{\frac{-1+\sqrt{1+4c_W}}{2}:\ W\in\mathcal{F}(A)\right\}.
$$
Write $j(c)=(-1+\sqrt{1+4c})/2$ for one entry.

**It passes the test.** At $M_2(\mathbb{C})$ the centre, the defining module, and the adjoint have $c=0,\tfrac34,2$. The formula gives $0,\tfrac12,1$.

**The cases.** The table includes the extra cases of Part II, because the failure is clearest there; the six test algebras of this part are a subset.

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
| $M_4(\mathbb{C})$ | $\{0,0.958,1.562\}$ |
| $M_5(\mathbb{C})$ | $\{0,1.128,1.791\}$ |
| $M_6(\mathbb{C})$ | $\{0,1.280,2\}$ |
| $M_n(\mathbb{C})$ | $\{0,j(\tfrac{n^2-1}{2n}),j(n)\}$ |

**The failure on $M_n$.** The table gives the defining and the adjoint entries for $n=2,\ldots,6$.

| $n$ | $c$ on $\mathbb{C}^n$ | $j$ | $c$ on $\mathfrak{sl}_n$ | $j$ |
|---|---|---|---|---|
| $2$ | $\tfrac34$ | $\tfrac12$ | $2$ | $1$ |
| $3$ | $\tfrac43$ | $0.758$ | $3$ | $1.303$ |
| $4$ | $\tfrac{15}{8}$ | $0.958$ | $4$ | $1.562$ |
| $5$ | $\tfrac{12}{5}$ | $1.128$ | $5$ | $1.791$ |
| $6$ | $\tfrac{35}{12}$ | $1.280$ | $6$ | $2$ |

**Why the numbers are not spins.** A spin is a half-integer. For $n=3$ the defining entry is $0.758$ and the adjoint entry is $1.303$. Neither is a half-integer. The values are square roots of rationals, and they drift with $n$. At $n=6$ the adjoint entry is $2$, a half-integer, so this one entry looks like a spin. It is a coincidence of $6=2\cdot3$, and the adjoint spin there is $5$. A plausible value is not a certificate.

**Why the test passes.** At $n=2$ the two Casimirs coincide, because the semisimple part is $\mathfrak{sl}_2$ and the adjoint is its defining module. The normalization $c=j(j+1)$ is then the right one: $\tfrac34=\tfrac12\cdot\tfrac32$ and $2=1\cdot2$. For $\mathfrak{sl}_n$ the defining module has $c=(n^2-1)/(2n)$, which is not $j(j+1)$ for a half-integer $j$ when $n\ge3$. At $n=3$, $c=\tfrac43$; $j=\tfrac12$ would give $\tfrac34$, and $j=1$ would give $2$. The inversion formula returns the real number $0.758$, which is not a label.

**Why it is dangerous.** The test accepts it. A filter that only checks $M_2(\mathbb{C})$ keeps the Casimir list. The next case rejects it. This is why the test is necessary but not sufficient, and why the method needs a separate section instead of a place among the four.

**Verdict.** Dubious. It is a formula for the spin of an $\mathfrak{su}(2)$ representation, applied outside its domain. It is exact on $\mathbb{H}$ over $\mathbb{R}$, $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $\mathbb{H}_{\mathbb D}$, because there the semisimple part is $\mathfrak{sl}_2$ after complexification, or a sum of two copies. It is not a definition of the spin of $M_n$ for $n\ge3$.

## 14. Summary

**The failing methods fail the test.** On $M_2(\mathbb{C})$ they give a proper subset, a wrong value, an infinite set, or a coefficient. They are incomplete as definitions of the spin list. The Casimir list is the exception: it passes the test and is still rejected.

**They are not useless.** Each captures a part: the carrier size, the Jordan chain, the corner chain, the Morita class, the eigenvalue count, the spin-$1$ carrier, the rotor parameter, a representation label, or the parity. §11 records the right use of each.

**The four methods the programme called general definitions are in Part II.** The triple, the module list, the highest-weight list, and the orbit list with the cut pass the same test. They are rejected in §25 for the same reason: a weight, a dimension or an orbit label is not a spin.

**The dubious method.** The Casimir list restricted to the natural family gives $\{0,\tfrac12,1\}$ on $M_2(\mathbb{C})$, so the test does not reject it. It is rejected because on $M_3(\mathbb{C})$ it returns $0.758$ and $1.303$, which are not half-integers. It is in §13.

**The list.** The non-pertinent methods are: dimension over $\mathbb{C}$; dimension over $\mathbb{R}$; the ladder list; the regular spin; the Peirce chain; the quiver; the spectral count; the adjoint alone; the half-angle; the unrestricted highest weight; the unrestricted Casimir; the unrestricted coadjoint; the circle weight; the ribbon twist; and, as dubious, the restricted Casimir list.


## Part II — The Supposed General Definitions

**These are the four methods the programme accepted.** Each produces $\{0,\tfrac12,1\}$ on $M_2(\mathbb{C})$. Each is a correct computation of something. None is a definition of spin, for the reasons stated in §25. The section numbers continue from Part I.

## 15. The Test and the Cases

**The algebras.** The complex numbers are $\mathbb{C}=\mathbb{R}[i]/(i^2+1)$. The split-complex numbers are $\mathbb{D}=\mathbb{R}[j]/(j^2-1)\cong\mathbb{R}\times\mathbb{R}$. The dual numbers are $\mathbb{D}'=\mathbb{R}[\varepsilon]/(\varepsilon^2)$, with $\varepsilon$ nilpotent of index $2$. The reduced biquaternions are $\mathbb{B}_{\mathrm r}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{C}\cong\mathbb{C}\times\mathbb{C}$. The quaternions are $\mathbb{H}=\mathbb{R}\{1,e_x,e_y,e_z\}$ with $e_x^2=e_y^2=e_z^2=-1$ and $e_xe_y=e_z$, cyclically. The split quaternions are $\mathbb{H}_{\mathrm s}$, the real algebra with generators $e_1^2=-1$, $e_2^2=e_3^2=+1$, anticommuting, and $e_1e_2=e_3$. The split biquaternions are $\mathbb{H}_{\mathbb D}=\mathbb{D}\otimes_{\mathbb{R}}\mathbb{H}\cong\mathbb{H}\times\mathbb{H}$. The matrix algebras are $M_n=M_n(\mathbb{C})$.

**The basic invariants.** The table records the field, the dimension, the simple modules, the nilpotents, the idempotents, and whether a spin triple exists in the algebra itself. The rows $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{B}$, and $M_2(\mathbb{C})$ are the same algebra, $M_2(\mathbb{C})$; they are listed separately because Part VI names the three constructions separately. The split quaternions are listed as $\mathbb{H}_{\mathrm s}\cong M_2(\mathbb{R})$, and the split biquaternions as $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$.

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

**The commutative algebras.** $\mathbb{C}$ over $\mathbb{R}$ and over $\mathbb{C}$ is a field: every nonzero element is invertible, the only idempotents are $0$ and $1$, and every bracket vanishes. $\mathbb{D}$ is not a field: it has the idempotents $e_\pm=\tfrac12(1\pm j)$ and the zero divisors $1\pm j$. The dual numbers $\mathbb{D}'$ have the nilpotent $\varepsilon$ and the maximal ideal $(\varepsilon)$, and only the idempotents $0,1$. The nilpotent does not give a triple: every element of $\mathbb{D}'$ has the single eigenvalue $a$ (its scalar part), so no $S$ has the spectrum $j,j-1,\ldots,-j$ with $j>0$. The reduced biquaternions $\mathbb{B}_{\mathrm r}$ have the two central idempotents $\Pi_\pm=\tfrac12(1\pm j)$ and two non-isomorphic simple modules $\mathbb{C}_\pm$. All of them are commutative, so every bracket vanishes and every element is central; none has a spin triple.

**The quaternions.** $\mathbb{H}$ over $\mathbb{R}$ is a division algebra. Its only nilpotent is $0$ and its only idempotents are $0$ and $1$. It has no spin triple in itself: for every $S\in\mathbb{H}$ the eigenvalues of $\operatorname{ad}_S$ are $0$ and $\pm2i\lvert s\rvert$, where $s$ is the imaginary part, and the value $1$ never occurs, so $[S,U]=U$ has no nonzero real solution. The triple exists in the complexification $\mathbb{B}$. The split biquaternions $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$ are a product of two division algebras, so they have no nilpotent and no spin triple either; their complexification is $\mathbb{B}\times\mathbb{B}$.

**The matrix algebras.** $M_n$ has the principal triple
$$
S=\operatorname{diag}\left(\tfrac{n-1}{2},\tfrac{n-3}{2},\ldots,-\tfrac{n-1}{2}\right),\qquad
U=\sum_{i=1}^{n-1}E_{i,i+1},\qquad
V=\sum_{i=1}^{n-1}i(n-i)E_{i+1,i}.
$$
The defining module $\mathbb{C}^n$ has weights $\tfrac{n-1}{2},\ldots,-\tfrac{n-1}{2}$. The adjoint module has weights the differences of those numbers, from $-(n-1)$ to $n-1$.

**The biquaternion carriers.** At $M_2(\mathbb{C})$ the three carriers are the centre $\mathbb{C}I$, the defining module $\mathbb{C}^2$, and the traceless part $\mathfrak{sl}_2$. Their dimensions are $1,2,3$. The observed set $0,\tfrac12,1$ is the set of their spins. Every definition below reads this family in a different way.

## 16. The Natural Carrier Family

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

**The small size.** The family has at most six classes in the cases above. It has three classes for $\mathbb{D}$, $\mathbb{B}_{\mathrm r}$, $\mathbb{H}$ over $\mathbb{R}$ and over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $M_n$: one or two simple modules, and an adjoint that splits into the centre and the traceless part. It has two classes for $\mathbb{C}$ over $\mathbb{R}$. It has one class for $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, and $\mathbb{D}'$, whose regular module has a unique simple constituent. It has six classes for $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$, because each factor contributes a simple module, a centre line, and a traceless part. A non-semisimple algebra, or a product with more simple modules, has a larger family; $\mathbb{H}_{\mathbb D}$ is the only such case here.

**At $M_2(\mathbb{C})$.** The family is the centre $\mathbb{C}I$, the defining module $\mathbb{C}^2$, and the traceless part $\mathfrak{sl}_2$. These are exactly the three carriers of the biquaternion.

## 17. The Triple

**Two gradings.** The section records two gradings. The idempotent grading $S_{\mathrm{id}}$ gives the flat list $\{0,\tfrac12,1\}$ for every $n\ge2$. The chain grading $S$ of a nilpotent gives the triple list, and it grows with the length of the chain. The two are different elements; they agree on the idempotent's own two-level chain.

**The idempotent grading.** Let $e$ be an idempotent with $e\ne0$ and $e\ne1_A$, and put $f=1_A-e$. Define
$$
S_{\mathrm{id}}=e-\tfrac12 1_A=\tfrac12(e-f).
$$
This is the whole definition of the idempotent element: one idempotent and one subtraction. No nilpotent is chosen, and no formula is postulated.

**The weights of $S_{\mathrm{id}}$.** Since $e^2=e$,
$$
S_{\mathrm{id}}^2=e^2-e+\tfrac14 1_A=\tfrac14 1_A,
$$
so $S_{\mathrm{id}}$ is semisimple with spectrum contained in $\{\pm\tfrac12\}$; the spectrum is exactly $\{\pm\tfrac12\}$ because $e\ne0,1_A$. On the Peirce corners $A_{st}=e_sAe_t$,
$$
\operatorname{ad}_{S_{\mathrm{id}}} x=\tfrac12(s-t)x,\qquad s,t\in\{+1,-1\}.
$$
So $L_{S_{\mathrm{id}}}$ has weights $\pm\tfrac12$ on $Ae$, and $\operatorname{ad}_{S_{\mathrm{id}}}$ has weights $0,\pm1$ on the adjoint. The three carrier spins are obtained in one line.

| carrier | operator | weights | spin |
|---|---|---|---|
| diagonal part $A_{++}\oplus A_{--}$ | $\operatorname{ad}_{S_{\mathrm{id}}}$ | $0$ | $0$ |
| Peirce carrier $Ae$ | $L_{S_{\mathrm{id}}}$ | $\pm\tfrac12$ | $\tfrac12$ |
| off-diagonal part $A_{+-}\oplus A_{-+}$ | $\operatorname{ad}_{S_{\mathrm{id}}}$ | $\pm1$ | $1$ |

No value comes from nowhere. The value $\tfrac12$ is an eigenvalue of $S_{\mathrm{id}}$; the value $1$ is the difference of two such eigenvalues; the value $0$ is the diagonal.

**The idempotent list.** It is $\{0,\tfrac12,1\}$ exactly when $A$ has a non-central idempotent, and it is independent of the choice of $e$. It is $\{0,\tfrac12\}$ when every nontrivial idempotent is central, and $\{0\}$ when there is none. The centre contributes $0$ always. The Peirce carrier $Ae$ contributes $\tfrac12$ for every nontrivial $e$; its lower level $-\tfrac12$ is present exactly when $fAe\ne0$. The adjoint contributes $1$ exactly when a mixed corner is nonzero, and its string is full exactly when both mixed corners are nonzero.

| algebra | idempotent | $S_{\mathrm{id}}$ | list |
|---|---|---|---|
| $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{R}$, $\mathbb{H}$ over $\mathbb{R}$, $\mathbb{D}'$ | none | $0$ | $\{0\}$ |
| $\mathbb{D}$ | $e_+$ | $j/2$ | $\{0,\tfrac12\}$ |
| $\mathbb{B}_{\mathrm r}$ | $\Pi_+$ | $\tfrac12(\Pi_+-\Pi_-)$ | $\{0,\tfrac12\}$ |
| $\mathbb{H}_{\mathbb D}$ | $(1,0)$ | $\tfrac12(1,-1)$ | $\{0,\tfrac12\}$ |
| $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, $M_n$, $T_2$ | $E_{11}$ | $\operatorname{diag}(\tfrac12,-\tfrac12,\dots)$ | $\{0,\tfrac12,1\}$ |

In $T_2$ only $A_{+-}$ is nonzero, so the value $1$ is a top without the full string $1,0,-1$; the triple list of $T_2$ is $\{0\}$. The idempotent list records tops; the triple below certifies fullness.

**Computed weights for $M_n$.** With $e=E_{11}$, $L_{S_{\mathrm{id}}}$ gives $-\tfrac12$ and $+\tfrac12$; $\operatorname{ad}_{S_{\mathrm{id}}}$ gives $-1$, $0$ and $1$, for every $n$. The list does not grow with $n$.

**The companion count.** Every $\nu\in fAe$ is square-zero and satisfies $[S_{\mathrm{id}},\nu]=-\nu$. The corner $fAe$ is the lowering space. Its companion count is the least number of generators over $D=eAe$, and for $M_N$ with an idempotent of rank $r$ it is
$$
s=\left\lceil\frac{N-r}{r}\right\rceil=\left\lceil\frac Nr\right\rceil-1;
$$
for a primitive idempotent, $s=N-1$. The corner has $r(N-r)$ parameters, so the count is not the dimension; the multiplicity of the weight $-\tfrac12$ on the carrier is $r(N-r)$. The count measures the elaboration of the nilpotent part; it does not raise the spin.

**Two elements named $S$.** The idempotent element $S_{\mathrm{id}}$ and the chain grading $S$ of the triple are different in general. They coincide on the idempotent's own two-level chain, where $S=\tfrac12(e-f)$; in general they are different elements. The idempotent list is the list of $S_{\mathrm{id}}$; the triple list is the list of all chain gradings. For $n\ge3$ the principal pair uses a longer chain and a different $S$.

**The relations are consequences.** The triple is the method whose list grows with $n$ through longer chains, and every value in it is realised by a chain in $A$. Its relations are therefore derived, not postulated. The input is a nilpotent $U$; $S$ is the grading of its chain; $V$ is forced. Nothing else is assumed.

**The input.** Let $U\in A$ be a nonzero nilpotent and let $x_0,\dots,x_{\ell-1}$ be a Jordan chain written from the top down,
$$
Ux_0=0,\qquad Ux_k=x_{k-1}\quad(k=1,\dots,\ell-1),
$$
so $x_0$ is the top and $x_{\ell-1}$ is the bottom. A nilpotent is intrinsic data: it exists in $M_n$, in $\mathbb{B}$ and in $\mathbb{D}'$, and it does not exist in the division algebras $\mathbb{H}$ and $\mathbb{C}$. The chain is the sequence of states that $U$ steps through.

**The grading $S$.** The chain is finite, so it has a top and a bottom. Label the levels as a spin: the top is $j$, the bottom is $-j$, and consecutive levels differ by one. With $\ell$ levels this forces $j=(\ell-1)/2$ and
$$
Sx_k=(j-k)x_k.
$$
The labels are the only symmetric unit-step labelling of a finite chain. The spectrum $j,j-1,\dots,-j$ is the level number, not an assumption.

**The partner $V$.** The operator $U$ steps one level up, toward $x_0$. A carrier also needs the step down, so let
$$
Vx_k=c_kx_{k+1}\quad(k=0,\dots,\ell-2),\qquad Vx_{\ell-1}=0.
$$
Then
$$
[U,V]x_k=(c_k-c_{k-1})x_k,\qquad c_{-1}=0.
$$
The requirement $[U,V]=2S$ gives $c_k-c_{k-1}=2(j-k)$. With $c_{-1}=0$ the sum is
$$
c_k=(k+1)(\ell-1-k).
$$
So $V$ is not extra data: it is the unique operator that closes with $S$.

**Existence.** The formula gives the only possible $V$; it gives an element of $A$ exactly when the shift is realised by multiplication in $A$. In $M_n$ and in $\mathbb{B}$ it is. In a commutative algebra it is not: $[U,V]=0$ for all $U,V$, so $S=0$ and there is no nonzero triple. This is why $\mathbb{D}'$ has a nilpotent and no triple.

**The three relations.** With these definitions,
$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S
$$
hold, one line each. The first says $U$ raises the level by one, the second says $V$ lowers it by one, the third is the definition $S=\tfrac12[U,V]$. Equivalently, the input is the pair $(U,V)$ constructed above, with $S=\tfrac12[U,V]$; the chain of $U$ supplies the levels.

**Why the factor $2$.** The step of $S$ is one unit, so the step of $2S$ is two. The element $H=2S$ is the coroot normalisation of the frame-root articles. The spin is read from $S$, never from $H$.

**Closure.** The relations are the Chevalley relations of $\mathfrak{sl}_2$ with $H=2S$:
$$
[H,U]=2U,\qquad [H,V]=-2V,\qquad [U,V]=H.
$$
Jacobi holds on the span, so for a nonzero nilpotent whose shift is an element of $A$, the span is a copy of $\mathfrak{sl}_2$ in $A$. A triple is a copy of $\mathfrak{sl}_2$ with a chosen Cartan element, and the method asks whether the algebra has rank one.

**The biquaternion.** In $\mathbb{B}$ the two Peirce nilpotents $\vec\Upsilon_-\in\mathbb{B}_{+-}$ and $\vec\Upsilon_+\in\mathbb{B}_{-+}$ satisfy
$$
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad \vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,
$$
so
$$
[\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Pi_+-\tilde\Pi_-=2S.
$$
The triple is the frame. This is why the biquaternion passes without extra structure. In general, if $u\in eAf$ and $v\in fAe$ satisfy $uv=e$ and $vu=f$, the same computation gives $[u,v]=2S$; the biquaternion is the case where the companion corner is one-dimensional.

**Why the list grows.** In $M_n$ a nilpotent has index at most $n$, so $\ell$ runs from $2$ to $n$ and the spins run over
$$
0,\ \tfrac12,\ \dots,\ \frac{n-1}{2};
$$
the adjoint adds the integers $0,1,\dots,n-1$. The growth is the growth of possible chain lengths.

**Definition (spin triple).** A **spin triple** in $A$ is a triple $(S,U,V)$ satisfying the three relations. By the derivation above, such a triple is the same data as a nonzero nilpotent with a Jordan chain for which the shift is an element of $A$; the levels are then forced. The **triple list** is the set over all triples in $A$, with the spin of a carrier read as the top eigenvalue of $S$ on it.

**The flat idempotent list and the growing triple list.** The idempotent list is $\{0,\tfrac12,1\}$ for every $M_n$, $n\ge2$, and it should not be read as the triple list. The idempotent's companions are square-zero, so the companion chain on the column has length two and top $\tfrac12$; the adjoint string has length three and top $1$. Neither grows with $n$. The triple list quantifies over all triples, including nilpotents of index $\ell>2$, and it is the list that grows with $n$. The two lists agree only where the longest chain has length two, which is the $M_2$ case. The Peirce chain of *The Incomplete Definitions of the Spin of an Algebra* is a third object: it reads only the corners $e_iAe_{i+1}$ and gives $\{0,\tfrac12\}$ on $M_2(\mathbb{C})$, missing the adjoint value.

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

**What the definition does.** The triple gives the closure of the ladder and the growing list. The idempotent element $S_{\mathrm{id}}$ gives the flat list $\{0,\tfrac12,1\}$ without any nilpotent; it is the grading of the Peirce corners, not the grading of a chain. On $M_n$ the triple gives the principal list $\{0,(n-1)/2,n-1\}$ and the adjoint content of the row. It is the definition used in the principal-pair articles and in the biquaternion articles. The triple list is not intrinsic to $\mathbb{R}$, $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, $\mathbb{B}_{\mathrm r}$, $\mathbb{H}$, or $\mathbb{H}_{\mathbb D}$: those algebras have no nonzero triple, so it collapses to $\{0\}$ (or to the list of the complexification). The idempotent list is finer there: it is $\{0,\tfrac12\}$ on $\mathbb{D}$, $\mathbb{B}_{\mathrm r}$ and $\mathbb{H}_{\mathbb D}$, because those algebras have a nontrivial central idempotent but no nonzero mixed corner.

**Verdict.** Rejected. It is a correct description of the principal $\mathfrak{sl}_2$ of $M_n$, and it is not a definition of spin. On $M_2(\mathbb{C})$ it gives $\{0,\tfrac12,1\}$ because the three natural carriers have those weights; that coincidence is what the programme mistook for a definition.

## 18. The Module List

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

**Verdict.** Rejected. It reads a dimension converted by $(\dim-1)/2$. A dimension is not a weight.

## 19. The Highest-Weight List

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

**Verdict.** Rejected. It is the highest weight of a chosen principal $\mathfrak{sl}_2$, that is, a representation label. It needs a choice of triple and it names no physical carrier.

## 20. The Orbit List

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

**The rows without a semisimple part.** $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, and $\mathbb{B}_{\mathrm r}$ have no semisimple part, so they have no $\mathfrak{sl}_2$ orbits; their list is $\{0\}$ even when the cut would allow more. The same remark applies to the highest-weight list.

**What it gives.** It is exact at $M_2(\mathbb{C})$ because $\dim\mathfrak{sl}_2=3$ gives the cut $j\le1$. For $M_n$ with $n\ge3$ the list uses the principal $\mathfrak{sl}_2$; the cut is the adjoint dimension. It is overcomplete for $n\ge3$: the adjoint of $\mathfrak{sl}_3$ has dimension $8$, and the cut admits spins up to $\tfrac72$; at $M_6$ the cut admits spins up to $17$. The cut is not intrinsic to the orbit; it uses the module dimensions.

**Verdict.** Rejected. It is an orbit label with a dimension cut. The cut is extra data, and the list is overcomplete above $n=2$.

## 21. The Four Agree on $M_2(\mathbb{C})$

**The table.** The four definitions and the carrier each reads.

| definition | what it reads | result on $M_2(\mathbb{C})$ |
|---|---|---|
| triple | the brackets on all carriers | $\{0,\tfrac12,1\}$ |
| module list | dimensions of the natural family | $\{0,\tfrac12,1\}$ |
| highest-weight list | top weights on the natural family | $\{0,\tfrac12,1\}$ |
| orbit list | orbits with $2j+1\le3$ | $\{0,\tfrac12,1\}$ |

**The three values are the three carriers.** The centre gives $0$; the defining module gives $\tfrac12$; the traceless part of the adjoint gives $1$. The four definitions read the same three carriers.

**They are not restatements.** The triple reads the brackets. The module list reads the dimensions. The highest-weight list reads the top weight. The orbit list reads the coadjoint orbit. The formulas are different and the data are different. They agree at $M_2(\mathbb{C})$ because the natural family is exactly the three carriers.

## 22. The Four Diverge Above $M_2(\mathbb{C})$

**The table.**

| definition | $M_3(\mathbb{C})$ | $M_4(\mathbb{C})$ | $M_5(\mathbb{C})$ | $M_6(\mathbb{C})$ |
|---|---|---|---|---|
| triple, all | $\{0,\tfrac12,1,2\}$ | $\{0,\tfrac12,1,\tfrac32,2,3\}$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,4,5\}$ |
| triple, principal | $\{0,1,2\}$ | $\{0,\tfrac32,3\}$ | $\{0,2,4\}$ | $\{0,\tfrac52,5\}$ |
| module list | $\{0,1,\tfrac72\}$ | $\{0,\tfrac32,7\}$ | $\{0,2,\tfrac{23}{2}\}$ | $\{0,\tfrac52,17\}$ |
| highest-weight list | $\{0,1,2\}$ | $\{0,\tfrac32,3\}$ | $\{0,2,4\}$ | $\{0,\tfrac52,5\}$ |
| orbit list | $\{0,\ldots,\tfrac72\}$ | $\{0,\ldots,7\}$ | $\{0,\ldots,\tfrac{23}{2}\}$ | $\{0,\ldots,17\}$ |

**Which generalize.** The all-triple list and the highest-weight list give half-integer values on $M_n$. The module list gives the adjoint-dimension value, which is $\tfrac72$ or $\tfrac{23}{2}$, not the adjoint spin. The orbit list is overcomplete. Only the triple and the highest-weight list generalize as computations of the principal weights; neither is a definition of spin, and the other two are exact only at $n=2$.

**The programme's reading.** For the biquaternion the four agree. For $M_n$ above $n=2$ the programme took the triple's list as the physical list. That is the error. The physical list is fixed by the field equation and by the little group, not by the principal triple. The module list and the orbit list are approximations to the defining and adjoint data; they are not general definitions either. The four agree at $M_2(\mathbb{C})$ because the natural family there is exactly the centre, the defining module and the traceless part. The agreement is a property of the smallest case.

## 23. Checks

**The triple.** With $S=\operatorname{diag}(\tfrac12,-\tfrac12)$, $U=E_{12}$, $V=E_{21}$,
$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S.
$$
The defining module has weights $\pm\tfrac12$; the adjoint has weights $0,\pm1$; the centre has weight $0$.

**The left multiplication.** $L_S$ on $M_2(\mathbb{C})$ has eigenvalues $\pm\tfrac12$, each of multiplicity $2$. These are the weights of the defining module; its top weight is $\tfrac12$.

**The adjoint.** $\operatorname{ad}_S$ has eigenvalues $0$ of multiplicity $2$ and $\pm1$. These are the adjoint weights $0,\pm1$; the adjoint spin is $1$.

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
| $M_2$ orbit cut | $2j+1\le3$ | $j\le1$ |
| $\mathbb{H}$ adjoint | $0$ (multiplicity $2$), $\pm2i$ | normalized $0,\pm1$ |

## 24. The Four Methods in All Cases

**The table.** One row per case, one column per method. The base field is the one stated in §15.

| algebra | triple | module | highest weight | orbit |
|---|---|---|---|---|
| $\mathbb{R}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{R}$ | $\{0\}$ | $\{0,\tfrac12\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{C}$ over $\mathbb{C}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{D}'$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{B}_{\mathrm r}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ | $\{0\}$ |
| $\mathbb{H}$ over $\mathbb{R}$ | $\{0\}$ | $\{0,1,\tfrac32\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}$ over $\mathbb{C}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathrm s}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{B}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $\mathbb{H}_{\mathbb D}$ | $\{0\}$ | $\{0,1,\tfrac32\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_2(\mathbb{C})$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ | $\{0,\tfrac12,1\}$ |
| $M_3(\mathbb{C})$ | $\{0,\tfrac12,1,2\}$ | $\{0,1,\tfrac72\}$ | $\{0,1,2\}$ | $\{0,\tfrac12,\ldots,\tfrac72\}$ |
| $M_4(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,3\}$ | $\{0,\tfrac32,7\}$ | $\{0,\tfrac32,3\}$ | $\{0,\tfrac12,\ldots,7\}$ |
| $M_5(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,3,4\}$ | $\{0,2,\tfrac{23}{2}\}$ | $\{0,2,4\}$ | $\{0,\tfrac12,\ldots,\tfrac{23}{2}\}$ |
| $M_6(\mathbb{C})$ | $\{0,\tfrac12,1,\tfrac32,2,\tfrac52,3,4,5\}$ | $\{0,\tfrac52,17\}$ | $\{0,\tfrac52,5\}$ | $\{0,\tfrac12,\ldots,17\}$ |
| $M_n(\mathbb{C})$ | $\{0,\tfrac12,\ldots,\tfrac{n-1}{2}\}\cup\{0,1,\ldots,n-1\}$ | $\{0,\tfrac{n-1}{2},\tfrac{n^2-2}{2}\}$ | $\{0,\tfrac{n-1}{2},n-1\}$ | $\{0,\tfrac12,\ldots,\tfrac{n^2-2}{2}\}$ |

**The agreements.** On $\mathbb{R}$, $\mathbb{C}$ over $\mathbb{C}$, $\mathbb{D}$, $\mathbb{D}'$, and $\mathbb{B}_{\mathrm r}$ all four give $\{0\}$. On $\mathbb{H}$ over $\mathbb{C}$, $\mathbb{H}_{\mathrm s}$, $\mathbb{B}$, and $M_2(\mathbb{C})$ all four give $\{0,\tfrac12,1\}$; this is the biquaternion list. $\mathbb{C}$ over $\mathbb{R}$ is the one commutative case where the module list separates: it gives $\{0,\tfrac12\}$ from the real dimension of $\mathbb{C}$, while the other three give $\{0\}$.

**The scope.** The rows are the finite-dimensional algebras over $\mathbb{R}$ or $\mathbb{C}$ that the corpus treats as categories. The categories *Complexoid*, *Split-Complexoid*, *Quaternioid*, and *Biquaternion Algebraic Structures* are not separate algebras: they carry extra products, forms, and subspaces on $\mathbb{C}$, $\mathbb{D}$, $\mathbb{H}$, and $\mathbb{B}$, which are already rows. *Structural Comparison around Biquaternions* compares the rows and adds no algebra. The Booleans, $\mathbb{N}$, and $\mathbb{Z}$ are not finite-dimensional algebras over a field, and $\mathbb{Q}$ is excluded by the convention that the base field is $\mathbb{R}$ or $\mathbb{C}$; the four definitions do not apply to them.

**Two real forms do not agree.** On $\mathbb{H}$ over $\mathbb{R}$ and on $\mathbb{H}_{\mathbb D}\cong\mathbb{H}\times\mathbb{H}$ the triple gives only $\{0\}$, because neither algebra has a nonzero nilpotent. The module list gives $\{0,1,\tfrac32\}$, because the simple module has real dimension $4$. The highest-weight and orbit lists give $\{0,\tfrac12,1\}$, because each semisimple factor is $\mathfrak{su}(2)$ and the carrier is its fundamental representation. A spin-$\tfrac12$ carrier can exist without a triple.

**The reduced biquaternion.** The row uses the complex base field of the corpus. Over $\mathbb{R}$ the two simple modules have real dimension $2$ and the module list becomes $\{0,\tfrac12\}$; the other three lists remain $\{0\}$, because the algebra is commutative and has no nilpotent. The reduced biquaternion has central idempotents but no nilpotent, so it has no triple and no spin-$\tfrac12$ value in either reading.

**Above $M_2(\mathbb{C})$ the four diverge.** At $M_3$ the module list reads the adjoint dimension $8$, the highest-weight list returns $1$ and $2$, and the orbit list returns every half-integer up to $\tfrac72$. The divergence grows with $n$: at $M_6$ the module list returns $17$, the highest-weight list returns $\tfrac52$ and $5$, and the orbit list returns every half-integer up to $17$. The triple list is finite in each case, with values up to $n-1$.

**Two different obstructions.** $\mathbb{D}'$ has a nonzero nilpotent but no semisimple element with distinct eigenvalues; $\mathbb{H}$ over $\mathbb{R}$ has a spin-$\tfrac12$ carrier but no nilpotent. Neither has a triple. A triple needs both a nilpotent and a semisimple grading element, and neither condition alone suffices.

**The Casimir is not in the table.** It passes the $M_2(\mathbb{C})$ test, but on $M_3(\mathbb{C})$ it returns $0.758$ and $1.303$. These are not half-integers, so they are not spins. The formula $j=(-1+\sqrt{1+4c})/2$ is an $\mathfrak{su}(2)$ formula; it is meaningful only when the semisimple part is $\mathfrak{sl}_2$. The Casimir is therefore a representation label, not a definition of the algebra's spin list. It is in §13.

**What the table selects.** The $M_2(\mathbb{C})$ test is passed by all four because the natural family there is exactly the centre, the defining module, and the traceless part, of dimensions $1,2,3$. The test does not separate them, and it does not reject the Casimir either. The test is invalid as a test of spin: it selects by the answer. The divergence on $M_n$ for $n\ge3$ shows only that the four computations are different.


## 25. The Verdict

**All of it is rejected as a definition of spin.** The methods of Part I fail the programme's own test. The four methods of Part II pass it. Both verdicts are irrelevant, because the test is not a test of spin. This section states why, and then states what survives.

### The Eight Errors

**1. A weight is not a spin.** A weight is an eigenvalue of a chosen element on a chosen carrier. A spin is a label of the rotation group in the rest frame. The two coincide only when the element is the rotation generator $S_z$, the carrier is the rest-frame one-particle space, and the eigenvalue is measured in units of $\hbar$. The programme fixed the element by a triple, fixed the carrier by a module of the algebra, and never checked either condition. The number it computed is a highest weight. Calling it a spin is an interpretation, and the interpretation needs the physics that the programme left out.

**2. An algebra has no spin.** Spin is a property of a particle, not of an algebra. An algebra can carry a representation of the rotation group. That representation can be the rotation representation of a particle. The algebra alone does not know which representation it is carrying, whether the carrier is a rest frame, or whether the particle exists. The phrase "the spin of the algebra" is a category error. The phrase "the spin of a carrier" is shorthand for the physical conditions above and is not a definition either.

**3. The test is rigged.** The $M_2(\mathbb{C})$ test fixes the answer in advance. Every natural construction on $M_2(\mathbb{C})$ reads the same three spaces: the centre, the defining module and the traceless part. Any formula fitted to their dimensions, their weights or their orbit areas returns $\{0,\tfrac12,1\}$. The test therefore accepts the triple, the module list, the highest-weight list and the orbit list, and it accepts the Casimir list too. It rejects a method only when the method happens to read a different object. A test that accepts everything natural and rejects only the unnatural is not a test of spin.

**4. The physics is absent.** The programme uses no $\hbar$, no rest frame, no Poincaré group, no little group, no mass, no helicity and no spin–statistics. It cannot distinguish the rotation group from an internal $SU(2)$, the spin from isospin, or the rest-frame spin from a flavour quantum number. The observed values $0,\tfrac12,1$ enter only as the target of the fit. That is why the fit succeeds on $M_2(\mathbb{C})$ and fails everywhere else.

**5. The carriers were confused with the particles.** The centre, the Peirce plane and the traceless part are three carriers of $\mathbb{B}$. They are not three particles. The centre carries the trivial representation; the Peirce plane carries the defining representation of $M_2(\mathbb{C})$, which is the spin-$\tfrac12$ representation of the rotation subgroup; the traceless part carries the adjoint representation of the rotation subgroup, which is spin $1$. Those are correct statements about the rotation action. They do not say that the Higgs is the centre, the electron is a Peirce plane, or the photon is $\mathfrak{sl}_2$. The physical identification is an interpretation supplied by the Standard Model, and it is not derived.

**6. The half-angle was confused with the weight.** The rotor is $\exp(\tfrac{\theta}{2}\vec u)$ for every spin. On a carrier of spin $j$ the rotation operator is $\exp(-i\theta\,\hat n\cdot\vec J/\hbar)$, whose eigenvalues are $e^{-im_s\theta}$, with $m_s=-j,\dots,j$. The exponent coefficient is $m_s$, not $\theta/2$. The $\theta/2$ is the coordinate of the defining spinor, where $m_s=\pm\tfrac12$. It is a coordinate of the rotor, not the spin, and it equals the spin only at $j=\tfrac12$, and then only numerically.

**7. The adjoint was confused with the spin.** The adjoint of $\mathfrak{so}(3)$ on $\mathbb{R}^3$ is the spin-$1$ representation. The adjoint of $\mathfrak{so}(3,1)$ on $\mathbb{R}^4$ is the six-dimensional antisymmetric tensor, not the four-vector. The adjoint of $\mathbb{B}$ is a carrier of the rotation subgroup; its spatial part is the triplet. The triplet carries spin $1$; it is not the definition of spin $1$, and the higher integer carriers are symmetric traceless tensors, not the adjoint of $M_n$ for $n>2$.

**8. The Bhabha label was confused with the spin.** The Bhabha–Gel'fand–Yaglom label $s=\lvert l-\bar l\rvert$ is the lowest spin in the Lorentz string carried by $\tau^{l\bar l}$. It is not the physical spin. The vector $\tau^{\frac12,\frac12}$ has $s=0$ by this label and contains the spin-$1$ Proca field; the physical spin is fixed by the field equation and its constraints. The label is a representation datum, and the corpus's own maths article says so.

### The Four "General Definitions", One by One

| method | what it computes | why it is not spin |
|---|---|---|
| triple | the brackets of a chosen $\mathfrak{sl}_2$ | any $\mathfrak{sl}_2$ qualifies, including isospin and flavour; no rotation group, no rest frame |
| module list | dimensions of the natural modules, converted by $(\dim-1)/2$ | a dimension is not a weight; the formula gives the defining spin only on the defining module |
| highest-weight list | top weights of a chosen principal $\mathfrak{sl}_2$ | a representation label of a chosen triple; no physics selects the triple or the carrier |
| orbit list | coadjoint orbit areas with a dimension cut | an orbit label with extra data; overcomplete above $M_2$ |

**The triple.** A spin triple is a copy of $\mathfrak{sl}_2$ with a normalisation. The relations $[S,U]=U$, $[S,V]=-V$ and $[U,V]=2S$ define the triple, not the spin. A two-level atom, an isospin doublet and a beam splitter all carry such a triple. The triple becomes the rotation triple only when $S$ is identified with $S_z/\hbar$ and the carrier with the rest-frame space. That identification is physical.

**The module list.** The formula $j=(\dim V-1)/2$ reads the size of a module. It gives the correct defining spin of $M_n$ on $\mathbb{C}^n$ and the wrong value on the adjoint. It cannot see a weight.

**The highest-weight list.** This is the closest of the four, and it is still not a definition. It needs a choice of Cartan, a positive system and a principal $\mathfrak{sl}_2$. Different choices give different lists. The highest weight is a representation label; the spin is the little-group label of the physical state.

**The orbit list.** The orbit method gives the spin of a representation of $SU(2)$ after a choice of normalisation. The cut $2j+1\le\dim W$ is extra data. It is a geometric realisation of a representation label, not a property of the algebra.

### The Casimir

The Casimir list is the one method that passes the $M_2(\mathbb{C})$ test and still fails. At $M_3(\mathbb{C})$ it returns $0.758$ and $1.303$, which are not half-integers. The formula $j=(-1+\sqrt{1+4c})/2$ is the $\mathfrak{su}(2)$ formula $c=j(j+1)$ inverted. It is valid only when the semisimple part is $\mathfrak{sl}_2$ and the module is an $\mathfrak{sl}_2$ module. For $\mathfrak{sl}_n$ with $n\ge3$ the Casimir of the defining module is $(n^2-1)/(2n)$, not $j(j+1)$ for a half-integer $j$. The list is a formula applied outside its domain.

### What Survives

The purge removes the doctrine, not the algebra. Five statements survive as correct mathematics, with their status stated.

**1. The rotation triple of $\mathbb{B}$.** The elements

$$
S_k=\tfrac{i}{2}\vec e_k,\qquad [S_i,S_j]=i\epsilon_{ijk}S_k,
$$

are the rotation generators in the Hermitian subspace. On the Peirce plane $S_+=\mathbb{B}\tilde\Pi_+$ the left action $L_{S_z}$ has weights $\pm\tfrac12$. On the traceless part $V=\ker\operatorname{tr}$ the adjoint action $\operatorname{ad}_{S_z}$ has weights $+1,0,-1$. These are the spin-$\tfrac12$ and spin-$1$ representations of the rotation group. This is a statement about the rotation action, not a definition of spin.

**2. The centre is the trivial carrier.** $\mathbb{C}_{\mathbb{B}}$ carries the trivial representation of the rotation group. It is the carrier of a scalar field. It is not "spin $0$" by definition; it is the space on which the rotation acts trivially.

**3. The tensor construction.** The pure spin-$j$ carrier is the symmetric part of the $2j$-fold tensor power of the defining module,

$$
\mathrm{Sym}^{2j}(S),\qquad \dim_{\mathbb{C}}=2j+1,
$$

inside $\mathbb{B}^{\otimes 2j}\cong M_{2^{2j}}(\mathbb{C})$. The constraints of the field equation select the pure spin from the product. This is the correct route to higher spin, and it is not a property of $\mathbb{B}$ alone.

**4. The half-angle.** The rotor $\exp(\tfrac{\theta}{2}\vec u)$ acts on the defining spinor with exponent $\pm i\theta/2$ and on the vector with exponent $\pm i\theta$. The half-angle is the coordinate of the defining representation. It is not the spin.

**5. The Peirce index.** The right action of the root gives $R_{\tilde\Xi}=+1$ on $S_+$ and $-1$ on $S_-$. That sign labels two isomorphic copies of one left module. It is not a spin and not a chirality. Chirality is the central sign $\chi=ij$, which grades $S$ against $S^{\mathrm{c}}$.

### The Rule

**No formula in this file defines spin.** The file is kept as a record of a failed programme, not as a reference. A future article that wants to use a weight, a dimension, a Peirce index or a Casimir must say what physical representation it is reading and why the carrier is the rest-frame one. If it cannot, it is doing representation theory, and it should say so.

**The one-line verdict.** The programme computed the weights of $\mathfrak{sl}_2$ actions on the modules of $M_2(\mathbb{C})$, found $\{0,\tfrac12,1\}$, and mistook the coincidence for a definition of spin.

## Further Reading

- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the three carriers of $\mathbb{B}$ and their rotation content, stated as carriers and not as a definition.
- [The Spin–Statistics Theorem in Biquaternionic Form](../articles_physics/the-spin-statistics-theorem-in-biquaternionic-form.html), for the rotation double cover and the statistics pairing.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the adjoint action as the spin-$1$ carrier of the rotation subgroup.
- [The Spinor Module in Biquaternionic Form and Its Lorentz Action](../articles_physics/the-spinor-module-in-biquaternionic-form-and-its-lorentz-action.html), for the defining module and its Lorentz action.
- [The Spinor Representation of the Lorentz Group in Biquaternionic Form](../articles_physics/the-spinor-representation-of-the-lorentz-group-in-biquaternionic-form.html), for the $(j_L,j_R)$ labels and the rotation content.
- [The Spinor-Helicity Formalism and Biquaternions](../articles_physics/the-spinor-helicity-formalism-and-biquaternions.html), for helicity as the massless little-group label.
- [Higher Spin from Tensor Products](../articles_physics/higher-spin-from-tensor-products-why-the-biquaternion-algebra-admits-only-spin-0-and-one-half.html), for the tensor construction of the higher carriers.
- [Chirality: The Conjugate Pair](../articles_maths/chirality-the-conjugate-pair.html), for the central sign $\chi=ij$ and the separation from the Peirce index.
- [The Spin of a Biquaternion](../articles_maths/the-spin-of-a-biquaternion.html), for the rotation triple and the weights, now stated as a computation.
- [The Peirce Decomposition of the Biquaternion Algebra](../articles_maths/the-peirce-decomposition-of-the-biquaternion-algebra.html), for the idempotents and the corners.
