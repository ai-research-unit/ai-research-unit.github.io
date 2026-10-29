# __Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion__

## Introduction

This article computes the exponential polar decomposition of a biquaternion that is N-regular and spectrally degenerate, that is, one with

$$
\langle\tilde Q\rangle_{\natural}\neq0,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2=0.
$$

The word is the four-factor product

$$
\tilde Q=r\,e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and two real unit axes. Every element of the sector has one, and it is unique up to the usual degeneracies of the axes. The article proves this from the Cartan decomposition and computes the shape that the word takes in this sector.

The shape is rigid. The unit factor is $\pm$unipotent: it is $\varepsilon(e_t+\vec\Upsilon)$ with $\varepsilon=\pm1$ and $\vec\Upsilon^2=0$. Its two eigenvalues coincide, its minimal polynomial is a square, and it has no eigenbasis. The two angles of the word are not independent: the scalar part of the unit factor forces

$$
\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon,
$$

and on the Jordan part the two axes are orthogonal. The whole element is the scalar part times a unipotent written in the orthogonal frame,

$$
\tilde Q=Q_t\Bigl(e_t+i\tanh\frac{\psi}{2}\vec u_{\mathrm b}
+\tan\frac{\theta}{2}\vec u_{\mathrm r}
+i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}\Bigr),
$$

so the four word parameters reduce to the single complex number $Q_t$, one angle and a frame. The true logarithm is exact and truncated,

$$
\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon,
$$

while the sum of the four exponents is not a logarithm: the boost and the rotor do not commute, and the log defect is the cross term plus the nonlinear terms.

The companion article *Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion* treats the case $B^2\neq0$. The two articles are independent: each defines the word, proves existence and uniqueness, and develops the logarithm and the group law. This article does not use the companion, and the companion does not use this one. The two sectors are the two sides of the pair of conditions $\operatorname{Sc}\tilde U=\pm1$ and $\operatorname{Sc}\tilde U\neq\pm1$.

The article assumes *The Polar Decomposition of a N-Regular Biquaternion* for the modulus–unit theorem, *Biquaternion Elementary Functions* for the exponential and the logarithm, and *The N-Regular, Spectrally Degenerate Sector* for the normal forms and the two strata. It does not treat the spectral algebra of the sector, the Peirce decomposition or the spinors. The numerical cases are in *Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion*.

**The plan.** The word, its two unit factors and the seven data are boxed and proved in §*The Result in Terms of the Coordinates*. The domain is fixed in §*The Domain*, with its two strata. The word and its component form are in §*The Decomposition*. §*The Unipotent Unit Factor* proves the rigidity: the scalar constraint, the orthogonal frame and the closed form. §*The Two Strata* treats the scalar line and the Jordan part separately. Existence and uniqueness are proved in §*Existence and Uniqueness*. The logarithm, the group law, the matrix picture, the exponential coordinates and the boundary follow. The summary collects the formulas.


## The Result in Terms of the Coordinates

**Setting.** Use the normal form of §*The Normal Form*, $\tilde Q=Q_t(e_t+\vec\Upsilon)$, and write

$$
\vec\Upsilon=\vec A+i\vec B,\qquad \vec A,\vec B\in\mathbb R^3,\qquad a=\lVert\vec A\rVert.
$$

Since $\vec\Upsilon^2=0$, one has $\vec A\cdot\vec B=0$ and $\lVert\vec A\rVert=\lVert\vec B\rVert=a$. In terms of the coordinates, write $Q_t=q_t+iq'_t$ and $Q_j=q_j+iq'_j$ for $j=x,y,z$, with the eight coefficients real, and put $\vec q=(q_x,q_y,q_z)$ and $\vec q'=(q'_x,q'_y,q'_z)$. Then

$$
\vec A=\frac{q_t\,\vec q+q'_t\,\vec q'}{q_t^2+q_t'^2},\qquad
\vec B=\frac{q_t\,\vec q'-q'_t\,\vec q}{q_t^2+q_t'^2},
$$

since $Q_t^{-1}=(q_t-iq'_t)/(q_t^2+q_t'^2)$ and $\vec\Upsilon=\vec Q\,Q_t^{-1}$.

**Theorem (the word and its seven data).** On the Jordan part $a>0$, every $\tilde Q$ of the sector is

$$
\boxed{\;\tilde Q=Q_t(e_t+\vec\Upsilon)=r e^{i\alpha}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)\;}
$$

with the two unit factors

$$
\boxed{\;\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b},\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}\;}
$$

and with the seven data determined by $Q_t,Q_x,Q_y,Q_z$. Here $\Rho$ is the principal square root of $Q_t^2$, that is, the root with non-negative real part and, on the imaginary axis, non-negative imaginary part.

$$
\boxed{\;r=|Q_t|,\qquad
\Rho=\begin{cases}Q_t,&\operatorname{Re}Q_t>0\ \text{or}\ \bigl(\operatorname{Re}Q_t=0,\ \operatorname{Im}Q_t>0\bigr),\\[2pt]-Q_t,&\text{otherwise},\end{cases}\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1\;}
$$

$$
\boxed{\;\alpha=\arg\Rho=\begin{cases}\arg Q_t,&\varepsilon=+1,\\[2pt]\arg(-Q_t),&\varepsilon=-1,\end{cases}\;}
$$

$$
\boxed{\;\psi=2\operatorname{arsinh}a\;}
$$

$$
\boxed{\;\theta=\begin{cases}2\arctan a,&\varepsilon=+1,\\[2pt]2\pi-2\arctan a,&\varepsilon=-1.\end{cases}\;}
$$

$$
\boxed{\;\vec u_{\mathrm b}=\frac{\vec B+\vec A\times\vec B}{a\sqrt{1+a^2}},\qquad
\vec u_{\mathrm r}=\varepsilon\,\frac{\vec A}{a}\;}
$$

$$
\boxed{\;\tilde u_{\mathrm r}=\varepsilon\,\frac{e_t+\vec A}{\sqrt{1+a^2}},\qquad
\tilde U_{\mathrm b}=\sqrt{1+a^2}\,e_t+\frac{i}{\sqrt{1+a^2}}\bigl(\vec B+\vec A\times\vec B\bigr)\;}
$$

On the scalar line $a=0$ one has $\vec\Upsilon=0$, $\psi=0$, and $\theta=0$ if $\varepsilon=+1$, $\theta=2\pi$ if $\varepsilon=-1$; both axes are arbitrary.

*Proof.*

**The modulus and the sign.** Since $N=Q_t^2$, the modulus satisfies $\Rho^2=Q_t^2$, hence $\Rho=\pm Q_t$. The principal branch selects the sign displayed, and $r=|\Rho|=|Q_t|$, $\varepsilon=Q_t/\Rho=\pm1$. Writing $\Rho=re^{i\alpha}$ gives $\alpha=\arg\Rho$, with the principal argument in $(-\pi,\pi]$; since $\Rho=\varepsilon Q_t$, this is the box for $\alpha$.

**The structure of $\vec\Upsilon$.** With $\vec\Upsilon=\vec A+i\vec B$,

$$
\vec\Upsilon^2=\vec A^2-\vec B^2+2i\vec A\cdot\vec B
=\bigl(\lVert\vec B\rVert^2-\lVert\vec A\rVert^2\bigr)+2i\vec A\cdot\vec B,
$$

because $\vec A^2=-\lVert\vec A\rVert^2$ and $\vec B^2=-\lVert\vec B\rVert^2$ for real vectors. The vanishing of $\vec\Upsilon^2$ gives $\lVert\vec A\rVert=\lVert\vec B\rVert=a$ and $\vec A\cdot\vec B=0$.

**The product $\tilde U\tilde U^*$.** The unit factor is $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ and its star conjugate is $\tilde U^*=\varepsilon(e_t-\bar{\vec\Upsilon})$. Hence

$$
\tilde U\tilde U^*=(e_t+\vec\Upsilon)(e_t-\bar{\vec\Upsilon})
=e_t+\vec\Upsilon-\bar{\vec\Upsilon}-\vec\Upsilon\bar{\vec\Upsilon}.
$$

Now $\vec\Upsilon-\bar{\vec\Upsilon}=2i\vec B$, and, using $\vec A\cdot\vec B=0$ and $\lVert\vec A\rVert=\lVert\vec B\rVert=a$,

$$
\vec\Upsilon\bar{\vec\Upsilon}
=(\vec A+i\vec B)(\vec A-i\vec B)
=-2a^2-2i\,\vec A\times\vec B.
$$

Therefore

$$
\tilde U\tilde U^*=(1+2a^2)e_t+2i\bigl(\vec B+\vec A\times\vec B\bigr).
$$

**The boost.** Since $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}$ $*$-unitary, $\tilde U\tilde U^*=\tilde U_{\mathrm b}^2$. With $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$,

$$
\tilde U_{\mathrm b}^2=\cosh\psi\,e_t+i\sinh\psi\,\vec u_{\mathrm b}.
$$

Comparing the scalar parts gives $\cosh\psi=1+2a^2=1+2\sinh^2\frac{\psi}{2}$, so $\sinh\frac{\psi}{2}=a$, $\cosh\frac{\psi}{2}=\sqrt{1+a^2}$ and $\psi=2\operatorname{arsinh}a$. Comparing the vector parts gives $\sinh\psi\,\vec u_{\mathrm b}=2(\vec B+\vec A\times\vec B)$. Since $\vec A\cdot\vec B=0$,

$$
\lVert\vec B+\vec A\times\vec B\rVert^2=\lVert\vec B\rVert^2+\lVert\vec A\times\vec B\rVert^2=a^2+a^4=a^2(1+a^2),
$$

so $2\lVert\vec B+\vec A\times\vec B\rVert=2a\sqrt{1+a^2}=\sinh\psi$. This gives the boxes for $\vec u_{\mathrm b}$ and $\tilde U_{\mathrm b}$.

**The rotor.** Put $c=\sqrt{1+a^2}$ and $w=\sinh\frac{\psi}{2}\vec u_{\mathrm b}=(\vec B+\vec A\times\vec B)/c$, so that $\tilde U_{\mathrm b}=c\,e_t+iw$. The candidate

$$
\tilde u_{\mathrm r}=\varepsilon\,\frac{e_t+\vec A}{c}
$$

is a unit real quaternion, because $(e_t+\vec A)(e_t-\vec A)=e_t-\vec A^2=(1+a^2)e_t=c^2e_t$. Moreover, using $\vec B\vec A=-\vec A\times\vec B$ and $(\vec A\times\vec B)\vec A=a^2\vec B$,

$$
w(e_t+\vec A)=\frac{(\vec B+\vec A\times\vec B)(e_t+\vec A)}{c}=c\,\vec B,
$$

hence

$$
\tilde U_{\mathrm b}\tilde u_{\mathrm r}
=(c\,e_t+iw)\,\varepsilon\,\frac{e_t+\vec A}{c}
=\varepsilon\bigl(e_t+\vec A+i\vec B\bigr)
=\varepsilon(e_t+\vec\Upsilon)=\tilde U.
$$

By the uniqueness of the polar decomposition, this is the rotor, and the box for $\tilde u_{\mathrm r}$ follows.

**The angles.** From the box, $\operatorname{Sc}\tilde u_{\mathrm r}=\varepsilon/c$ and $\mathrm{Vect}\tilde u_{\mathrm r}=\varepsilon\vec A/c$. With $\theta\in[0,2\pi]$, $\cos\frac{\theta}{2}=\varepsilon/c$ and $\sin\frac{\theta}{2}=a/c\ge0$. For $\varepsilon=+1$ this gives $\frac{\theta}{2}=\arctan a$; for $\varepsilon=-1$ it gives $\frac{\theta}{2}=\pi-\arctan a$. Hence the box for $\theta$, and

$$
\vec u_{\mathrm r}=\frac{\mathrm{Vect}\tilde u_{\mathrm r}}{\sin\frac{\theta}{2}}
=\varepsilon\,\frac{\vec A}{a}.
$$

**The scalar line.** If $a=0$ then $\vec B=0$ and $\vec A=0$, so $\vec\Upsilon=0$ and $\tilde Q=Q_te_t$. Then $\psi=0$, and the rotor is $\varepsilon e_t$, that is, $\theta=0$ for $\varepsilon=+1$ and $\theta=2\pi$ for $\varepsilon=-1$. Both axes are arbitrary. $\square$

**Check.** For

$$
\tilde Q=e_t+\frac{i}{\sqrt2}\vec e_x+\vec e_y+\frac{i}{\sqrt2}\vec e_z,
$$

one has $\vec A=\vec e_y$, $\vec B=(\vec e_x+\vec e_z)/\sqrt2$, $a=1$, $Q_t=1$, $\varepsilon=1$. The boxes give

$$
\psi=1.762747174,\qquad
\theta=\frac{\pi}{2},\qquad
\vec u_{\mathrm b}=\vec e_x,\qquad
\vec u_{\mathrm r}=\vec e_y,\qquad
\tilde u_{\mathrm r}=\frac{e_t+\vec e_y}{\sqrt2},\qquad
\tilde U_{\mathrm b}=\sqrt2\,e_t+i\vec e_x.
$$

## The Domain

### The Defining Condition

Let

$$
\tilde Q=Q_te_t+Q_x\vec e_x+Q_y\vec e_y+Q_z\vec e_z,
\qquad
N=\langle\tilde Q\rangle_{\natural}=Q_t^2+Q_x^2+Q_y^2+Q_z^2,
\qquad
B^2=Q_x^2+Q_y^2+Q_z^2.
$$

The **spectrally degenerate sector** is

$$
\Sigma_{10}=\{\tilde Q\in\mathbb{B}:\ N\neq0,\ B^2=0\}.
$$

The name is the one of *The Spectrum*: the element is N-regular when $N\neq0$, and spectrally degenerate when $B^2=0$. The sector is one of the four of the algebra; this article treats the combination $10$, and the companion treats $11$.

### The Normal Form

**Proposition (the normal form).** Every $\tilde Q\in\Sigma_{10}$ has a unique writing

$$
\boxed{\tilde Q=Q_t\bigl(e_t+\vec\Upsilon\bigr)},
\qquad
\vec\Upsilon^2=0,
\qquad
Q_t\neq0,
$$

with $Q_t$ the scalar part and $\vec\Upsilon$ the vector part divided by $Q_t$.

*Proof.* Since $B^2=0$ the vector part is null, $\vec Q^2=-B^2=0$. Since $N=Q_t^2+B^2=Q_t^2$ and $N\neq0$, the scalar part is nonzero. Put $\vec\Upsilon=\vec Q/Q_t$; then $\vec\Upsilon^2=\vec Q^2/Q_t^2=0$, and $\tilde Q=Q_te_t+\vec Q=Q_t(e_t+\vec\Upsilon)$. The writing is unique because $Q_t$ is the scalar part. $\square$

The element is a scalar multiple of a unipotent element. The unipotent factor $e_t+\vec\Upsilon$ has norm one, because

$$
\langle e_t+\vec\Upsilon\rangle_{\natural}=1+\vec\Upsilon^2=1,
$$

and it is invertible, with inverse $e_t-\vec\Upsilon$.

### The Two Strata

The vanishing of $\vec\Upsilon$ cuts the sector into two strata.

| Stratum | Condition | Form | Real dimension |
|---|---|---|---|
| scalar line | $\vec\Upsilon=0$ | $Q_te_t$ | $2$ |
| Jordan part | $\vec\Upsilon\neq0$ | $Q_t(e_t+\vec\Upsilon)$ | $6$ |

The scalar line is the set of nonzero complex scalars; it is closed in the sector and of measure zero. The Jordan part is open and dense; it is the set on which the minimal polynomial is $(X-Q_t)^2$ and the geometric multiplicity is one. The two strata are the two possible Jordan forms of an element with a single eigenvalue.

The sector is connected, of complex dimension $3$ and real dimension $6$. It is closed under inversion,

$$
\tilde Q^{-1}=Q_t^{-1}\bigl(e_t-\vec\Upsilon\bigr)\in\Sigma_{10},
$$

but it is not closed under multiplication; §*The Group Law* gives the exact criterion. It is not a subgroup: the identity lies in it, but the product of two elements can leave it.

### The Unit Factor

The modulus is the principal square root of $N=Q_t^2$. Since $Q_t^2$ has the two square roots $\pm Q_t$, the modulus is $\Rho=\pm Q_t$, and the unit factor is

$$
\tilde U=\frac{\tilde Q}{\Rho}
=\frac{Q_t}{\Rho}\bigl(e_t+\vec\Upsilon\bigr)
=\varepsilon\bigl(e_t+\vec\Upsilon\bigr),
\qquad
\varepsilon=\frac{Q_t}{\Rho}=\pm1.
$$

The sign $\varepsilon$ is fixed by the branch of the modulus. It is $+1$ when $\Rho=Q_t$ and $-1$ when $\Rho=-Q_t$. The unit factor is therefore $\pm$unipotent, and the sign is the only trace of the scalar part that survives in it.

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

The scalars are central; the two exponentials are not. The order of the factors is part of the definition: the boost stands to the left of the rotor.

### The Four Factors

| Factor | Exponent | Closed form | Range |
|---|---|---|---|
| scale | $\ln r$ | $r$ | $r>0$ |
| phase | $i\alpha$ | $e^{i\alpha}$ | $\alpha\in(-\frac{\pi}{2},\frac{\pi}{2}]$ |
| boost | $i\frac{\psi}{2}\vec u_{\mathrm b}$ | $\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}$ | $\psi\ge0$ |
| rotor | $\frac{\theta}{2}\vec u_{\mathrm r}$ | $\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}$ | $\theta\in[0,2\pi]$ |

The boost is Hermitian positive of norm one; the rotor is a unit real quaternion. The product is the unit factor $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, and $\tilde Q=\Rho\tilde U$ with $\Rho=r e^{i\alpha}$.

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

The scalar part is

$$
\operatorname{Sc}\tilde U=c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c,
$$

and the vector part is the remaining three terms. The norm of $\tilde U$ is one, so

$$
\bigl(\operatorname{Sc}\tilde U\bigr)^2+\vec U\cdot\vec U=1.
$$

## The Unipotent Unit Factor

### The Scalar Constraint

**Theorem (the rigidity of the word).** Let $\tilde Q\in\Sigma_{10}$ with word as above. Then

$$
\operatorname{Sc}\tilde U=\varepsilon=\pm1,
\qquad
\bigl(\tilde U-\varepsilon e_t\bigr)^2=0,
$$

and the parameters satisfy

$$
\boxed{\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon},
\qquad
\boxed{\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0}.
$$

*Proof.* By the normal form, $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ with $\vec\Upsilon^2=0$. Its scalar part is $\varepsilon$, and

$$
\bigl(\tilde U-\varepsilon e_t\bigr)^2
=\varepsilon^2\vec\Upsilon^2=0.
$$

The scalar part of the component form is $c_{\mathrm b}c_{\mathrm r}-i s_{\mathrm b}s_{\mathrm r}c$. It equals the real number $\varepsilon$, so its imaginary part vanishes, which gives the second equation, and its real part gives the first. $\square$

The two equations are the whole constraint. The scalar part of the unit factor is a complex equation, and the unitarity of $\tilde U$ has already been used; the constraint is one complex equation on the six parameters of the unit factor, which is why the unipotent set has real dimension four.

### The Orthogonal Frame

**Theorem (the orthogonal frame).** On the Jordan part of $\Sigma_{10}$, the word has

$$
\psi>0,
\qquad
\theta\notin\{0,\pi,2\pi\},
\qquad
\vec u_{\mathrm b}\perp\vec u_{\mathrm r},
$$

and the two angles are tied by

$$
\boxed{\Bigl\lvert\cos\frac{\theta}{2}\Bigr\rvert=\frac{1}{\cosh\frac{\psi}{2}}},
\qquad
\varepsilon=\operatorname{sgn}\cos\frac{\theta}{2}.
$$

Conversely, every choice of $\theta\in(0,\pi)\cup(\pi,2\pi)$, of $\vec u_{\mathrm b}\in S^2$ and of $\vec u_{\mathrm r}$ in the great circle orthogonal to $\vec u_{\mathrm b}$, with $\psi$ defined by the displayed relation, gives a word of an element of the Jordan part.

*Proof.* On the Jordan part $\vec\Upsilon\neq0$, so $\tilde U\neq\varepsilon e_t$. If $\psi=0$ then $c_{\mathrm b}=1$ and the first constraint gives $c_{\mathrm r}=\pm1$, so $\theta\in\{0,2\pi\}$ and the component form is $\tilde U=\pm e_t$, a contradiction. Hence $\psi>0$ and $s_{\mathrm b}>0$. If $\theta=0$ or $2\pi$ then $s_{\mathrm r}=0$ and the component form is again scalar. If $\theta=\pi$ then $c_{\mathrm r}=0$, and the first constraint gives $0=\pm1$, impossible. Hence $\theta\notin\{0,\pi,2\pi\}$ and $s_{\mathrm r}>0$. The second constraint then forces $c=0$. The first gives $|c_{\mathrm b}c_{\mathrm r}|=1$, which is the displayed relation, and the sign of $c_{\mathrm r}$ is the sign of $\varepsilon$. The converse is a direct substitution: with orthogonal axes and the relation, the scalar part is $\varepsilon$ and the vector part is null, so the unit factor is unipotent and the element lies in the Jordan part. $\square$

The frame is therefore orthogonal, and one of the two angles is a function of the other. The independent data of the unipotent factor are one angle and a frame: $\theta$ (one real number), $\vec u_{\mathrm b}$ (two), and $\vec u_{\mathrm r}$ in the orthogonal circle (one), which is four real dimensions, the dimension of the punctured nilpotent cone.

### The Closed Form

Substituting the constraints into the component form gives the shape of the whole sector.

**Theorem (the closed form).** Every $\tilde Q\in\Sigma_{10}$ is

$$
\boxed{\;
\tilde Q=Q_t\Bigl(e_t+
i\tanh\frac{\psi}{2}\,\vec u_{\mathrm b}
+\tan\frac{\theta}{2}\,\vec u_{\mathrm r}
+i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}\Bigr)
\;}
$$

with $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon$; on the Jordan part the two axes are orthogonal. Equivalently,

$$
\boxed{\;
\tilde Q=Q_t\Bigl(e_t+\vec\Upsilon\Bigr),
\qquad
\vec\Upsilon=i\tanh\frac{\psi}{2}\,\vec u_{\mathrm b}
+\tan\frac{\theta}{2}\,\vec u_{\mathrm r}
+i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\;}
$$

*Proof.* The scalar part of the unit factor is $\varepsilon$, so $c_{\mathrm r}=\varepsilon/c_{\mathrm b}$. On the Jordan part $s_{\mathrm r}>0$, and $\tan\frac{\theta}{2}=s_{\mathrm r}/c_{\mathrm r}=\varepsilon c_{\mathrm b}s_{\mathrm r}$, hence $s_{\mathrm r}=\varepsilon\tan\frac{\theta}{2}/c_{\mathrm b}$. The component form then gives

$$
i s_{\mathrm b}c_{\mathrm r}
=i\varepsilon\tanh\frac{\psi}{2},
\qquad
c_{\mathrm b}s_{\mathrm r}
=\varepsilon\tan\frac{\theta}{2},
\qquad
i s_{\mathrm b}s_{\mathrm r}
=i\varepsilon\tanh\frac{\psi}{2}\tan\frac{\theta}{2}.
$$

The vector part of the unit factor is $\varepsilon$ times the bracket, and $\tilde U=\varepsilon(e_t+\vec\Upsilon)$, so the bracket is $\vec\Upsilon$; hence $\tilde Q=Q_t(e_t+\vec\Upsilon)$. On the scalar line $\tan\frac{\theta}{2}=\tanh\frac{\psi}{2}=0$, and the same display reduces to $Q_te_t$. $\square$

The formula is the exact shape of the sector. The complex number $Q_t$ carries the scale and the phase; the rest is a unipotent written in the frame. The vector part is automatically null: with the three orthogonal directions, its square is

$$
\vec\Upsilon^2=\tanh^2\frac{\psi}{2}-\tan^2\frac{\theta}{2}
+\tanh^2\frac{\psi}{2}\tan^2\frac{\theta}{2},
$$

which vanishes by $|\cos\frac{\theta}{2}|=1/\cosh\frac{\psi}{2}$. The cross term carries the plus sign because its coefficient is imaginary.

**Remark (the scalar factor).** The unit factor depends only on $\theta$ and the frame, not on $Q_t$. Changing $Q_t$ by a nonzero complex number changes the scale and the phase, and possibly the sign $\varepsilon$, but leaves $\vec\Upsilon$ unchanged. The sector is the product of the scalar line $\mathbb{C}^{\times}$ with the punctured nilpotent cone; the frame and the two angles are functions of the second factor alone, and the sign is carried by the first.

## The Two Strata

### The Scalar Line

On the scalar line $\vec\Upsilon=0$, the element is $Q_te_t$, the unit factor is $\varepsilon e_t$, and

$$
\psi=0,
\qquad
\theta\in\{0,2\pi\},
\qquad
\vec u_{\mathrm b},\vec u_{\mathrm r}\ \text{free}.
$$

The word is

$$
\tilde Q=r e^{i\alpha}\,\varepsilon e_t
=Q_te_t.
$$

The sign $\varepsilon$ is fixed by the branch: if $\Rho=Q_t$ then $\varepsilon=+1$ and $\theta=0$; if $\Rho=-Q_t$ then $\varepsilon=-1$ and $\theta=2\pi$. The axes are undefined, because the boost and the rotor are central. The scalar line is the normal locus of the sector: a normal element with a single eigenvalue is a scalar, and every scalar is normal.

### The Jordan Part

On the Jordan part $\vec\Upsilon\neq0$, the element is defective: its minimal polynomial is $(X-Q_t)^2$, its geometric multiplicity is one, and it has no eigenbasis. The word has

$$
\psi>0,
\qquad
\theta\in(0,\pi)\cup(\pi,2\pi),
\qquad
\vec u_{\mathrm b}\perp\vec u_{\mathrm r},
$$

and the two possible signs of $\cos\frac{\theta}{2}$ are the two values of $\varepsilon$. The word is

$$
\tilde Q=Q_t\Bigl(e_t+\vec\Upsilon(\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})\Bigr),
$$

with $\vec\Upsilon$ as in the closed form and $\psi$ determined by $\theta$. The data are

$$
\underbrace{2}_{Q_t}
+\underbrace{1}_{\theta}
+\underbrace{2}_{\vec u_{\mathrm b}}
+\underbrace{1}_{\vec u_{\mathrm r}\perp\vec u_{\mathrm b}}
=6,
$$

the real dimension of the sector. The rapidity and the sign are functions of the angle.

The Jordan part is unbounded: as $\theta\to\pi$, $\psi\to\infty$ and $|\vec\Upsilon|\to\infty$. The value $\theta=\pi$ is not attained, because it would force $c_{\mathrm r}=0$ and violate the scalar constraint.

## Existence and Uniqueness

**Theorem (the exponential polar decomposition).** Every $\tilde Q\in\Sigma_{10}$ has a unique writing

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

gives a unique factorization $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde U_{\mathrm b}\in P$ and $\tilde u_{\mathrm r}\in K$. A positive Hermitian determinant-one matrix is the exponential of a unique Hermitian traceless matrix, which is $i\frac{\psi}{2}\vec u_{\mathrm b}$ with $\psi\ge0$ and a unit axis. A $*$-unitary determinant-one matrix is the exponential of an anti-Hermitian traceless matrix, which is $\frac{\theta}{2}\vec u_{\mathrm r}$ with $\theta\in[0,2\pi]$. The endpoint $\theta=2\pi$ is the central rotor $-e_t$, where the axis is undefined. The scale and the phase are the polar coordinates of $\Rho$, unique in the branch. $\square$

The proof uses only the invertibility of $\tilde Q$; the degeneracy $B^2=0$ enters only through the domain. This is why the companion article can repeat the same theorem verbatim.

**The degeneracies.** The boost axis is undefined at $\psi=0$; the rotor axis is undefined at $\theta=0$ and $\theta=2\pi$. In this sector the first case is the scalar line and the second contains it; on the Jordan part both angles are nonzero and both axes are defined and orthogonal.

| Parameter | Range | Unique? |
|---|---|---|
| $r$ | $(0,\infty)$ | yes |
| $\alpha$ | $(-\frac{\pi}{2},\frac{\pi}{2}]$ | yes: the branch |
| $\psi$ | $[0,\infty)$ | yes |
| $\vec u_{\mathrm b}$ | $S^2$ | no: undefined at $\psi=0$ |
| $\theta$ | $[0,2\pi]$ | yes |
| $\vec u_{\mathrm r}$ | $S^2$ | no: undefined at $\theta\in\{0,2\pi\}$ |

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

of real dimensions $1+1+3+3=8$.

### The Exact Logarithm

The special feature of the sector is that the true logarithm is not a transcendental object: the unipotent factor has a truncated logarithm.

**Theorem (the exact logarithm).** For $\tilde Q=Q_t(e_t+\vec\Upsilon)\in\Sigma_{10}$,

$$
\boxed{\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon},
$$

where $\log Q_t$ is any logarithm of the nonzero complex number $Q_t$ and the principal choice is $\ln|Q_t|+i\arg Q_t$. The right-hand side is exact, with no series and no correction.

*Proof.* The exponential of a nilpotent element truncates:

$$
\exp(\vec\Upsilon)=e_t+\vec\Upsilon,
$$

because $\vec\Upsilon^2=0$. The scalar $Q_t$ commutes with $\vec\Upsilon$, so

$$
\exp(\log Q_t+\vec\Upsilon)=Q_t(e_t+\vec\Upsilon)=\tilde Q.
$$

$\square$

The logarithm is the sum of the scalar logarithm and the nilpotent vector part. The period $2\pi ik\,e_t$ can be added to the scalar logarithm, and no other ambiguity is present on the Jordan part: the logarithm is unique modulo the central periods, because the nilpotent part is fixed by $\tilde Q$.

The operator form of this single exponent is in §*The Exponential at the Wall* of *The One-Sided Operators of a N-Regular, Spectrally Degenerate Biquaternion* and of *The Sandwich of a N-Regular, Spectrally Degenerate Biquaternion*: the exponential of the left multiplication is the shear $\exp(L_{\tilde Q})=e^{Q_t}(I+Q_tL_{\vec\Upsilon})$, and the sandwich is the null rotation $\Theta_{\tilde Q}=|Q_t|^2e^{A+B}$.

### The Formal Exponent and the Defect

The **formal exponent** is the sum of the four exponents,

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

It is not the logarithm. The true logarithm is

$$
\operatorname{Log}\tilde Q=\ln r+i\alpha+i\pi\frac{1-\varepsilon}{2}+\vec\Upsilon,
$$

because $Q=\Rho\tilde U$ with $\Log\tilde U=\vec\Upsilon+i\pi\frac{1-\varepsilon}{2}$, so $\Log\tilde Q=\log\Rho+\Log\tilde U$; equivalently, $\log Q_t=\log\Rho+i\pi\frac{1-\varepsilon}{2}$ and the unipotent part adds $\vec\Upsilon$. The **log defect** is therefore explicit:

$$
\boxed{\;
\operatorname{Log}\tilde Q-\tilde Q_{\log}
=i\pi\frac{1-\varepsilon}{2}
+i\Bigl(\varepsilon\tanh\frac{\psi}{2}-\frac{\psi}{2}\Bigr)\vec u_{\mathrm b}
+\Bigl(\varepsilon\tan\frac{\theta}{2}-\frac{\theta}{2}\Bigr)\vec u_{\mathrm r}
+i\varepsilon\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\;\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
\;}
$$

The **defect** is the norm of $\exp(\tilde Q_{\log})-\tilde Q$, not the norm of the log defect, because the exponential is not linear. The log defect shows the three corrections: the scalar period, the nonlinear terms $\varepsilon\tanh\frac{\psi}{2}-\frac{\psi}{2}$ and $\varepsilon\tan\frac{\theta}{2}-\frac{\theta}{2}$, and the cross term. The numerical defect is computed in the worked examples.

On the Jordan part the cross term is nonzero, because $\psi>0$, $\theta\notin\{0,\pi,2\pi\}$ and the axes are orthogonal. The formal exponent is therefore not the logarithm. The cross term has the shape of the first correction of the Baker–Campbell–Hausdorff series,

$$
\frac12[\tilde H,\tilde K]
=\frac{i\psi\theta}{4}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

with the sign of $\varepsilon$; the exact log defect also contains the nonlinear terms $\varepsilon\tanh\frac{\psi}{2}-\frac{\psi}{2}$ and $\varepsilon\tan\frac{\theta}{2}-\frac{\theta}{2}$.

On the scalar line the cross term is absent, and the formal exponent is a logarithm: for $\varepsilon=+1$ it is $\ln r+i\alpha$, and for $\varepsilon=-1$ it is $\ln r+i\alpha+\pi\vec u_{\mathrm r}$, whose exponential is $-\Rho$ for every unit $\vec u_{\mathrm r}$.

### The Fibre

The exponential is not injective. Its kernel contains the central periods $2\pi ik\,e_t$, the pure periods $2\pi\vec U$ for real unit vectors, and the mixed elements $\pi i\,e_t+\pi\vec U$. The fibre over an element is not a coset of the kernel, because the exponential is not a homomorphism.

On the Jordan part the fibre is cut to one point, up to the axis degeneracies, by the word map

$$
(r,\alpha,\psi,\vec u_{\mathrm b},\theta,\vec u_{\mathrm r})
\longmapsto
r e^{i\alpha}\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr).
$$

The word is a section of that map, not of the exponential. The exact logarithm $\log Q_t+\vec\Upsilon$ is a section of the exponential modulo the central periods; it is not the formal exponent.

## The Group Law

The sector is closed under inversion:

$$
\tilde Q^{-1}=Q_t^{-1}\bigl(e_t-\vec\Upsilon\bigr).
$$

It is not closed under multiplication. The product of two elements is

$$
\tilde Q_1\tilde Q_2
=Q_{t1}Q_{t2}\bigl(e_t+\vec\Upsilon_1\bigr)\bigl(e_t+\vec\Upsilon_2\bigr)
=Q_{t1}Q_{t2}\bigl(e_t+\vec\Upsilon_1+\vec\Upsilon_2+\vec\Upsilon_1\vec\Upsilon_2\bigr).
$$

Let

$$
s=\vec\Upsilon_1\cdot\vec\Upsilon_2.
$$

The scalar part of the product is $Q_{t1}Q_{t2}(1-s)$, and the product has norm one, so its vector form is

$$
\boxed{B^2(\tilde Q_1\tilde Q_2)=Q_{t1}^2Q_{t2}^2\,s(2-s)}.
$$

The product lies in $\Sigma_{10}$ exactly when $s=0$ or $s=2$; otherwise it lies in $\Sigma_{11}$.

*Proof.* Write the product as $Q_{t1}Q_{t2}W$, with $W=(1+\vec\Upsilon_1)(1+\vec\Upsilon_2)$. The scalar part of $W$ is $1-\vec\Upsilon_1\cdot\vec\Upsilon_2=1-s$, because the dot part of $\vec\Upsilon_1\vec\Upsilon_2$ is $-\vec\Upsilon_1\cdot\vec\Upsilon_2$ and the cross part is a pure vector. The norm of $W$ is one, because it is the product of two unipotent elements of norm one. An element of norm one with scalar part $1-s$ has vector form $1-(1-s)^2=s(2-s)$; the central scalar $Q_{t1}Q_{t2}$ multiplies the vector form by $(Q_{t1}Q_{t2})^2$. $\square$

**Example.** Take $u_1=e_t+\vec e_x+i\vec e_y$ and $u_2=e_t+\vec e_y+i\vec e_z$. Then $s=i$, and

$$
u_1u_2=(1-i)e_t+\vec e_y+(1+i)\vec e_z,
$$

with $B^2=1+2i\neq0$. The product has left the sector. Take instead $u_1$ and $u_2=e_t+\vec e_x-i\vec e_y$; then $s=2$, and

$$
u_1u_2=-e_t+2\vec e_x-2i\vec e_z,
$$

with $B^2=0$; the product stays. The two cases are the two roots of $s(2-s)=0$.

The bracket structure is the one of the Cartan pair.

| Bracket | Lies in | Reading |
|---|---|---|
| $[\mathfrak{k},\mathfrak{k}]$ | $\mathfrak{k}$ | two rotors compose to a rotor |
| $[\mathfrak{p},\mathfrak{p}]$ | $\mathfrak{k}$ | two boosts compose to a boost times a rotor |
| $[\mathfrak{k},\mathfrak{p}]$ | $\mathfrak{p}$ | a rotor conjugates a boost to a boost |

The sector is a subset of the group, not a subgroup: it is inverse-closed, and the product of two of its elements stays in it only on the quadric $s(2-s)=0$.

## The Matrix Picture

The matrix model is

$$
\mathsf M(\tilde Q)=Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z.
$$

It is a $\mathbb{C}$-algebra homomorphism, so $\mathsf M(\exp\tilde X)=\exp(\mathsf M(\tilde X))$, and the polar word becomes the polar decomposition of $\mathrm{GL}_2(\mathbb{C})$,

$$
\mathsf M(\tilde Q)=r e^{i\alpha}\,\mathsf M(\tilde U_{\mathrm b})\,\mathsf M(\tilde u_{\mathrm r}),
$$

with $\mathsf M(\tilde U_{\mathrm b})$ positive definite of determinant one and $\mathsf M(\tilde u_{\mathrm r})$ $*$-unitary of determinant one.

On the Jordan part, $\mathsf M(\vec\Upsilon)$ is a nonzero nilpotent matrix, so

$$
\mathsf M(\tilde Q)=Q_t\bigl(I+N\bigr),
\qquad
N=\mathsf M(\vec\Upsilon),
\qquad
N^2=0,
\qquad
N\neq0.
$$

The matrix is $Q_t$ times a single unipotent Jordan block. Its eigenvalue is $Q_t$, with algebraic multiplicity two and geometric multiplicity one; its determinant is $Q_t^2$; its two singular values are $r e^{\psi/2}$ and $r e^{-\psi/2}$. The polar factors are the positive and $*$-unitary factors of the block, and the $*$-unitary factor is the rotor. The sign $\varepsilon$ is the sign of the scalar part of the unit block.

The spectral reading is degenerate in the matrix picture: the matrix has no eigenbasis, the two eigenvalues coincide, and the diagonal form does not exist. The polar decomposition still exists, because it is the Cartan decomposition of $SL(2,\mathbb{C})$, which does not require diagonalizability. This is the matrix form of the contrast between the two articles.

## The Exponential Coordinates

The data of the sector are

$$
\underbrace{2}_{Q_t}
+\underbrace{1}_{\theta}
+\underbrace{2}_{\vec u_{\mathrm b}}
+\underbrace{1}_{\vec u_{\mathrm r}\perp\vec u_{\mathrm b}}
=6,
$$

the real dimension of $\Sigma_{10}$. The rapidity and the sign are determined by

$$
\cosh\frac{\psi}{2}=\frac{1}{\lvert\cos\frac{\theta}{2}\rvert},
\qquad
\varepsilon=\operatorname{sgn}\cos\frac{\theta}{2}.
$$

The coordinate map is

$$
(Q_t,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})
\longmapsto
Q_t\Bigl(e_t+\vec\Upsilon(\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})\Bigr),
$$

from $\mathbb{C}^{\times}\times\bigl((0,\pi)\cup(\pi,2\pi)\bigr)\times US^2$ to the Jordan part, where $US^2=\{(\vec u_{\mathrm b},\vec u_{\mathrm r}):\lvert\vec u_{\mathrm b}\rvert=\lvert\vec u_{\mathrm r}\rvert=1,\ \vec u_{\mathrm b}\perp\vec u_{\mathrm r}\}$ is the unit tangent bundle of the sphere. It is a bijection onto the Jordan part; the scalar line is the common limit $\theta\to0$ and $\theta\to2\pi$, where the frame is free.

The coordinate lines are three families:

- the **scalar line** $Q_t\mapsto Q_t(e_t+\vec\Upsilon)$, a complex plane with the origin removed;
- the **angle line** $\theta\mapsto Q_t(e_t+\vec\Upsilon(\theta,\ldots))$, a non-compact curve from the scalar line to infinity, with $\psi$ growing as $\theta\to\pi$;
- the **frame sphere** $(\vec u_{\mathrm b},\vec u_{\mathrm r})\mapsto Q_t(e_t+\vec\Upsilon)$, a circle bundle over $S^2$.

The sector retracts onto the scalar line, because the nilpotent part can be contracted to zero along $\vec\Upsilon\mapsto(1-t)\vec\Upsilon$, which stays null. Hence $\Sigma_{10}$ is connected and $\pi_1(\Sigma_{10})=\mathbb{Z}$, carried by the phase of $Q_t$.

The **conformal factor** is read in the coordinates. Under the sandwich $\tilde QX\tilde Q^*$, the quaternionic norm of $X$ is multiplied by

$$
|Q_t|^4=\bigl\lvert\langle\tilde Q\rangle_{\natural}\bigr\rvert^2,
$$

so lengths are multiplied by $|Q_t|^2=\lvert\langle\tilde Q\rangle_{\natural}\rvert$. The scale is the modulus of the scalar part; the angle and the frame are isometries of the form.

## The Boundary

The sector is closed under inversion but not under multiplication. It is a complex hypersurface of $\mathbb{B}$, not an open set: its closure is the spectral cone $B^2=0$, and the points of that closure with $N=0$ form the nilpotent stratum $\Sigma_{00}$.

### The Nilpotent Stratum

As $Q_t\to0$ with $\vec\Upsilon$ fixed, the element tends to zero and the modulus tends to zero. The unit factor does not degenerate:

$$
\tilde U=\varepsilon\bigl(e_t+\vec\Upsilon\bigr)
$$

is independent of $Q_t$. The scale collapses, the phase follows the argument of $Q_t$, and the unipotent shape survives. This is the structural difference from the regular sector, where the rapidity diverges as the modulus vanishes. In $\Sigma_{10}$ the modulus is the scalar part, and the only thing that vanishes is the scalar.

A nonzero nilpotent of $\Sigma_{00}$ is reached by letting $Q_t\to0$ and $\vec\Upsilon\to\infty$ at the rate $Q_t\vec\Upsilon\to\vec N$ with $\vec N^2=0$. The unit factor diverges, the word parameters leave every bounded set, and the limit is the nilpotent. The sector is not compact, and the angle $\theta\to\pi$ is the direction in which it is unbounded.

### The Spectral Wall

Seen from $\Sigma_{11}$, the locus $B^2=0$ is a wall: the word converges to the word of the limit, as the companion article proves, while the eigenbasis diverges and the spectral decomposition disappears. Seen from $\Sigma_{10}$, the same locus is the ambient space. The two descriptions are the two sides of one hypersurface: defective elements, no eigenbasis, and a polar word that is still defined.

| Approach | Locus | What happens |
|---|---|---|
| nilpotent stratum | $N=0$, $B^2=0$ | $Q_t\to0$; the unit factor survives if $\vec\Upsilon$ is fixed; the scale vanishes |
| spectral wall from $\Sigma_{11}$ | $B^2=0$, $N\neq0$ | the word converges; the eigenbasis diverges |

## Summary

### Main Formulas

| Object | Formula |
|---|---|
| domain | $N\neq0$, $B^2=0$ |
| normal form | $\tilde Q=Q_t(e_t+\vec\Upsilon)$, $\vec\Upsilon^2=0$ |
| word | $\tilde Q=r e^{i\alpha}\exp(i\frac{\psi}{2}\vec u_{\mathrm b})\exp(\frac{\theta}{2}\vec u_{\mathrm r})$ |
| unit factor | $\tilde U=\varepsilon(e_t+\vec\Upsilon)$, $\varepsilon=Q_t/\Rho=\pm1$ |
| scalar constraint | $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\varepsilon$ |
| axis constraint | $\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$ |
| Jordan part | $\psi>0$, $\theta\notin\{0,\pi,2\pi\}$, $\vec u_{\mathrm b}\perp\vec u_{\mathrm r}$ |
| angle relation | $|\cos\frac{\theta}{2}|=1/\cosh\frac{\psi}{2}$ |
| closed form | $\tilde Q=Q_t\bigl(e_t+i\tanh\frac{\psi}{2}\vec u_{\mathrm b}+\tan\frac{\theta}{2}\vec u_{\mathrm r}+i\tanh\frac{\psi}{2}\tan\frac{\theta}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}\bigr)$ |
| exact logarithm | $\operatorname{Log}\tilde Q=\log Q_t+\vec\Upsilon$ |
| formal exponent | $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$ |
| log defect | the five-term difference of §*The Formal Exponent and the Defect* |
| defect | $\lVert\exp(\tilde Q_{\log})-\tilde Q\rVert$, computed in the worked examples |
| explicit data | §*The Result in Terms of the Coordinates*: boxes for $r,\Rho,\varepsilon,\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r},\tilde u_{\mathrm r},\tilde U_{\mathrm b}$ |
| product criterion | $B^2(\tilde Q_1\tilde Q_2)=Q_{t1}^2Q_{t2}^2s(2-s)$, $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$ |
| dimension | $6$: $Q_t$ (2), angles (2), frame (3), angle relation (1) |

### What the Sector Shows

- The word exists for every element of the sector, and it is unique up to the axis degeneracies.
- The unit factor is $\pm$unipotent. Its two eigenvalues coincide, its minimal polynomial is a square, and it has no eigenbasis.
- The scalar part of the unit factor is $\pm1$. This is one complex equation, and it forces the two angles to satisfy $\cosh\frac{\psi}{2}\cos\frac{\theta}{2}=\pm1$.
- On the Jordan part the two axes are orthogonal, and the rapidity is a function of the rotor angle. The word has four real data, not six.
- The true logarithm is exact and truncated, $\log Q_t+\vec\Upsilon$; the formal exponent is not a logarithm, and the log defect is the cross term plus the nonlinear terms.
- The sector is inverse-closed but not product-closed: the product of two elements stays in it exactly on $s(2-s)=0$.
- The sector is the limit of the regular one at $B^2=0$: the word survives everywhere, while the spectral basis survives only on the scalar line and degenerates on the Jordan part.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $Q_t,Q_x,Q_y,Q_z$ | the four complex coordinates |
| $Q_\mu=q_\mu+iq'_\mu$ | the eight real coordinates |
| $\vec q=(q_x,q_y,q_z)$, $\vec q'=(q'_x,q'_y,q'_z)$ | the real and imaginary vector coordinates |
| $N=\langle\tilde Q\rangle_{\natural}$ | the reduced product $Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| $B^2$ | the vector form $Q_x^2+Q_y^2+Q_z^2$ |
| $\Sigma_{10}$ | the N-regular, spectrally degenerate sector |
| $\vec\Upsilon=\vec Q/Q_t$ | the nilpotent direction, $\vec\Upsilon^2=0$ |
| $\vec A=\operatorname{Re}\vec\Upsilon$, $\vec B=\operatorname{Im}\vec\Upsilon$ | the real and imaginary parts, $\vec A\cdot\vec B=0$ |
| $a=\lVert\vec A\rVert=\lVert\vec B\rVert$ | the common length |
| $\Rho=r e^{i\alpha}$ | the modulus, principal square root of $N$ |
| $\varepsilon=Q_t/\Rho=\pm1$ | the sign of the unit factor |
| $\tilde U=\varepsilon(e_t+\vec\Upsilon)$ | the unit factor |
| $\tilde U_{\mathrm b}$ | the Hermitian positive factor |
| $\tilde u_{\mathrm r}$ | the rotor |
| $\psi$ | the rapidity |
| $\theta$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the two axes, orthogonal on the Jordan part |
| $c=\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | the cosine between the axes |
| $\tilde H,\tilde K$ | the Cartan pair |
| $\tilde Q_{\log}$ | the formal exponent |
| $s=\vec\Upsilon_1\cdot\vec\Upsilon_2$ | the product invariant |
| $\mathsf M(\tilde Q)$ | the matrix $Q_tI-iQ_x\sigma_x-iQ_y\sigma_y-iQ_z\sigma_z$ |
| $c_{\mathrm b},s_{\mathrm b},c_{\mathrm r},s_{\mathrm r}$ | the half-angle cosines and sines |

## Further Reading

- [Exponential Polar Decomposition of a N-Regular, Spectrally Regular Biquaternion](exponential-polar-decomposition-of-an-n-regular-spectrally-regular-biquaternion.html), the companion for $B^2\neq0$, independent of this article.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a N-Regular, Spectrally Degenerate Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-n-regular-spectrally-degenerate-biquaternion.html), for the polar word read against the Jordan form.
- [Worked Examples of Exponential Polar Decomposition of a N-Regular, Spectrally Degenerate Biquaternion](worked-examples-of-exponential-polar-decomposition-of-an-n-regular-spectrally-degenerate-biquaternion.html), for the numerical cases, the scalar line, the Jordan part and the defect tables.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus–unit theorem and the group of units.
- [The N-Regular, Spectrally Degenerate Sector](the-n-regular-spectrally-degenerate-sector.html), for the normal forms and the two strata.
- [The Spectrum](the-spectrum.html), for the four sectors and the discriminants.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the fibre.
- [Biquaternion Lie Group and Exponential Structure](biquaternion-lie-group-and-exponential-structure.html), for the Cartan decomposition and the Baker–Campbell–Hausdorff series.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
