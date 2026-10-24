# __Modulus–Unit Polar Decomposition of Biquaternions__

## Introduction

This article treats the **modulus–unit polar decomposition** of a biquaternion: the writing

$$
\tilde Q=\Rho\,\tilde U,\qquad \Rho\in\mathbb C,\quad \Rho\neq0,\qquad \tilde U\in\mathbb B,\quad \langle\tilde U\rangle_{\natural}=1,
$$

with $\Rho$ the **modulus** and $\tilde U$ the **unit factor**, together with the split of the two sides into four factors,

$$
\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad r=\lvert\Rho\rvert>0,\qquad \lvert\zeta\rvert=1,\qquad \tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*},\qquad \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t .
$$

It is the algebraic member of the polar decompositions of $\mathbb B$: it uses only the norm, the two conjugations and the square root, and it chooses no coordinate on the unit fibre. The four factors are the biquaternion analogue of the two factors of the quaternion case, and their real dimensions $1+1+3+3$ fill the eight of the algebra.

Three differences from the quaternion case shape the whole article. The norm is complex, so the modulus is a complex number fixed only after a branch is chosen, and it splits into a positive scale and a central phase on the unit circle. The unit factor is not compact: it is the norm-one group $SL_2(\mathbb C)$, of real dimension six. And the unit factor splits again, into a Hermitian positive factor, the **boost**, and a unitary factor, the **rotor**; the rotor is the compact part, a unit real quaternion, and the boost carries the three non-compact directions. The quaternion article has one factor beyond the scale because its norm is definite; the biquaternion article has three, because its norm is indefinite and its unit group is not compact.

The plan is as follows. The two factors are defined (§*The Two Factors*), the four factors are described (§*The Four Factors*), the three pairings are introduced (§*The Three Pairings*), existence and uniqueness are proved (§*Existence and Uniqueness*), the group of units and its maximal compact subgroup are described (§*The Group of Units and the Unitary Group*), the two real halves are distinguished (§*The Two Halves*), the matrix picture is given (§*The Matrix Picture*), the algorithm is stated (§*The Algorithm*), one element is computed in full (§*Worked Example*), and the article closes with the summary and the notation.

The conventions and the symbols are those of *The Four Forms and the Four Algebraic Norms*, *Norm and Invertibility in the General Quaternionic Algebra*, *The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone* and *Conventions in Mathematics*; the symbols are collected in §*Summary of Notation*. The word is written with the plain product, the only associative product of the twelve of *Symmetric and Antisymmetric Decomposition of the Four General Products*, and the matrix model is $M_2(\mathbb C)$ of *Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb C)$ of Biquaternions*.

Every numerical value displayed below was recomputed in double precision.

## The Two Factors

### The Biquaternion Norm and the Modulus

The biquaternion norm of $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, with $Q_\mu\in\mathbb C$, is

$$
\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\tilde Q^{\natural}\tilde Q=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2}.
$$

It is the diagonal of the general quaternionic bilinear form, the algebraic norm of the plain product in the classification of *The Four Forms and the Four Algebraic Norms*, and under the matrix model it is the determinant,

$$
\det M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}.
$$

It is central, complex valued and multiplicative,

$$
\langle\tilde Q_1\tilde Q_2\rangle_{\natural}=\langle\tilde Q_1\rangle_{\natural}\langle\tilde Q_2\rangle_{\natural},
$$

and it vanishes on the **zero-divisor cone**: an element is invertible exactly when $\langle\tilde Q\rangle_{\natural}\neq0$ (*Norm and Invertibility in the General Quaternionic Algebra*). The cone is one complex equation, hence two real equations, of real codimension two; it is not the vanishing set of a definite form, and it is the boundary of the group of units.

The **modulus** is a square root of the norm,

$$
\Rho^{2}=\langle\tilde Q\rangle_{\natural}.
$$

Two roots differ by a sign, so the modulus is not defined by the norm alone. The branch is fixed once and for all. With $a=\operatorname{Re}\langle\tilde Q\rangle_{\natural}$ and $b=\operatorname{Im}\langle\tilde Q\rangle_{\natural}$, put

$$
\Rho=\sqrt{\frac{\lvert\langle\tilde Q\rangle_{\natural}\rvert+a}{2}}+i\,\operatorname{sgn}(b)\sqrt{\frac{\lvert\langle\tilde Q\rangle_{\natural}\rvert-a}{2}},\qquad \operatorname{sgn}(0)=+1,
$$

the sign convention at $b=0$ placing a negative real norm on the positive imaginary axis. The root so defined lies in the **principal half-plane**

$$
\mathcal H=\{\Rho\in\mathbb C:\operatorname{Re}\Rho>0\}\cup\{it:t>0\},
$$

and the other root $-\Rho$ lies outside it. On $\mathcal H$ the root is a function of the norm and is unique; it is continuous away from the negative real axis, where the branch cut lies, and it is the only convention of the decomposition.

The **scale** and the **central phase** are the polar coordinates of the modulus on $\mathcal H$,

$$
r=\lvert\Rho\rvert=\sqrt{\lvert\langle\tilde Q\rangle_{\natural}\rvert},\qquad \zeta=\frac{\Rho}{\lvert\Rho\rvert}.
$$

The scale is a positive real and the phase is a unit complex number in the half of the circle cut by $\mathcal H$,

$$
\zeta\in\{\zeta\in\mathbb C:\lvert\zeta\rvert=1,\ \operatorname{Re}\zeta>0\}\cup\{i\}.
$$

The phase takes the value $1$ on the positive real axis and $i$ on the positive imaginary axis, and it never takes the value $-1$ or $-i$: the phase ranges over the open right semicircle together with $i$, and $-i$ is the open end of the cut.

### The Unit Factor and the Norm-One Group

The **unit factor** is

$$
\tilde U=\frac{\tilde Q}{\Rho}=\frac{\tilde Q}{\sqrt{\langle\tilde Q\rangle_{\natural}}}.
$$

It satisfies $\langle\tilde U\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}/\Rho^{2}=1$, so it lies on the **norm-one set**

$$
\mathbb B^{\times}_{1}=\{\tilde U\in\mathbb B:\langle\tilde U\rangle_{\natural}=1\}.
$$

The set is a group. If $\langle\tilde U_1\rangle_{\natural}=\langle\tilde U_2\rangle_{\natural}=1$ then multiplicativity gives $\langle\tilde U_1\tilde U_2\rangle_{\natural}=1$, and the inverse of a norm-one element is its conjugate, $\tilde U^{-1}=\tilde U^{\natural}$, because $\tilde U\tilde U^{\natural}=1$. Under the matrix model the norm is the determinant, so the group is the special linear group,

$$
\boxed{\; \mathbb B^{\times}_{1}\cong SL_2(\mathbb C) \;},
$$

of complex dimension three and real dimension six (*The Group of Units of the Biquaternion Algebra and the Complement of the Zero-Divisor Cone*).

The norm-one group is not compact. It contains the Hermitian positive elements of determinant one, and those are unbounded: the element $c\,e_t+i\sqrt{c^{2}-1}\,\vec e_x$ has norm one for every $c\ge1$. This is the sharpest difference from the quaternion case, where the norm-one set is the sphere $S^3$, compact and of real dimension three. The biquaternion unit factor has three compact directions and three non-compact ones, and the split into boost and rotor separates them.

The phrase **unit factor** names the norm-one elements. It is not the **group of units** $\mathbb B^{\times}$, which is the wider set of invertible elements; the two senses of the word *unit* are kept apart throughout, as in *Conventions in Mathematics*, §*The Unitary Convention*. In the biquaternion algebra the two sets differ: $\mathbb B^{\times}=\mathbb B\setminus\mathcal N$ is the complement of the cone, of real dimension eight, and $\mathbb B^{\times}_{1}$ is a hypersurface inside it, of real dimension six.

### The Count of the Parameters

A biquaternion carries eight real parameters. The modulus carries two, the scale and the phase. The unit factor is constrained by the single complex equation $\langle\tilde U\rangle_{\natural}=1$ on the eight parameters of $\mathbb B$, so it retains six real degrees of freedom. The counts add:

$$
8=2+6 .
$$

The six split again. The boost is constrained by $\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*}$ and $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$: Hermitian elements form a real subspace of dimension four, positivity is an open condition, and the determinant condition removes one dimension, so the boost has three. The rotor is constrained by $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$ and by the reality of its coefficients, which is the unitary group of determinant one, of real dimension three. Thus

$$
\boxed{\; 8=1+1+3+3 \;}.
$$

The first two are the scale and the phase, the last two the boost and the rotor. No coordinate on either three-dimensional factor has been chosen: the boost is a hyperbolic space and the rotor is the sphere $S^3$, and a chart of either is a separate question.

## The Four Factors

The word is

$$
\tilde Q=r\,\zeta\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

and the following table records the four factors once. The columns give the value, the equation that defines it from $\tilde Q$, its real dimension, the action by which it acts on the algebra, and the subspaces it preserves. The action column follows the convention of *The Action of the Polar Decomposition on the Hermitian and Anti-Hermitian Subspaces*: the sandwich by the factor in view, except for the central phase, whose sandwich is the identity and whose action is therefore recorded as central multiplication.

| # | factor | name | value | defining equation | real dimension | action | stable subspaces |
|---|---|---|---|---|---|---|---|
| 1 | $r$ | scale | $\mathbb R_{>0}$ | $r=\lvert\Rho\rvert$, $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$ | $1$ | $\tilde Q\mapsto r^{2}\tilde Q$ | $\mathbb C_{\mathbb B}$, $\mathrm{Vect}(\mathbb B)$, $\mathbb H_{\mathbb B}$, $i\mathbb H_{\mathbb B}$, $\mathbb M_+$, $\mathbb M_-$ |
| 2 | $\zeta$ | central phase | $\{\lvert\zeta\rvert=1,\operatorname{Re}\zeta>0\}\cup\{i\}$ | $\zeta=\Rho/\lvert\Rho\rvert$ | $1$ | $\tilde Q\mapsto\zeta\tilde Q$ | $\mathbb C_{\mathbb B}$, $\mathrm{Vect}(\mathbb B)$ |
| 3 | $\tilde U_{\mathrm b}$ | boost | $\tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*}$, $\tilde U_{\mathrm b}>0$, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$ | $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$ | $3$ | $\tilde Q\mapsto\tilde U_{\mathrm b}\tilde Q\tilde U_{\mathrm b}^{*}$ | $\mathbb M_+$, $\mathbb M_-$ |
| 4 | $\tilde u_{\mathrm r}$ | rotor | $SU(2)$, the unit real quaternions | $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ | $3$ | $\tilde Q\mapsto\tilde u_{\mathrm r}\tilde Q\tilde u_{\mathrm r}^{-1}$ | $\mathbb C_{\mathbb B}$, $\mathrm{Vect}(\mathbb B)$, $\mathbb H_{\mathbb B}$, $i\mathbb H_{\mathbb B}$, $\mathbb M_+$, $\mathbb M_-$ |

The table is the biquaternion counterpart of the two-row table of *Modulus–Unit Polar Decomposition of Quaternions*: there the factors are the modulus and the rotor, here they are four, and the two extra rows are the ones the complex norm creates. The order of the last two is fixed in §*The Order of the Factors*.

### The Scale

The first factor is the positive real

$$
r=\lvert\Rho\rvert=\sqrt{\lvert\langle\tilde Q\rangle_{\natural}\rvert}.
$$

It is central and fixed by all four conjugations of the algebra: the quaternion conjugation, the coefficientwise conjugation, the Hermitian conjugation and its negative. It scales the element rigidly, since replacing $\tilde Q$ by $\lambda\tilde Q$ with $\lambda>0$ multiplies $r$ by $\lambda$ and leaves the other three factors unchanged. It is one exactly when $\lvert\langle\tilde Q\rangle_{\natural}\rvert=1$, that is, on the elements whose norm has unit modulus. These are the elements of the form $\zeta\tilde U$: the unit-norm elements times the unit circle of the centre.

The scale is the only factor written without a sign ambiguity. It is the modulus of the complex modulus, and it is the factor that survives unchanged in the quaternion case, where it is the whole modulus.

### The Central Phase

The second factor is the unit complex number

$$
\zeta=\frac{\Rho}{\lvert\Rho\rvert},\qquad \Rho^{2}=\langle\tilde Q\rangle_{\natural}.
$$

It is central, of real dimension one, and lies on the scalar line $\mathbb C_{\mathbb B}=\mathbb C e_t$. Being central, it commutes with the other three factors and may be moved through the word at no cost. It is the only factor that is both central and compact.

The phase records the direction of the norm, placed in the branch. Its two extremal values are the two halves of the algebra. On the real quaternion subspace $\mathbb H_{\mathbb B}$ the norm is a sum of four real squares, hence a positive real, and the phase is $1$. On the imaginary translate $i\mathbb H_{\mathbb B}$ the norm is the negative of a sum of four real squares, hence a negative real, and the phase is $i$. These are the two ends of the branch, and the values between them are attained by the elements that are in neither half.

Under the conjugations the phase is conjugated by the coefficientwise and the Hermitian conjugation, $\zeta\mapsto\bar\zeta$, and fixed by the quaternion conjugation, which acts on the coefficients of the quaternion factor and not on the central scalar. It is trivial exactly when the norm is a positive real, that is, when $\Rho$ is real positive.

### The Boost

The third factor is the **boost**

$$
\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2},\qquad \tilde U_{\mathrm b}^{2}=\tilde U\tilde U^{*},\qquad \tilde U_{\mathrm b}=\tilde U_{\mathrm b}^{*},\qquad \tilde U_{\mathrm b}>0 .
$$

The element $\tilde U\tilde U^{*}$ is Hermitian, because $(\tilde U\tilde U^{*})^{*}=\tilde U\tilde U^{*}$, and positive definite, because it is the product of an invertible element and its Hermitian conjugate. It has determinant one, since $\det(\tilde U\tilde U^{*})=\langle\tilde U\rangle_{\natural}\overline{\langle\tilde U\rangle_{\natural}}=1$; its unique Hermitian positive square root therefore also has determinant one, $\langle\tilde U_{\mathrm b}\rangle_{\natural}=1$. The boost is the Hermitian positive factor of the polar decomposition of the unit factor, taken on the left.

It is not compact. The set of Hermitian positive elements of determinant one is the hyperbolic space $H^{3}$, of real dimension three, and it is the non-compact half of the unit factor. Its elements are written

$$
\tilde U_{\mathrm b}=a\,e_t+i\vec w,\qquad a\in\mathbb R,\quad \vec w\in\mathbb R^{3},\quad a\ge1,\quad a^{2}-\lvert\vec w\rvert^{2}=1,
$$

with $a=\operatorname{Sc}\tilde U_{\mathrm b}$ and $\vec w$ the vector of the three coefficients of $i\vec e_k$. The scalar part is real and at least one, and the vector part is purely imaginary; the boost is the only factor whose coefficients are not all real and not all complex.

**Closed form.** The square root is computed without a spectral decomposition. Since $\tilde U\tilde U^{*}$ is Hermitian positive of determinant one, Cayley–Hamilton gives $(\tilde U\tilde U^{*})^{2}-2\operatorname{Sc}(\tilde U\tilde U^{*})\,\tilde U\tilde U^{*}+e_t=0$, and the root is

$$
\tilde U_{\mathrm b}=\frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2\bigl(1+\operatorname{Sc}(\tilde U\tilde U^{*})\bigr)}} .
$$

Its inverse, used below for the rotor, is

$$
\tilde U_{\mathrm b}^{-1}=\frac{\bigl(2\operatorname{Sc}(\tilde U\tilde U^{*})+1\bigr)e_t-\tilde U\tilde U^{*}}{\sqrt{2\bigl(1+\operatorname{Sc}(\tilde U\tilde U^{*})\bigr)}} .
$$

Both denominators are real and positive, because $\operatorname{Sc}(\tilde U\tilde U^{*})\ge1$ for a positive element of determinant one. The two formulas are the coordinate form of the boost, and they are the only place where the square root is evaluated in practice.

Under the quaternion and the coefficientwise conjugation the boost is replaced by its inverse, $\tilde U_{\mathrm b}\mapsto\tilde U_{\mathrm b}^{-1}$; under the Hermitian conjugation it is fixed, $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$. It is trivial exactly when $\tilde U\tilde U^{*}=e_t$, that is, when the unit factor is unitary and the element is $r\zeta\tilde u_{\mathrm r}$: a scale, a phase and a rotor, with no boost.

### The Rotor

The fourth factor is the **rotor**

$$
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U,\qquad \tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t,\qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

It is unitary, because $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=\tilde U_{\mathrm b}^{-1}\tilde U\tilde U^{*}\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{-1}\tilde U_{\mathrm b}^{2}\tilde U_{\mathrm b}^{-1}=e_t$, and it has determinant one, because $\det\tilde u_{\mathrm r}=\det\tilde U_{\mathrm b}^{-1}\det\tilde U=1$. Its coefficients are real. The unitary group of determinant one is $SU(2)$, and under the matrix model the real quaternions of norm one are exactly $SU(2)$:

$$
SU(2)=\{\tilde u\in\mathbb H_{\mathbb B}:\langle\tilde u\rangle_{\natural}=1\}=S^{3}.
$$

So the rotor is a unit real quaternion, and the name is the corpus's for a unit quaternion (*Conventions in Mathematics*, §*Symbols*). It is the compact factor of the unit factor, the three directions that remain bounded.

The rotor is the unitary factor of the polar decomposition of $\tilde U$,

$$
\tilde U=\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

and the reconstruction is the statement that the two polar decompositions of $\tilde U$, on the left and on the right, agree on the same pair. Under the quaternion conjugation the rotor is replaced by its inverse, $\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1}$; it is fixed by the coefficientwise conjugation, its coefficients being real; and the Hermitian conjugation, which is the coefficientwise conjugation after the quaternion one, also sends it to its inverse. It is trivial exactly when $\tilde U$ is Hermitian positive, that is, when the element is $r\zeta\tilde U_{\mathrm b}$: a scale, a phase and a boost, with no rotor.

**Closed form.** From the two displayed formulas,

$$
\tilde u_{\mathrm r}=\frac{\bigl(2\operatorname{Sc}(\tilde U\tilde U^{*})+1\bigr)e_t-\tilde U\tilde U^{*}}{\sqrt{2\bigl(1+\operatorname{Sc}(\tilde U\tilde U^{*})\bigr)}}\;\tilde U .
$$

The reality of the coefficients is not visible in this expression and is a consequence of the two polar decompositions; it is the statement that the unitary factor of an element of $SL_2(\mathbb C)$ lies in the compact real form $SU(2)$.

### The Order of the Factors

The scale and the phase are central and may be placed anywhere in the word. The boost and the rotor do not commute, and their order is part of the definition: the boost is the left Hermitian factor, so the word is boost then rotor, $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. The other order gives a different pair,

$$
\tilde u_{\mathrm r}\tilde U_{\mathrm b}=\bigl(\tilde u_{\mathrm r}\tilde U_{\mathrm b}\tilde u_{\mathrm r}^{-1}\bigr)\tilde u_{\mathrm r},
$$

in which the rotor conjugates the boost and the two factors are interchanged. The two words are equal exactly when the boost and the rotor commute, that is, when the rotor lies in the commutant of the boost. The order is recorded in the table and used throughout.

The word has one residual sign. Replacing $\Rho$ by $-\Rho$ leaves the scale and the boost unchanged and sends $\zeta\mapsto-\zeta$, $\tilde u_{\mathrm r}\mapsto-\tilde u_{\mathrm r}$; the product $\zeta\tilde u_{\mathrm r}$ is unchanged, so the four-factor word is the same element. The branch fixes $\Rho$ and therefore fixes the pair $(\zeta,\tilde u_{\mathrm r})$; without the branch the pair is defined only up to the simultaneous sign, which is the biquaternion analogue of the sign carried by the unit factor in the quaternion case.

## The Three Pairings

The four factors can be bracketed in three ways, and each bracketing is a **pairing**. The pairings regroup the same four factors; they differ in where the brackets fall and in what the bracketed pairs are recognised to be. Two are **partial**: a composite factor has to be built from a part of the element, and the construction can fail. The third is **total**.

### The Quaternion Pairing

The quaternion pairing joins the scale to the rotor and the phase to the boost:

$$
\tilde Q=\bigl(r\tilde u_{\mathrm r}\bigr)\bigl(\zeta\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr).
$$

The first factor is the real quaternion $r\tilde u_{\mathrm r}$, which is the modulus–unit form of an ordinary quaternion: a positive scale times a unit real quaternion. The second factor is the central phase times the boost carried into the rotor frame; its coefficients are complex in general. The pairing is partial: its construction from the element divides by the part of $\tilde Q$ whose four coefficients are real, so it is available only where that part is nonzero.

The two factors split the norm. The modulus carries the scale, $\langle\tilde q\rangle_{\natural}=r^{2}$; it is a real quaternion, fixed by complex conjugation. The second factor carries the phase, $\langle\zeta\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\rangle_{\natural}=\zeta^{2}$, of modulus one. The product is the norm of the element, $r^{2}\zeta^{2}=\Rho^{2}$. Since the modulus is invertible, the second factor is also the element divided on the left by it,

$$
\zeta\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde q^{-1}\tilde Q,
$$

and complex conjugation acts on it alone,

$$
\overline{\tilde Q}=\tilde q\,\zeta^{-1}\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}^{-1}\tilde u_{\mathrm r}.
$$

### The Hamilton Root Pairing

The Hamilton root pairing joins the scale to the phase and the boost to the rotor:

$$
\tilde Q=(r\zeta)(\tilde U_{\mathrm b}\tilde u_{\mathrm r}),\qquad r\zeta=\Rho.
$$

The first factor is the complex modulus $\Rho$. The second is read on the root of $-e_t$ parallel to the vector part. Writing $\tilde Q=Q_te_t+\vec Q$ with $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ and $B^2=Q_x^2+Q_y^2+Q_z^2$, the second factor is

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\cos\Theta+\vec U\sin\Theta,\qquad
\vec U=\frac{\vec Q}{B},\qquad
\cos\Theta=\frac{Q_t}{\Rho},\qquad
\sin\Theta=\frac{B}{\Rho}.
$$

The axis $\vec U$ is the root of $-e_t$ parallel to the vector part, $\vec U^{2}=-e_t$, so it is fixed by the vector part up to the sign of $B$. The pairing is partial: the normalisation divides by $B$, so the vector part must be non-null.

The first factor is central, so it commutes with the second, and the second is the unit factor itself, $\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q/\Rho$, of norm one. The whole norm is therefore carried by the first factor, $\langle\tilde Q\rangle_{\natural}=\Rho^{2}$. The vector part is the complex multiple of the axis and the scalar part the multiple of the cosine,

$$
\vec Q=B\vec U,\qquad Q_t=\Rho\cos\Theta,\qquad \vec Q^{2}=-B^{2}e_t,
$$

so the square of the vector part is a scalar, and $\cos^{2}\Theta+\sin^{2}\Theta=1$ is the norm identity $Q_t^{2}+B^{2}=\langle\tilde Q\rangle_{\natural}$.

### The Cartan Hermitian Pairing

The Cartan Hermitian pairing joins the scale to the boost and the phase to the rotor:

$$
\tilde Q=\tilde H\,(\zeta\tilde u_{\mathrm r}),\qquad \tilde H=r\tilde U_{\mathrm b}.
$$

The first factor is Hermitian positive and the second is unitary. The pairing solves $\tilde Q\tilde Q^{*}=\tilde H^{2}$, so $\tilde H=(\tilde Q\tilde Q^{*})^{1/2}$ and the second factor is $\tilde H^{-1}\tilde Q$: both are functions of the element alone. It is total on the invertible elements, and it is the algebra form of the matrix polar decomposition.

Each factor carries one part of the norm. The first is Hermitian, $\tilde H^{*}=\tilde H$, and its norm is the positive real $r^{2}$; the second is unitary, $(\zeta\tilde u_{\mathrm r})^{*}=(\zeta\tilde u_{\mathrm r})^{-1}$, and its norm is the unit complex $\zeta^{2}$; the product $r^{2}\zeta^{2}=\Rho^{2}$ is the splitting of the determinant in the matrix model. The first factor determines the scale and the boost without ambiguity, $r=\sqrt{\langle\tilde H\rangle_{\natural}}$ and $\tilde U_{\mathrm b}=\tilde H/r$; the second determines the phase as the principal square root of its norm, $\zeta^{2}=\langle\zeta\tilde u_{\mathrm r}\rangle_{\natural}$, and the rotor is the second factor divided by the phase.

The three pairings are collected in the table.

| pairing | first factor | second factor | available when |
|---|---|---|---|
| quaternion | $r\tilde u_{\mathrm r}$ | $\zeta\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and the part of $\tilde Q$ with real coefficients is nonzero |
| Hamilton root | $\Rho=r\zeta$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\langle\tilde Q\rangle_{\natural}\neq0$ and the vector part is non-null |
| Cartan Hermitian | $r\tilde U_{\mathrm b}$ | $\zeta\tilde u_{\mathrm r}$ | $\tilde Q$ is invertible |

The quaternion and Hamilton root domains are not nested, and the Cartan domain contains both. Within the Cartan domain, the elements outside both partial domains are the nonzero purely imaginary complex scalars.

## Existence and Uniqueness

**Theorem.** Every invertible biquaternion has exactly one modulus–unit polar decomposition with modulus in the principal half-plane, and exactly one four-factor word.

**Existence.** Let $\tilde Q$ be invertible, so $\langle\tilde Q\rangle_{\natural}\neq0$. Let $\Rho$ be the principal root of the norm and put $\tilde U=\tilde Q/\Rho$. Then $\Rho\neq0$, $\langle\tilde U\rangle_{\natural}=1$, and $\tilde Q=\Rho\tilde U$. Put $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$ and $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$. The first is Hermitian positive of determinant one, the second is unitary of determinant one with real coefficients, and $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. With $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$ the word follows.

**Uniqueness.** Suppose $\tilde Q=\Rho\tilde U=\Rho'\tilde U'$ with $\Rho,\Rho'\in\mathcal H$ and $\langle\tilde U\rangle_{\natural}=\langle\tilde U'\rangle_{\natural}=1$. Taking norms gives $\Rho^{2}=\Rho'^{2}$, so $\Rho'=\pm\Rho$; both lie in $\mathcal H$, which contains no pair of opposite points, so $\Rho'=\Rho$. Dividing, $\tilde U'=\tilde U$. The polar decomposition of $\tilde U$ is unique: $\tilde U\tilde U^{*}$ has exactly one Hermitian positive square root, hence $\tilde U_{\mathrm b}$ is unique, and then $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ is unique. The four factors follow from $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$.

**The domain.** The word exists exactly on the invertible elements. On the zero-divisor cone the norm vanishes, the modulus is zero, and no factorisation exists: the product of the four factors has norm $r^{2}\zeta^{2}=\Rho^{2}$, of modulus $r^{2}>0$, so it cannot vanish. The cone is the boundary of the domain and the only obstruction; the origin is on it, and the decomposition fails there with the rest.

**The generalized extension.** The word fails on the cone, but the two-factor Cartan form does not. *The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone* replaces the unitary factor by a partial isometry and the positive definite factor by a positive semidefinite one, and obtains a unique pair $\tilde Q=\tilde H\tilde U$ for every element, with $\tilde H=\sqrt{\tilde Q\tilde Q^{*}}$ and $\tilde U=\tilde H^{+}\tilde Q$. On the punctured cone the pair reads $\tilde Q=\sigma\tilde U$ and $\tilde H=\sigma\tilde U\tilde U^{*}$, with $\sigma=\lVert\tilde Q\rVert_{\mathrm F}$, so the positive factor is a scaled idempotent and the partial isometry is the normalised element. The extension does not produce a four-factor word, and it does not replace the word off the cone; it is the polar decomposition of the whole algebra, of which the word is the restriction to the group of units.

The uniqueness is a statement about the factors, not about a coordinate on the boost or on the rotor. Two different charts of $H^{3}$ assign different parameters to the same boost, and two different charts of $S^{3}$ assign different parameters to the same rotor; the factors themselves are fixed.

## The Group of Units and the Unitary Group

### The Splitting of the Group of Units

The group of units is $\mathbb B^{\times}=\mathbb B\setminus\mathcal N$, the complement of the zero-divisor cone. The decomposition read as a map

$$
\Phi:\mathbb B^{\times}\longrightarrow\mathcal H\times SL_2(\mathbb C),\qquad \Phi(\tilde Q)=(\Rho,\tilde U),
$$

is a bijection: it is injective by the uniqueness theorem, and it is surjective because for $(\Rho,\tilde U)\in\mathcal H\times SL_2(\mathbb C)$ the element $\Rho\tilde U$ has norm $\Rho^{2}$, whose principal root is $\Rho$. Under the matrix model it is the factorisation of an invertible matrix into a complex scalar and a matrix of determinant one.

The map is not a group homomorphism. The scale is multiplicative and the phase is multiplicative only up to a sign,

$$
r(\tilde Q_1\tilde Q_2)=r(\tilde Q_1)r(\tilde Q_2),\qquad \zeta(\tilde Q_1\tilde Q_2)=\varepsilon\,\zeta(\tilde Q_1)\zeta(\tilde Q_2),\qquad \varepsilon=\pm1,
$$

with $\varepsilon=-1$ exactly when the product $\Rho_1\Rho_2$ leaves the principal half-plane. The sign is central, so it can be absorbed by the phase or by the rotor. The product of two words is

$$
r_1r_2\,\varepsilon\,\zeta_1\zeta_2\;\tilde U_{\mathrm b,1}\,\tilde u_{\mathrm r,1}\,\tilde U_{\mathrm b,2}\,\tilde u_{\mathrm r,2},
$$

and the middle product $\tilde u_{\mathrm r,1}\tilde U_{\mathrm b,2}$ has to be split again, as a boost times a rotor, before the four factors are read. The factors multiply, but the parameters of the boost and of the rotor do not add. In the matrix model the group is $\mathbb B^{\times}\cong GL_2(\mathbb C)$ and the map $\Phi$ is the factorisation $GL_2(\mathbb C)\to\mathcal H\times SL_2(\mathbb C)$, which is a bijection of manifolds but not an isomorphism of groups.

### The Maximal Compact Subgroup

**Proposition.** The maximal compact subgroup of $\mathbb B^{\times}$ is the unitary group $U(2)$, and it is the set of words with $r=1$ and $\tilde U_{\mathrm b}=e_t$,

$$
U(2)=\{\zeta\,\tilde u_{\mathrm r}:\lvert\zeta\rvert=1,\ \tilde u_{\mathrm r}\in SU(2)\}.
$$

**Proof.** The compact part of the word is the phase times the rotor, and both are unitary, so their product is unitary; the scale and the boost are positive and non-compact. Conversely every unitary matrix of the algebra is of this form: if $V$ is unitary, then $\det V$ is a unit complex number, choose $\zeta$ in the branch with $\zeta^{2}=\det V$, and $K=\zeta^{-1}V$ is unitary of determinant one, hence a unit real quaternion. The map $(\zeta,K)\mapsto\zeta K$ is two-to-one, with $(\zeta,K)$ and $(-\zeta,-K)$ giving the same unitary, so

$$
\boxed{\; U(2)\cong\bigl(S^{1}\times SU(2)\bigr)/\{\pm1\} \;}.
$$

Any compact subgroup of $\mathbb B^{\times}$ has a bounded scale, hence scale one, and a bounded boost. The boost is trivial on a compact subgroup: if $\tilde U_{\mathrm b}\neq e_t$ has eigenvalue $\lambda\neq1$, the powers $\tilde U_{\mathrm b}^{n}$ have eigenvalue $\lambda^{n}$, which is unbounded or tends to zero, so the subgroup generated by $\tilde U_{\mathrm b}$ is not compact. Hence a compact subgroup lies in $U(2)$, which is compact, and $U(2)$ is maximal compact.

**The retraction.** The group retracts onto $U(2)$ by

$$
r_t=(1-t)r+t,\qquad \tilde U_{\mathrm b}(t)=\frac{(1-t)\tilde U_{\mathrm b}+t\,e_t}{\sqrt{\bigl\langle (1-t)\tilde U_{\mathrm b}+t\,e_t\bigr\rangle_{\natural}}},\qquad \zeta_t=\zeta,\qquad \tilde u_{\mathrm r}(t)=\tilde u_{\mathrm r},
$$

for $t\in[0,1]$. The denominator is real and positive, the path stays Hermitian positive of determinant one, and at $t=1$ the boost is $e_t$ and the scale is one. So $U(2)$ is a deformation retract of the group. In particular $\mathbb B^{\times}$ is connected, and its fundamental group is that of $U(2)$, namely $\mathbb Z$, generated by the loop of the central phase around the cone (*The Biquaternion Unit Group as a Topological Group*). The rotor contributes the simply connected compact factor $SU(2)=S^{3}$, so the fundamental group of the group of units is carried by the phase alone.

### The Two Circles

The compact part has two circular directions: one is the central phase, the other is the circle inside the rotor. They are not interchangeable. The central phase is central and acts on the whole algebra by multiplication; the circle inside the rotor is a one-parameter subgroup of $SU(2)$ and acts by conjugation, fixing the scalar line and acting on the vector part. The first is the direction that produces the fundamental group of the group of units; the second lies in the simply connected sphere and contributes no loop.

This is the exact biquaternion counterpart of the absence of a second continuous factor in the quaternion case. There the sphere is simple modulo its centre, and the only factor beyond it is the scale line. Here the unit fibre is $SL_2(\mathbb C)$, whose compact part is $SU(2)$, and the extra compact direction is the centre of the algebra, not a factor of the sphere. The scale line and the phase circle are the two directions of the complex modulus.

## The Two Halves

### The Real Quaternion Subspace and Its Imaginary Translate

Every biquaternion is written uniquely as a real quaternion plus $i$ times a real quaternion,

$$
\tilde Q=\tilde q+i\tilde p,\qquad \tilde q,\tilde p\in\mathbb H_{\mathbb B},\qquad \mathbb B=\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B},
$$

where $\mathbb H_{\mathbb B}$ is the real span of $e_t,\vec e_x,\vec e_y,\vec e_z$ and $i$ is the central scalar imaginary. The two summands are real vector spaces of dimension four. This is the biquaternion analogue of the scalar–vector split of the quaternion case, and it is the split in which the indefiniteness of the norm is visible.

On the two halves the norm reads

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde q\rangle_{\natural}-\langle\tilde p\rangle_{\natural}+2i\,\langle\tilde q,\tilde p\rangle,
$$

with $\langle\tilde q\rangle_{\natural}=\sum_\mu q_\mu^{2}$ the real quaternion norm and $\langle\tilde q,\tilde p\rangle=\operatorname{Sc}(\tilde q^{\natural}\tilde p)$ the Euclidean inner product of $\mathbb R^{4}$. The real part is the difference of the two squared lengths and the imaginary part is twice their inner product. The norm therefore vanishes exactly when the two halves have equal length and are orthogonal: two real equations on eight parameters, a cone of real codimension two.

### Where the Factors Lie

The four factors distribute over the two halves as follows. The scale is a real scalar and lies in the first half. The phase is a complex scalar: it is $1$ or $i$ on the two halves and a genuine complex number between them. The rotor is a real quaternion and lies in the first half. The boost has its scalar part in the first half and its vector part in the second,

$$
\tilde U_{\mathrm b}=a\,e_t+i\vec w,\qquad a\in\mathbb R,\quad \vec w\in\mathbb R^{3},\qquad a^{2}-\lvert\vec w\rvert^{2}=1 .
$$

So the boost is the only factor that uses both halves, and it is the factor that carries the indefiniteness: its scalar part is at least one and its vector part is tied to it by the determinant condition. The boost is trivial exactly when the unit factor is unitary, that is, on the elements $r\zeta\tilde u_{\mathrm r}$; in particular it is trivial on both halves.

This is the precise sense in which the biquaternion case is the complexification of the quaternion one. The rotor, the scale and the trivial phase are the quaternion decomposition; the phase circle and the boost are the two directions added by the complex scalars, one compact and one not.

## The Matrix Picture

### The Embedding in M_2(C)

The algebra is isomorphic to the complex matrix algebra,

$$
M_2:\mathbb B\longrightarrow M_2(\mathbb C),\qquad M_2(e_t)=I,\qquad M_2(\vec e_k)=-i\sigma_k,
$$

with $\sigma_k$ the Pauli matrices, and the isomorphism is one of complex algebras, not only of real ones (*Introduction to the 2×2 Matrix Element Representation $M_2(\mathbb C)$ of Biquaternions*). Two identities hold. The determinant is the biquaternion norm,

$$
\det M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural},
$$

and the norm-one group is the special linear group,

$$
M_2(\mathbb B^{\times}_{1})=SL_2(\mathbb C).
$$

### The Matrix of the Word

Let $M=M_2(\tilde Q)$, $M_{\mathrm b}=M_2(\tilde U_{\mathrm b})$ and $M_{\mathrm r}=M_2(\tilde u_{\mathrm r})$. The word becomes

$$
M=r\,\zeta\,M_{\mathrm b}\,M_{\mathrm r},\qquad M_{\mathrm b}=M_{\mathrm b}^{\dagger},\quad M_{\mathrm b}>0,\quad \det M_{\mathrm b}=1,\quad M_{\mathrm r}\in SU(2).
$$

The matrix polar decomposition of $M$ groups the four factors into two:

$$
\boxed{\; M=P\,V,\qquad P=(MM^{\dagger})^{1/2}=r\,M_{\mathrm b},\qquad V=\zeta\,M_{\mathrm r} \;}.
$$

The positive factor is the scale times the boost, Hermitian positive of determinant $r^{2}$; the unitary factor is the phase times the rotor, unitary of determinant $\zeta^{2}$. The matrix decomposition does not see the split of $P$ into scale and boost, nor that of $V$ into phase and rotor; those splits use the fact that $P$ is a positive real multiple of an element of the algebra with determinant one, and that $V$ is a unit complex multiple of a real quaternion.

| factor | matrix | determinant | action |
|---|---|---|---|
| scale | $rI$, $r>0$ | $r^{2}$ | dilation of ratio $r$ |
| central phase | $\zeta I$, $\lvert\zeta\rvert=1$ | $\zeta^{2}$ | central multiplication |
| boost | $M_{\mathrm b}$, Hermitian positive | $1$ | congruence $X\mapsto M_{\mathrm b}XM_{\mathrm b}^{\dagger}$ |
| rotor | $M_{\mathrm r}\in SU(2)$ | $1$ | conjugation $X\mapsto M_{\mathrm r}XM_{\mathrm r}^{-1}$ |
| $\tilde Q$ | $M$ | $\Rho^{2}$ | — |

The table is the matrix counterpart of the four-factor table of §*The Four Factors*, and the two rows that the matrix polar decomposition merges are the two pairs that the algebra distinguishes.

## The Algorithm

The factors are computed in five steps, each a finite sequence of algebraic operations on the eight real coordinates of $\tilde Q$.

**Step 1, the norm.** Compute $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$. If it is zero, stop: the element is a zero divisor and has no decomposition. Otherwise continue.

**Step 2, the modulus.** Compute $\Rho$ from the branch formula of §*The Biquaternion Norm and the Modulus*. The result lies in $\mathcal H$ and satisfies $\Rho^{2}=\langle\tilde Q\rangle_{\natural}$.

**Step 3, the scale and the phase.** Put $r=\lvert\Rho\rvert$ and $\zeta=\Rho/r$. Then $r>0$, $\lvert\zeta\rvert=1$, and $\Rho=r\zeta$.

**Step 4, the unit factor.** Put $\tilde U=\tilde Q/\Rho$. Check $\langle\tilde U\rangle_{\natural}=1$; the check is the identity $\langle\tilde Q\rangle_{\natural}/\Rho^{2}=1$.

**Step 5, the boost and the rotor.** Compute $\tilde U\tilde U^{*}$, then

$$
\tilde U_{\mathrm b}=\frac{\tilde U\tilde U^{*}+e_t}{\sqrt{2\bigl(1+\operatorname{Sc}(\tilde U\tilde U^{*})\bigr)}},\qquad
\tilde u_{\mathrm r}=\frac{\bigl(2\operatorname{Sc}(\tilde U\tilde U^{*})+1\bigr)e_t-\tilde U\tilde U^{*}}{\sqrt{2\bigl(1+\operatorname{Sc}(\tilde U\tilde U^{*})\bigr)}}\;\tilde U .
$$

The scalar $\operatorname{Sc}(\tilde U\tilde U^{*})$ is real and at least one, so the two denominators are real and positive. The five steps use one square root of a complex number, one square root of a real number and no spectral decomposition.

**The checks.** Three identities close the computation: $\tilde U_{\mathrm b}^{2}=\tilde U\tilde U^{*}$, $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, and $r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q$. The first is the definition of the root, the second is the unitarity of the rotor, and the third is the word. A computation that passes the three has the four factors right.

## Worked Example

### An Element with a Complex Norm

Take

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y .
$$

The norm is

$$
\langle\tilde Q\rangle_{\natural}=(1+i)^{2}+1+i^{2}=2i+1-1=2i,
$$

so the element is invertible and the branch is not on the cut. The modulus is the principal root of $2i$,

$$
\Rho=1+i,\qquad r=\sqrt{2}=1.4142135624,\qquad \zeta=\frac{1+i}{\sqrt{2}}=0.7071067812+0.7071067812\,i .
$$

The unit factor is

$$
\tilde U=\frac{\tilde Q}{1+i}=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
$$

with norm one. The Hermitian element is

$$
\tilde U\tilde U^{*}=2e_t-i\vec e_x+i\vec e_y+i\vec e_z,\qquad \operatorname{Sc}(\tilde U\tilde U^{*})=2,\qquad \sqrt{2(1+2)}=\sqrt{6},
$$

and the two remaining factors are

$$
\tilde U_{\mathrm b}=\frac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt{6}},\qquad
\tilde u_{\mathrm r}=\sqrt{\frac{2}{3}}\,e_t+\frac{1}{\sqrt{6}}\vec e_x+\frac{1}{\sqrt{6}}\vec e_y .
$$

The factors are collected in the table.

| factor | value | norm |
|---|---|---|
| $r$ | $\sqrt{2}$ | — |
| $\zeta$ | $\dfrac{1+i}{\sqrt{2}}$ | $1$ |
| $\tilde U_{\mathrm b}$ | $\dfrac{3e_t-i\vec e_x+i\vec e_y+i\vec e_z}{\sqrt{6}}$ | $1$ |
| $\tilde u_{\mathrm r}$ | $\sqrt{\dfrac{2}{3}}\,e_t+\dfrac{1}{\sqrt{6}}\vec e_x+\dfrac{1}{\sqrt{6}}\vec e_y$ | $1$ |

### The Checks

The boost is Hermitian and its square is the Hermitian element: $\tilde U_{\mathrm b}^{2}=2e_t-i\vec e_x+i\vec e_y+i\vec e_z$. The rotor is real and unitary: $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^{*}=e_t$, and its coefficients are real. The word reconstructs the element,

$$
r\zeta\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}=(1+i)\,\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q,
$$

and the double-precision error is zero in each of the four coefficients. The phase lies in the branch, since $\operatorname{Re}\zeta>0$; the scale is $\sqrt{2}$ and the element has norm of modulus $2$, as it must.

The example is generic enough to exhibit all four factors: the boost is not trivial, because $\tilde U\tilde U^{*}\neq e_t$; the rotor is not trivial, because $\tilde U$ is not Hermitian; and the phase is neither $1$ nor $i$, because the element is in neither real half.

## Summary

Every invertible biquaternion has exactly one modulus–unit polar decomposition $\tilde Q=\Rho\tilde U$ with modulus in the principal half-plane and unit factor of norm one, and exactly one four-factor word $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$. The scale is positive, the phase is a unit complex number in the right half of the circle, the boost is Hermitian positive of determinant one, and the rotor is a unit real quaternion. The dimensions are $1+1+3+3=8$.

The modulus is complex because the norm is complex; it is the determinant in the matrix model. The unit factor is the norm-one group $SL_2(\mathbb C)$, of real dimension six and not compact; its compact part is the rotor, and its non-compact part is the boost. The decomposition exists exactly on the complement of the zero-divisor cone, a cone of real codimension two.

The group of units is $\mathbb B^{\times}\cong GL_2(\mathbb C)$. The map $\tilde Q\mapsto(\Rho,\tilde U)$ is a bijection onto $\mathcal H\times SL_2(\mathbb C)$ but not a group homomorphism: the phase is multiplicative only up to the sign that the branch forces, and that sign is absorbed by the simultaneous sign of the phase and the rotor. The maximal compact subgroup is $U(2)$, the set of words with unit scale and trivial boost, and it is a deformation retract of the group; its fundamental group is $\mathbb Z$.

The four factors regroup into the three pairings: the quaternion pairing, which joins the scale to the rotor; the Hamilton root pairing, which joins the scale to the phase and reads the rest on a root of $-e_t$; and the Cartan Hermitian pairing, which joins the scale to the boost and the phase to the rotor. The first two are partial, the third is total.

In the matrix picture the four factors group into the positive factor $rM_{\mathrm b}$ and the unitary factor $\zeta M_{\mathrm r}$ of the polar decomposition of $M_2(\tilde Q)$. The algebra sees the finer split; the matrix decomposition does not.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb B=\mathbb C\otimes_{\mathbb R}\mathbb H$ | the biquaternion algebra, basis $e_t,\vec e_x,\vec e_y,\vec e_z$, central $i$ |
| $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ | a biquaternion, $Q_\mu\in\mathbb C$ |
| $\vec Q=Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$, $B^2=Q_x^2+Q_y^2+Q_z^2$ | the vector part and the squared vector part |
| $\vec U=\vec Q/B$, $\Theta$ | the Hamilton axis, the root of $-e_t$ parallel to the vector part, and the complex angle of the Hamilton root pairing |
| $\tilde Q^{\natural}=Q_te_t-Q_x\vec e_x-Q_y\vec e_y-Q_z\vec e_z$ | the quaternion conjugation |
| $\tilde Q^{*}=\overline{\tilde Q^{\natural}}$ | the Hermitian conjugation |
| $\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}=\tilde Q\tilde Q^{\natural}$ | the biquaternion norm, complex valued, multiplicative |
| $\mathcal N=\{\langle\tilde Q\rangle_{\natural}=0\}$ | the zero-divisor cone, of real codimension two |
| $\Rho$ | the modulus, the principal square root of the norm, in $\mathcal H$ |
| $\mathcal H=\{\operatorname{Re}\Rho>0\}\cup\{it:t>0\}$ | the principal half-plane of the modulus |
| $r=\lvert\Rho\rvert$ | the scale, a positive real |
| $\zeta=\Rho/r$ | the central phase, $\lvert\zeta\rvert=1$ |
| $\tilde U=\tilde Q/\Rho$ | the unit factor, $\langle\tilde U\rangle_{\natural}=1$ |
| $\mathbb B^{\times}_{1}=\{\langle\tilde U\rangle_{\natural}=1\}\cong SL_2(\mathbb C)$ | the norm-one group, of real dimension six |
| $\tilde U_{\mathrm b}=(\tilde U\tilde U^{*})^{1/2}$ | the boost, Hermitian positive of determinant one |
| $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ | the rotor, a unit real quaternion, $SU(2)=S^{3}$ |
| $\tilde q=r\tilde u_{\mathrm r}$ | the quaternion modulus, a real quaternion, first factor of the quaternion pairing |
| $\tilde H=r\tilde U_{\mathrm b}$ | the Hermitian positive factor, first factor of the Cartan Hermitian pairing |
| $\mathbb M_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}$ | the Hermitian and anti-Hermitian subspaces |
| $\mathbb H_{\mathbb B}$ | the real quaternion subspace, $\mathbb B=\mathbb H_{\mathbb B}\oplus i\mathbb H_{\mathbb B}$ |
| $\mathbb C_{\mathbb B}=\mathbb C e_t$ | the central scalar line |
| $\mathrm{Vect}(\mathbb B)$ | the elements of vanishing scalar part |
| $\mathbb B^{\times}\cong GL_2(\mathbb C)$ | the group of units |
| $U(2)=\{\zeta\tilde u_{\mathrm r}\}$ | the maximal compact subgroup |
| $M_2$ | the isomorphism $\mathbb B\to M_2(\mathbb C)$, $M_2(\vec e_k)=-i\sigma_k$ |

## Further Reading

- Roger A. Horn and Charles R. Johnson, *Matrix Analysis* (Cambridge University Press, 1985), for the polar decomposition of an invertible matrix, the positive square root and the unitary group.
- J. P. Ward, *Quaternions and Cayley Numbers* (Kluwer, 1997), for the biquaternion algebra, its matrix models and its conjugations.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge University Press, 2nd edition 2001), for the quaternion unit sphere, the complexification and the unitary groups.
- John Stillwell, *Naive Lie Theory* (Springer, 2008), for $SU(2)$, $U(2)$ and the Cartan decomposition of $SL_2(\mathbb C)$.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), the companion that reads the same four factors as exponentials, with the two logarithms, the kernel and the closed forms of the boost and of the rotor, and with the boundary of the word: the null cone, the minimal idempotents and the boundary limits.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html), the grouping of the scale with the rotor.
- [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), the grouping of the scale with the phase, read on a root of $-e_t$.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), the grouping of the scale with the boost and the phase with the rotor.
- [The Generalized Polar Decomposition of a Biquaternion: Partial Isometries and the Null Cone](the-general-polar-decomposition-of-a-biquaternion-partial-isometries-and-the-null-cone.html), the extension of the two-factor Cartan form to the whole algebra, with the positive semidefinite factor, the partial isometry and the rank-one reading of the cone.
