# __The Polar Decomposition of a N-Regular Biquaternion__

## Introduction

The general polar decomposition of *The Polar Decomposition of a Biquaternion* writes every biquaternion as

$$
\tilde Q=\tilde Q_H\,\tilde Q_0,
$$

with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. On the $\natural$-regular elements, those with $\langle\tilde Q\rangle_{\natural}\neq0$, the pair sharpens: $\tilde Q_H$ is positive definite and $\tilde Q_0$ is $*$-unitary. This article takes the pair apart.

The pair has two factors, and each factor splits again into two. The element is written first as a modulus times a unit factor,

$$
\tilde Q=\Rho\,\tilde U,\qquad \Rho^{2}=\langle\tilde Q\rangle_{\natural},\qquad \langle\tilde U\rangle_{\natural}=1,
$$

and then each of the two is split:

$$
\Rho=r\,\zeta,\qquad \tilde U=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}.
$$

The four factors are the **scale** $r>0$, the **central phase** $\zeta$ of modulus one, the **boost** $\tilde U_{\mathrm b}$, Hermitian positive definite of norm one, and the **rotor** $\tilde u_{\mathrm r}$, a unit real quaternion. Read as a word,

$$
\boxed{\;\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\;}
$$

The two levels are collected in the table.

| reading | form | factors | real dimensions |
|---|---|---|---|
| Cartan pair | $\tilde Q=\tilde Q_H\tilde Q_0=(r\tilde U_{\mathrm b})(\zeta\tilde u_{\mathrm r})$ | $2$ | $4+4$ |
| modulus–unit | $\tilde Q=\Rho\tilde U=(r\zeta)(\tilde U_{\mathrm b}\tilde u_{\mathrm r})$ | $2$ | $2+6$ |
| word | $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $4$ | $1+1+3+3$ |

The same four factors are regrouped in three ways, and the article follows the splits and the regroupings. It proves the sharpening and computes the modulus and the unit factor (§*The Two Factors*), splits them into the four factors (§*The Four Factors*), reads the group of units (§*The Group of Units*), separates the two halves of the algebra (§*The Two Halves*), gives the three pairings (§*The Three Pairings*), records the matrix picture (§*The Matrix Picture*), reads the word on the spinor module (§*The Operator Reading: the Twist*), proves existence and uniqueness (§*Existence and Uniqueness*), and closes with the algorithm and a worked example.

The conventions and the symbols are those of *Conventions in Mathematics*, *N-Regularity and N-Degeneracy in the Biquaternion Algebra* and *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the symbols are collected in §*Summary of Notation*. The product is the plain product, the conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the norm is the quaternionic norm $\langle\tilde Q\rangle_{\natural}$.

## The Two Factors

Let $\tilde Q$ be $\natural$-regular, $\langle\tilde Q\rangle_{\natural}\neq0$. Then $\tilde Q$ is invertible (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The $\natural$-regular case: The Group of Units*), and the two factors of the general decomposition are

$$
\tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\qquad \tilde Q_0=\tilde Q_H^{-1}\tilde Q .
$$

**Proposition (the sharpened factors).** If $\langle\tilde Q\rangle_{\natural}\neq0$, then $\tilde Q_H$ is positive definite and $\tilde Q_0$ is $*$-unitary.

*Proof.* The element $\tilde Q\tilde Q^{*}$ is Hermitian and positive definite, being the product of an invertible element and its Hermitian conjugate; its unique square root in the cone is positive definite, so $\tilde Q_H$ is positive definite and invertible. Then

$$
\tilde Q_0\tilde Q_0^{*}=\tilde Q_H^{-1}\tilde Q\tilde Q^{*}\tilde Q_H^{-1}=\tilde Q_H^{-1}\tilde Q_H^{2}\tilde Q_H^{-1}=e_t,
$$

and symmetrically $\tilde Q_0^{*}\tilde Q_0=e_t$. $\square$

The unitarity is the sharpening: the partial isometry of the general case is now invertible, and its two projections are both $e_t$.

**The modulus.** The norm is a complex number, and it vanishes exactly on the zero-divisor cone $\mathcal N$ (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*). A modulus is a square root of the norm,

$$
\Rho^{2}=\langle\tilde Q\rangle_{\natural},
$$

and the two roots differ by a sign, so the root is not defined by the norm alone. The branch is fixed once and for all. With $a=\operatorname{Re}\langle\tilde Q\rangle_{\natural}$ and $b=\operatorname{Im}\langle\tilde Q\rangle_{\natural}$, put

$$
\Rho=\sqrt{\frac{\lvert\langle\tilde Q\rangle_{\natural}\rvert+a}{2}}+i\,\operatorname{sgn}(b)\sqrt{\frac{\lvert\langle\tilde Q\rangle_{\natural}\rvert-a}{2}},\qquad \operatorname{sgn}(0)=+1 .
$$

The root lies in the **principal half-plane**

$$
\mathcal H=\{\Rho\in\mathbb C:\operatorname{Re}\Rho>0\}\cup\{it:t>0\},
$$

and the other root $-\Rho$ lies outside it. On $\mathcal H$ the root is a function of the norm and is unique. The sign convention at $b=0$ places a negative real norm on the positive imaginary axis, and the root is continuous away from the negative real axis, where the branch cut lies. The branch is the only convention of the decomposition.

**The scale and the phase.** The polar coordinates of the modulus on $\mathcal H$ are

$$
r=\lvert\Rho\rvert=\sqrt{\lvert\langle\tilde Q\rangle_{\natural}\rvert}>0,\qquad \zeta=\frac{\Rho}{\lvert\Rho\rvert},\qquad \lvert\zeta\rvert=1 .
$$

The phase lies in the half of the unit circle cut by the branch,

$$
\zeta\in\{\zeta\in\mathbb C:\lvert\zeta\rvert=1,\ \operatorname{Re}\zeta>0\}\cup\{i\},
$$

it takes the value $1$ on the positive real axis and $i$ on the positive imaginary axis, and it never takes the values $-1$ or $-i$.

**The unit factor.** Put

$$
\tilde U=\frac{\tilde Q}{\Rho}.
$$

Since $\Rho$ is central and $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$, the norm is multiplicative and

$$
\langle\tilde U\rangle_{\natural}=\frac{\langle\tilde Q\rangle_{\natural}}{\Rho^{2}}=1 .
$$

The unit factor lies on the norm-one set

$$
\mathbb B^{\times}_{1}=\{\tilde U\in\mathbb B:\langle\tilde U\rangle_{\natural}=1\},
$$

which is a group: the product of two norm-one elements has norm one, and the inverse of a norm-one element is its conjugate, $\tilde U^{-1}=\tilde U^{\natural}$. Under the matrix model the norm is the determinant, so the group is the special linear group,

$$
\boxed{\;\mathbb B^{\times}_{1}\cong SL_2(\mathbb C)\;}
$$

of complex dimension three and real dimension six (*N-Regularity and N-Degeneracy in the Biquaternion Algebra*, §*The $\natural$-regular case: The Group of Units*).

The group is not compact. It contains the Hermitian positive elements of norm one, and those are unbounded: the element $c\,e_t+i\sqrt{c^{2}-1}\,\vec e_x$ has norm one for every $c\ge1$. This is the sharpest difference from the quaternion case, where the norm-one set is the sphere $S^{3}$. The biquaternion unit factor has three compact directions and three non-compact ones, and the split into boost and rotor separates them.

The phrase **unit factor** names the norm-one elements. It is not the **group of units** $\mathbb B^{\times}$, the wider set of invertible elements; the two senses of the word *unit* are kept apart throughout, as in *Conventions in Mathematics*, §*The Unitary Convention*. The group of units is $\mathbb B\setminus\mathcal N$, of real dimension eight, and the norm-one group is a hypersurface inside it.

**The count.** A biquaternion carries eight real parameters. The modulus carries two, the scale and the phase. The unit factor is constrained by the single complex equation $\langle\tilde U\rangle_{\natural}=1$, so it retains six real degrees of freedom. Thus

$$
8=2+6 .
$$

No coordinate has been chosen on the unit factor: the equation is one complex condition, and the six parameters are the dimension of $SL_2(\mathbb C)$, not a chart.

## The Four Factors

The two factors of the previous section are each the product of two.

### The split of the modulus

The modulus splits into the scale and the phase,

$$
\Rho=r\,\zeta,\qquad r>0,\qquad \lvert\zeta\rvert=1 .
$$

The two are central and commute with every element. They carry the norm between them,

$$
r^{2}=\lvert\langle\tilde Q\rangle_{\natural}\rvert,\qquad \zeta^{2}=\frac{\langle\tilde Q\rangle_{\natural}}{\lvert\langle\tilde Q\rangle_{\natural}\rvert},
$$

so the scale is the modulus of the norm and the phase is its unimodular direction, read through the branch.

### The split of the unit factor

**The boost.** The **boost** of $\tilde Q$ is

$$
\tilde U_{\mathrm b}=\bigl(\tilde U\tilde U^{*}\bigr)^{1/2}.
$$

It is Hermitian, $\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*}$, positive definite, and of norm one. Indeed $\tilde U\tilde U^{*}$ is Hermitian positive definite, because $\tilde U$ is invertible, and its norm is $\langle\tilde U\rangle_{\natural}\overline{\langle\tilde U\rangle_{\natural}}=1$; the square root in the cone is therefore Hermitian positive definite of norm one. The boost is the Hermitian positive factor of the polar decomposition of the unit factor on the left,

$$
\tilde U=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}.
$$

**Closed form.** Put $s=\operatorname{Sc}(\tilde U\tilde U^{*})$. The Cayley–Hamilton identity of $\tilde U\tilde U^{*}$ is $X^{2}-2sX+e_t=0$, because its determinant is one, and the square root is

$$
\boxed{\;\tilde U_{\mathrm b}=\frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2(1+s)}}\;}
$$

with inverse

$$
\tilde U_{\mathrm b}^{-1}=\frac{(2s+1)e_t-\tilde U\tilde U^{*}}{\sqrt{2(1+s)}} .
$$

The scalar $s$ is real and at least one: in the matrix model the two eigenvalues of $\tilde U\tilde U^{*}$ are positive and of product one, so their sum is at least two. The denominators are therefore real and positive. The boost is the non-compact half of the unit factor; the set of Hermitian positive elements of norm one is the hyperbolic space $H^{3}$, of real dimension three.

**The rotor.** The **rotor** of $\tilde Q$ is

$$
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U .
$$

It is $*$-unitary, because

$$
\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=\tilde U_{\mathrm b}^{-1}\tilde U\tilde U^{*}\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{-1}\tilde U_{\mathrm b}^{2}\tilde U_{\mathrm b}^{-1}=e_t,
$$

and it has norm one, by multiplicativity. Its coefficients are real. Write $\tilde u_{\mathrm r}=\tilde q_1+i\tilde q_2$ with $\tilde q_1,\tilde q_2$ real quaternions. The identity $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$ gives $\lvert\tilde q_1\rvert^{2}+\lvert\tilde q_2\rvert^{2}=1$ in scalar parts, and the identity $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ gives $\lvert\tilde q_1\rvert^{2}-\lvert\tilde q_2\rvert^{2}=1$. Hence $\lvert\tilde q_2\rvert=0$ and $\tilde q_2=0$, so the rotor is a real quaternion. It is therefore a unit real quaternion, an element of

$$
SU(2)=\{\tilde u\in\mathbb H_{\mathbb B}:\langle\tilde u\rangle_{\natural}=1\}=S^{3},
$$

the compact half of the unit factor. Its closed form is

$$
\tilde u_{\mathrm r}=\frac{(2s+1)e_t-\tilde U\tilde U^{*}}{\sqrt{2(1+s)}}\;\tilde U .
$$

Both conditions are needed in the reality argument: unitarity alone does not force the coefficients to be real, and the norm-one condition alone does not force the element to be $*$-unitary. Together they do.

### The word

Combining the two splits,

$$
\boxed{\;\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\;}
$$

with the four factors of the table.

| factor | value | defining equation | real dimension | type |
|---|---|---|---|---|
| $r$ | scale | $r=\lvert\Rho\rvert$, $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$ | $1$ | positive real, central |
| $\zeta$ | central phase | $\zeta=\Rho/r$ | $1$ | unit complex scalar, central |
| $\tilde U_{\mathrm b}$ | boost | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$ | $3$ | Hermitian positive definite, norm one |
| $\tilde u_{\mathrm r}$ | rotor | $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ | $3$ | unit real quaternion, $SU(2)$ |

The four dimensions add to eight, $8=1+1+3+3$, the real dimension of the algebra. The scale and the phase are central and commute with the other two; the boost and the rotor do not commute, and their order is part of the definition: the boost is the left Hermitian factor, so the word is boost then rotor. The other order gives a different pair, $\tilde u_{\mathrm r}\tilde U_{\mathrm b}=(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1})\tilde u_{\mathrm r}$, equal to the first exactly when the boost and the rotor commute.

**The two readings.** The four factors regroup into the Cartan pair and into the modulus–unit pair:

$$
\boxed{\;\tilde Q_H=r\,\tilde U_{\mathrm b},\qquad \tilde Q_0=\zeta\,\tilde u_{\mathrm r},\qquad \Rho=r\zeta,\qquad \tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}.\;}
$$

Indeed $\tilde Q\tilde Q^{*}=r^{2}\tilde U_{\mathrm b}^{2}$, since $\zeta$ and $\tilde u_{\mathrm r}$ are $*$-unitary, so the Hermitian square root is $r\tilde U_{\mathrm b}$; and $\tilde Q_H^{-1}\tilde Q=\zeta\tilde u_{\mathrm r}$. The Hermitian factor carries the scale and the boost, and the $*$-unitary factor the phase and the rotor. The first is Hermitian positive definite, the second $*$-unitary, and the two are the Cartan Hermitian pair of §*The Three Pairings*. The modulus–unit pair brackets the same word the other way, and the two bracketings are the two two-factor readings of the four factors.

### The branch cut

The four separate factors are not continuous across the negative real axis of the norm, although the pair $(\tilde Q_H,\tilde Q_0)$ is. At a norm that crosses the cut, $\Rho$ jumps from $i\sqrt{\lvert N\rvert}$ to $-i\sqrt{\lvert N\rvert}$, so $\zeta$ and $\tilde u_{\mathrm r}$ both change sign while their product does not. The scale, the boost, the Hermitian factor and the $*$-unitary factor are continuous there; the phase and the rotor are not. The four-factor word is therefore a decomposition of the element into four continuous functions off the cut, and into four functions that jump together on it.

## The Group of Units

The group of units is the $\natural$-regular set, $\mathbb B^{\times}=\mathbb B\setminus\mathcal N$, the complement of the zero-divisor cone. The decomposition read as a map

$$
\Phi:\mathbb B^{\times}\longrightarrow\mathcal H\times SL_2(\mathbb C),\qquad \Phi(\tilde Q)=(\Rho,\tilde U),
$$

is a bijection: it is injective by the uniqueness theorem, and it is surjective because for $(\Rho,\tilde U)\in\mathcal H\times SL_2(\mathbb C)$ the element $\Rho\tilde U$ has norm $\Rho^{2}$, whose principal root is $\Rho$. Under the matrix model it is the factorisation of an invertible matrix into a complex scalar and a matrix of determinant one.

The map is not a group homomorphism. The scale is multiplicative, and the phase is multiplicative only up to a sign,

$$
r(\tilde Q_1\tilde Q_2)=r(\tilde Q_1)r(\tilde Q_2),\qquad \zeta(\tilde Q_1\tilde Q_2)=\varepsilon\,\zeta(\tilde Q_1)\zeta(\tilde Q_2),\qquad \varepsilon=\pm1,
$$

with $\varepsilon=-1$ exactly when the product $\Rho_1\Rho_2$ leaves the principal half-plane. The sign is central, so it can be absorbed by the phase or by the rotor. The factors multiply, but the parameters of the boost and of the rotor do not add: after the multiplication the middle product $\tilde u_{\mathrm r,1}\tilde U_{\mathrm b,2}$ has to be split again.

**Proposition (the maximal compact subgroup).** The maximal compact subgroup of $\mathbb B^{\times}$ is the $*$-unitary group $U(2)$, the set of words with $r=1$ and $\tilde U_{\mathrm b}=e_t$,

$$
U(2)=\{\zeta\,\tilde u_{\mathrm r}:\lvert\zeta\rvert=1,\ \tilde u_{\mathrm r}\in SU(2)\}.
$$

*Proof.* The compact part of the word is the phase times the rotor, and both are $*$-unitary, so their product is $*$-unitary; the scale and the boost are positive and non-compact. Conversely, if $V$ is $*$-unitary, then $\det V$ is a unit complex number; choose $\zeta$ in the branch with $\zeta^{2}=\det V$, and $K=\zeta^{-1}V$ is $*$-unitary of determinant one, hence a unit real quaternion. Any compact subgroup has a bounded scale, hence scale one, and a bounded boost; the boost is trivial on it, since the powers of an eigenvalue $\lambda\neq1$ are unbounded or tend to zero. Hence a compact subgroup lies in $U(2)$, which is compact and therefore maximal. $\square$

The group retracts onto $U(2)$ by shrinking the scale to one and pushing the boost to $e_t$ along the Hermitian positive elements of norm one. In particular $\mathbb B^{\times}$ is connected, and its fundamental group is that of $U(2)$, namely $\mathbb Z$, generated by the phase loop around the cone (*The Biquaternion Unit Group as a Topological Group*). The rotor contributes the simply connected factor $SU(2)=S^{3}$, so the fundamental group is carried by the phase alone.

The compact part has two circular directions, and they are not interchangeable. The central phase is central and acts on the whole algebra by multiplication; the circle inside the rotor is a one-parameter subgroup of $SU(2)$ and acts by conjugation, fixing the scalar line and acting on the vector part. The first carries the fundamental group of the group of units; the second lies in the simply connected sphere and contributes no loop. The extra compact direction is the centre of the algebra, not a factor of the sphere. This is the biquaternion counterpart of the absence of a second continuous factor in the quaternion case: there the sphere is simple modulo its centre, and the only factor beyond it is the scale line.

## The Two Halves

Every biquaternion is written uniquely as a real quaternion plus $i$ times a real quaternion,

$$
\tilde Q=\tilde q+i\tilde p,\qquad \tilde q,\tilde p\in\mathbb H_{\mathbb B},\qquad \mathbb B=\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B},
$$

where $\mathbb H_{\mathbb B}$ is the real span of $e_t,\vec e_x,\vec e_y,\vec e_z$ and $i$ is the central scalar imaginary. On the two halves the norm reads

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde q\rangle_{\natural}-\langle\tilde p\rangle_{\natural}+2i\,\langle\tilde q,\tilde p\rangle,
$$

with $\langle\tilde q\rangle_{\natural}=\sum_\mu q_\mu^{2}$ the real quaternion norm and $\langle\tilde q,\tilde p\rangle=\operatorname{Sc}(\tilde q^{\natural}\tilde p)$ the Euclidean inner product of $\mathbb R^{4}$. The real part is the difference of the two squared lengths and the imaginary part is twice their inner product, so the norm vanishes exactly when the halves have equal length and are orthogonal.

The four factors sit in the two halves as follows. The scale is a real scalar and lies in the first half. The phase is a complex scalar, so its imaginary part is central. The rotor is a real quaternion and lies in the first half. The boost has its scalar part in the first half and its vector part in the second,

$$
\tilde U_{\mathrm b}=a\,e_t+i\vec w,\qquad a\in\mathbb R,\quad \vec w\in\mathbb R^{3},\qquad a^{2}-\lvert\vec w\rvert^{2}=1 .
$$

The boost is the only factor whose vector part lies in the second half, and it is the factor that carries the indefiniteness: its scalar part is at least one and its vector part is tied to it by the norm-one condition. The boost is trivial exactly when the unit factor is $*$-unitary, that is, on the elements $r\zeta\tilde u_{\mathrm r}$; in particular it is trivial on both halves.

This is the precise sense in which the biquaternion case is the complexification of the quaternion one. The scale and the rotor are the quaternion polar decomposition; the complex scalar adds the phase, one compact direction, and the second half adds the boost, three non-compact ones.

## The Three Pairings

The four factors can be bracketed in three ways. Each bracketing is a **pairing**: the factors are regrouped, and the two composite factors are recognised as elements of a smaller structure. Two pairings are partial, their construction dividing by a part of the element that can vanish; the third is total on the $\natural$-regular set.

### The quaternion pairing

$$
\tilde Q=\bigl(r\tilde u_{\mathrm r}\bigr)\bigl(\zeta\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr).
$$

The first factor is the real quaternion $r\tilde u_{\mathrm r}$: a positive scale times a unit real quaternion. The second is the phase times the boost carried into the rotor frame. The pairing is partial: its construction divides by the part of $\tilde Q$ whose four coefficients are real, so it is available only where that part is nonzero.

### The Hamilton root pairing

$$
\tilde Q=(r\zeta)\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)=\Rho\,\tilde U .
$$

The first factor is the complex modulus. The second is the unit factor, read on the root of $-e_t$ parallel to the vector part. With $\tilde Q=Q_te_t+\vec Q$, $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ and $B$ a chosen square root of $B^{2}$,

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\cos\Theta+\vec U\sin\Theta,\qquad \vec U=\frac{\vec Q}{B},\qquad \cos\Theta=\frac{Q_t}{\Rho},\qquad \sin\Theta=\frac{B}{\Rho}.
$$

The pairing is partial: the normalisation divides by $B$, so the vector part must be non-null, $B^{2}\neq0$.

### The Cartan Hermitian pairing

$$
\tilde Q=\bigl(r\tilde U_{\mathrm b}\bigr)\bigl(\zeta\tilde u_{\mathrm r}\bigr)=\tilde Q_H\,\tilde Q_0 .
$$

The first factor is Hermitian positive definite, the second $*$-unitary. The pairing solves $\tilde Q\tilde Q^{*}=\tilde H^{2}$, so both factors are functions of the element alone, and it is total on the $\natural$-regular set. It is the algebra form of the matrix polar decomposition.

The three pairings are collected in the table.

| pairing | first factor | second factor | available when |
|---|---|---|---|
| quaternion | $r\tilde u_{\mathrm r}$ | $\zeta\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and the real-coefficient part is nonzero |
| Hamilton root | $\Rho$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $B^{2}\neq0$ |
| Cartan Hermitian | $r\tilde U_{\mathrm b}$ | $\zeta\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ |

The two partial domains are not nested, and the Cartan domain contains both. The elements of the $\natural$-regular set outside both partial domains are the nonzero purely imaginary complex scalars.

## The Matrix Picture

The algebra is isomorphic to the complex matrix algebra,

$$
M_2:\mathbb B\longrightarrow M_2(\mathbb C),\qquad M_2(e_t)=I,\qquad M_2(\vec e_k)=-i\sigma_k,
$$

with $\sigma_k$ the Pauli matrices, and the isomorphism is one of complex algebras, not only of real ones (*$M_2(\mathbb{C})$ Model : The Product, the Trace and the Determinant*). The determinant is the biquaternion norm,

$$
\det M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},
$$

and the norm-one group is the special linear group.

The word becomes

$$
M=r\,\zeta\,M_{\mathrm b}\,M_{\mathrm r},\qquad M_{\mathrm b}=M_{\mathrm b}^{\dagger},\quad M_{\mathrm b}>0,\quad \det M_{\mathrm b}=1,\quad M_{\mathrm r}\in SU(2),
$$

and the matrix polar decomposition groups it into two:

$$
M=P\,V,\qquad P=(MM^{\dagger})^{1/2}=r\,M_{\mathrm b},\qquad V=\zeta\,M_{\mathrm r}.
$$

The positive factor is the scale times the boost, of determinant $r^{2}$; the $*$-unitary factor is the phase times the rotor, of determinant $\zeta^{2}$. The matrix decomposition does not see the split of $P$ into scale and boost, nor that of $V$ into phase and rotor: those splits use the fact that $P$ is a positive real multiple of an element of the algebra of determinant one, and that $V$ is a unit complex multiple of a real quaternion.

| factor | matrix | determinant | action |
|---|---|---|---|
| scale | $rI$, $r>0$ | $r^{2}$ | dilation of ratio $r$ |
| central phase | $\zeta I$, $\lvert\zeta\rvert=1$ | $\zeta^{2}$ | central multiplication |
| boost | $M_{\mathrm b}$, Hermitian positive | $1$ | congruence $X\mapsto M_{\mathrm b}XM_{\mathrm b}^{\dagger}$ |
| rotor | $M_{\mathrm r}\in SU(2)$ | $1$ | conjugation $X\mapsto M_{\mathrm r}XM_{\mathrm r}^{-1}$ |

## The Operator Reading: the Twist

The word also acts. On the module $S=\mathbb{C}^2$ left multiplication is

$$
\psi\longmapsto\mathsf M_2(\tilde Q)\,\psi=\Rho\,\mathsf M_2(\tilde U)\,\psi ,
$$

with $\mathsf M_2(\tilde U)\in SL_2(\mathbb{C})$. The scalar $\Rho$ needs no module of its own: by Schur's lemma the centre acts on a simple module by a scalar, so the scale and the phase multiply the module instead of enlarging it. They produce a one-dimensional representation of the scaling group,

$$
\chi(\Rho)=\Rho ,
$$

and the module on which the general element acts is the spinor module **twisted by $\chi$**, written $S\otimes\chi$. The norm-one case $\Rho=1$ is the untwisted case; the untwisted operators are the norm-one elements, the double cover of the Lorentz group.

A **spinor** is a vector of the module, not the operator and not the rotor. The word writes the operator as $\Rho\tilde U$; the spinor is what that operator acts on. The distinction matters because the operator has more factors than the module can distinguish: the module sees the scale and the phase only through the single scalar $\Rho$.

### The Labels of the Twisted Representations

A character of the scaling group is

$$
\chi_{a,b}(A)=A^{a}\bar A^{b},\qquad A=r\zeta,\quad a,b\in\mathbb{C},\quad a-b\in\mathbb{Z},
$$

the last condition making the character single-valued on $\mathbb{C}^{\times}$. The irreducible smooth finite-dimensional modules of the group of units are

$$
(j,j')_{(a,b)}=V_j\boxtimes V_{j'}\otimes\chi_{a,b},
$$

where $V_j$ is the $SL_2(\mathbb{C})$-module of spin $j$ of *Biquaternion Rotations and Lorentz Transformations*, §*Finite-Dimensional Representations of the Lorentz Group*. The central element $-I$ acts on $(j,j')$ by $(-1)^{2j+2j'}$ and through the character by $(-1)^{a-b}$, so a twisted module exists exactly when

$$
a-b\equiv 2j+2j'\pmod 2 .
$$

The defining module of $GL_2(\mathbb{C})$ is $(\tfrac12,0)_{(1,0)}$: a spinor is multiplied by $A$, which is a square root of the determinant character, since $\det(AI)=A^{2}$.

Reality and unitarity read off the character. Complex conjugation exchanges the two factors and conjugates the character, $\overline{(j,j')_{(a,b)}}=(j',j)_{(b,a)}$, so a module is self-conjugate exactly when $j=j'$ and $b=a$. And $\lvert\chi_{a,b}(A)\rvert=r^{\mathrm{Re}(a+b)}$, so the twist is $*$-unitary exactly when $\mathrm{Re}(a+b)=0$; even then the norm-one part contributes no nontrivial finite-dimensional $*$-unitary representation, which is the non-unitarity recorded for $SL_2(\mathbb{C})$ in the rotations article.

### What the Algebra Carries

The algebra is four-dimensional over $\mathbb{C}$, and its natural self-actions carry a short list:

- **Left multiplication.** $\mathbb{B}\cong S\oplus S$ as a left module, so $L$ carries two copies of $(\tfrac12,0)_{(1,0)}$.
- **Right multiplication.** $\mathbb{B}\cong S^{*}\oplus S^{*}$ with $S^{*}\cong S$, so $R$ carries two copies of the same chirality, twisted the same way. Neither one-sided action produces the opposite handedness.
- **The sandwich.** It is irreducible on the algebra and carries $(\tfrac12,\tfrac12)_{(1,1)}$, the four-vector scaled by $r^{2}$.
- **Nothing higher.** The modules of $M_2(\mathbb{C})$ are direct sums of copies of $S$, so every irreducible summand is the spinor and the dimension is even. The modules $(1,0)$, $(1,1)$ and $(\tfrac32,0)$ are not of that form. The tower is generated by the symmetric powers of $S$ and of $\bar S$, built in the tensor category.

The regular modules themselves are *The Category of Modules*; the two-sided operator that carries the four-vector is *The Two-Sided Operator of a N-Regular, Spectrally Regular Biquaternion*.

## Existence and Uniqueness

**Theorem.** Every $\natural$-regular biquaternion $\tilde Q$ has exactly one modulus–unit decomposition with modulus in $\mathcal H$, and exactly one four-factor word with that modulus.

*Proof (existence).* Let $\Rho$ be the principal square root of $\langle\tilde Q\rangle_{\natural}$ in $\mathcal H$, and put $\tilde U=\tilde Q/\Rho$. Then $\langle\tilde U\rangle_{\natural}=1$, so $\tilde U$ is invertible and the boost and rotor of §*The Four Factors* are defined. With $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$ the word follows by multiplication. $\square$

*Proof (uniqueness).* Suppose $\tilde Q=\Rho\tilde U=\Rho'\tilde U'$ with $\Rho,\Rho'\in\mathcal H$ and $\langle\tilde U\rangle_{\natural}=\langle\tilde U'\rangle_{\natural}=1$. Taking norms gives $\Rho^{2}=\Rho'^{2}$, so $\Rho'=\pm\Rho$; both lie in $\mathcal H$, which contains no pair of opposite points, so $\Rho'=\Rho$. Dividing, $\tilde U'=\tilde U$. The polar decomposition of $\tilde U$ is unique: $\tilde U\tilde U^{*}$ has exactly one Hermitian positive square root, hence $\tilde U_{\mathrm b}$ is unique, and then $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ is unique. $\square$

The word exists exactly on the $\natural$-regular elements. On the null cone the norm vanishes, the modulus is zero, and no modulus–unit form exists; the two-factor decomposition survives and is the subject of *The Polar Decomposition of a N-Degenerate Biquaternion*.

The uniqueness is a statement about the factors, not about a coordinate on the boost or on the rotor. Two different charts of $H^{3}$ assign different parameters to the same boost, and two different charts of $S^{3}$ assign different parameters to the same rotor; the factors themselves are fixed.

## The Algorithm

The four factors are computed in five steps.

1. **The norm.** Compute $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$. If it is zero, stop: the element is $\natural$-degenerate and has no four-factor word.

2. **The modulus.** Compute $\Rho$ from the branch formula of §*The Two Factors*. The result satisfies $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$ and lies in $\mathcal H$.

3. **The scale and the phase.** Put $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$.

4. **The unit factor.** Put $\tilde U=\tilde Q/\Rho$ and check $\langle\tilde U\rangle_{\natural}=1$.

5. **The boost and the rotor.** Compute $\tilde U\tilde U^{*}$ and $s=\operatorname{Sc}(\tilde U\tilde U^{*})$, then

    $$
    \tilde U_{\mathrm b}=\frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2(1+s)}},\qquad
    \tilde u_{\mathrm r}=\frac{(2s+1)e_t-\tilde U\tilde U^{*}}{\sqrt{2(1+s)}}\;\tilde U .
    $$

    The checks are

    $$
    \tilde U_{\mathrm b}^{2}=\tilde U\tilde U^{*},\qquad
    \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t,\qquad
    r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}=\tilde Q .
    $$

The five steps use one square root of a complex number and one of a real number, and no spectral decomposition.

## Worked Example

Take

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y .
$$

The norm is

$$
\langle\tilde Q\rangle_{\natural}=(1+i)^{2}+1+i^{2}=2i+1-1=2i,
$$

so $\lvert N\rvert=2$, $a=0$, $b=2$, and the principal root is $\Rho=1+i$. The scale and the phase are

$$
r=\sqrt2,\qquad \zeta=\frac{1+i}{\sqrt2}.
$$

The unit factor is

$$
\tilde U=\frac{\tilde Q}{1+i}=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
$$

with norm one. The Hermitian square is

$$
\tilde U\tilde U^{*}=2e_t-i\vec e_x+i\vec e_y+i\vec e_z,\qquad s=2,\qquad 2(1+s)=6,
$$

and the boost and the rotor are

$$
\tilde U_{\mathrm b}=\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt6},\qquad
\tilde u_{\mathrm r}=\sqrt{\frac23}\,e_t+\frac{1}{\sqrt6}\vec e_x+\frac{1}{\sqrt6}\vec e_y .
$$

The four factors are collected in the table.

| factor | value | quaternionic norm |
|---|---|---|
| $r$ | $\sqrt2$ | $r^{2}=2$ |
| $\zeta$ | $(1+i)/\sqrt2$ | $\zeta^{2}=i$ |
| $\tilde U_{\mathrm b}$ | $(3e_t-i\vec e_x+i\vec e_y+i\vec e_z)/\sqrt6$ | $1$ |
| $\tilde u_{\mathrm r}$ | $\sqrt{2/3}\,e_t+\vec e_x/\sqrt6+\vec e_y/\sqrt6$ | $1$ |

The checks hold: $\tilde U_{\mathrm b}^{2}=\tilde U\tilde U^{*}$, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, and $r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q$. The Hermitian factor is $\tilde Q_H=r\tilde U_{\mathrm b}$, of norm $r^{2}=2$, and the $*$-unitary factor is $\tilde Q_0=\zeta\tilde u_{\mathrm r}$, of norm $\zeta^{2}=i$; their product has norm $2i$, the norm of the element.

## Summary

The polar decomposition of an $\natural$-regular biquaternion is the modulus–unit form, refined factor by factor into four, and read on the spinor module as a twisted representation.

| item | result |
|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| Cartan pair | $\tilde Q=\tilde Q_H\tilde Q_0$, $\tilde Q_H$ positive definite, $\tilde Q_0$ $*$-unitary |
| modulus–unit | $\tilde Q=\Rho\tilde U$, $\Rho\in\mathcal H$, $\langle\tilde U\rangle_{\natural}=1$ |
| modulus | $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$, $\Rho\in\mathcal H$ |
| scale and phase | $r=\lvert\Rho\rvert$, $\zeta=\Rho/r$ |
| boost | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$, Hermitian positive definite, norm one |
| rotor | $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$, unit real quaternion |
| word | $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| dimensions | $8=2+6=1+1+3+3$ |
| two readings | $\tilde Q_H=r\tilde U_{\mathrm b}$, $\tilde Q_0=\zeta\tilde u_{\mathrm r}$ |
| spinor module | $S\otimes\chi$ with $\chi(\Rho)=\Rho$; the irreducible modules $(j,j')_{(a,b)}$, $a-b\equiv2j+2j'\pmod2$ |
| unit group | $SL_2(\mathbb C)\cong H^{3}\times S^{3}$ |
| group of units | $\mathbb B^{\times}\cong GL_2(\mathbb C)$, maximal compact $U(2)$, fundamental group $\mathbb Z$ |
| pairings | quaternion, Hamilton root, Cartan Hermitian; the first two partial, the last total |
| closed forms | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*}+e_t)/\sqrt{2(1+s)}$, $\tilde u_{\mathrm r}=\bigl((2s+1)e_t-\tilde U\tilde U^{*}\bigr)\tilde U/\sqrt{2(1+s)}$ |

The four statements to carry away are these. On the $\natural$-regular set the general pair sharpens, the Hermitian factor becoming positive definite and the isometry factor $*$-unitary. The pair then splits twice, the modulus into a scale and a phase and the unit factor into a boost and a rotor, and the four factors fill the eight dimensions of the algebra. The regroupings of the four factors give the two-factor readings and the three pairings, of which the Cartan Hermitian pairing is the general polar decomposition itself. Read on the spinor module $S=\mathbb{C}^{2}$, left multiplication acts by the scalar $\Rho$ and the norm-one operator $\tilde U$; the scale and the phase enter through the character $\chi(\Rho)=\Rho$, and the irreducible modules are the $(j,j')_{(a,b)}$ with $a-b\equiv2j+2j'\pmod2$.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q$ | an $\natural$-regular biquaternion |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, complex and nonzero |
| $\Rho$ | the modulus, the principal root of $\langle\tilde Q\rangle_{\natural}$ in $\mathcal H$ |
| $r$ | the scale, $\lvert\Rho\rvert$ |
| $\zeta$ | the central phase, $\Rho/r$ |
| $\tilde U$ | the unit factor, $\tilde Q/\Rho$, of norm one |
| $\tilde U_{\mathrm b}$ | the boost, $(\tilde U\tilde U^{*})^{1/2}$ |
| $\tilde u_{\mathrm r}$ | the rotor, $\tilde U_{\mathrm b}^{-1}\tilde U$ |
| $\tilde Q_H$ | the Hermitian factor, $r\tilde U_{\mathrm b}$ |
| $\tilde Q_0$ | the $*$-unitary factor, $\zeta\tilde u_{\mathrm r}$ |
| $s$ | $\operatorname{Sc}(\tilde U\tilde U^{*})$ |
| $B^{2}$ | $Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $H^{3}$ | the Hermitian positive elements of norm one |
| $S$ | the spinor module $\mathbb{C}^{2}$ |
| $\chi$, $\chi_{a,b}$ | the characters $\chi(\Rho)=\Rho$ and $\chi_{a,b}(A)=A^{a}\bar A^{b}$ |
| $(j,j')_{(a,b)}$ | the irreducible module $V_j\boxtimes V_{j'}\otimes\chi_{a,b}$ |
| $\mathcal H$ | the principal half-plane of the modulus |

## Further Reading

- Roger Penrose, "A generalized inverse for matrices", *Proceedings of the Cambridge Philosophical Society* **51** (1955) 406–413. The four equations and the matrix polar decomposition.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013). The polar decomposition, its Hermitian and $*$-unitary factors, and the numerical algorithms.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008). The matrix square root, the polar factor and their derivatives.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution and the Hermitian structures the factors carry.
- *Exponential Polar Decomposition of Biquaternions*, for the same four factors read as exponentials, with the two logarithms and the boundary limits at the cone.
- *The Quaternion Pairing of the Polar Decomposition of Biquaternions*, *The Hamilton Root Pairing of the Polar Decomposition of Biquaternions* and *The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions*, for the three regroupings of the four factors.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), §*Finite-Dimensional Representations of the Lorentz Group*, for the spin-$j$ modules and the non-unitarity, and §*The Double Covers and the Lorentz Group*, for the double cover.
- [The Category of Modules](the-category-of-modules.html), for the regular modules and the bi-module structure used in §*What the Algebra Carries*.
- [The Polar Decomposition of a Biquaternion](the-polar-decomposition-of-a-biquaternion.html) and [The Polar Decomposition of a N-Degenerate Biquaternion](the-polar-decomposition-of-an-n-degenerate-biquaternion.html), for the two-factor pair that the word refines and its behaviour on the cone.
