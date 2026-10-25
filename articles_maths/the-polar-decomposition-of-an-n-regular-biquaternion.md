# __The Polar Decomposition of an N-Regular Biquaternion__

## Introduction

The general polar decomposition of *The Polar Decomposition of a Biquaternion* writes every biquaternion as

$$
\tilde Q=\tilde Q_H\,\tilde Q_0,
$$

with $\tilde Q_H$ Hermitian positive semidefinite and $\tilde Q_0$ a partial isometry. On the N-regular elements, those with $\langle\tilde Q\rangle_{\natural}\neq0$, the two factors sharpen: $\tilde Q_H$ is positive definite and $\tilde Q_0$ is unitary. This article refines the pair into four factors,

$$
\boxed{\;\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}\;}
$$

with $r>0$ a positive real, $\zeta$ a unit complex scalar in a fixed branch, $\tilde U_{\mathrm b}$ Hermitian positive definite of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. The four are the **scale**, the **central phase**, the **boost** and the **rotor**, and their real dimensions $1+1+3+3$ fill the eight of the algebra.

The article derives the word from the two-factor decomposition (§*The Two Factors*), defines the four factors and their closed forms (§*The Four Factors*), introduces the three pairings of the word (§*The Three Pairings*), proves existence and uniqueness (§*Existence and Uniqueness*), reads the unit factor as the group $SL_2(\mathbb C)$ (§*The Group of the Unit Factor*), gives the algorithm and a worked example (§*The Algorithm*, §*Worked Example*), and closes with the summary and the notation.

The word exists exactly on the complement of the null cone, the set $\langle\tilde Q\rangle_{\natural}\neq0$. On the null cone the modulus vanishes and the word does not exist; what survives there is the two-factor decomposition, and it is *The Polar Decomposition of an N-Degenerate Biquaternion*. The general pair, its uniqueness by the two ideals, and the invariants it carries are *The Polar Decomposition of a Biquaternion* and are cited, not repeated.

The conventions and the symbols are those of *Conventions in Mathematics*, *N-Regularity and Degeneracy in the Biquaternion Algebra* and *The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra*; the symbols are collected in §*Summary of Notation*. The product is the plain product, the conjugation is ${}^{*}=\bar{\cdot}\circ{}^{\natural}$, and the norm is the quaternionic norm $\langle\tilde Q\rangle_{\natural}$.

## The Two Factors

Let $\tilde Q$ be N-regular, $\langle\tilde Q\rangle_{\natural}\neq0$. Then $\tilde Q$ is invertible (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Group of Units*), and the two factors of the general decomposition are

$$
\tilde Q_H=\bigl(\tilde Q\tilde Q^{*}\bigr)^{1/2},\qquad \tilde Q_0=\tilde Q_H^{-1}\tilde Q .
$$

**Proposition (the sharpened factors).** If $\langle\tilde Q\rangle_{\natural}\neq0$, then $\tilde Q_H$ is positive definite and $\tilde Q_0$ is unitary.

*Proof.* The element $\tilde Q\tilde Q^{*}$ is Hermitian and positive definite, being the product of an invertible element and its Hermitian conjugate; its unique square root in the cone is positive definite, so $\tilde Q_H$ is positive definite and invertible. Then

$$
\tilde Q_0\tilde Q_0^{*}=\tilde Q_H^{-1}\tilde Q\tilde Q^{*}\tilde Q_H^{-1}=\tilde Q_H^{-1}\tilde Q_H^{2}\tilde Q_H^{-1}=e_t,
$$

and symmetrically $\tilde Q_0^{*}\tilde Q_0=e_t$. $\square$

The unitarity is the sharpening: the partial isometry of the general case is now invertible, and its two projections are both $e_t$.

**The modulus.** The norm is a nonzero complex number, and its two square roots differ by a sign. The branch is fixed once and for all. Write $N=\langle\tilde Q\rangle_{\natural}=u+iv$ and put

$$
\Rho=\sqrt{\frac{\lvert N\rvert+u}{2}}+i\,\operatorname{sgn}(v)\sqrt{\frac{\lvert N\rvert-u}{2}},\qquad \operatorname{sgn}(0)=+1 .
$$

Then $\Rho^{2}=N$, and $\Rho$ lies in the **principal half-plane**

$$
\mathcal H=\{\Rho\in\mathbb C:\operatorname{Re}\Rho>0\}\cup\{it:t>0\},
$$

while the other root $-\Rho$ lies outside it. The number $\Rho$ is the **modulus** of $\tilde Q$. Its square is the matrix determinant in the model $M_2(\mathbb C)$, and it is central.

The **scale** and the **central phase** are the polar coordinates of the modulus on $\mathcal H$,

$$
r=\lvert\Rho\rvert=\sqrt{\lvert N\rvert}>0,\qquad \zeta=\frac{\Rho}{\lvert\Rho\rvert},\qquad \lvert\zeta\rvert=1 .
$$

The phase lies in the half of the unit circle cut by the branch,

$$
\zeta\in\{\zeta\in\mathbb C:\lvert\zeta\rvert=1,\ \operatorname{Re}\zeta>0\}\cup\{i\},
$$

so it takes the value $1$ on the positive real axis and $i$ on the positive imaginary axis, and never the values $-1$ or $-i$.

**The unit factor.** Put

$$
\tilde U=\frac{\tilde Q}{\Rho}.
$$

Since $\Rho$ is central and $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$, the norm is multiplicative and

$$
\langle\tilde U\rangle_{\natural}=\frac{\langle\tilde Q\rangle_{\natural}}{\Rho^{2}}=1 .
$$

The unit factor lies on the norm-one set, the group $SL_2(\mathbb C)$ of §*The Group of the Unit Factor*. The decomposition

$$
\tilde Q=\Rho\,\tilde U,\qquad \Rho\in\mathcal H,\quad \Rho^{2}=\langle\tilde Q\rangle_{\natural},\quad \langle\tilde U\rangle_{\natural}=1,
$$

is the **modulus–unit** form of the element.

## The Four Factors

The modulus splits into the scale and the phase, and the unit factor splits into a Hermitian part and a unitary part.

### The boost

**Definition.** The **boost** of $\tilde Q$ is

$$
\tilde U_{\mathrm b}=\bigl(\tilde U\tilde U^{*}\bigr)^{1/2}.
$$

It is Hermitian, $\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*}$, positive definite, and of norm one. Indeed $\tilde U\tilde U^{*}$ is Hermitian positive definite, because $\tilde U$ is invertible, and its norm is $\langle\tilde U\rangle_{\natural}\overline{\langle\tilde U\rangle_{\natural}}=1$; the square root in the cone is therefore Hermitian positive definite of norm one. The boost is the Hermitian positive factor of the polar decomposition of the unit factor on the left,

$$
\tilde U=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}.
$$

**Closed form.** Put $s=\operatorname{Sc}(\tilde U\tilde U^{*})$. The Cayley–Hamilton identity of $\tilde U\tilde U^{*}$ is $X^{2}-2sX+e_t=0$, because its determinant is $1$, and the square root is

$$
\boxed{\;\tilde U_{\mathrm b}=\frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2(1+s)}}\;}
$$

with inverse

$$
\tilde U_{\mathrm b}^{-1}=\frac{(2s+1)e_t-\tilde U\tilde U^{*}}{\sqrt{2(1+s)}} .
$$

The scalar $s$ is real and at least one: the two eigenvalues of $\tilde U\tilde U^{*}$ are positive and of product one, so their sum is at least two. The denominators are therefore real and positive. The boost is the non-compact half of the unit factor; the set of Hermitian positive elements of norm one is the hyperbolic space $H^{3}$, of real dimension three.

### The rotor

**Definition.** The **rotor** of $\tilde Q$ is

$$
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U .
$$

It is unitary, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, because

$$
\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=\tilde U_{\mathrm b}^{-1}\tilde U\tilde U^{*}\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{-1}\tilde U_{\mathrm b}^{2}\tilde U_{\mathrm b}^{-1}=e_t,
$$

and it has norm one, by multiplicativity. Its coefficients are real. To see this, write $\tilde u_{\mathrm r}=q_{1}+iq_{2}$ with $q_{1},q_{2}$ real quaternions. The identity $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$ gives $\lvert q_{1}\rvert^{2}+\lvert q_{2}\rvert^{2}=1$, and the identity $\langle\tilde u_{\mathrm r}\rangle_{\natural}=1$ gives $\lvert q_{1}\rvert^{2}-\lvert q_{2}\rvert^{2}=1$ and $\langle q_{1},q_{2}\rangle=0$. Hence $\lvert q_{2}\rvert=0$ and $q_{2}=0$, so the rotor is a real quaternion. It is therefore a unit real quaternion, an element of

$$
SU(2)=\{\tilde u\in\mathbb H_{\mathbb B}:\langle\tilde u\rangle_{\natural}=1\}=S^{3},
$$

the compact half of the unit factor. Its closed form is

$$
\tilde u_{\mathrm r}=\frac{(2s+1)e_t-\tilde U\tilde U^{*}}{\sqrt{2(1+s)}}\;\tilde U .
$$

### The word and the count

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

The four dimensions add to eight, $8=1+1+3+3$, the real dimension of the algebra. The scale and the phase are central and commute with the other two; the boost and the rotor do not commute, and their order is part of the definition: the boost is the left Hermitian factor, so the word is boost then rotor.

**The two-factor reading.** The four factors regroup into the two factors of the general article:

$$
\boxed{\;\tilde Q_H=r\,\tilde U_{\mathrm b},\qquad \tilde Q_0=\zeta\,\tilde u_{\mathrm r}.\;}
$$

Indeed $\tilde Q\tilde Q^{*}=r^{2}\tilde U_{\mathrm b}^{2}$, since $\zeta$ and $\tilde u_{\mathrm r}$ are unitary, so the Hermitian square root is $r\tilde U_{\mathrm b}$; and $\tilde Q_H^{-1}\tilde Q=\zeta\tilde u_{\mathrm r}$. The Hermitian factor carries the scale and the boost, and the unitary factor the phase and the rotor. The first is Hermitian positive definite, the second unitary, and the two are the Cartan Hermitian pair of §*The Three Pairings*.

**The residual sign.** The branch fixes $\Rho$. Replacing $\Rho$ by $-\Rho$ leaves the scale and the boost unchanged and sends $\zeta\mapsto-\zeta$ and $\tilde u_{\mathrm r}\mapsto-\tilde u_{\mathrm r}$; the product $\zeta\tilde u_{\mathrm r}$ is unchanged, so the four-factor word is the same element. Without the branch the pair $(\zeta,\tilde u_{\mathrm r})$ is defined only up to the simultaneous sign, which is the biquaternion analogue of the sign carried by the unit factor in the quaternion case.

## The Three Pairings

The four factors can be bracketed in three ways. Each bracketing is a **pairing**: the factors are regrouped, and the two composite factors are recognised as elements of a smaller structure. Two pairings are partial, their construction dividing by a part of the element that can vanish; the third is total on the N-regular set.

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

The first factor is Hermitian positive definite, the second unitary. The pairing solves $\tilde Q\tilde Q^{*}=\tilde H^{2}$, so both factors are functions of the element alone, and it is total on the N-regular set. It is the algebra form of the matrix polar decomposition.

The three pairings are collected in the table.

| pairing | first factor | second factor | available when |
|---|---|---|---|
| quaternion | $r\tilde u_{\mathrm r}$ | $\zeta\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and the real-coefficient part is nonzero |
| Hamilton root | $\Rho$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and $B^{2}\neq0$ |
| Cartan Hermitian | $r\tilde U_{\mathrm b}$ | $\zeta\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ |

The two partial domains are not nested, and the Cartan domain contains both. The elements of the N-regular set outside both partial domains are the nonzero purely imaginary complex scalars.

## Existence and Uniqueness

**Theorem.** Every N-regular biquaternion $\tilde Q$ has exactly one modulus–unit decomposition with modulus in $\mathcal H$, and exactly one four-factor word with that modulus.

*Proof (existence).* Let $\Rho$ be the principal square root of $\langle\tilde Q\rangle_{\natural}$ in $\mathcal H$, and put $\tilde U=\tilde Q/\Rho$. Then $\langle\tilde U\rangle_{\natural}=1$, so $\tilde U$ is invertible and the boost and rotor of §*The Four Factors* are defined. With $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$ the word follows by multiplication. $\square$

*Proof (uniqueness).* Suppose $\tilde Q=\Rho\tilde U=\Rho'\tilde U'$ with $\Rho,\Rho'\in\mathcal H$ and $\langle\tilde U\rangle_{\natural}=\langle\tilde U'\rangle_{\natural}=1$. Taking norms gives $\Rho^{2}=\Rho'^{2}$, so $\Rho'=\pm\Rho$; both lie in $\mathcal H$, which contains no pair of opposite points, so $\Rho'=\Rho$. Dividing, $\tilde U'=\tilde U$. The polar decomposition of $\tilde U$ is unique: $\tilde U\tilde U^{*}$ has exactly one Hermitian positive square root, hence $\tilde U_{\mathrm b}$ is unique, and then $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ is unique. $\square$

The word exists exactly on the N-regular elements. On the null cone the norm vanishes, the modulus is zero, and no modulus–unit form exists; the two-factor decomposition survives and is the subject of *The Polar Decomposition of an N-Degenerate Biquaternion*.

## The Group of the Unit Factor

The unit factor is an element of the norm-one group

$$
\mathbb B^{\times}_{1}=\{\tilde U\in\mathbb B:\langle\tilde U\rangle_{\natural}=1\}\cong SL_2(\mathbb C),
$$

of complex dimension three and real dimension six (*N-Regularity and Degeneracy in the Biquaternion Algebra*, §*The Group of Units*). The map

$$
H^{3}\times SU(2)\longrightarrow SL_2(\mathbb C),\qquad (\tilde U_{\mathrm b},\tilde u_{\mathrm r})\longmapsto\tilde U_{\mathrm b}\tilde u_{\mathrm r},
$$

is a diffeomorphism: it is the polar decomposition of the unit factor, bijective by the uniqueness theorem, and smooth with smooth inverse. The boost is the non-compact factor $H^{3}$, the rotor the compact factor $S^{3}$, and the two dimensions add to six. The unit factor is not compact, and the split separates its three bounded directions from its three unbounded ones.

In the matrix model $M_2(\mathbb C)$ the square of the modulus is the determinant, the boost is the Hermitian positive matrix of determinant one, and the rotor is the special unitary matrix. The word is the matrix polar decomposition read in the algebra.

## The Algorithm

The four factors are computed in five steps.

1. **The norm.** Compute $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$. If it is zero, stop: the element is N-degenerate and has no four-factor word.
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

so $\lvert N\rvert=2$, $u=0$, $v=2$, and the principal root is $\Rho=1+i$. The scale and the phase are

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

The checks hold: $\tilde U_{\mathrm b}^{2}=\tilde U\tilde U^{*}$, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, and $r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q$. The Hermitian factor is $\tilde Q_H=r\tilde U_{\mathrm b}$, of norm $r^{2}=2$, and the unitary factor is $\tilde Q_0=\zeta\tilde u_{\mathrm r}$, of norm $\zeta^{2}=i$.

## Summary

The polar decomposition of an N-regular biquaternion is the modulus–unit form refined into four factors.

| item | result |
|---|---|
| domain | $\langle\tilde Q\rangle_{\natural}\neq0$ |
| two factors | $\tilde Q=\tilde Q_H\tilde Q_0$, $\tilde Q_H$ positive definite, $\tilde Q_0$ unitary |
| modulus | $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$, $\Rho\in\mathcal H$ |
| scale and phase | $r=\lvert\Rho\rvert$, $\zeta=\Rho/r$ |
| unit factor | $\tilde U=\tilde Q/\Rho$, $\langle\tilde U\rangle_{\natural}=1$ |
| boost | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$, Hermitian positive definite, norm one |
| rotor | $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$, unit real quaternion |
| word | $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| dimensions | $8=1+1+3+3$ |
| two-factor reading | $\tilde Q_H=r\tilde U_{\mathrm b}$, $\tilde Q_0=\zeta\tilde u_{\mathrm r}$ |
| unit group | $SL_2(\mathbb C)\cong H^{3}\times S^{3}$ |
| pairings | quaternion, Hamilton root, Cartan Hermitian; the first two partial, the last total |
| closed forms | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*}+e_t)/\sqrt{2(1+s)}$, $\tilde u_{\mathrm r}=\bigl((2s+1)e_t-\tilde U\tilde U^{*}\bigr)\tilde U/\sqrt{2(1+s)}$ |

The three statements to carry away are these. On the N-regular set the Hermitian factor is positive definite and the isometry factor is unitary, so the general pair sharpens. The unit factor splits uniquely into a boost and a rotor, the non-compact and the compact halves, and the modulus splits into a scale and a phase. The four factors regroup into three pairings, of which the Cartan Hermitian one is the general two-factor decomposition itself.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\tilde Q$ | an N-regular biquaternion |
| $N=\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm, complex and nonzero |
| $\Rho$ | the modulus, the principal root of $N$ in $\mathcal H$ |
| $r$ | the scale, $\lvert\Rho\rvert$ |
| $\zeta$ | the central phase, $\Rho/r$ |
| $\tilde U$ | the unit factor, $\tilde Q/\Rho$, of norm one |
| $\tilde U_{\mathrm b}$ | the boost, $(\tilde U\tilde U^{*})^{1/2}$ |
| $\tilde u_{\mathrm r}$ | the rotor, $\tilde U_{\mathrm b}^{-1}\tilde U$ |
| $s$ | $\operatorname{Sc}(\tilde U\tilde U^{*})$ |
| $B^{2}$ | $Q_x^{2}+Q_y^{2}+Q_z^{2}$ |
| $H^{3}$ | the Hermitian positive elements of norm one |

## Further Reading

- Roger Penrose, "A generalized inverse for matrices", *Proceedings of the Cambridge Philosophical Society* **51** (1955) 406–413. The four equations and the matrix polar decomposition.
- Gene H. Golub and Charles F. Van Loan, *Matrix Computations*, 4th edition (Johns Hopkins University Press, 2013). The polar decomposition, its Hermitian and unitary factors, and the numerical algorithms.
- Nicholas J. Higham, *Functions of Matrices: Theory and Computation* (SIAM, 2008). The matrix square root, the polar factor and their derivatives.
- Max-Albert Knus, Alexander Merkurjev, Markus Rost and Jean-Pierre Tignol, *The Book of Involutions*, Colloquium Publications 44 (American Mathematical Society, 1998). Algebras with involution and the Hermitian structures the factors carry.
