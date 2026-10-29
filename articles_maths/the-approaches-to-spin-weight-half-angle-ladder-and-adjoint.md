# __The Approaches to Spin: Weight, Half-Angle, Ladder and Adjoint__

## Introduction

**The corpus reads spin in four ways, and the four readings meet in one formula.** The weight of a frame root; the half-angle of a polar rotor; the length of a Peirce ladder; the adjoint action on the material sector. The first, third and fourth produce a spin; the second produces the coordinate of the weight. They meet in the invariant below.

**The invariant.** Let $A$ be a finite-dimensional algebra over a field of characteristic zero, $h$ a grading element (a frame root, a Cartan element), and $W$ a carrier on which $h$ acts. The weights are the eigenvalues of $\rho(h)$; the spin is half the highest weight:

$$
j(W)=\frac{\lambda_{\max}\bigl(\rho(h|_W)\bigr)}{2}.
$$

The factor $\tfrac12$ converts the root's weights, which are twice the spin weights, to the spin. Equivalently, with $S=\tfrac12 h$, the spin is the highest weight of $S$.

**The four readings.**

- **Weight.** $j=\lambda_{\max}/2$. The frame root $h=2e-1$ of the biquaternion has weights $\pm1$ on the spinor and $0,\pm2$ on the traceless part, giving $j=\tfrac12$ and $j=1$.
- **Half-angle.** The rotor is $\exp(\theta h/2)$. The exponent is $\theta/2$; the phase on a weight-$m$ vector is $e^{i\theta m}$. The half-angle is the coordinate, not the spin.
- **Ladder.** A chain of length $\ell$ carries $W_{(\ell-1)/2}$; the spin is $j=(\ell-1)/2$. The chain is the weight string made concrete.
- **Adjoint.** The adjoint action doubles the defining weights; its spin is $2j$. Integer spins live on the adjoint, half-integer spins on the defining or spinor module.

**The correction.** The polar articles do not identify the half-angle with the spin. *Chirality: The Conjugate Pair* says that the half-angle is not the spin and not a normalisation of the spin. *The General Definition of Spin* says that it is a coordinate of the weight, not the highest weight. *Spinors as Peirce Coordinates in $n$ Dimensions* says that the Peirce spinor carries no half-angle at all. *Integer-Spin Quantization and the Adjoint Action on the Material Sector* says that the factor $\tfrac12$ in the adjoint generator is the Hermitian normalisation, not a half-angle. The apparent conflict is a surface reading. At $j=\tfrac12$ the coefficient $\tfrac12$ in $\theta/2$ and the spin are both $\tfrac12$, and the numerical coincidence hides the difference; at $j=1$ the coefficient is still $\tfrac12$ while the spin is $1$.

**The four halves.** The symbol $\tfrac12$ occurs four times in the story, with four different roles: the weight-to-spin conversion $j=\lambda_{\max}/2$; the antisymmetrisation $S=\tfrac12[U,V]$; the half-angle $\theta/2$ of the rotor; and the Hermitian normalisation $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$. They are not the same half. Conflating them is the source of most of the confusion, and §6 separates them in a table.

**Roadmap.** §1 states the weight-first definition and the biquaternion. §2 treats the half-angle and the polar word. §3 treats the ladder and the general-$n$ content. §4 treats the adjoint and integer spin. §5 treats the Jordan type and the degrees of degeneracy. §6 collects the four halves and the reconciliations. §7 checks the numbers. No existing article is changed; the article is a synthesis of *The General Definition of Spin*, *The Spin of a Biquaternion*, *The Weight of a Frame Root and the Spin Quantum Number*, *The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$*, *Integer-Spin Quantization and the Adjoint Action on the Material Sector*, *Chirality: The Conjugate Pair* and the polar-operator articles.

## 1. The Invariant

### The Weight-First Definition

**Definition (frame and frame root).** A **frame** of an algebra $A$ is a complete family of primitive idempotents $e_1,\dots,e_m$:

$$
e_i e_j=\delta_{ij}e_i,\qquad \sum_{i=1}^{m}e_i=1_A .
$$

A **frame root** is a linear combination $h=\sum_i s_i e_i$ with scalar weights $s_i$. The **Peirce weight** of the corner $e_iAe_j$ under left multiplication by $h$ is $s_i$; under the adjoint action it is $s_i-s_j$.

**Definition (carrier, weight, spin).** A **carrier** is a module of the triple or of the algebra on which $h$ acts. Its **weights** are the eigenvalues of $\rho(h)$; its **highest weight** is $\lambda_{\max}$; its **spin** is

$$
j=\frac{\lambda_{\max}}{2}.
$$

The spin is a property of the carrier and the root, not of the algebra alone.

**The factor of two.** The spin element $S$ has weights $m$, and the frame root is $h=2S$, with weights $2m$. The spin is the highest $m$, hence half the highest weight of $h$. In the corpus's notation the root is written $H=2S$ when the integer weights are wanted, and $S$ when the spin weights are wanted. The two notations name the same triple.

**Remark (a root with gaps).** A frame root whose weights on a carrier do not form a full string $j,j-1,\dots,-j$ does not define an irreducible carrier. The highest weight divided by two is then the top of a reducible content, not the spin of a single summand. The weight-first definition is therefore used with a root that is the grading of a spin triple; the string is full by construction. The ladder of §3 is the certificate of fullness.

### The Biquaternion

The balanced frame of $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is the pair $\tilde\Pi_+,\tilde\Pi_-$ with

$$
\tilde\Pi_+=\tfrac12(e_t+i\vec e_z),\qquad
\tilde\Pi_-=e_t-\tilde\Pi_+=\tfrac12(e_t-i\vec e_z),
$$

and the frame root is

$$
h=2\tilde\Pi_+-1=\tilde\Pi_+-\tilde\Pi_-=\tilde\Xi=i\vec e_z .
$$

**The spinor carrier.** On $S_+=\mathbb{B}\tilde\Pi_+$, with basis $(\tilde\Pi_+,\vec\Upsilon_+)$, the left action of $h$ has weights $+1$ and $-1$. The highest weight is $1$, so

$$
j=\frac{1}{2}.
$$

**The traceless carrier.** On $V=\ker\operatorname{tr}$, with basis $(\vec\Upsilon_-,\tilde\Xi,\vec\Upsilon_+)$, the adjoint action of $h$ has weights $+2,0,-2$. The highest weight is $2$, so

$$
j=\frac{2}{2}=1.
$$

**The centre.** On $\mathbb{C}e_t$ the adjoint action of $h$ is zero, so $j=0$.

The three carriers give the elementary list

$$
\{0,\tfrac12,1\},
$$

as in *Spin and the Three Elementary Carriers*. The factor $\tfrac12$ is visible twice: in the spinor weight $\pm\tfrac12$ and in the conversion from the root weight $1$ to the spin $\tfrac12$. They are the same numerical value here, and only here.

### General $n$

Let $A=M_n(\mathbb{C})$ with a frame $e_1,\dots,e_n$ and root $h=\sum_i s_i e_i$. On the defining module $\mathbb{C}^n$ the weights are $s_1,\dots,s_n$; on the adjoint they are $s_i-s_j$. The spin is the highest weight divided by two.

**The principal chain.** In the chain basis of a nilpotent of type $(n)$, the grading is

$$
S=\operatorname{diag}\left(\frac{n-1}{2},\frac{n-3}{2},\dots,-\frac{n-1}{2}\right),
\qquad h=2S .
$$

The weights of $h$ are $n-1,n-3,\dots,-(n-1)$, and the spin is $(n-1)/2$. This is the principal pair of *The General Definition of Spin*.

**The balanced frame.** For even $n$ the balanced frame has two idempotents and root $h=2e-1$ with weights $\pm1$; the carrier is $\mathbb{C}^n$ with content $rW_{1/2}$ and spin $\tfrac12$. The balanced frame reproduces the biquaternion value in every even dimension, as the Peirce computation of *The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$* shows.

**The general root.** A root of the diagonal frame, $h=\sum_i s_iE_{ii}$, has weights $s_i$; the spin is $\max s_i/2$ when the weights form a full string. The frame root is thus the general form of the weight-first definition, and the biquaternion root $2e-1$ is the two-idempotent case.

**Result.** The weight-first definition is one formula, $j=\lambda_{\max}(\rho(h))/2$, and it gives $0,\tfrac12,1$ for the biquaternion and $(n-1)/2$ for the principal chain. The ladder and adjoint readings compute the same invariant on other objects.

## 2. The Half-Angle

### The Rotor Stores Half the Angle

Let $h$ be the frame root and $S=h/2$. The rotor of the frame is

$$
R(\theta)=\exp\left(\frac{\theta h}{2}\right)=\exp(\theta S).
$$

On a weight-$m$ vector,

$$
R(\theta)v_m=e^{i\theta m}v_m
$$

in the compact case, and $e^{\theta m}$ in the hyperbolic case. The exponent coefficient is $\theta/2$; the phase angle is $\theta m$. The **half-angle** is $\theta/2$; the **spin** is the largest $m$.

For the spinor, $m=\pm\tfrac12$: the rotor acts by $e^{\pm i\theta/2}$, and the coefficient of $\theta$ in $\theta/2$ is $\tfrac12$. For the vector, $m=\pm1,0$: the rotor acts by $e^{\pm i\theta}$, and the coefficient is still $\tfrac12$, while the spin is $1$. The coefficient does not change with the carrier; the spin does. The equality at the spinor is the numerical coincidence of $j=\tfrac12$ with the coefficient $\tfrac12$, not an identity of the two notions.

**Result.** The rotor stores half the rotation angle in its exponent; the spin is the highest weight on which the rotor acts. The half-angle is a coordinate of the rotor, not a property of the carrier.

### The One-Sided Operator and the Two-Sided Sandwich

The biquaternion has two operators attached to a unit element $\tilde u$:

- the **one-sided** operator $L_{\tilde u}$, left multiplication;
- the **two-sided** operator $\Theta_{\tilde u}$, the sandwich $X\mapsto\tilde uX\tilde u^{*}$, whose infinitesimal form is the adjoint action $\operatorname{ad}_{\vec u}$.

The corpus's theorem is exact:

$$
L_{\tilde u_{\mathrm r}}=\exp\left(\frac{\theta}{2}L_{\vec u_{\mathrm r}}\right)
\Longrightarrow (\alpha,\beta)\mapsto(e^{i\theta/2}\alpha,e^{-i\theta/2}\beta),
$$

$$
\Theta_{\tilde u_{\mathrm r}}=\exp\left(\frac{\theta}{2}\operatorname{ad}_{\vec u_{\mathrm r}}\right)
\Longrightarrow \vec v\mapsto R_{\vec u_{\mathrm r}}(\theta)\vec v .
$$

The exponent is $\tfrac{\theta}{2}$ in both readings. In the one-sided case it multiplies the two spinor coordinates and produces the half-angle. In the two-sided case the same exponent acts through $\operatorname{ad}_{\vec u}=2[\vec u\times]$, and the factor $2$ doubles it to the full angle $\theta$. The half-angle belongs to the one-sided spinor action; the full angle belongs to the two-sided vector action. This is the content of *The One-Sided Operator Exponential of a N-Regular, Spectrally Regular Biquaternion*.

**Corollary.** The half-angle is not a normalisation of the spin. It is the exponent of the one-sided action, and the factor $2$ in the adjoint action cancels it. The same $\theta/2$ gives $e^{\pm i\theta/2}$ on the spinor and $R(\theta)$ on the vector.

### The Polar Regular and Degenerate Words

The polar decomposition of a biquaternion has two regimes.

- **N-regular.** The four-factor word exists: modulus, phase, boost and rotor. The rotor is the one-sided exponential, and its angle is the half-angle. The eigenbasis exists when the spectrum is regular; the polar word supplies the unitary factor.
- **N-degenerate.** The two-factor word remains: modulus and unit, with the unit a partial isometry on the nilpotent. The four-factor word collapses, and the half-angle is not part of the degenerate word.

The spin ladder is on the degenerate side: the nilpotents $U,V$ have norm zero, and their chains have no rotor angle. The spin value is still defined, by the chain length of §3, and it is $\tfrac12$ for the biquaternion. The nonzero nilpotent therefore extends to a pair whose carrier has spin $\tfrac12$ and no half-angle. This is the sharpest proof that the half-angle and the spin are different data.

**Result.** The polar decomposition classifies the element and its operator word; it does not classify the spin. The half-angle is a feature of the N-regular one-sided action. The spin is a feature of the ladder, and the ladder lives on the N-degenerate side.

### What the Corpus Says

The corpus states the separation in four places, and the synthesis only collects them.

- *Chirality: The Conjugate Pair*: "The half-angle $\theta/2$ of the polar decomposition is the exponential coordinate of the weight $\tfrac12$ on the spinor carrier... The half-angle is not the spin and it is not a normalisation of the spin."
- *The General Definition of Spin*: "The angle $\theta/2$ of the rotor is half the exponential coordinate $\theta$ of the spin operator; it is a coordinate of the weight, not the highest weight. The spin is $j$."
- *Spinors as Peirce Coordinates in $n$ Dimensions*: "The Peirce spinor carries no half-angle. A half-angle requires two further choices: a one-parameter path of families generated by rotations, and a lift of that path to a double cover of the rotation group... the half-angle is a path-and-lift parameter, not a Peirce object."
- *Integer-Spin Quantization and the Adjoint Action on the Material Sector*: "The factor $\tfrac12$ in $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$ is the Hermitian normalisation, not a half-angle... The half-angle belongs to the one-sided exponent of a unit rotor, not to this generator."

The polar articles compute the half-angle correctly. The identification of the half-angle with the spin is a misreading of those computations, and the corpus itself corrects it.

## 3. The Ladder

### The Triple as Certificate

**Definition (spin triple).** A **spin pair** is a pair $(U,V)$ with

$$
[U,V]\neq0,\qquad [[U,V],U]=2U,\qquad [[U,V],V]=-2V .
$$

The **spin element** is $S=\tfrac12[U,V]$, and the **triple** is $(S,U,V)$ with

$$
[S,U]=U,\qquad [S,V]=-V,\qquad [U,V]=2S .
$$

**Theorem (the chain lemma).** Let $U$ be nilpotent and $x_0,\dots,x_{\ell-1}$ a Jordan chain, $Ux_0=0$, $Ux_k=x_{k-1}$. Put $j=(\ell-1)/2$ and define

$$
Sx_k=(j-k)x_k,\qquad
Vx_k=(k+1)(\ell-1-k)x_{k+1}\ (k<\ell-1),\qquad
Vx_{\ell-1}=0 .
$$

Then $(S,U,V)$ is a spin triple on the span of the chain, the weights of $S$ are $j,j-1,\dots,-j$, and the spin is $j$.

*Proof.* The three relations are checked on the chain: $[S,U]x_k=Ux_k$, $[S,V]x_k=-Vx_k$, and $[U,V]x_k=2(j-k)x_k=2Sx_k$. The weights are the eigenvalues of $S$. $\square$

**Result.** A chain of length $\ell$ carries $W_{(\ell-1)/2}$; the spin is half the length minus one half. The triple is the certificate that the string $j,j-1,\dots,-j$ is full, not a second definition of spin.

**Remark (the antisymmetrisation half).** The factor $\tfrac12$ in $S=\tfrac12[U,V]$ is the antisymmetrisation of the product. It is not the weight-to-spin factor and not the half-angle. The symmetric part is the central scalar $\tfrac12\{\tilde\Upsilon_-,\tilde\Upsilon_+\}=\tfrac12e_t$ in the biquaternion, and it carries no weight; the antisymmetric part carries the whole weight content.

### The Biquaternion Ladder

The frame pair is $(\vec\Upsilon_-,\vec\Upsilon_+)$, with

$$
\vec\Upsilon_-\vec\Upsilon_+=\tilde\Pi_+,\qquad
\vec\Upsilon_+\vec\Upsilon_-=\tilde\Pi_-,\qquad
[\vec\Upsilon_-,\vec\Upsilon_+]=\tilde\Pi_+-\tilde\Pi_-=2\tilde S_{\vec u}.
$$

On the spinor $S_+$ the chain has length $2$, so $j=\tfrac12$. On the traceless part the adjoint chain has length $3$, so $j=1$. The ladder reproduces the weight-first numbers without computing an eigenvalue.

### The General $n$ Content

Let $U\in M_n(\mathbb{C})$ have Jordan type $\lambda=(\lambda_1,\dots,\lambda_r)$. The chain decomposition gives

$$
\mathbb{C}^n\cong\bigoplus_{i=1}^{r}W_{(\lambda_i-1)/2},
$$

so the defining spin is

$$
j_{\mathrm{def}}=\frac{\lambda_1-1}{2},
$$

and the multiplicity of $W_j$ is the number of blocks of size $2j+1$. The Jordan type is recovered from the content; the degeneracy type and the spin content are one datum.

The adjoint content is

$$
\mathfrak{gl}_n\cong\bigoplus_{i,j=1}^{r}W_{a_i}\otimes W_{a_j},
\qquad a_i=\frac{\lambda_i-1}{2},
$$

with the Clebsch–Gordan decomposition of each product. The adjoint spin is

$$
j_{\mathrm{adj}}=\lambda_1-1=2j_{\mathrm{def}},
$$

and the content can contain half-integer summands even though the adjoint spin is an integer. The elementary list is

$$
\Sigma(M_n,\lambda)=\left\{0,\ \frac{\lambda_1-1}{2},\ \lambda_1-1\right\},
$$

which is the principal list of $M_{\lambda_1}$. The possible lists are the principal lists of $M_1,\dots,M_n$; the possible defining spins are $0,\tfrac12,\dots,\tfrac{n-1}{2}$; the number of nilpotent orbits is $p(n)$.

**Example ($M_5$).**

| $\lambda$ | $\lambda_1$ | $\dim\mathcal O_\lambda$ | $j_{\mathrm{def}}$ | adjoint content |
|---|---|---|---|---|
| $(5)$ | $5$ | $20$ | $2$ | $0,1,2,3,4$ |
| $(4,1)$ | $4$ | $18$ | $\tfrac32$ | $0(2),1(1),\tfrac32(2),2(1),3(1)$ |
| $(3,2)$ | $3$ | $16$ | $1$ | $0(2),\tfrac12(2),1(2),\tfrac32(2),2(1)$ |
| $(3,1,1)$ | $3$ | $14$ | $1$ | $0(5),1(5),2(1)$ |
| $(2,2,1)$ | $2$ | $12$ | $\tfrac12$ | $0(5),\tfrac12(4),1(4)$ |
| $(2,1,1,1)$ | $2$ | $8$ | $\tfrac12$ | $0(10),\tfrac12(6),1(1)$ |
| $(1^5)$ | $1$ | $0$ | no pair | $0(25)$ |

The notation $j(m)$ means the summand $W_j$ with multiplicity $m$; an entry without a parenthesis has multiplicity one. The two types $(3,2)$ and $(3,1,1)$ have the same defining spin and the same elementary list, but different adjoint content.

### The Ladder and the Polar Cells

At $n=2$ the nilpotent cone has one nonzero orbit: the type $(2)$, spin $\tfrac12$. The polar cells of $\mathbb{B}$ are four: $\Sigma_{00}$, $\Sigma_{01}$, $\Sigma_{10}$, $\Sigma_{11}$, cut by $\det$ and $B^2$. The ladder $\vec\Upsilon_-$ lies in $\Sigma_{00}$, and the spin element $\tilde S_{\vec u}=\tfrac12\tilde\Xi$ lies in $\Sigma_{11}$. The cells describe the three elements of the triple, not the spin value. They cannot separate the zero nilpotent from the nonzero one: both lie in $\Sigma_{00}$, and only the nonzero one carries a pair. The Jordan type is the finer invariant.

At $n\ge3$ the nilpotent cone has $p(n)$ orbits, while the two scalar conditions still give four cells. The cells are coarser than the Jordan type for every $n\ge2$; the case $M_2$ already shows it.

## 4. The Adjoint

### Integer Spin from the Adjoint

The rotation generators of the material sector are the inner derivations

$$
J_k=\frac{1}{2}\operatorname{ad}_{i\vec e_k}.
$$

The factor $\tfrac12$ is the Hermitian normalisation, not a half-angle. On the vector part $V=\operatorname{span}\{\vec e_x,\vec e_y,\vec e_z\}$,

$$
J_3\vec e_x=i\vec e_y,\qquad J_3\vec e_y=-i\vec e_x,\qquad J_3\vec e_z=0,
$$

so the weights are $+1,-1,0$, and the spin is $1$. The quadratic Casimir is $J^2=2I$, which is $j(j+1)$ at $j=1$. The weight basis $\varepsilon_\pm=(\vec e_x\pm i\vec e_y)/\sqrt2$, $\varepsilon_0=\vec e_z$ is the polarization triad of the massive vector field.

**The material sector.** The material sector splits as

$$
\mathbb{M}_-=\operatorname{span}_{\mathbb{R}}\{ie_t\}\oplus V,
$$

of real dimensions $1$ and $3$: the scalar direction carries spin $0$, the vector part carries spin $1$. The adjoint action preserves the split and acts trivially on the scalar direction. For higher integer spin the carrier is the symmetric traceless rank-$s$ tensor of $V$, of dimension $2s+1$, with the angular momentum the sum of the adjoint actions on the factors. The rank-one case is the adjoint itself; the rank-two case is the graviton.

**Result.** Integer spin is the adjoint reading: the carrier is a tensor of the material vector, the generator is $\tfrac12\operatorname{ad}_{i\vec e_k}$, and the weights are integers. The factor $\tfrac12$ normalises the Hermitian generator; the adjoint factor $2$ in $\operatorname{ad}$ doubles the exponent to the full rotation angle.

### The Adjoint's Half

Two different halves are visible in the adjoint formula. The factor $\tfrac12$ in $J_k$ is the Hermitian normalisation, and the factor $2$ in $\operatorname{ad}_{\vec u}=2[\vec u\times]$ is the doubling that turns the exponent $\theta/2$ into the full angle $\theta$. Neither is the weight-to-spin factor. The half-angle of the one-sided spinor action belongs to $L$, not to $\operatorname{ad}$.

The adjoint's spin is read from the weights: $+1,0,-1$ give $j=1$, and in general the adjoint spin is $2j_{\mathrm{def}}$. The half in $J_k$ does not halve the spin; the weights are already integers.

### The Two Integrality Classes

The two carriers of the biquaternion separate the two integrality classes:

- the **spinor module** $S_+$ (or $S_-$), a minimal left ideal, carries half-integer spin $\tfrac12$;
- the **adjoint module** $\mathfrak{gl}_2=\mathbb{C}e_t\oplus V$ carries the integer spins $0$ and $1$.

The separation is structural, not a convention. The left action on a simple module has half-integer weights; the adjoint action on the algebra has integer weights. In $M_n(\mathbb{C})$ the same distinction separates the defining carrier $\mathbb{C}^n$, whose spin depends on the triple, from the adjoint $\mathfrak{gl}_n$, whose spin is $2j_{\mathrm{def}}$. The defining carrier is a spinor module only at $n=2$.

**Corollary.** The integer-spin quantization of the material sector and the half-integer spin of the spinor are not rival readings of one carrier. They are the two carriers. The adjoint gives the integer tower $0,1,2,\dots$ (the centre, the vector, the symmetric traceless tensors); the defining gives the half-integer value of the biquaternion and the general-$n$ content of §3.

## 5. The General $n$: Jordan Type and Degeneracy

### The Content and the Elementary List

The general-$n$ refinement is the Jordan type. The partition $\lambda$ of $n$ is the type of the ladder; the defining content is $\bigoplus_iW_{(\lambda_i-1)/2}$; the spin is $(\lambda_1-1)/2$; the adjoint spin is $\lambda_1-1$; the elementary list is $\{0,(\lambda_1-1)/2,\lambda_1-1\}$. The type is recovered from the content, so the content is a complete invariant of the ladder.

### The Degrees of Degeneracy

The question about "varying degrees of degeneracy" has a precise answer. There are five different counts, and they should not be conflated:

| object | count for $M_n$ | grows with $n$? |
|---|---|---|
| polar cells of $\mathbb{B}$ $(\det,B^2)$ | $4$ | no |
| nilpotent orbits (Jordan types) | $p(n)$ | yes |
| elementary lists | $n$ | yes |
| defining spins | $n$ | yes |
| defining contents | $p(n)$ | yes |

The polar cells are cut by two scalar conditions and stay at four. The nilpotent orbits are the partitions and grow as $p(n)$: $2,3,5,7,11$ for $n=2,\dots,6$. The elementary lists grow linearly, because they depend only on the largest part; the contents grow as the partitions.

**The spectral partition is not the spin partition.** The eigenvalues of an element $Q$ give a spectral partition (the multiplicities of the eigenvalues), but the spin depends on the nilpotent part, not on the eigenvalues. The example is decisive in $M_3$: the element $J_3(0)$ has eigenvalue $0$ with multiplicity $3$ and spin $1$; the element $J_2(0)\oplus0$ has the same eigenvalue $0$ with multiplicity $3$ and spin $\tfrac12$. The spectral partition is the same, the spin is not. The polar arrangement does not see the difference either: both are in the zero-determinant, zero-discriminant cell, the analogue of $\Sigma_{00}$ for $M_3$. The Jordan type is the invariant that does.

**The dominance order.** The nilpotent orbits are ordered by the dominance order,

$$
\lambda\le\mu\quad\Longleftrightarrow\quad\sum_{i\le k}\lambda_i\le\sum_{i\le k}\mu_i\ \text{for all }k,
$$

and the orbit of $\lambda$ lies in the closure of the orbit of $\mu$ exactly when $\lambda\le\mu$. The regular orbit $(n)$ is open and dense; the zero orbit $(1^n)$ is closed. The $M_5$ table is ordered this way.

**The spin is not monotone.** Along the dominance order from $(n)$ to $(1^n)$, the defining spin $(\lambda_1-1)/2$ decreases weakly, and the number of blocks increases. The most degenerate type, $(1^n)$, has no pair; the least degenerate nonzero type, $(n)$, has the largest spin. More degeneracy does not mean more spin: it means a smaller largest block and a smaller spin, while the number of possible types grows.

**Result.** The right count for the spin possibilities is the number of nilpotent orbits, $p(n)$, not the number of polar cells. The extra degrees of degeneracy of $M_5$ and $M_6$ are the extra partitions; the values they add are the smaller spins and the finer adjoint contents, not a larger spin at the degenerate end.

## 6. The Four Halves and the Reconciliations

### The Four Halves

| occurrence | where | role | what it is not |
|---|---|---|---|
| $j=\lambda_{\max}/2$ | weight-first | root weights to spin weights | not the half-angle |
| $S=\tfrac12[U,V]$ | triple | antisymmetrisation of the product | not the weight-to-spin factor |
| $\exp(\theta h/2)$ | rotor | exponent coefficient (half-angle) | not the spin |
| $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$ | adjoint | Hermitian normalisation | not a half-angle |

The table is the whole correction in one place: the same symbol marks four different operations, and no two of them coincide. The spinor weight $\pm\tfrac12$ is the value on which these operations act; it is not a fifth factor.

### The Table of Approaches

| approach | object | formula | carrier | what it is not |
|---|---|---|---|---|
| weight / frame root | $h$ | $j=\lambda_{\max}(\rho(h))/2$ | defining or adjoint | not the half-angle |
| half-angle / polar | rotor $\exp(\theta h/2)$ | exponent $\theta/2$ | one-sided spinor action | not the spin |
| ladder / triple | chain length $\ell$ | $j=(\ell-1)/2$ | triple module | not a new definition |
| adjoint / material | $\operatorname{ad}_h$ | $j_{\mathrm{adj}}=\lambda_{\max}/2=2j$ | adjoint $\mathfrak{gl}_n$ | not the defining spin |
| Jordan type | partition $\lambda$ | $\bigoplus_iW_{(\lambda_i-1)/2}$ | defining | not the polar cell |
| Peirce / chirality | Peirce index | — | — | not the spin, not the chirality |

The first four rows are the four readings; the fifth is the general-$n$ form of the ladder; the sixth is a contrast, not a reading.

### The Common Formula

For a triple whose defining spin is $j$,

$$
j=\frac{\lambda_{\max}(\rho(h))}{2}=\frac{\ell-1}{2}=\frac{\lambda_1-1}{2},
\qquad
j_{\mathrm{adj}}=2j=\lambda_1-1 .
$$

The spinor rotation has period $4\pi$ because $j=\tfrac12$; the integer representation has period $2\pi$ because $j$ is an integer. The period is a property of the weight, not of the half-angle.

### The Corrections

- **The half-angle is not the spin.** It is the exponent coordinate of the rotor; the coefficient of $\theta$ in $\theta/2$ equals the spin only at $j=\tfrac12$, and the equality is numerical. At $j=1$ the coefficient is $\tfrac12$ and the spin is $1$.
- **The adjoint's half is not a half-angle.** The factor $\tfrac12$ in $J_k$ is the Hermitian normalisation; the adjoint weights are integers.
- **The Peirce index is not the chirality.** The right action of $S$ is $\pm\tfrac12$ on the two Peirce planes; that sign labels two copies of one left module. The chirality is the central $\chi=ij$ of the complexified algebra, $\chi^2=1$, equivalently the grading $S\oplus S^{\mathrm c}$; the Peirce index is a copy index.
- **The triple is not the definition.** It is the certificate that the weight string is full. The definition is the highest weight; the triple makes the string concrete.
- **The polar cells are not the Jordan type.** Four cells versus $p(n)$ orbits. The cells cannot separate the zero nilpotent from the nonzero one.
- **Integer and half-integer spin are not a contradiction.** They are the two carriers: the adjoint and the spinor.
- **More degeneracy does not mean more spin.** The number of orbits grows; the spin of the most degenerate nonzero type is the smallest.

## 7. Checks

### The Biquaternion

The root $h=i\vec e_z$ has weights $+1,-1$ on the spinor and $+2,0,-2$ on the traceless part. The weights of $S=h/2$ are $\pm\tfrac12$ and $\pm1,0$, so $j=\tfrac12$ and $j=1$. The rotor $R(\theta)=\exp(\theta\vec e_z/2)$ acts on the spinor by $e^{\pm i\theta/2}$ and on the vector by $e^{\pm i\theta}$; the coefficient of $\theta$ in $\theta/2$ is $\tfrac12$ in both, the spin is not. The adjoint generator $J_3=\tfrac12\operatorname{ad}_{i\vec e_z}$ has weights $+1,-1,0$ on the vector part and Casimir $2$.

### $M_3(\mathbb{C})$

For the type $(3)$, the chain basis gives

$$
S=\operatorname{diag}(1,0,-1),\qquad
U=E_{12}+2E_{23},\qquad
V=2E_{21}+E_{32}.
$$

The defining content is $W_1$; the adjoint content is $W_0\oplus W_1\oplus W_2$; the spin is $1$. For the type $(2,1)$,

$$
S=\operatorname{diag}\left(\tfrac12,-\tfrac12,0\right),\qquad
U=E_{12},\qquad
V=E_{21}.
$$

The defining content is $W_{1/2}\oplus W_0$; the adjoint content is $W_1\oplus2W_{1/2}\oplus2W_0$; the spin is $\tfrac12$.

### $M_4(\mathbb{C})$

The principal type $(4)$ has $S=\operatorname{diag}(\tfrac32,\tfrac12,-\tfrac12,-\tfrac32)$ and spin $\tfrac32$; the adjoint content is $0,1,2,3$. The balanced type $(2,2)$ has $S=\operatorname{diag}(\tfrac12,-\tfrac12,\tfrac12,-\tfrac12)$ and spin $\tfrac12$; the adjoint content is $0(4),1(4)$.

### The Casimir

On a chain of length $\ell=2j+1$, the Casimir $C=S^2+\tfrac12(UV+VU)$ acts by $j(j+1)$. For the type $\lambda$ the characteristic polynomial is

$$
\prod_{i=1}^{r}\left(X-\frac{\lambda_i-1}{2}\cdot\frac{\lambda_i+1}{2}\right)^{\lambda_i}.
$$

For $M_5$ with $\lambda=(3,2)$, this is $(X-2)^3(X-\tfrac34)^2$, as the content $W_1\oplus W_{1/2}$ requires. The triple relations, the chain coefficients and the Casimir eigenvalues were checked symbolically for every partition of $n\le7$.

## 8. Summary

- The corpus's approaches to spin are four readings of one invariant. The invariant is $j=\lambda_{\max}(\rho(h))/2$ for a grading $h$; with $S=h/2$, the spin is the highest weight of $S$.
- The weight reading gives $j=\lambda_{\max}/2$; the biquaternion root $h=2e-1$ gives $j=\tfrac12$ on the spinor and $j=1$ on the traceless part.
- The half-angle reading gives the exponent $\theta/2$ of the rotor. The coefficient of $\theta$ in $\theta/2$ is not the spin; it coincides with it only at $j=\tfrac12$. The one-sided operator produces the half-angle; the two-sided sandwich produces the full angle, because $\operatorname{ad}=2[\times]$.
- The ladder reading gives $j=(\ell-1)/2$. The triple is the certificate that the weight string is full, not a new definition.
- The adjoint reading gives integer spins: the vector part has weights $\pm1,0$, spin $1$; the factor $\tfrac12$ in $J_k=\tfrac12\operatorname{ad}_{i\vec e_k}$ is the Hermitian normalisation, not a half-angle.
- In general $n$, the Jordan type $\lambda$ gives the defining content $\bigoplus_iW_{(\lambda_i-1)/2}$, the spin $(\lambda_1-1)/2$, the adjoint spin $\lambda_1-1=2j$, and the elementary list $\{0,(\lambda_1-1)/2,\lambda_1-1\}$. The possible lists are the principal lists of $M_1,\dots,M_n$; the possible defining spins are $0,\tfrac12,\dots,\tfrac{n-1}{2}$.
- The degrees of degeneracy are the nilpotent orbits, $p(n)$ of them, not the four polar cells. The spectral partition is not enough: $J_3(0)$ and $J_2(0)\oplus0$ have the same spectrum and different spins. More degeneracy does not mean more spin.
- The four occurrences of $\tfrac12$ — weight-to-spin, antisymmetrisation, half-angle, Hermitian normalisation — are different operations. Separating them removes the apparent conflict between the polar, ladder, adjoint and weight readings.
- The biquaternion is the case $n=2$: the elementary list is $\{0,\tfrac12,1\}$; the polar cells add no spin value; the two integrality classes are the spinor module and the adjoint material sector.

## Summary of Notation

| symbol | meaning |
|---|---|
| $A$ | a finite-dimensional algebra |
| $e_i$ | frame idempotents, $e_ie_j=\delta_{ij}e_i$, $\sum e_i=1_A$ |
| $h=\sum_i s_i e_i$ | frame root (grading element) |
| $S=h/2$ | spin element |
| $j=\lambda_{\max}/2$ | spin of a carrier |
| $W_j$ | irreducible module, dimension $2j+1$, weights $j,\dots,-j$ |
| $U,V$ | ladder operators, nilpotent |
| $[S,U]=U$, $[S,V]=-V$, $[U,V]=2S$ | triple relations |
| $\ell=2j+1$ | chain length |
| $\lambda=(\lambda_1,\dots,\lambda_r)$ | Jordan type, partition of $n$ |
| $j_{\mathrm{def}}=(\lambda_1-1)/2$ | defining spin |
| $j_{\mathrm{adj}}=\lambda_1-1=2j_{\mathrm{def}}$ | adjoint spin |
| $p(n)$ | number of partitions of $n$ |
| $\Sigma_{ij}$ | polar cells of $\mathbb{B}$ |
| $L_{\tilde u}$ | one-sided operator (left multiplication) |
| $\Theta_{\tilde u}$ | two-sided operator (sandwich) |

## Further Reading

- [The General Definition of Spin](the-general-definition-of-spin.html), for the spin pair, the triple, the structure theorem, the principal and balanced lists, and the list of what is not a definition.
- [The Weight of a Frame Root and the Spin Quantum Number](the-weight-of-a-frame-root-and-the-spin-quantum-number.html), for the frame root $h=2e-1$, the Peirce weights and the weight-first reading.
- [The Spin of a Biquaternion](the-spin-of-a-biquaternion.html), for the frame pair, the three carriers, the half-angle and the adjoint.
- [Spin and the Three Elementary Carriers](../articles_physics/spin-and-the-three-elementary-carriers.html), for the elementary list $\{0,\tfrac12,1\}$ of $\mathbb{B}$.
- [The Spin Chain and the Adjoint Decomposition of $M_n(\mathbb{C})$](the-spin-chain-and-the-adjoint-decomposition-mnc.html), for the principal chain and the adjoint decomposition.
- [Integer-Spin Quantization and the Adjoint Action on the Material Sector in Biquaternionic Form](../articles_physics/integer-spin-quantization-and-the-adjoint-action-on-the-material-sector-in-biquaternionic-form.html), for the adjoint reading, the vector triplet, the material sector and the Hermitian normalisation.
- [Angular Momentum and Spin in Biquaternionic Form](../articles_physics/angular-momentum-and-spin-in-biquaternionic-form.html), for the angular-momentum algebra and the addition of angular momenta.
- [The One-Sided Operator Exponential of a N-Regular, Spectrally Regular Biquaternion](the-one-sided-operator-exponential-of-a-n-regular-spectrally-regular-biquaternion.html), for the one-sided half-angle and the two-sided full angle.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html) and [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the regular and degenerate polar words.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-eigenbasis-of-a-spectrally-regular-biquaternion.html) and [The Jordan Basis of a Spectrally Degenerate Biquaternion](the-jordan-basis-of-a-spectrally-degenerate-biquaternion.html), for the two carrier bases.
- [Chirality: The Conjugate Pair](chirality-the-conjugate-pair.html), for the statement that the half-angle is not the spin and for the central $\chi=ij$.
- [Spinors as Peirce Coordinates in $n$ Dimensions](spinors-as-peirce-coordinates-in-n-dimensions.html), for the absence of a half-angle in the Peirce data.
- [Modules over $k[x]$ and the Jordan Form](modules-over-kx-and-the-jordan-form.html) and [Nilpotent Elements and the Jordan–Chevalley Decomposition](nilpotent-elements-and-the-jordan-chevalley-decomposition.html), for the Jordan type.
- [Peirce Coordinates and Companion Nilpotents](peirce-coordinates-and-companion-nilpotents.html), for the frame and its nilpotents.
- [The Adjoint Action, the Orbits and the Flag Variety of $M_3(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m3c.html), [of $M_4(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m4c.html), [of $M_5(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m5c.html) and [of $M_6(\mathbb{C})$](the-adjoint-action-the-orbits-and-the-flag-variety-of-m6c.html), for the nilpotent orbits and their dimensions.
- [Representations of Lie Algebras](representations-of-lie-algebras.html) and [The Casimir Operator](the-casimir-operator.html), for the highest-weight theorem and the eigenvalue $j(j+1)$.
