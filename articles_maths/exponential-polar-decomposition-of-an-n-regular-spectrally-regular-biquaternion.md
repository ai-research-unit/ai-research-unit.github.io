# __Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion__

## Introduction

This article computes the exponential polar decomposition of a biquaternion that is N-regular and spectrally regular, that is, one with

$$
\langle\tilde Q\rangle_{\natural}\neq0,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2\neq0.
$$

The word is the four-factor product

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and two real unit axes. Every element of the sector has one, and it is unique up to the usual degeneracies of the axes. The article proves this from the Cartan decomposition, computes the closed forms, and reads the word against the spectral decomposition.

The spectral reading is the subject that distinguishes this article from the general theory. The element has two distinct eigenvalues $\lambda_\pm=Q_t\pm iB$ and an eigenbasis. The unit factor is diagonal in that basis, with eigenvalues $\mu_\pm=\lambda_\pm/\Rho$. The polar factors are diagonal in the same basis exactly when the element is normal, and that is exactly the case in which the two axes are parallel and the word collapses to a single exponential. In the general, non-normal case the eigenbasis is not a polar basis: the spectrum determines the two eigenvalues of the unit factor, but it does not determine the rapidity, the rotor angle or the axes. The worked examples show the gap numerically.

The companion article *Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion* treats the case $B^2=0$. The two articles are independent: each defines the word, proves existence and uniqueness, and develops the logarithm and the group law. This article does not use the companion, and the companion does not use this one. The boundary of the sector has two pieces: the null cone $\langle\tilde Q\rangle_{\natural}=0$, where the modulus vanishes, and the spectral cone $B^2=0$, where the eigenbasis degenerates while the word remains finite. The second piece is the doorway to the companion, and it is treated in §*The Two Walls*.

The article assumes *The Polar Decomposition of a N-Regular Biquaternion* for the modulus–unit theorem, *Biquaternion Elementary Functions* for the exponential and the logarithm, and *The Eigenbasis of a Spectrally Regular Biquaternion* for the eigenbasis. It does not treat the Peirce decomposition, the spinors or the spectral algebra of the sector; those are in the articles cited. The numerical cases are in *Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion*.

**The plan.** The word, its two unit factors and the seven data are boxed and proved in §*The Result in Terms of the Coordinates*. The domain is fixed in §*The Domain*. The word and its component form are stated in §*The Decomposition*. The spectral reading occupies §*The Spectral Reading*, with the eigenbasis, the normal case and the non-normal case. Existence and uniqueness are proved in §*Existence and Uniqueness*. The logarithm, the group law, the matrix picture and the exponential coordinates follow. §*The Two Walls* treats the boundary. The summary collects the formulas and the comparison between the polar and the spectral data.


## The Result in Terms of the Coordinates

**Setting.** Let $\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z$ with complex coordinates, and put

$$
N=Q_t^2+Q_x^2+Q_y^2+Q_z^2,\qquad
B^2=Q_x^2+Q_y^2+Q_z^2,\qquad
\lVert\tilde Q\rVert_E^2=|Q_t|^2+|Q_x|^2+|Q_y|^2+|Q_z|^2.
$$

On the sector $N\neq0$ and $B^2\neq0$. Here $\operatorname{Arg}$ is the principal argument in $(-\pi,\pi]$, $\lVert\cdot\rVert$ is the Euclidean norm of a real three-vector, $\operatorname{Im}$ acts componentwise, and $(j,k,l)$ is a cyclic permutation of $(x,y,z)$.

**Theorem (the word and its seven data).** Every $\tilde Q$ of the sector is

$$
\boxed{\;\tilde Q=r e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)\;}
$$

with the two unit factors

$$
\boxed{\;\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}\;}
$$

and with the seven data determined by $Q_t,Q_x,Q_y,Q_z$. Write $\vec Q=(Q_x,Q_y,Q_z)$.

$$
\boxed{\;r=\sqrt{|N|},\qquad \Rho=r e^{i\alpha}\;}
$$

$$
\boxed{\;\alpha=\frac12\operatorname{Arg}N\;}
$$

$$
\boxed{\;\cosh\psi=\frac{\lVert\tilde Q\rVert_E^2}{|N|},\qquad \psi=\operatorname{arcosh}\frac{\lVert\tilde Q\rVert_E^2}{|N|}\;}
$$

$$
\boxed{\;C=\sqrt{\frac{\lVert\tilde Q\rVert_E^2+|N|}{2}},\qquad S=\sqrt{\frac{\lVert\tilde Q\rVert_E^2-|N|}{2}},\qquad \cosh\frac{\psi}{2}=\frac{C}{\sqrt{|N|}},\qquad \sinh\frac{\psi}{2}=\frac{S}{\sqrt{|N|}}\;}
$$

$$
\boxed{\;a_j=\frac{2}{|N|}\Bigl(\operatorname{Im}\bigl(\bar Q_tQ_j\bigr)-\operatorname{Im}\bigl(Q_k\bar Q_l\bigr)\Bigr),\qquad \vec a=(a_x,a_y,a_z),\qquad \vec u_{\mathrm b}=\frac{\vec a}{\lVert\vec a\rVert}\;}
$$

$$
\boxed{\;\tilde U_{\mathrm b}=\frac{C\,e_t+iS\,\vec u_{\mathrm b}}{\sqrt{|N|}}
=\frac{\sqrt{\lVert\tilde Q\rVert_E^2+|N|}\;e_t+i\sqrt{\lVert\tilde Q\rVert_E^2-|N|}\;\vec u_{\mathrm b}}{\sqrt{2|N|}}\;}
$$

$$
\boxed{\;\tilde u_{\mathrm r}=\frac{e^{-i\alpha}}{|N|}\bigl(C-iS\,\vec u_{\mathrm b}\bigr)\tilde Q\;}
$$

$$
\boxed{\;\theta=2\arccos\frac{C\operatorname{Re}\bigl(e^{-i\alpha}Q_t\bigr)-S\operatorname{Im}\bigl(e^{-i\alpha}D\bigr)}{|N|},\qquad D=\vec u_{\mathrm b}\cdot\vec Q\;}
$$

$$
\boxed{\;\vec u_{\mathrm r}=\frac{e^{-i\alpha}\bigl(C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr)}{\bigl\lVert C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr\rVert}\;}
$$

The boost axis is undefined when $\psi=0$; the rotor axis is undefined when $\theta\in\{0,2\pi\}$. The vector $\mathrm{Vect}\tilde u_{\mathrm r}$ is the vector part of $\tilde u_{\mathrm r}$. At $\psi=0$ the boost is $e_t$, and the box for $\tilde u_{\mathrm r}$ reduces to $\tilde u_{\mathrm r}=\tilde Q/\Rho$.

*Proof.*

**The modulus.** By the modulus–unit theorem, $\Rho$ is the principal square root of $N$. Write $\Rho=re^{i\alpha}$ with $r>0$ and $\alpha\in(-\pi/2,\pi/2]$. Then $r^2=|\Rho|^2=|N|$ and $2\alpha\equiv\operatorname{Arg}N\pmod{2\pi}$. The range of $\alpha$ selects the representative, so $r=\sqrt{|N|}$ and $\alpha=\frac12\operatorname{Arg}N$.

**The product $\tilde Q\tilde Q^*$.** With $\tilde Q^*=\bar Q_t-\bar{\vec Q}$,

$$
\tilde Q\tilde Q^*
=(Q_t+\vec Q)(\bar Q_t-\bar{\vec Q})
=\bigl(|Q_t|^2+|\vec Q|^2\bigr)e_t+\bar Q_t\vec Q-Q_t\bar{\vec Q}-\vec Q\times\bar{\vec Q}.
$$

The scalar part is $\lVert\tilde Q\rVert_E^2=|Q_t|^2+|\vec Q|^2$. For pure quaternions $u,v$ one has $uv=-u\cdot v+u\times v$, with the bilinear dot product. Hence, componentwise,

$$
\bar Q_t\vec Q-Q_t\bar{\vec Q}=2i\operatorname{Im}\bigl(\bar Q_t\vec Q\bigr),
\qquad
\bigl(\vec Q\times\bar{\vec Q}\bigr)_j=2i\operatorname{Im}\bigl(Q_k\bar Q_l\bigr),
$$

and therefore

$$
\tilde Q\tilde Q^*=\lVert\tilde Q\rVert_E^2\,e_t+i|N|\vec a,
$$

with $\vec a$ the vector of the box.

**The boost.** The unit factor is $\tilde U=\tilde Q/\Rho$, so

$$
\tilde U\tilde U^*=\frac{\tilde Q\tilde Q^*}{|\Rho|^2}
=\frac{\lVert\tilde Q\rVert_E^2}{|N|}\,e_t+i\vec a.
$$

The word gives $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}$ unitary, hence

$$
\tilde U\tilde U^*=\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}^2.
$$

With $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ and $\vec u_{\mathrm b}^2=-1$,

$$
\tilde U_{\mathrm b}^2=\cosh\psi\,e_t+i\sinh\psi\,\vec u_{\mathrm b}.
$$

Comparing the scalar parts gives $\cosh\psi=\lVert\tilde Q\rVert_E^2/|N|$ and $\psi=\operatorname{arcosh}(\lVert\tilde Q\rVert_E^2/|N|)$; the argument is real because $\lVert\tilde Q\rVert_E^2\ge|N|$ by Cauchy–Schwarz. Comparing the vector parts gives $\sinh\psi\,\vec u_{\mathrm b}=\vec a$, hence $\vec u_{\mathrm b}=\vec a/\lVert\vec a\rVert$ when $\psi>0$. The box for $\tilde U_{\mathrm b}$ follows from $\cosh\frac{\psi}{2}=\sqrt{(\lVert\tilde Q\rVert_E^2+|N|)/(2|N|)}$ and $\sinh\frac{\psi}{2}=\sqrt{(\lVert\tilde Q\rVert_E^2-|N|)/(2|N|)}$.

**The rotor.** The boost is Hermitian of norm one, so $\tilde U_{\mathrm b}^{-1}=\tilde U_{\mathrm b}^{\natural}=\cosh\frac{\psi}{2}e_t-i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$. Therefore

$$
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U
=\frac{1}{\Rho}\Bigl(\cosh\frac{\psi}{2}e_t-i\sinh\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\tilde Q.
$$

Substituting the half-angle values, and using $\Rho=re^{i\alpha}$ and $r^2=|N|$, gives the box for $\tilde u_{\mathrm r}$.

**The angles.** By the existence theorem, $\tilde u_{\mathrm r}$ is a unit real quaternion. Write $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ with $\theta\in[0,2\pi]$, so $\operatorname{Sc}\tilde u_{\mathrm r}=\cos\frac{\theta}{2}$ and $\mathrm{Vect}\tilde u_{\mathrm r}=\sin\frac{\theta}{2}\vec u_{\mathrm r}$ with $\sin\frac{\theta}{2}\ge0$. For a real unit vector $u$ and a complex vector $\tilde V$ with scalar part $\tilde V_t$, one has $u\tilde V=\tilde V_tu-u\cdot\tilde V+u\times\tilde V$. Applying this to the box for $\tilde u_{\mathrm r}$ gives, with $D=\vec u_{\mathrm b}\cdot\vec Q$,

$$
\operatorname{Sc}\tilde u_{\mathrm r}=\frac{e^{-i\alpha}}{|N|}\bigl(CQ_t+iSD\bigr),
\qquad
\mathrm{Vect}\tilde u_{\mathrm r}=\frac{e^{-i\alpha}}{|N|}\bigl(C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\bigr).
$$

Taking the real part of the scalar part gives the box for $\theta$. Taking the norm of the vector part gives $\sin\frac{\theta}{2}=\lVert C\vec Q-iS(Q_t\vec u_{\mathrm b}+\vec u_{\mathrm b}\times\vec Q)\rVert/|N|$, and $\vec u_{\mathrm r}=\mathrm{Vect}\tilde u_{\mathrm r}/\sin\frac{\theta}{2}$ is the box for $\vec u_{\mathrm r}$.

**The assembly.** The boost box gives $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ and the rotor box gives $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$; their product is $\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde U=\tilde Q/\Rho$, which is the word. $\square$

**Check.** For

$$
\tilde Q=\Bigl(1-\frac{i}{2}\Bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z,
$$

one has $N=1$ and $\lVert\tilde Q\rVert_E^2=3$, hence $r=1$, $\alpha=0$, $\psi=1.762747174$, $\vec a=2\sqrt2\,\vec e_x$ and $\vec u_{\mathrm b}=\vec e_x$. The boxes give

$$
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x,
\qquad
\tilde u_{\mathrm r}=\frac{1}{\sqrt2}e_t+\frac12(\vec e_x+\vec e_y),
\qquad
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2}.
$$

## The Domain

### The Two Invariants

Let

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2.
$$

The number $N$ is the reduced product $\tilde Q\tilde Q^{\natural}$, and $B^2$ is the quadratic form of the vector part. The two are complex numbers. The **spectrally regular sector** is

$$
\Sigma_{11}=\{\tilde Q\in\mathbb{B}:\ N\neq0,\ B^2\neq0\}.
$$

The name is the one of *The Spectrum*: the element is N-regular when $N\neq0$, and spectrally regular when $B^2\neq0$. The two conditions are independent, and their four combinations are the four sectors of the algebra. This article treats the combination $11$; the companion treats $10$.

### Five Descriptions

The sector has five equivalent descriptions.

**Proposition (the descriptions of $\Sigma_{11}$).** For $\tilde Q\in\mathbb{B}$ the following are equivalent.

1. $N\neq0$ and $B^2\neq0$.
2. The two eigenvalues $\lambda_\pm=Q_t\pm iB$ are distinct and nonzero.
3. The minimal polynomial $X^2-2Q_tX+N$ is squarefree with nonzero constant term.
4. The element is a unit and its spectrum has two distinct points.
5. With $\Rho$ the principal square root of $N$ and $\tilde U=\tilde Q/\Rho$, the scalar part of $\tilde U$ is not $\pm1$.

*Proof.* The characteristic polynomial is $X^2-2Q_tX+N$. Its discriminant is $4(Q_t^2-N)=-4B^2$, so it is squarefree exactly when $B^2\neq0$, and its constant term is nonzero exactly when $N\neq0$. The eigenvalues are $Q_t\pm iB$, distinct and nonzero under the same two conditions. The element is a unit because $N\neq0$. A scalar has $B^2=0$, but $B^2=0$ also allows the non-scalar Jordan elements; the spectral condition is the distinctness, not the non-scalarity. For the last item, $\operatorname{Sc}\tilde U=Q_t/\Rho$, hence

$$
\bigl(\operatorname{Sc}\tilde U\bigr)^2=\frac{Q_t^2}{N},
\qquad
B^2=N-Q_t^2=N\Bigl(1-\bigl(\operatorname{Sc}\tilde U\bigr)^2\Bigr),
$$

so $B^2\neq0$ is equivalent to $\operatorname{Sc}\tilde U\notin\{1,-1\}$. $\square$

The last description is the one that separates this article from its companion: the two sectors are the two sides of the pair of hyperplanes $\operatorname{Sc}\tilde U=\pm1$ in the group of units.

### Geometry

The sector is the complement of the union $NB^2=0$ of the null cone and the spectral cone. It is open and dense in $\mathbb{B}$, of complex dimension $4$ and real dimension $8$. It is not a subgroup: $e_t$ has $B^2=0$ and lies outside, and the scalar line $\mathbb{C}^{\times}e_t$ lies entirely outside. It contains the pure vectors with $B^2\neq0$, such as $\vec e_x+\vec e_y$, for which $Q_t=0$ and the two eigenvalues are opposite. It also contains every Hermitian element with $B^2<0$ and $N\neq0$, such as $\sqrt2\,e_t+i\vec e_x$.

The sector is connected, and it is not simply connected; the loop $t\mapsto e_t+\varepsilon e^{2\pi it}\vec e_x$ winds around the spectral cone. The topology is not used below beyond the parameter count.

## The Decomposition

### The Word

**Definition.** An **exponential polar decomposition** of $\tilde Q$ is a writing

$$
\boxed{\;
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\,e^{i\alpha}\,
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),\quad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
\;}
$$

with

$$
r>0,\qquad
\alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\qquad
\psi\ge0,\qquad
\theta\in[0,2\pi],
$$

and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors, called the **boost axis** and the **rotor axis**. The four factors are the **scale** $r$, the **phase** $e^{i\alpha}$, the **boost** $\tilde U_{\mathrm b}$ and the **rotor** $\tilde u_{\mathrm r}$, both written in the box.

The scalars are central; the two exponentials are not. The order of the factors is part of the definition: the boost stands to the left of the rotor. The reverse order is another word, and the two are related by the Cartan involution, not by a commutation.

### The Four Factors

The factors have closed forms in the basis $e_t,\vec e_x,\vec e_y,\vec e_z$.

| Factor | Exponent | Closed form | Range |
|---|---|---|---|
| scale | $\ln r$ | $r$ | $r>0$ |
| phase | $i\alpha$ | $e^{i\alpha}$ | $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| boost | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}$ | $\psi\ge0$ |
| rotor | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$ |

The boost is Hermitian positive of norm one; the rotor is a unit real quaternion. The product $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ is the unit factor of $\tilde Q$, and

$$
\tilde Q=\Rho\,\tilde U,
\qquad
\Rho=r e^{i\alpha}.
$$

The modulus $\Rho$ is the principal square root of $N$, in the branch with non-negative real part and, on the negative real axis, non-negative imaginary part. The scale and the phase are the polar coordinates of $\Rho$. The unit factor is recovered as $\tilde U=\tilde Q/\Rho$ and has norm one.

### The Component Form

Let

$$
c_{\mathrm b}=\cosh\frac{\psi}{2},
\qquad
s_{\mathrm b}=\sinh\frac{\psi}{2},
\qquad
c_{\mathrm r}=\cos\frac{\theta}{2},
\qquad
s_{\mathrm r}=\sin\frac{\theta}{2},
\qquad
c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}.
$$

Multiplying the two exponentials in the order of the word gives

$$
\boxed{\;
\tilde U=\bigl(c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c\bigr)e_t
+i s_{\mathrm b}c_{\mathrm r}\,\vec u_{\mathrm b}
+c_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm r}
+i s_{\mathrm b}s_{\mathrm r}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\;}
$$

The four terms are the scalar term, corrected by the angle between the axes, the boost axis, the rotor axis and the cross term. The cross term is present exactly when both angles are nonzero and the axes are neither parallel nor antiparallel. It is the term that a sum of the two exponents cannot produce, because the sum contains only the two axes and their linear combinations.

The scalar part is

$$
\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c,
$$

and the vector part is the remaining three terms. The norm of $\tilde U$ is one, so

$$
\bigl(\operatorname{Sc}\tilde U\bigr)^2+\vec U\cdot\vec U=1,
$$

and the eigenvalues of $\tilde U$ are

$$
\mu_\pm=\operatorname{Sc}\tilde U\pm i\sqrt{1-\bigl(\operatorname{Sc}\tilde U\bigr)^2}.
$$

### The Parameter Count

The data are

$$
\underbrace{1}_{\ln r}
+\underbrace{1}_{\alpha}
+\underbrace{1+2}_{\psi,\vec u_{\mathrm b}}
+\underbrace{1+2}_{\theta,\vec u_{\mathrm r}}
=8,
$$

the real dimension of the group of units. The word is a coordinate system on that group, cut by the ranges of the two angles and of the phase. The two axes are points of $S^2$.

## The Spectral Reading

### The Eigenbasis

Let $\tilde Q\in\Sigma_{11}$, and fix a square root $B$ of $B^2$. Define

$$
\vec\Xi=-i\frac{\vec Q}{B},
\qquad
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2},
\qquad
\lambda_\pm=Q_t\pm iB.
$$

**Proposition (the eigenbasis).** The element $\vec\Xi$ is a root of one,

$$
\vec\Xi^2=e_t,
$$

the two elements $\tilde\Pi_\pm$ are complementary idempotents,

$$
\tilde\Pi_\pm^2=\tilde\Pi_\pm,
\qquad
\tilde\Pi_+\tilde\Pi_-=\tilde\Pi_-\tilde\Pi_+=0,
\qquad
\tilde\Pi_++\tilde\Pi_-=e_t,
$$

and

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-.
$$

The eigenvalues are distinct and nonzero, and the idempotents are the spectral projections.

*Proof.* For a pure vector, $\vec Q^2=-\vec Q\cdot\vec Q=-B^2$. Hence

$$
\vec\Xi^2=\Bigl(-i\frac{\vec Q}{B}\Bigr)^2=(-i)^2\frac{\vec Q^2}{B^2}=(-1)\frac{-B^2}{B^2}=e_t.
$$

The idempotent identities follow from $\vec\Xi^2=e_t$ and the commutation of $\vec\Xi$ with itself. The spectral decomposition is checked by expanding the right-hand side:

$$
\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
=\frac{\lambda_++\lambda_-}{2}e_t+\frac{\lambda_+-\lambda_-}{2}\vec\Xi
=Q_te_t+iB\vec\Xi
=Q_te_t+\vec Q.
$$

$\square$

The two signs of $B$ exchange $\vec\Xi$ with $-\vec\Xi$, $\tilde\Pi_+$ with $\tilde\Pi_-$, and $\lambda_+$ with $\lambda_-$; the unordered pair is unchanged. The element is semisimple, its minimal polynomial is $X^2-2Q_tX+N$, and its centraliser is $\mathbb{C}[\tilde Q]\cong\mathbb{C}\oplus\mathbb{C}$.

### The Unit Factor on the Eigenlines

Since $\tilde U=\tilde Q/\Rho$ and $\Rho$ is central,

$$
\tilde U=\mu_+\tilde\Pi_++\mu_-\tilde\Pi_-,
\qquad
\mu_\pm=\frac{\lambda_\pm}{\Rho}.
$$

The two eigenvalues of the unit factor satisfy

$$
\mu_+\mu_-=\frac{N}{\Rho^2}=1,
\qquad
\mu_++\mu_-=\frac{2Q_t}{\Rho}=2\operatorname{Sc}\tilde U,
\qquad
\mu_+\neq\mu_-.
$$

They are the roots of $X^2-2U_tX+1$, with $U_t=\operatorname{Sc}\tilde U$, hence

$$
\boxed{\mu_\pm=U_t\pm i\sqrt{1-U_t^2}}.
$$

The spectrum of $\tilde U$ therefore depends on $\tilde Q$ only through the single complex number $U_t=Q_t/\Rho$. The two eigenvalues are distinct because $B^2\neq0$, and their product is one.

The spectral data of the element and of the unit factor are related by

$$
\lambda_\pm=\Rho\mu_\pm,
\qquad
N=\Rho^2,
\qquad
Q_t=\Rho U_t,
\qquad
B^2=\Rho^2(1-U_t^2).
$$

The last identity is the spectral form of the defining condition: the sector $B^2\neq0$ is the locus $U_t^2\neq1$, and the spectral cone $B^2=0$ is the locus $U_t=\pm1$.

### The Normal Case

The eigenbasis is a polar basis when the element commutes with its Hermitian conjugate.

**Lemma.** For every $\tilde Q=Q_te_t+\vec Q$,

$$
[\tilde Q,\tilde Q^*]=-2\,\vec Q\times\overline{\vec Q}.
$$

*Proof.* The scalar parts are central and commute with everything. For pure vectors,

$$
\vec Q\,\overline{\vec Q}=-\vec Q\cdot\overline{\vec Q}+\vec Q\times\overline{\vec Q},
\qquad
\overline{\vec Q}\,\vec Q=-\vec Q\cdot\overline{\vec Q}-\vec Q\times\overline{\vec Q},
$$

so the commutator is $-2\vec Q\times\overline{\vec Q}$. $\square$

**Theorem (the normal dichotomy).** For $\tilde Q\in\Sigma_{11}$ with word as above, the following are equivalent.

1. $\tilde Q$ is normal, $[\tilde Q,\tilde Q^*]=0$.
2. $\vec Q\times\overline{\vec Q}=0$, that is, $\vec Q=\zeta\vec u$ with $\zeta\in\mathbb{C}$ and $\vec u$ a real unit vector.
3. The two polar factors $\tilde U_{\mathrm b}$ and $\tilde u_{\mathrm r}$ commute with $\tilde Q$.
4. The two axes are parallel or antiparallel, or one of the two angles vanishes.
5. The word is a single exponential.

In this case the common axis is $\pm i\vec\Xi$ whenever it is defined, and

$$
\boxed{\;
\tilde Q=r e^{i\alpha}\exp\Bigl(\frac{\theta+i\psi}{2}\vec u\Bigr),
\qquad
\vec u=\pm i\vec\Xi,
\;}
$$

with the sign chosen so that $\psi\ge0$. The eigenvalues of the unit factor are

$$
\boxed{\mu_\pm=e^{\mp\frac{\psi}{2}}e^{\pm i\frac{\theta}{2}}},
$$

and the spectrum of $\tilde U$ determines the two angles,

$$
\psi=\ln\Bigl\lvert\frac{\mu_-}{\mu_+}\Bigr\rvert,
\qquad
\theta=2\arg\mu_+\pmod{2\pi}.
$$

*Proof.* The equivalence of 1 and 2 is the lemma, with the rank-one condition on the complex vector $\vec Q$. If $\tilde Q$ is normal then $\tilde U$ is normal, because $\tilde U=\tilde Q/\Rho$ and $\Rho$ is central. The Hermitian factor $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$ is a function of $\tilde U\tilde U^*$, hence commutes with $\tilde U$, and $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ commutes with $\tilde U$ as well. Both commute with $\tilde Q=\Rho\tilde U$, which gives 3. Conversely, if the two factors commute with $\tilde Q$, they commute with $\tilde U$ and with each other, so

$$
\tilde Q\tilde Q^*=|\Rho|^2\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*\tilde U_{\mathrm b}
=|\Rho|^2\tilde U_{\mathrm b}^2
=\tilde Q^*\tilde Q,
$$

which gives 1. If 3 holds, both factors are functions of $\tilde U$, hence diagonal in its eigenbasis, so their axes are the two eigenlines, which are $\pm i\vec\Xi$; this gives 4. If 4 holds, the two exponents commute, so the product is the exponential of their sum, which gives 5. If 5 holds, $\tilde Q$ is a scalar multiple of the exponential of a complex multiple of a real pure vector, and such an exponential is normal; this gives 1.

For the formula, write $\tilde U_{\mathrm b}=\exp(i\frac{\psi}{2}\vec u)$ and $\tilde u_{\mathrm r}=\exp(\frac{\theta}{2}\vec u)$ on the common axis. Their product is $\exp(\frac{\theta+i\psi}{2}\vec u)$ because the exponents commute. On the two eigenlines the product acts by $e^{-\psi/2}e^{i\theta/2}$ and $e^{\psi/2}e^{-i\theta/2}$; with the labelling of $\mu_\pm$ fixed by $\lambda_\pm$, and the sign of the common axis chosen accordingly, this is the displayed pair $e^{\mp\psi/2}e^{\pm i\theta/2}$. The extraction of the angles follows from the moduli and the arguments. $\square$

The display is the **amalgamation** of the four factors into one exponential. The complex angle is $\frac{\theta+i\psi}{2}$; the real part is the rotor angle and the imaginary part is the rapidity. The sign of the imaginary part is the sign convention of the boost: the other choice reverses the common axis.

**Remark (the axes in the normal case).** The common axis is $\pm i\vec\Xi$. Since $\vec\Xi=-i\vec Q/B$ and $\vec Q=\zeta\vec u$, the axis is $\pm\vec u$: the real direction of the vector part. The eigenbasis and the polar frame are the same frame. The element is normal exactly when its vector part has a real direction; a complex vector part with two independent real directions is non-normal.

### The Non-Normal Case

In the general case the polar factors are not functions of $\tilde Q$, and the eigenbasis is not a polar basis.

**Proposition (the failure of the spectral reading).** Let $\tilde Q\in\Sigma_{11}$ be non-normal. Then

$$
[\tilde U_{\mathrm b},\tilde Q]\neq0,
\qquad
[\tilde u_{\mathrm r},\tilde Q]\neq0,
$$

and the axes are not the eigenlines. The eigenvalues $\mu_\pm$ still determine the unordered pair $\{\mu_+,\mu_-\}$, but they do not determine $\psi$, $\theta$, $\vec u_{\mathrm b}$ or $\vec u_{\mathrm r}$.

*Proof.* The factors commute with $\tilde Q$ exactly when the element is normal, by the theorem. If they do not commute, they are not diagonal in the eigenbasis, so their axes cannot be the eigenlines. The eigenvalues of $\tilde U$ are functions of $U_t$ alone, by $\mu_\pm=U_t\pm i\sqrt{1-U_t^2}$; the word parameters also depend on the relative angle of the axes, through $\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c$. There are different triples $(\psi,\theta,c)$ with the same $U_t$, hence the same spectrum, and with different words. $\square$

The last sentence is the precise statement of the gap. In the normal case $c=\pm1$, and the pair $(\psi,\theta)$ is recovered from the spectrum. In the non-normal case $c$ is a third unknown, and the spectrum is one complex equation for three real unknowns.

**Example.** Let $\tilde Q=\bigl(1-\frac{i}{2}\bigr)e_t+\frac{1+i}{\sqrt2}\vec e_x+\frac{1}{\sqrt2}\vec e_y+\frac{i}{2}\vec e_z$. It is N-regular and spectrally regular, and non-normal, because

$$
\vec Q\times\overline{\vec Q}
=\Bigl(-\frac{i}{\sqrt2},\frac{i}{\sqrt2},i\Bigr)\neq0.
$$

Its word has

$$
\psi=1.7627471740,
\qquad
\vec u_{\mathrm b}=\vec e_x,
\qquad
\theta=\frac{\pi}{2},
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2},
\qquad
c=\frac{1}{\sqrt2}.
$$

The eigenvalues of the unit factor have moduli $0.480533816$ and $2.081019$, and arguments $\pm0.674888846$. The normal-case formulas would give $\psi=1.466$ and $\theta=1.350$, not the true $1.763$ and $1.571$. The spectrum is the same; the reading is not.

The example is case 5 of the worked examples. The gap is not a rounding effect: the ratio of the two moduli is $4.331$, whose logarithm is $1.466$, while the rapidity is $1.763$.

### What the Spectrum Determines

The comparison is a count of real data.

| Data | Real dimension | Determines |
|---|---|---|
| $N$, $B^2$ | $4$ | $r,\alpha,U_t$ |
| spectrum $\{\lambda_+,\lambda_-\}$ | $4$ | the same, in spectral form |
| eigenprojectors $\tilde\Pi_\pm$ | $4$ | the eigenlines; the polar axes only in the normal case |
| word $(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})$ | $8$ | the element |

The spectrum and the eigenprojectors together determine the element. The polar word is another eight data. The two parametrizations share the four data $(r,\alpha,U_t)$; the spectrum determines the remaining data only in the normal case, where the eigenprojectors are the polar axes. In the non-normal case the eigenprojectors do not determine the polar axes, and the spectrum does not determine the two angles.

The spectral decomposition is a diagonalization over $\mathbb{C}$: it writes $\tilde Q$ as two complex multiples of two idempotents. The polar decomposition is a Cartan decomposition over $\mathbb{R}$: it writes $\tilde U$ as a positive Hermitian factor times a unitary factor. The two agree on the scalar factor and on the eigenvalues of $\tilde U$, and on nothing else in the non-normal case.

**Remark (the two decompositions are transverse).** The eigenbasis depends on the complex structure of the vector part; the polar frame depends on the Hermitian structure of the unit factor. The normal elements are the intersection: the elements for which the two frames coincide. The intersection is the normal set, $Q_t+\zeta\vec u$ with $Q_t,\zeta\in\mathbb{C}$ and $\vec u\in S^2$, of real dimension $2+2+2=6$; it is not open in the sector.

## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every $\tilde Q\in\Sigma_{11}$ has a unique writing

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\tilde U_{\mathrm b}$ Hermitian positive of norm one, and $\tilde u_{\mathrm r}$ a unit real quaternion. Consequently it has the exponential word above; the axes are unique when $\psi>0$ and $\theta\notin\{0,2\pi\}$.

*Proof.* The modulus $\Rho$ is the principal square root of $N$, and $\tilde U=\tilde Q/\Rho$ has norm one. The matrix image of $\tilde U$ lies in $SL(2,\mathbb{C})$. The global Cartan decomposition

$$
SL(2,\mathbb{C})=P\cdot K,
\qquad
P=\{\text{positive Hermitian of determinant }1\},
\qquad
K=SU(2),
$$

gives a unique factorization $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}\in P$ and $\tilde u_{\mathrm r}\in K$. A positive Hermitian determinant-one matrix is the exponential of a unique Hermitian traceless matrix, which is $i\frac{\psi}{2}\vec u_{\mathrm b}$ with $\psi\ge0$ and a unit axis. A unitary determinant-one matrix is the exponential of an anti-Hermitian traceless matrix, which is $\frac{\theta}{2}\vec u_{\mathrm r}$ with $\theta\in[0,2\pi]$. The endpoint $\theta=2\pi$ is the central rotor $-e_t$, where the axis is undefined. The scale and the phase are the polar coordinates of $\Rho$, unique in the branch. $\square$

The proof uses only the invertibility of $\tilde Q$; the spectral condition $B^2\neq0$ enters only through the domain, not through the existence. This is why the companion article can repeat the same theorem verbatim.

**The degeneracies.** The boost axis is undefined at $\psi=0$, where the boost is the identity. The rotor axis is undefined at $\theta=0$, where the rotor is the identity, and at $\theta=2\pi$, where the rotor is $-e_t$ for every axis. These are the usual coordinate singularities of polar coordinates; the element is smooth there and the word is unique.

| Parameter | Range | Unique? |
|---|---|---|
| $r$ | $(0,\infty)$ | yes |
| $\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | yes: the branch |
| $\psi$ | $[0,\infty)$ | yes |
| $\vec u_{\mathrm b}$ | $S^2$ | no: undefined at $\psi=0$ |
| $\theta$ | $[0,2\pi]$ | yes |
| $\vec u_{\mathrm r}$ | $S^2$ | no: undefined at $\theta\in\{0,2\pi\}$ |

At a degeneracy the word is still unique as an element of the group, but the coordinate chart is singular. The singularity is not a failure of the decomposition; it is the price of the polar coordinates.

## The Logarithm

### The Cartan Logarithm

Write $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ and put

$$
\tilde H=\operatorname{Log}\tilde U_{\mathrm b}=i\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde K=\operatorname{Log}\tilde u_{\mathrm r}=\frac{\theta}{2}\vec u_{\mathrm r}.
$$

The pair $(\tilde H,\tilde K)$ is the **Cartan logarithm** of $\tilde U$. It is unique with the ranges of the theorem, except at the central rotor, and it satisfies

$$
\tilde U=\exp(\tilde H)\exp(\tilde K).
$$

The two exponents lie in the two summands of the Cartan decomposition of the Lie algebra,

$$
\mathbb{B}=\mathbb{R}e_t\ \oplus\ i\mathbb{R}e_t\ \oplus\ \mathfrak{p}\ \oplus\ \mathfrak{k},
\qquad
\mathfrak{p}=i\{\text{real pure vectors}\},
\qquad
\mathfrak{k}=\{\text{real pure vectors}\},
$$

of real dimensions $1+1+3+3=8$. The boost exponent is in $\mathfrak{p}$ and the rotor exponent in $\mathfrak{k}$.

### The Single Logarithm

A **single logarithm** of $\tilde Q$ is an element $\operatorname{Log}\tilde Q$ with $\exp(\operatorname{Log}\tilde Q)=\tilde Q$. Since $\mathbb{B}\cong M_2(\mathbb{C})$ and every invertible complex matrix has a logarithm, the exponential is surjective onto the units. A single logarithm is related to the Cartan logarithm by

$$
\operatorname{Log}\tilde Q=\ln r+i\alpha+\operatorname{Log}\bigl(\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr),
$$

where the last term is a logarithm inside $\mathfrak{gl}(2,\mathbb{C})$, not inside $\mathfrak{sl}(2,\mathbb{C})$; its trace may be a nonzero multiple of $2\pi i$.

The **formal exponent** is the sum of the four exponents,

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is not the single logarithm in general. The **log defect** is the Baker–Campbell–Hausdorff correction, whose first term is

$$
\frac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}
\in\mathfrak{p}.
$$

The first correction is again a boost. The formal exponent is a logarithm exactly when this correction and all higher ones vanish. In the normal case the axes are parallel, the commutator vanishes, and the formal exponent is a logarithm. In the non-normal case the correction is nonzero, and the exponential of the formal exponent misses the element; the worked examples give defects $0.5$ and $0.4222$.

### The Fibre

The exponential is not injective. Its kernel contains the central periods $2\pi ik\,e_t$, the pure periods $2\pi\vec U$ for real unit vectors, and the mixed elements $\pi i\,e_t+\pi\vec U$. The fibre over an element is not a coset of the kernel, because the exponential is not a homomorphism.

The polar parameters do not cut the fibre of the exponential to one point: the four exponents sum to the formal exponent, which is not a logarithm. What they cut to one point, up to the axis degeneracies, is the fibre of the **word map**

$$
(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})
\longmapsto
r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The word is a section of that map, not of the exponential. It is a global coordinate system on the group of units, and its domain is the complement of the null cone.

## The Group Law

The product of two words is

$$
\bigl(r_1e^{i\alpha_1}e^{\tilde H_1}e^{\tilde K_1}\bigr)
\bigl(r_2e^{i\alpha_2}e^{\tilde H_2}e^{\tilde K_2}\bigr)
=r_1r_2e^{i(\alpha_1+\alpha_2)}e^{\tilde H_1}e^{\tilde K_1}e^{\tilde H_2}e^{\tilde K_2}.
$$

The central factors add. The non-central ones do not: the middle product $e^{\tilde K_1}e^{\tilde H_2}$ must be re-split as a boost times a rotor. The first correction is a commutator, so the rotor of the first word conjugates the boost of the second; the parameters of the product are not the sums of the parameters.

The brackets of the two summands close as a symmetric pair.

| Bracket | Lies in | Reading |
|---|---|---|
| $[\mathfrak{k},\mathfrak{k}]$ | $\mathfrak{k}$ | two rotors compose to a rotor |
| $[\mathfrak{p},\mathfrak{p}]$ | $\mathfrak{k}$ | two boosts compose to a boost times a rotor |
| $[\mathfrak{k},\mathfrak{p}]$ | $\mathfrak{p}$ | a rotor conjugates a boost to a boost |

The second row is the Thomas–Wigner rotation. The third is the statement that the boost set is a symmetric space and not a group: the commutator of an infinitesimal rotor and an infinitesimal boost is a boost, so the boost directions are stable under the adjoint action of the rotor, while the boost set itself is not closed under multiplication. The first row is the subgroup $SU(2)$ of the rotor.

| Data | Law |
|---|---|
| scale and phase | multiply |
| boost | conjugated by the rotor, not added |
| rotor | multiplies |
| exponent | does not add: the Baker–Campbell–Hausdorff correction |
| group | $\mathbb{B}^{\times}\cong\mathrm{GL}_2(\mathbb{C})$ |

## The Matrix Picture

The matrix model is

$$
\mathsf M(\tilde Q)=Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z.
$$

It is a $\mathbb{C}$-algebra homomorphism, so $\mathsf M(\exp\tilde X)=\exp(\mathsf M(\tilde X))$, and the polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M(\tilde Q)=r e^{i\alpha}\,\mathsf M(\tilde U_{\mathrm b})\,\mathsf M(\tilde u_{\mathrm r}),
$$

with $\mathsf M(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M(\tilde u_{\mathrm r})$ unitary of determinant one.

The spectral reading is the diagonalization of the matrix. The matrix $\mathsf M(\tilde Q)$ has the two distinct eigenvalues $\lambda_\pm$, and it is diagonalizable; the eigenbasis is a basis of $\mathbb{C}^2$ consisting of the two eigenvectors. The polar factors are the positive and unitary factors of the matrix polar decomposition. They are diagonal in that basis exactly when the matrix is normal, which is the matrix form of the theorem of §*The Normal Case*.

The four exponents sit in the two summands of

$$
\mathfrak{gl}_2(\mathbb{C})=\mathfrak{u}(2)\oplus\mathfrak{H},
\qquad
\mathfrak{u}(2)=\{X:X^\dagger=-X\},
\qquad
\mathfrak{H}=\{X:X^\dagger=X\},
$$

of real dimensions $4$ and $4$. The scale and the boost lie in $\mathfrak H$; the phase and the rotor lie in $\mathfrak u(2)$. The central real line is the scale, the central imaginary line is the phase, and the traceless parts are the boost and the rotor.

| Matrix object | Algebra object | Dimension | Factor |
|---|---|---|---|
| positive determinant-one matrix | Hermitian positive unit-norm element | $3$ | boost |
| unitary determinant-one matrix | unit real quaternion | $3$ | rotor |
| positive real scalar | scale | $1$ | $r$ |
| unit complex scalar | phase | $1$ | $e^{i\alpha}$ |

The two scales of the matrix are $r e^{\psi/2}$ and $r e^{-\psi/2}$, each with multiplicity one in the regular sector. Their product is $r^2=|\Rho|^2$, and their ratio is $e^{\psi}$. The determinant is $N=\Rho^2$, of modulus $r^2$.

## The Exponential Coordinates

The parameters $r,\alpha,\psi,\theta$ and the two axes are coordinates on the group of units. Their ranges make the map a bijection up to the axis degeneracies. The coordinate lines are the four one-parameter families:

- the **scale line** $r\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a half-line;
- the **phase circle** $\alpha\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, a circle cut to a half-open interval by the branch;
- the **boost hyperbola** $\psi\mapsto r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\tilde u_{\mathrm r}$, a non-compact ray;
- the **rotor arc** $\theta\mapsto r e^{i\alpha}\tilde U_{\mathrm b}\exp(\frac{\theta}{2}\vec u_{\mathrm r})$, a great semicircle from $e_t$ to $-e_t$.

The positive cone $P$ is homeomorphic to $\mathbb{R}^3$ and the rotor group $K=SU(2)$ is $S^3$, so

$$
SL(2,\mathbb{C})\simeq\mathbb{R}^3\times S^3.
$$

The group of units retracts onto $U(2)$, and $U(2)\cong U(1)\times SU(2)$ as a space, so

$$
\mathbb{B}^{\times}\simeq S^1\times S^3.
$$

The branch of the modulus makes $\tilde Q\mapsto(\Rho,\tilde U)$ a bijection onto $\mathbb{C}^{\times}\times SL(2,\mathbb{C})$, but not a homeomorphism: on the cut the phase jumps by $-1$ and the rotor changes sign. The fundamental group is $\mathbb{Z}$, carried by the phase.

The **conformal factor** is read in the coordinates. Under the sandwich $\tilde QX\tilde Q^*$, the quaternionic norm of $X$ is multiplied by

$$
r^4=\exp(4\ln r)=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^2,
$$

so lengths are multiplied by $r^2=|\langle\tilde Q\rangle_{\natural}|$. The scale exponent is a quarter of the logarithm of the conformal factor; the phase, the boost and the rotor are isometries of the form.

## The Two Walls

The sector is the complement of the union of two cones.

| Wall | Equation | Stratum | What happens to the word |
|---|---|---|---|
| null cone | $N=0$ | $\Sigma_{01}\cup\Sigma_{00}$ | $r\to0$, $\psi\to\infty$ |
| spectral cone | $B^2=0$ | $\Sigma_{10}\cup\Sigma_{00}$ | word finite, eigenbasis degenerates |

The two cones meet at $\Sigma_{00}$, the nilpotent stratum. The two walls behave differently, and the difference is the subject of this section.

### The Null Cone

On the null cone the modulus vanishes and no unit factor exists. A nonzero element of the cone is a zero divisor of rank one. As an element of the sector approaches the cone with $B^2$ bounded away from zero, the rapidity diverges and the scale collapses. The standard family is

$$
\tilde Q(\psi)=R e^{-\psi/2}\,\zeta\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\tilde u_{\mathrm r},
\qquad
\psi>0,
$$

with $R>0$, $|\zeta|=1$ and unit axes. Every member is a unit, with modulus $R e^{-\psi/2}$, and its word has rapidity $\psi$. The limit is

$$
\tilde Q(\psi)\longrightarrow
\frac{R\zeta}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r},
\qquad
\psi\to\infty,
$$

a nonzero null element of rank one. It is nilpotent exactly when $\tilde u_{\mathrm r}$ anticommutes with $\vec u_{\mathrm b}$, and it has nonzero scalar part otherwise. The scale vanishes as $e^{-\psi/2}$ and the boost diverges as $e^{\psi/2}$; the product stays finite.

### The Spectral Cone

On the spectral cone the word does not diverge. Let $\tilde Q_k\to\tilde Q_0$ with $N_k\to N_0\neq0$ and $B_k^2\to0$. The modulus converges, the unit factor converges, and the Cartan factors converge, because the Cartan decomposition is continuous. Hence the polar data have a limit: the limiting word is the word of $\tilde Q_0$, which lies in $\Sigma_{10}$ and is treated in the companion article.

The eigenbasis does not survive. The root is

$$
\vec\Xi=-i\frac{\vec Q}{B},
$$

and $B\to0$ while $\vec Q\to\vec Q_0\neq0$ on the spectral cone, so $|\vec\Xi|\to\infty$. The idempotents

$$
\tilde\Pi_\pm=\frac{e_t\pm\vec\Xi}{2}
$$

diverge, and the spectral decomposition has no limit. The eigenvalues $\lambda_\pm=Q_t\pm iB$ coalesce, the minimal polynomial becomes a square, and the element becomes defective.

**Proposition (the word survives the spectral wall, the eigenbasis does not).** Let $\tilde Q_k\in\Sigma_{11}$ converge to $\tilde Q_0\in\Sigma_{10}$ with $N_0\neq0$ and $\vec Q_0\neq0$, so that the limit lies in the Jordan part. Then $\tilde U_k\to\tilde U_0$, $\tilde U_{\mathrm b,k}\to\tilde U_{\mathrm b,0}$ and $\tilde u_{\mathrm r,k}\to\tilde u_{\mathrm r,0}$, so the word converges to the word of $\tilde Q_0$. The root $\vec\Xi_k$ diverges in norm, and no spectral idempotent of $\tilde Q_k$ converges to a nonzero idempotent.

*Proof.* The modulus is continuous in $N$ away from zero, and the Cartan factors are continuous functions of $\tilde U$; this gives the convergence of the word. The root satisfies $|\vec\Xi_k|=|\vec Q_k|/|B_k|\to\infty$ because $\vec Q_k\to\vec Q_0\neq0$ and $B_k\to0$. An idempotent of the form $(e_t\pm\vec\Xi_k)/2$ is unbounded, so it has no finite limit. $\square$

At the scalar line the limit is different. If $\tilde Q_0=Q_0e_t$ is a nonzero scalar, then $\vec Q_0=0$, the root is $0/0$, and its limit depends on the path: the family $Q_k=1+\epsilon_k\vec e_x$ has $\vec\Xi_k=-i\vec e_x$, so the idempotents converge to nonzero idempotents of the ambient algebra even though the limit is scalar. The eigenvalues coalesce, but the eigenbasis need not diverge. The proposition is therefore stated for the Jordan part, which is the part of the wall that the sector meets transversally.

The contrast is the exact content of the difference between the two articles. The polar decomposition is a decomposition of the group of units, and it is continuous across the spectral wall. The spectral decomposition is a decomposition of the element, and it degenerates there. The sector $\Sigma_{11}$ is the open set on which both exist; its wall $B^2=0$ is where only the polar one survives.

## Summary

### Main Formulas

| Object | Formula |
|---|---|
| domain | $N\neq0$, $B^2\neq0$ |
| word | $\tilde Q=r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| modulus | $\Rho=r e^{i\alpha}=(N)^{1/2}$ in the branch |
| unit factor | $\tilde U=\tilde Q/\Rho=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| boost | $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ |
| rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ |
| component form | $\tilde U=(c_{\mathrm b}c_{\mathrm r}-is_{\mathrm b}s_{\mathrm r}c)e_t+is_{\mathrm b}c_{\mathrm r}\vec u_{\mathrm b}+c_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm r}+is_{\mathrm b}s_{\mathrm r}\vec u_{\mathrm b}\times\vec u_{\mathrm r}$ |
| eigenvalues | $\lambda_\pm=Q_t\pm iB$ |
| eigenbasis | $\vec\Xi=-i\vec Q/B$, $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ |
| unit-factor eigenvalues | $\mu_\pm=\lambda_\pm/\Rho=U_t\pm i\sqrt{1-U_t^2}$ |
| normal case | $\mu_\pm=e^{\mp\psi/2}e^{\pm i\theta/2}$, axes $\pm i\vec\Xi$ |
| normal criterion | $\vec Q\times\overline{\vec Q}=0$ |
| spectral wall | $B^2=0\iff U_t=\pm1$ |
| explicit data | §*The Result in Terms of the Coordinates*: boxes for $r,\alpha,\psi,\vec u_{\mathrm b},\tilde U_{\mathrm b},\tilde u_{\mathrm r},\theta,\vec u_{\mathrm r}$ |

### The Comparison

| Property | Spectral reading | Polar reading |
|---|---|---|
| decomposition of | the element $\tilde Q$ | the unit factor $\tilde U$ |
| factors | two idempotents | positive Hermitian times unitary |
| coefficients | $\lambda_\pm$ | exponentials of $\psi,\theta$ |
| diagonal in the eigenbasis | always | exactly when normal |
| survives $B^2\to0$ | no on the Jordan part | yes |
| real dimension | $8$ | $8$ |
| shared data | $r,\alpha,U_t$ | $r,\alpha,U_t$ |

### What the Sector Shows

- The word exists for every element of the sector, and it is unique up to the axis degeneracies.
- The eigenbasis exists because the two eigenvalues are distinct. It is a spectral basis, not a polar basis.
- The polar factors are diagonal in the eigenbasis exactly for the normal elements, and those are exactly the elements whose two axes are parallel and whose word is a single exponential.
- In the non-normal case the spectrum determines the eigenvalues of the unit factor but not the rapidity, the rotor angle or the axes. The polar word carries four real data that the spectrum does not.
- The word is continuous across the spectral wall $B^2=0$; on the Jordan part the eigenbasis is not. This is why the spectrally degenerate case needs its own article, and why it can reuse the word verbatim.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $Q_t,Q_x,Q_y,Q_z$ | the four complex coordinates |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | the vector form $Q_x^2+Q_y^2+Q_z^2$ |
| $\Sigma_{11}$ | the N-regular, spectrally regular sector |
| $\Rho=r e^{i\alpha}$ | the modulus, principal square root of $N$ |
| $\tilde U=\tilde Q/\Rho$ | the unit factor |
| $\tilde U_{\mathrm b},\tilde u_{\mathrm r}$ | the Hermitian positive factor and the rotor, $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| $\psi$ | the rapidity |
| $\theta$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the two axes |
| $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | the cosine between the axes |
| $\vec\Xi=-i\vec Q/B$ | the root of one carried by the element |
| $\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi)$ | the spectral idempotents |
| $\lambda_\pm=Q_t\pm iB$ | the eigenvalues |
| $\mu_\pm=\lambda_\pm/\Rho$ | the eigenvalues of the unit factor |
| $\tilde H,\tilde K$ | the Cartan pair |
| $\tilde Q_{\log}$ | the formal exponent |
| $\mathsf M(\tilde Q)$ | the matrix $Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z$ |
| $c_{\mathrm b},s_{\mathrm b},c_{\mathrm r},s_{\mathrm r}$ | the half-angle cosines and sines |
| $\lVert\tilde Q\rVert_E^2=|Q_t|^2+|\vec Q|^2$ | the Euclidean norm squared of the coordinates |
| $\vec a$ | the vector $\sinh\psi\,\vec u_{\mathrm b}$ |
| $C,S$ | the half-angle numerators, $\cosh\frac{\psi}{2}=C/\sqrt{|N|}$, $\sinh\frac{\psi}{2}=S/\sqrt{|N|}$ |
| $\mathrm{Vect}\tilde X$ | the vector part of $\tilde X$ |

## Further Reading

- [Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), the companion for $B^2=0$, independent of this article.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Regular Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-regular-biquaternion.html), for the dictionary between the word and the eigenvalue data.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), for the numerical cases, the normal and non-normal comparison, and the defect tables.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem and the group of units.
- [The Eigenbasis of a Spectrally Regular Biquaternion](the-spectrally-regular-sector-and-construction-of-the-eigenbasis-of-a-biquaternion.html), for the eigenbasis, the Peirce corners and the spinors.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), for the four sectors and the discriminants.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the fibre.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Cartan decomposition and the Baker–Campbell–Hausdorff series.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
