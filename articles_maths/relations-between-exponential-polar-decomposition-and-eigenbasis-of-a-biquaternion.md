# __Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion__

## Introduction

A biquaternion carries two decompositions of the same element. The **eigenvalue decomposition** of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*, writes a biquaternion $\tilde Q=Q_te_t+\vec Q$ with $Q_x^2+Q_y^2+Q_z^2\neq0$ as

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\lambda_\pm=Q_t\pm i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2},
\quad
\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi),
\quad
\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2},
$$

with $\lambda_\pm$ the complex eigenvalues and $\tilde\Pi_\pm$ the eigenprojections. The square root is the branch fixed by the labelling of the two eigenvalues; the other branch exchanges $\lambda_+$ with $\lambda_-$ and $\tilde\Pi_+$ with $\tilde\Pi_-$. The **exponential polar decomposition** of *Exponential Polar Decomposition of Biquaternions* writes every invertible $\tilde Q$ as

$$
\tilde Q=r\,\exp(i\alpha)\,
\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\,
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$, $\psi\ge0$, $\theta\in[0,2\pi]$ and real unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$. This article states the relation between the two writings. It repeats no proof from the three source articles: the spectrum and the eigenprojections are those of the eigenvalue article, the exponential and the logarithm are those of the elementary article, and the polar word is that of the polar article.

The relation is richer than in the two commutative cases. There the eigenprojections are fixed and the two eigenvalues determine the polar parameters. Here the eigenprojections vary with the element, and the eigenvalues alone determine the modulus, the phase, and the two eigenvalues $\lambda_\pm/(re^{i\alpha})$ of the unit factor, equivalently its scalar part and $D=(\vec U\cdot\vec U)^{1/2}$. The remaining polar data — the split between the boost and the rotor and the two axes — are carried by the eigenprojections, or equivalently by the Cartan decomposition of the unit factor. The dictionary is therefore a two-step one: the eigenvalues give the scalar factor and the eigenvalues of the unit factor; the eigenprojections complete the unit factor.

**The results.** The product of the eigenvalues is the reduced product,

$$
\lambda_+\lambda_-=Q_t^2+Q_x^2+Q_y^2+Q_z^2=r^2e^{2i\alpha},
$$

so $r=\bigl\lvert Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr\rvert^{1/2}$ and $\alpha=\tfrac12\operatorname{Arg}\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)$. Write the unit factor as $\tilde U=\tilde Q/(re^{i\alpha})=U_te_t+\vec U$. Its two eigenvalues are

$$
\frac{\lambda_+}{re^{i\alpha}}=U_t+i\bigl(\vec U\cdot\vec U\bigr)^{1/2},
\qquad
\frac{\lambda_-}{re^{i\alpha}}=U_t-i\bigl(\vec U\cdot\vec U\bigr)^{1/2},
$$

and their sum is twice the scalar part:

$$
\frac{\lambda_++\lambda_-}{re^{i\alpha}}=2\operatorname{Sc}\tilde U
=2\Bigl(\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\Bigr).
$$

This is one complex equation for the three real data $(\psi,\theta,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})$. The eigenvalues therefore leave one real degree of freedom among the boost, the rotor and the angle between the axes; the eigenprojections supply it, together with the directions of the axes. The table summarises what each side determines.

| Question | Answer |
|---|---|
| Element | $\tilde Q=Q_te_t+\vec Q$ |
| Eigenvalues | $\lambda_\pm=Q_t\pm i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$; variable |
| Polar parameters | $r>0$, $\alpha$, $\psi\ge0$, $\theta\in[0,2\pi]$, axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$ |
| Scalar factor from eigenvalues | $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\alpha=\tfrac12\operatorname{Arg}(\lambda_+\lambda_-)$ |
| Unit factor from eigenvalues | $\lambda_\pm/(re^{i\alpha})=U_t\pm i(\vec U\cdot\vec U)^{1/2}$ |
| Scalar part of the unit factor | $\operatorname{Sc}\tilde U=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}$ |
| Eigenprojections from polar data | those of $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, independent of $r,\alpha$ |
| Eigenvalues from polar data | $re^{i\alpha}\bigl(U_t\pm i(\vec U\cdot\vec U)^{1/2}\bigr)$ |
| Common domain | the units, $Q_t^2+Q_x^2+Q_y^2+Q_z^2=\lambda_+\lambda_-\neq0$ |
| Spectral domain | $Q_x^2+Q_y^2+Q_z^2\neq0$, plus the scalar case; the Jordan case has no two-term decomposition |

## The Two Decompositions

### The Eigenvalue Decomposition

For $\tilde Q=Q_te_t+\vec Q$, the spectrum is

$$
\sigma(\tilde Q)=\Bigl\{Q_t+i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2},\
Q_t-i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}\Bigr\}.
$$

The eigenvalues are distinct exactly when $Q_x^2+Q_y^2+Q_z^2\neq0$. In that case

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-,
\qquad
\tilde\Pi_\pm=\frac12(e_t\pm\vec\Xi),
\qquad
\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2},
$$

with $\tilde\Pi_\pm$ primitive, orthogonal and complete, but noncentral. They depend on $\tilde Q$: they are the two idempotents of the pure root $\vec\Xi$, and $\vec\Xi=\tilde\Pi_+-\tilde\Pi_-$. These are the statements of *The Spectrum*, §*The Spectral Criterion* and §*The Spectral Decomposition*.

| Spectral item | Value |
|---|---|
| Spectrum | $\Bigl\{Q_t+i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2},\ Q_t-i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}\Bigr\}$ |
| Sum | $\lambda_++\lambda_-=2Q_t$ |
| Product | $\lambda_+\lambda_-=Q_t^2+Q_x^2+Q_y^2+Q_z^2$ |
| Distinctness | $\lambda_+\neq\lambda_-\iff Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Eigenprojections | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$, $\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$ |
| Decomposition | $\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ in the distinct case |

### The Exponential Polar Decomposition

Every unit $\tilde Q\in\mathbb{B}^\times=\{Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0\}$ has a writing, unique up to the degeneracies of the axes,

$$
\tilde Q=r\,\exp(i\alpha)\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},
\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\quad
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with

$$
r>0,\quad
\alpha\in\Bigl(-\frac{\pi}{2},\frac{\pi}{2}\Bigr],\quad
\psi\ge0,\quad
\theta\in[0,2\pi],\quad
\lvert\vec u_{\mathrm b}\rvert=\lvert\vec u_{\mathrm r}\rvert=1.
$$

The factors are the scale $r$, the phase $\zeta=e^{i\alpha}$, the boost $\tilde U_{\mathrm b}$ and the rotor $\tilde u_{\mathrm r}$, in this order. The boost and the rotor do not commute in general, and the order matters. These are the statements of *Exponential Polar Decomposition of Biquaternions*, §*The Decomposition*, §*Existence and Uniqueness* and §*The Cartan Logarithm*.

| Polar item | Value |
|---|---|
| Domain | $\mathbb{B}^\times=\{\tilde Q:Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0\}$ |
| Decomposition | $\tilde Q=r\zeta\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| Scalar factor | $r>0$ |
| Phase | $\zeta=e^{i\alpha}$, $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ |
| Boost | $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}\,e_t+i\sinh\frac{\psi}{2}\,\vec u_{\mathrm b}$, $\psi\ge0$ |
| Rotor | $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r}$, $\theta\in[0,2\pi]$ |
| Unit factor | $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=Q/(r\zeta)$ |
| Parameters | $1+1+(1+2)+(1+2)=8$ real |

### The Common Domain

The spectral decomposition exists in the distinct case $Q_x^2+Q_y^2+Q_z^2\neq0$, and in the scalar case $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q=0$, including the zero element. The polar decomposition exists on all units. The two domains overlap but neither contains the other:

* a **zero divisor** with $Q_x^2+Q_y^2+Q_z^2\neq0$ and $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ has two distinct eigenvalues and a two-term spectral decomposition, but no polar word;
* a **Jordan element** with $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$ and $Q_t\neq0$ has a repeated eigenvalue and no two-term spectral decomposition, but it is a unit and has a polar word.

The table records the regimes of *The Spectrum*, §*The Two Cases*, with the polar status added; the zero element is separated from the scalar regime.

| Regime | Condition | Spectrum | Spectral decomposition | Polar decomposition |
|---|---|---|---|---|
| Distinct | $Q_x^2+Q_y^2+Q_z^2\neq0$, $Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$ | two distinct nonzero | yes | yes |
| Zero divisor | $Q_x^2+Q_y^2+Q_z^2\neq0$, $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ | two distinct, one zero | yes | no: boundary of the domain |
| Scalar | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q=0$, $Q_t\neq0$ | one repeated nonzero | one-term, $\tilde Q=Q_t e_t$ | yes, with $\psi=0$ and $\theta\in\{0,2\pi\}$ |
| Jordan | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | one repeated nonzero | no two-term decomposition | yes |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t=0$ | one eigenvalue $0$ | no | no: not a unit |
| Zero | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q=0$, $Q_t=0$ | the eigenvalue $0$ | one-term, $\tilde Q=0$ | no: not a unit |

The inclusion of domains is therefore not a chain: the zero divisors and the zero element are spectral but not polar, the Jordan elements are polar but not spectral, and only the distinct and nonzero scalar cases belong to both.

## The Dictionary

### The Scalar Factor

The reduced product is the product of the eigenvalues:

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=\lambda_+\lambda_-.
$$

In the polar writing, the central factor $re^{i\alpha}$ multiplies both eigenvalues, so

$$
\lambda_+\lambda_-=r^2e^{2i\alpha}.
$$

Hence

$$
r=\bigl\lvert Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr\rvert^{1/2}=\lvert\lambda_+\lambda_-\rvert^{1/2},
\qquad
\alpha=\tfrac12\operatorname{Arg}\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)
=\tfrac12\operatorname{Arg}(\lambda_+\lambda_-),
$$

with $\operatorname{Arg}$ in $(-\pi,\pi]$ and $\alpha$ in $(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$. The scale and the phase are therefore determined by the eigenvalue pair alone. This is the common pattern of the three algebras: the product of the eigenvalues is the reduced product, and its modulus and argument give the modulus and the phase; in the split-complex case the argument is the discrete sign.

| Quantity | Spectral formula |
|---|---|
| Reduced product | $Q_t^2+Q_x^2+Q_y^2+Q_z^2=\lambda_+\lambda_-$ |
| Scale | $r=\bigl\lvert Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr\rvert^{1/2}$ |
| Phase | $\alpha=\tfrac12\operatorname{Arg}\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)$ |
| Complex modulus | $r e^{i\alpha}=\bigl(Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ in the branch |

### The Unit Factor

Put

$$
\tilde U=\frac{\tilde Q}{r e^{i\alpha}}
=\tilde U_{\mathrm b}\tilde u_{\mathrm r}
=U_te_t+\vec U .
$$

The factor $\tilde U$ has determinant one, so in the matrix model it lies in $SL(2,\mathbb{C})$. Since $re^{i\alpha}$ is central, the eigenprojections of $\tilde Q$ and of $\tilde U$ are the same, and the eigenvalues are scaled:

$$
\boxed{\; \lambda_\pm=re^{i\alpha}\Bigl(U_t\pm i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr) \;}.
$$

The two eigenvalues of the unit factor are reciprocal. Their product is the reduced product of $\tilde U$,

$$
\Bigl(U_t+i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)
\Bigl(U_t-i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)
=U_t^2+\vec U\cdot\vec U=1,
$$

because $\tilde U\tilde U^{\natural}=e_t$. In the distinct case, the unit factor has the spectral decomposition

$$
\tilde U=\Bigl(U_t+i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)\tilde\Pi_+
+\Bigl(U_t-i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)\tilde\Pi_-,
$$

with

$$
\tilde\Pi_\pm=
\frac{\tilde U-\bigl(U_t\mp i(\vec U\cdot\vec U)^{1/2}\bigr)e_t}
{\pm2i\bigl(\vec U\cdot\vec U\bigr)^{1/2}},
$$

by the Lagrange–Sylvester formula of *The Lagrange–Sylvester Eigenprojector Formula*, applied to $\tilde U$. The formula is the one of the eigenvalue article with $\tilde U$ in place of $\tilde Q$; it is not a new identity. The eigenvalues of $\tilde U$ are reciprocal, as they must be for determinant one.

The table records the two levels.

| Object | Eigenvalue decomposition | Polar reading |
|---|---|---|
| $\tilde Q$ | $\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ | $r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| $\tilde U=\tilde Q/(re^{i\alpha})$ | $\bigl(U_t+i(\vec U\cdot\vec U)^{1/2}\bigr)\tilde\Pi_++\bigl(U_t-i(\vec U\cdot\vec U)^{1/2}\bigr)\tilde\Pi_-$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ |
| Eigenvalues | $\lambda_\pm=re^{i\alpha}\bigl(U_t\pm i(\vec U\cdot\vec U)^{1/2}\bigr)$ | from the boost and the rotor |
| Eigenprojections | $\tilde\Pi_\pm$ | the spectral data of $\tilde U$ |
| Sum | $\lambda_++\lambda_-=2re^{i\alpha}\operatorname{Sc}\tilde U$ | $2re^{i\alpha}\operatorname{Sc}\tilde U$ |

### The Scalar Part of the Unit Factor

**Proposition (the scalar-part formula).** With $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$,

$$
\boxed{\; \operatorname{Sc}\tilde U
=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2},
\qquad
\lambda_++\lambda_-=2re^{i\alpha}\operatorname{Sc}\tilde U \;}.
$$

*Proof.* The scalar part of a product of two biquaternions is $\operatorname{Sc}(XY)=X_0Y_0-\vec X\cdot\vec Y$. For

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r},
$$

the scalar part is

$$
\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-\Bigl(i\sinh\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)\cdot
\Bigl(\sin\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}.
$$

The trace of the matrix model is twice the scalar part, and the trace is the sum of the eigenvalues; the second identity follows.

The formula is the exact obstruction to reading the polar word from the eigenvalues. The right-hand side depends on the three real numbers $\psi/2\ge0$, $\theta/2\in[0,\pi]$ and $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\in[-1,1]$, but only through their two real combinations $\cosh(\psi/2)\cos(\theta/2)$ and $(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh(\psi/2)\sin(\theta/2)$. One real degree of freedom among the three is invisible to $\operatorname{Sc}\tilde U$, and therefore to the eigenvalues. The two axes are invisible to $\operatorname{Sc}\tilde U$ as well; the eigenprojections carry the complex line of $\vec U$, four real parameters, which encodes both the missing degree and the directions.

| Quantity | Depends on | Determined by $\lambda_\pm$? |
|---|---|---|
| $r,\alpha$ | $\lambda_+\lambda_-$ | yes |
| $U_t=\operatorname{Sc}\tilde U$ | $\psi/2$, $\theta/2$, $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | yes: $U_t=(\lambda_++\lambda_-)/(2re^{i\alpha})$ |
| $\vec U\cdot\vec U=1-U_t^2$ | the same | yes |
| $\psi/2$, $\theta/2$, $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ separately | the unit factor | no: one real degree of freedom |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the unit factor | no: the directions are not in $\operatorname{Sc}\tilde U$ |
| $\tilde\Pi_\pm$ | $\vec U$ | no: independent spectral data |

### The Eigenprojections

The eigenprojections of $\tilde Q$ are those of the unit factor:

$$
\tilde\Pi_\pm
=\frac{\tilde U-\bigl(U_t\mp i(\vec U\cdot\vec U)^{1/2}\bigr)e_t}
{\pm2i\bigl(\vec U\cdot\vec U\bigr)^{1/2}}
=\frac12(e_t\pm\vec\Xi),
\qquad
\vec\Xi=-i\frac{\vec Q}{\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}}
=-i\frac{\vec U}{\bigl(\vec U\cdot\vec U\bigr)^{1/2}},
$$

where $U_x,U_y,U_z$ are the vector coefficients of $\tilde U$. The formula requires $\vec U\cdot\vec U\neq0$; when the denominator vanishes there is no eigenprojection. The eigenprojections depend only on $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$, not on the scalar factor $re^{i\alpha}$. In the polar word they are therefore functions of $(\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})$, and at the boundary they become the idempotents of the pure root $\vec\Xi$.

The two decompositions see the unit factor in two different ways:

* the **eigenvalue decomposition** sees it through the two eigenvalues $U_t\pm i(\vec U\cdot\vec U)^{1/2}$ and the two eigenprojections $\tilde\Pi_\pm$; the eigenvalues give $U_t$ and $D=(\vec U\cdot\vec U)^{1/2}$, and the eigenprojections give the eigendirections;
* the **Cartan decomposition** sees it through the rapidity $\psi$, the angle $\theta$ and the two axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$.

Both are six real parameters: the two eigenvalues of $\tilde U$ are two complex numbers of product one, hence two real; an eigenprojection is four real; and $\psi,\theta$ with two unit vectors are six real. The dictionary between them is nonlinear and is the content of the scalar-part formula and of the eigenprojector formula. The next subsections record its two directions in full; the two extreme cases follow.

### The Polar Factors from the Spectral Data

The spectral data are the two eigenvalues $\lambda_\pm$ and the two eigenprojections $\tilde\Pi_\pm$. The polar word is recovered in five steps.

**Step 1: the scalar factor.** The product of the eigenvalues fixes the principal square root:

$$
r e^{i\alpha}=\bigl(\lambda_+\lambda_-\bigr)^{1/2},
\qquad
r=\bigl\lvert\lambda_+\lambda_-\bigr\rvert^{1/2},
\qquad
\alpha=\tfrac12\operatorname{Arg}\bigl(\lambda_+\lambda_-\bigr),
$$

with the square root in the branch $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$.

**Step 2: the unit factor.** With $\tilde U=U_te_t+\vec U$,

$$
\tilde U=\frac{\tilde Q}{r e^{i\alpha}}
=\frac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_+
+\frac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-
=\Bigl(U_t+i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)\tilde\Pi_+
+\Bigl(U_t-i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr)\tilde\Pi_- .
$$

The middle expression is the definition scaled by the central factor; the last is the spectral decomposition of $\tilde U$. The eigenprojections are those of $\tilde Q$, so the two spectral data determine $\tilde U$ completely.

**Step 3: the boost and the rotor.** The Cartan decomposition of $\tilde U$ is recovered by

$$
\tilde U_{\mathrm b}=\bigl(\tilde U\tilde U^*\bigr)^{1/2},
\qquad
\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U .
$$

The square root is the unique positive Hermitian square root. Since $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*=e_t$, one has

$$
\tilde U\tilde U^*=\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde u_{\mathrm r}^*\tilde U_{\mathrm b}^*=\tilde U_{\mathrm b}^2
=\cosh\psi\,e_t+i\sinh\psi\,\vec u_{\mathrm b},
$$

so the formula returns the boost $\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$, and $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ is unitary of determinant one. This is the Cartan decomposition $SL(2,\mathbb{C})=P\cdot K$ read algebraically.

**Step 4: the two angles and the two axes.** From the closed forms

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r},
$$

the scalar and vector parts read

$$
\frac{\psi}{2}=\operatorname{arcosh}\bigl(\operatorname{Sc}\tilde U_{\mathrm b}\bigr),
\qquad
\vec u_{\mathrm b}=\frac{\operatorname{Vect}\tilde U_{\mathrm b}}{i\sinh(\psi/2)},
$$

$$
\frac{\theta}{2}=\arccos\bigl(\operatorname{Sc}\tilde u_{\mathrm r}\bigr),
\qquad
\vec u_{\mathrm r}=\frac{\operatorname{Vect}\tilde u_{\mathrm r}}{\sin(\theta/2)}.
$$

Equivalently, without introducing the half-angles,

$$
\vec u_{\mathrm b}=
\frac{\operatorname{Vect}\tilde U_{\mathrm b}}
{i\bigl((\operatorname{Sc}\tilde U_{\mathrm b})^2-1\bigr)^{1/2}},
\qquad
\vec u_{\mathrm r}=
\frac{\operatorname{Vect}\tilde u_{\mathrm r}}
{\bigl(1-(\operatorname{Sc}\tilde u_{\mathrm r})^2\bigr)^{1/2}},
$$

with the square-root branches chosen so that the two vectors are real and of unit length. The first radicand is real because $\operatorname{Sc}\tilde U_{\mathrm b}=\cosh(\psi/2)\ge1$; the second is real because $\operatorname{Sc}\tilde u_{\mathrm r}=\cos(\theta/2)\in[-1,1]$ and $\theta/2\in[0,\pi]$.

**Step 5: what can fail.** The denominators $\sinh(\psi/2)$, $\sin(\theta/2)$ and $(\vec U\cdot\vec U)^{1/2}$ must be nonzero. When $\psi=0$, the boost is the identity and $\vec u_{\mathrm b}$ is undefined. When $\theta\in\{0,2\pi\}$, the rotor is $\pm e_t$ and $\vec u_{\mathrm r}$ is undefined. When $\vec U\cdot\vec U=0$, the eigenprojection formula fails, the two eigenvalues of $\tilde U$ coincide, and $\tilde U$ is a Jordan element. In each case the corresponding axis or eigendirection is undefined, while the other factors and the scalar factor remain defined.

| Step | Input | Formula | Output |
|---|---|---|---|
| 1 | $\lambda_\pm$ | $r e^{i\alpha}=(\lambda_+\lambda_-)^{1/2}$ | scale and phase |
| 2 | $\lambda_\pm,\tilde\Pi_\pm$ | $\tilde U=\dfrac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_+ +\dfrac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-$ | unit factor |
| 3 | $\tilde U$ | $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ | boost and rotor |
| 4 | $\tilde U_{\mathrm b}$ | $\psi=2\operatorname{arcosh}(\operatorname{Sc}\tilde U_{\mathrm b})$, $\vec u_{\mathrm b}=\operatorname{Vect}\tilde U_{\mathrm b}/(i\sinh(\psi/2))$ | rapidity and boost axis |
| 5 | $\tilde u_{\mathrm r}$ | $\theta=2\arccos(\operatorname{Sc}\tilde u_{\mathrm r})$, $\vec u_{\mathrm r}=\operatorname{Vect}\tilde u_{\mathrm r}/\sin(\theta/2)$ | rotor angle and rotor axis |
| 6 | all | $\tilde Q=r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | the element |

**The factors one by one.** Each polar factor has its own spectral decomposition, with idempotents built on its own axis. Since $(i\vec u_{\mathrm b})^2=e_t$ and $(i\vec u_{\mathrm r})^2=e_t$,

$$
\tilde U_{\mathrm b}
=e^{\psi/2}\frac{e_t+i\vec u_{\mathrm b}}{2}
+e^{-\psi/2}\frac{e_t-i\vec u_{\mathrm b}}{2},
\qquad
\tilde u_{\mathrm r}
=e^{-i\theta/2}\frac{e_t+i\vec u_{\mathrm r}}{2}
+e^{i\theta/2}\frac{e_t-i\vec u_{\mathrm r}}{2}.
$$

The first line exhibits the boost on the idempotents $\tfrac12(e_t\pm i\vec u_{\mathrm b})$, with eigenvalues $e^{\pm\psi/2}$; the second exhibits the rotor on the idempotents $\tfrac12(e_t\pm i\vec u_{\mathrm r})$, with eigenvalues $e^{\mp i\theta/2}$. The table collects the chain.

| Factor | Factorisation | Spectral decomposition | Eigenvalues |
|---|---|---|---|
| $\tilde U_{\mathrm b}$ | $\exp\bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\bigr)$ | $e^{\psi/2}\frac{e_t+i\vec u_{\mathrm b}}{2}+e^{-\psi/2}\frac{e_t-i\vec u_{\mathrm b}}{2}$ | $e^{\psi/2},e^{-\psi/2}$ |
| $\tilde u_{\mathrm r}$ | $\exp\bigl(\frac{\theta}{2}\vec u_{\mathrm r}\bigr)$ | $e^{-i\theta/2}\frac{e_t+i\vec u_{\mathrm r}}{2}+e^{i\theta/2}\frac{e_t-i\vec u_{\mathrm r}}{2}$ | $e^{-i\theta/2},e^{i\theta/2}$ |
| $\tilde U$ | $\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ | $\bigl(U_t+iD\bigr)\tilde\Pi_++\bigl(U_t-iD\bigr)\tilde\Pi_-$ | $U_t\pm iD$ |
| $\tilde Q$ | $r e^{i\alpha}\tilde U$ | $\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-$ | $\lambda_\pm$ |

where $D=(\vec U\cdot\vec U)^{1/2}$. The unit factor is not generally the exponential of the sum of the two exponents: the product of the two exponentials is the exponential of the sum only when the axes commute or one of the angles vanishes. This is the spectral reason the four factors do not merge.

### The Spectral Data from the Polar Factors

Given $r,\alpha$ and the four polar data $\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r}$, form

$$
\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b},
\qquad
\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r},
\qquad
\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}.
$$

Write $\tilde U=U_te_t+\vec U$. The scalar part and the vector part are those of the product:

$$
U_t=\operatorname{Sc}\tilde U
=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2},
$$

$$
\vec U=\operatorname{Vect}\tilde U
=i\sinh\frac{\psi}{2}\cos\frac{\theta}{2}\vec u_{\mathrm b}
+\cosh\frac{\psi}{2}\sin\frac{\theta}{2}\vec u_{\mathrm r}
+i\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\vec u_{\mathrm b}\times\vec u_{\mathrm r}.
$$

Then

$$
\lambda_\pm=r e^{i\alpha}\Bigl(U_t\pm i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr),
\qquad
\vec\Xi=-i\frac{\vec U}{\bigl(\vec U\cdot\vec U\bigr)^{1/2}},
\qquad
\tilde\Pi_\pm=\frac12\bigl(e_t\pm\vec\Xi\bigr),
$$

and

$$
\tilde Q=r e^{i\alpha}\tilde U
=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_- .
$$

This is the inverse of the chain of the preceding subsection. The consistency check is the product:

$$
\lambda_+\lambda_-
=r^2e^{2i\alpha}\Bigl(U_t^2+\vec U\cdot\vec U\Bigr)
=r^2e^{2i\alpha},
$$

because $U_t^2+\vec U\cdot\vec U=\tilde U\tilde U^{\natural}=1$. The sum gives the scalar-part formula:

$$
\lambda_++\lambda_-=2r e^{i\alpha}U_t.
$$

The denominator $(\vec U\cdot\vec U)^{1/2}$ is the only obstruction: when it vanishes, the two eigenvalues coincide at $r e^{i\alpha}U_t$ and there is no eigendirection, hence no two-term spectral decomposition. The polar word still exists.

### What Each Side Carries

| Spectral datum | What it fixes | Formula | What it leaves free |
|---|---|---|---|
| $\lambda_+\lambda_-$ | scale and phase | $r e^{i\alpha}=(\lambda_+\lambda_-)^{1/2}$ | — |
| $\lambda_\pm/(r e^{i\alpha})$ | the two eigenvalues of $\tilde U$ | $U_t\pm i(\vec U\cdot\vec U)^{1/2}$ | one real degree in $\psi,\theta,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ and three in the pair of axes |
| $\tilde\Pi_\pm$, equivalently $\vec\Xi$ | the eigendirections of $\tilde U$ | $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the two axis directions separately |
| $\lambda_\pm$ and $\tilde\Pi_\pm$ | the whole unit factor | $\tilde U=\dfrac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_+ +\dfrac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-$ | — |
| $\tilde U$ | boost and rotor | $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ | — |
| $\tilde U_{\mathrm b}$ | rapidity and boost axis | $\psi=2\operatorname{arcosh}(\operatorname{Sc}\tilde U_{\mathrm b})$, $\vec u_{\mathrm b}=\operatorname{Vect}\tilde U_{\mathrm b}/(i\sinh(\psi/2))$ | axis if $\psi=0$ |
| $\tilde u_{\mathrm r}$ | rotor angle and rotor axis | $\theta=2\arccos(\operatorname{Sc}\tilde u_{\mathrm r})$, $\vec u_{\mathrm r}=\operatorname{Vect}\tilde u_{\mathrm r}/\sin(\theta/2)$ | axis if $\theta\in\{0,2\pi\}$ |
| $\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the eigenvalues and eigenprojections | the formulas of §*The Spectral Data from the Polar Factors* | — |

Read down the table for the direction spectral to polar and up for the direction polar to spectral. The eigenvalues carry the scalar factor and the two eigenvalues of the unit factor; the eigenprojections carry the eigendirections. The angles and axes are a second coordinate system on the same six real dimensions: $U_t$ (two real) and $\vec\Xi$ (four real) on one side, $\psi,\theta$ and two unit vectors (six real) on the other. The nonlinear dictionary is the content of the scalar-part formula and of the Cartan square root.

### The Parallel-Axis Case

When the axes are parallel or antiparallel, the boost and the rotor commute and the four factors amalgamate into one exponential (*Exponential Polar Decomposition of Biquaternions*, §*One Exponential*). The eigenvalues then determine the rapidity and the angle; the common axis remains the spectral datum of the eigenprojection, and the dictionary closes once that axis is read.

For $\vec u_{\mathrm b}=\vec u_{\mathrm r}=\vec u$,

$$
\tilde U=\exp\Bigl(\bigl(\frac{\theta}{2}+i\frac{\psi}{2}\bigr)\vec u\Bigr),
\qquad
\lambda_+=r e^{i\alpha}e^{i\theta/2-\psi/2},
\qquad
\lambda_-=r e^{i\alpha}e^{-i\theta/2+\psi/2},
$$

so the eigenvalues determine $\psi$ and $\theta$:

$$
\psi=2\ln\Bigl\lvert\frac{r e^{i\alpha}}{\lambda_+}\Bigr\rvert
=2\ln\Bigl\lvert\frac{\lambda_-}{r e^{i\alpha}}\Bigr\rvert,
\qquad
\theta=2\operatorname{Arg}\Bigl(\frac{\lambda_+}{r e^{i\alpha}}\Bigr),
$$

with the branch of $\theta$ fixed by $[0,2\pi]$; for antiparallel axes the argument is $-\theta/2$, and the sign of the formula for $\theta$ is reversed. For $\vec u_{\mathrm b}=-\vec u_{\mathrm r}$ ($\vec u_{\mathrm b}=\vec u$, $\vec u_{\mathrm r}=-\vec u$),

$$
\tilde U=\exp\Bigl(\bigl(-\frac{\theta}{2}+i\frac{\psi}{2}\bigr)\vec u\Bigr),
\qquad
\lambda_+=r e^{i\alpha}e^{-i\theta/2-\psi/2},
\qquad
\lambda_-=r e^{i\alpha}e^{i\theta/2+\psi/2},
$$

and the signs of $\theta$ are exchanged in the two eigenvalues, while those of $\psi$ are not. The table collects the two alignments.

| Alignment | $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | $\tilde U$ | $\lambda_+$ | $\lambda_-$ |
|---|---|---|---|---|
| $\vec u_{\mathrm b}=\vec u_{\mathrm r}$ | $1$ | $\exp\bigl((\frac{\theta}{2}+i\frac{\psi}{2})\vec u\bigr)$ | $r e^{i\alpha}e^{i\theta/2-\psi/2}$ | $r e^{i\alpha}e^{-i\theta/2+\psi/2}$ |
| $\vec u_{\mathrm b}=-\vec u_{\mathrm r}$ | $-1$ | $\exp\bigl((-\frac{\theta}{2}+i\frac{\psi}{2})\vec u\bigr)$ | $r e^{i\alpha}e^{-i\theta/2-\psi/2}$ | $r e^{i\alpha}e^{i\theta/2+\psi/2}$ |

In both rows the eigenvalues determine $\psi$ and $\theta$: the modulus of $\lambda_+/(r e^{i\alpha})$ is $e^{-\psi/2}$, and its argument is $+\theta/2$ for parallel axes and $-\theta/2$ for antiparallel axes. The common axis is not determined by the eigenvalues: it is the remaining spectral datum, read from the eigenprojection.

### The General Case and the One-Parameter Family

When $0<\lvert\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}\rvert<1$, the scalar-part formula is one complex equation for $\psi,\theta,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$, and it leaves a one-parameter family. A clean exact family is obtained by fixing $\psi$ and $\theta$ and taking the rotor axis perpendicular to the boost axis, $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$. Then

$$
\operatorname{Sc}\tilde U=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
$$

is independent of the azimuth of $\vec u_{\mathrm r}$ around $\vec u_{\mathrm b}$. Rotating $\vec u_{\mathrm r}$ in the plane perpendicular to $\vec u_{\mathrm b}$ therefore changes $\tilde U$, and with it the eigenprojections and the polar word, while $\operatorname{Sc}\tilde U$ and the eigenvalues $\lambda_\pm$ stay fixed.

**Proposition (the eigenvalues do not determine the word).** For $\psi>0$, $\theta\notin\{0,2\pi\}$ and $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$, the family

$$
\boxed{\; \tilde U(\varphi)=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr)
\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}(\varphi)\Bigr),
\qquad
\vec u_{\mathrm r}(\varphi)\perp\vec u_{\mathrm b} \;},
$$

has constant eigenvalues $\lambda_\pm=r e^{i\alpha}(U_t\pm i(\vec U\cdot\vec U)^{1/2})$, but the eigenprojections and the polar axes vary with $\varphi$.

*Proof.* The scalar part is $\operatorname{Sc}\tilde U=\cosh(\psi/2)\cos(\theta/2)$, independent of $\varphi$, and the determinant is one; hence $U_t$ and $U_t^2+\vec U\cdot\vec U=1$ are constant, and the two eigenvalues are constant. The vector part of $\tilde U(\varphi)$ is

$$
\cosh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm r}(\varphi)
+i\sinh\frac{\psi}{2}\cos\frac{\theta}{2}\,\vec u_{\mathrm b}
+i\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\,\vec u_{\mathrm b}\times\vec u_{\mathrm r}(\varphi),
$$

which depends on $\varphi$; hence the eigenprojection depends on $\varphi$. The polar axis $\vec u_{\mathrm r}(\varphi)$ is the variable itself.

This is the structural difference from the split-complex and reduced biquaternion articles: there the eigenprojections are fixed, and the eigenvalues determine the polar parameters. Here the eigenvalues determine the scalar factor and the two eigenvalues of the unit factor, and the eigenprojections determine the rest.

## The Regimes

The spectral regimes and the polar status fit together as follows.

| Regime | Condition | Spectral data | Polar data |
|---|---|---|---|
| Distinct interior | $Q_x^2+Q_y^2+Q_z^2\neq0$, $Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$ | $\lambda_\pm$ distinct, nonzero; $\tilde\Pi_\pm$ variable | $r,\alpha,\psi,\theta$, axes; unique up to degeneracies |
| Zero divisor | $Q_x^2+Q_y^2+Q_z^2\neq0$, $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ | $\lambda_\pm$ distinct, one zero; rank one | none: boundary of the polar domain |
| Scalar | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q=0$, $Q_t\neq0$ | $\lambda_\pm=Q_t$; one-term decomposition | $r=\lvert Q_t\rvert$, $\psi=0$, $\theta\in\{0,2\pi\}$, $\alpha$ from the branch; axes undefined |
| Jordan | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t\neq0$ | $\lambda_\pm=Q_t$; no two-term decomposition | exists; $\psi,\theta$ and axes from the Cartan decomposition |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$, $Q_t=0$ | $\lambda_\pm=0$; no decomposition | none: not a unit |
| Zero | $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q=0$, $Q_t=0$ | $\lambda_\pm=0$; the zero element | none: not a unit |

### The Zero-Divisor Regime

For $Q_x^2+Q_y^2+Q_z^2\neq0$ and $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$, the eigenvalues are distinct and one of them vanishes. The eigenprojections are well defined, and

$$
\tilde Q=\lambda_+\tilde\Pi_+
\qquad\text{or}\qquad
\tilde Q=\lambda_-\tilde\Pi_-,
$$

a nonzero complex multiple of a minimal idempotent. The spectral decomposition exists and is rank one. The polar decomposition does not: the modulus vanishes, $r=0$, and the rapidity diverges. The zero-divisor set is the boundary of the polar domain, and its two components are read in §*The Boundary*.

### The Scalar Regime

For $\tilde Q=Q_te_t$ with $Q_t\neq0$, the two eigenvalues coincide at $Q_t$ and the element is central. The polar data are $r=\lvert Q_t\rvert$, $\psi=0$, and $\theta=0$ or $2\pi$; the phase $\alpha$ and the rotor are the two factors of the principal square root branch $r e^{i\alpha}$, with the sign ambiguity absorbed by the rotor as in *Exponential Polar Decomposition of Biquaternions*, §*Existence and Uniqueness*. The boost is the identity and the axes are undefined, as at every degenerate point of polar coordinates.

### The Jordan Regime

For $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$ and $Q_t\neq0$, the vector part is nilpotent, $\vec Q^2=0$, and

$$
\tilde Q=Q_te_t+\vec Q
=Q_t\Bigl(e_t+\frac{\vec Q}{Q_t}\Bigr),
\qquad
\Bigl(\frac{\vec Q}{Q_t}\Bigr)^2=0.
$$

The matrix model is a Jordan block with the repeated eigenvalue $Q_t$, and there is no two-term idempotent decomposition: the eigenprojection is not defined. The element is nevertheless a unit, and it has a polar word. Its unit factor is unipotent,

$$
\tilde U=e_t+\frac{\vec Q}{Q_t},
\qquad
\operatorname{Sc}\tilde U=1,
\qquad
\operatorname{Vect}\tilde U\cdot\operatorname{Vect}\tilde U=0.
$$

Both eigenvalues of $\tilde U$ are $1$, and the scalar-part formula reads

$$
1=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2},
$$

which determines a relation among $\psi$, $\theta$ and $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$, not the three separately. The polar word exists and is unique, while the spectral decomposition does not exist. This is the exact mirror of the zero-divisor case.

### The Nilpotent Regime

For $Q_x^2+Q_y^2+Q_z^2=0$, $\vec Q\neq0$ and $Q_t=0$, the element is a nonzero nilpotent and $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$. It has the single eigenvalue $0$, no two-term spectral decomposition, and no polar word. It is the second stratum of the zero-divisor boundary.

### The Absence of a Jordan Lattice

In the distinct case, the fibre of the exponential is a copy of $\mathbb{Z}^2$, one integer for each eigenprojection. In the Jordan case, the two eigenvalues coincide, the eigenprojection is undefined, and the fibre is discrete: the logarithm is the scalar logarithm of $Q_t$ plus the nilpotent term $\vec Q/Q_t$, with the single ambiguity $2\pi i\mathbb{Z}$. The polar word does not remove this ambiguity: the polar parameters are a section of the word map, not of the exponential. The next section states the distinction.

## The Exponential and the Logarithm

### The Kernel and the Fibre

The exponential of $\mathbb{B}$ is not injective. Its kernel is the set of exponents that exponentiate to the identity; by *Biquaternion Elementary Functions*, §*The Exponential*, it consists of the diagonalisable elements whose eigenvalues lie in $2\pi i\mathbb{Z}$, and it is not a subgroup. In spectral terms:

* in the distinct case, the logarithms of a unit are $\operatorname{Log}\tilde Q+2\pi i(m\tilde\Pi_++n\tilde\Pi_-)$, a copy of $\mathbb{Z}^2$;
* in the scalar case, the logarithms are the translate $\operatorname{Log}Q_t\,e_t+\ker\exp$ of the whole kernel by the scalar logarithm, because every kernel element may be added;
* in the Jordan case, the logarithm is discrete, one point for each choice of the scalar logarithm;
* on the zero-divisor and nilpotent boundary there is no logarithm.

These are the statements of *Biquaternion Elementary Functions*, §*The Logarithm* and §*The Domain and the Fibre*, with the eigenprojections of *The Biquaternion Eigenvalue Decomposition*, §*The Eigenprojectors*.

### The Polar Word Is Not a Logarithm

The four exponents sum to the **formal exponent**

$$
\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}.
$$

Its exponential is not $\tilde Q$ unless the axes are parallel or antiparallel, or one of $\psi,\theta$ vanishes. The defect is the Baker–Campbell–Hausdorff correction, whose first term is

$$
\tfrac12\Bigl[i\frac{\psi}{2}\vec u_{\mathrm b},\frac{\theta}{2}\vec u_{\mathrm r}\Bigr]
=\frac{i\psi\theta}{4}\vec u_{\mathrm b}\times\vec u_{\mathrm r},
$$

again a boost. In spectral terms, in the generic case the eigenvalues of the formal exponent are not $\log\lambda_\pm$; the commutator changes the exponent inside $\mathfrak{sl}(2,\mathbb{C})$, and hence the eigenvalues of its exponential, while leaving the determinant fixed. The polar word is a **section of the word map**

$$
(r,\alpha,\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r})
\longmapsto
r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r},
$$

not a section of the exponential. It cuts the fibre of the word map to one point, up to the degeneracies of the axes, while the fibre of the exponential remains the lattice or the discrete family above. This is the exact sense in which the polar decomposition is canonical while a logarithm is multivalued.

## The Boundary

The polar domain is the complement of the null cone $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$. In spectral coordinates the cone is the union $\lambda_+=0$ or $\lambda_-=0$. It has two strata, distinguished by whether $Q_x^2+Q_y^2+Q_z^2$ vanishes.

| Stratum | Condition | Spectral data | Form | Polar limit |
|---|---|---|---|---|
| Idempotent | $Q_x^2+Q_y^2+Q_z^2\neq0$, $Q_t^2+Q_x^2+Q_y^2+Q_z^2=0$ | $\lambda_+\neq\lambda_-$, one zero | $\tilde Q=\lambda_\sigma\tilde\Pi_\sigma$, a complex multiple of a minimal idempotent | $r\to0$, $\psi\to\infty$, $r e^{\psi/2}\to R$ |
| Nilpotent | $Q_x^2+Q_y^2+Q_z^2=0$, $Q_t=0$, $\vec Q\neq0$ | $\lambda_+=\lambda_-=0$, no eigenprojection | $\tilde Q=\vec Q$, $\vec Q^2=0$ | the same limit with the rotor anticommuting with the boost axis |

For the idempotent stratum, the eigenprojection is well defined, and the element is a nonzero complex multiple of $\tilde\Pi_\sigma=\tfrac12(e_t+\sigma\vec\Xi)$; the other eigenvalue is zero. For the nilpotent stratum, $Q_x^2+Q_y^2+Q_z^2=0$ and the eigenprojection formula fails, because the inverse square root $\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$ is undefined; the element is a pure nilpotent. The classification of the minimal idempotents and the Peirce decomposition are those of *Idempotents* and *The Peirce Decomposition*, §*The Peirce Decompositions*; they are not repeated here.

The polar word reaches the boundary with $r\to0$ and $\psi\to\infty$ at the rate $r e^{\psi/2}\to R$ with $0<R<\infty$. The limit is

$$
\frac{R\,e^{i\alpha}}{2}\bigl(e_t+i\vec u_{\mathrm b}\bigr)\tilde u_{\mathrm r},
$$

which is a nonzero complex multiple of a minimal idempotent when $\tilde u_{\mathrm r}$ does not anticommute with $\vec u_{\mathrm b}$, and a nilpotent when it does. This is the boundary form of the two strata: the eigenprojection survives in the first case and disappears in the second. The detailed boundary limits and the two strata are in *Exponential Polar Decomposition of Biquaternions*, §*The Boundary of the Word*; the classification of the minimal idempotents is in *Idempotents*. The present article records only their spectral reading.

## The Matrix Picture

Under the matrix model $\mathsf M_2$, the eigenvalue decomposition is the diagonal form

$$
\mathsf M_2(\tilde Q)\sim\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix}
$$

in the distinct case. The polar decomposition is the matrix product

$$
\mathsf M_2(\tilde Q)
=re^{i\alpha}\,\mathsf M_2(\tilde U_{\mathrm b})\,\mathsf M_2(\tilde u_{\mathrm r}),
$$

with

$$
\mathsf M_2(\tilde U_{\mathrm b})=\cosh\frac{\psi}{2}\,I+\sinh\frac{\psi}{2}\,\boldsymbol\sigma\cdot\vec u_{\mathrm b},
\qquad
\mathsf M_2(\tilde u_{\mathrm r})=\cos\frac{\theta}{2}\,I-i\sin\frac{\theta}{2}\,\boldsymbol\sigma\cdot\vec u_{\mathrm r}.
$$

The first factor is Hermitian positive with eigenvalues $e^{\pm\psi/2}$; the second is unitary with eigenvalues $e^{\mp i\theta/2}$; the product has determinant one and trace

$$
2\Bigl(\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\Bigr).
$$

Its eigenvalues are $\operatorname{Sc}\tilde U\pm i(\vec U\cdot\vec U)^{1/2}$, and those of $\tilde Q$ are $re^{i\alpha}$ times them, namely $\lambda_\pm$.

| Matrix | Eigenvalues | Spectral role |
|---|---|---|
| $\mathsf M_2(\tilde Q)$ | $\lambda_+,\lambda_-$ | the element |
| $\mathsf M_2(\tilde U_{\mathrm b})$ | $e^{\pm\psi/2}$ | the boost |
| $\mathsf M_2(\tilde u_{\mathrm r})$ | $e^{\mp i\theta/2}$ | the rotor |
| $\mathsf M_2(\tilde U)$ | $\operatorname{Sc}\tilde U\pm i(\vec U\cdot\vec U)^{1/2}$ | the unit factor |
| diagonal form | $\lambda_+,\lambda_-$ | the spectral decomposition |

The matrix picture makes the dimension count explicit: the diagonal form of the unit factor $\tilde U$ has one complex eigenvalue (two real) and one eigenprojection (four real), while the Cartan product has two real angles and two real axes (six real). The equality $2+4=6$ holds on both sides: the two eigenvalues of $\tilde U$ and the eigenprojection on one side, the two angles and the two axes on the other.

The full case-by-case computation is in *Worked Examples of Exponential Polar Decomposition of Biquaternions*; the examples here isolate the dictionary.

### A Pure Boost and a Pure Rotor

The two aligned cases are exact and illustrate the parallel-axis dictionary.

| Element | $\lambda_+$ | $\lambda_-$ | $r$ | $\alpha$ | $\psi$ | $\theta$ | Axes |
|---|---|---|---|---|---|---|---|
| $\tfrac54+\tfrac34 i\vec e_z$ | $\tfrac12$ | $2$ | $1$ | $0$ | $2\ln2$ | $0$ | $\vec u_{\mathrm b}=\vec e_z$, $\vec u_{\mathrm r}$ arbitrary |
| $\tfrac{\sqrt3}{2}+\tfrac12\vec e_z$ | $e^{i\pi/6}$ | $e^{-i\pi/6}$ | $1$ | $0$ | $0$ | $\pi/3$ | $\vec u_{\mathrm b}$ arbitrary, $\vec u_{\mathrm r}=\vec e_z$ |

In the first row the element is the boost $\exp(i\ln2\,\vec e_z)=\cosh\ln2+i\sinh\ln2\,\vec e_z$; its eigenvalues are $e^{\pm\ln2}=2,1/2$, labelled by the branch $\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}=i\sinh\ln2$; the other choice of the square root exchanges the two columns. In the second row the element is the rotor $\exp(\tfrac{\pi}{6}\vec e_z)=\cos\tfrac{\pi}{6}+\sin\tfrac{\pi}{6}\vec e_z$; its eigenvalues are $e^{\pm i\pi/6}$. In both rows the axes are parallel or one of the angles vanishes, so the four factors amalgamate into one exponential; the eigenvalues determine the angles, and the axis is the remaining datum.

### The Generic Jordan Element

Take the element of *Worked Examples of Exponential Polar Decomposition of Biquaternions*, §*Case 8*,

$$
\tilde Q=(1+i)e_t+\vec e_x+i\vec e_y.
$$

Its vector part is null, $Q_x^2+Q_y^2+Q_z^2=1+i^2=0$, so the eigenvalues coincide:

$$
\lambda_+=\lambda_-=1+i.
$$

The element is a Jordan block, and the two-term spectral decomposition does not exist. Its reduced product is $\tilde Q\tilde Q^{\natural}=(1+i)^2=2i$, so the scalar factor is

$$
r=\sqrt2,
\qquad
\alpha=\frac{\pi}{4},
\qquad
re^{i\alpha}=1+i.
$$

The unit factor is unipotent,

$$
\tilde U=e_t+\frac{1-i}{2}\vec e_x+\frac{1+i}{2}\vec e_y,
\qquad
\operatorname{Sc}\tilde U=1,
\qquad
\operatorname{Vect}\tilde U\cdot\operatorname{Vect}\tilde U=0.
$$

The polar data of *Exponential Polar Decomposition of Biquaternions* are

$$
\psi=\operatorname{arcosh}2=1.3169578969,
\qquad
\vec u_{\mathrm b}=\frac{-\vec e_x+\vec e_y+\vec e_z}{\sqrt3},
$$

$$
\theta=\arccos\frac13=1.2309594173,
\qquad
\vec u_{\mathrm r}=\frac{\vec e_x+\vec e_y}{\sqrt2},
$$

and the axes are perpendicular, $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}=0$. The scalar-part formula gives $1=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}$, which is consistent with $\operatorname{Sc}\tilde U=1$. The eigenvalues $\lambda_\pm=1+i$ determine $r,\alpha$ and $\operatorname{Sc}\tilde U$, but not $\psi,\theta$ or the axes: with the eigenprojection absent, they determine almost nothing of the polar word. The polar word itself is unique, because the element is fixed.

| Quantity | Value |
|---|---|
| $\lambda_+=\lambda_-$ | $1+i$ |
| $r$ | $\sqrt2$ |
| $\alpha$ | $\pi/4$ |
| $\operatorname{Sc}\tilde U$ | $1$ |
| $\operatorname{Vect}\tilde U\cdot\operatorname{Vect}\tilde U$ | $0$ |
| $\psi$ | $\operatorname{arcosh}2=1.3169578969$ |
| $\theta$ | $\arccos(1/3)=1.2309594173$ |
| $\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ | $0$ |
| Spectral decomposition | none: Jordan block |
| Polar decomposition | exists and is unique |

The example is the simplest case in which the two decompositions have different domains: the polar word exists, the two-term spectral decomposition does not, and the eigenvalues are repeated.

## Summary

For a biquaternion unit $\tilde Q=Q_te_t+\vec Q$ with distinct eigenvalues, the eigenvalue decomposition and the exponential polar decomposition are related by

$$
\tilde Q=\lambda_+\tilde\Pi_++\lambda_-\tilde\Pi_-
=r e^{i\alpha}\tilde U_{\mathrm b}\tilde u_{\mathrm r},
\qquad
\lambda_\pm=r e^{i\alpha}\Bigl(U_t\pm i\bigl(\vec U\cdot\vec U\bigr)^{1/2}\Bigr),
$$

with

$$
Q_t^2+Q_x^2+Q_y^2+Q_z^2=\lambda_+\lambda_-=r^2e^{2i\alpha},
$$

$$
\lambda_++\lambda_-=2r e^{i\alpha}\operatorname{Sc}\tilde U
=2r e^{i\alpha}\Bigl(\cosh\frac{\psi}{2}\cos\frac{\theta}{2}
-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}\Bigr).
$$

The eigenvalues determine the scalar factor $r e^{i\alpha}$ and the two eigenvalues $U_t\pm i(\vec U\cdot\vec U)^{1/2}$ of the unit factor, equivalently its scalar part $\operatorname{Sc}\tilde U$ and $D=(\vec U\cdot\vec U)^{1/2}$. They do not determine the individual values of $\psi$, $\theta$ and the angle between the axes that produce $\operatorname{Sc}\tilde U$, nor the two axes; the eigenprojections, equivalently the Cartan decomposition of the unit factor, carry the remaining data. In the parallel-axis case the eigenvalues determine the rapidity and the angle, and the common axis remains free; in the general case they leave a four-real-dimensional family, one real degree of freedom in the triple $(\psi,\theta,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})$ and three in the pair of axes.

### Main Results

The table collects the formulas in one place.

| Result | Expression |
|---|---|
| Eigenvalues from polar data | $\lambda_\pm=r e^{i\alpha}\bigl(U_t\pm i(\vec U\cdot\vec U)^{1/2}\bigr)$ |
| Scalar factor | $r=\sqrt{\lvert\lambda_+\lambda_-\rvert}$, $\alpha=\tfrac12\operatorname{Arg}(\lambda_+\lambda_-)$ |
| Unit factor eigenvalues | $U_t\pm i(\vec U\cdot\vec U)^{1/2}=\lambda_\pm/(r e^{i\alpha})$ |
| Scalar part | $\operatorname{Sc}\tilde U=\dfrac{\lambda_++\lambda_-}{2r e^{i\alpha}}=\cosh\frac{\psi}{2}\cos\frac{\theta}{2}-i(\vec u_{\mathrm b}\cdot\vec u_{\mathrm r})\sinh\frac{\psi}{2}\sin\frac{\theta}{2}$ |
| Product | $\lambda_+\lambda_-=Q_t^2+Q_x^2+Q_y^2+Q_z^2=r^2e^{2i\alpha}$ |
| Sum | $\lambda_++\lambda_-=2r e^{i\alpha}\operatorname{Sc}\tilde U$ |
| Eigenprojections | $\tilde\Pi_\pm=\dfrac{\tilde U-\bigl(U_t\mp i(\vec U\cdot\vec U)^{1/2}\bigr)e_t}{\pm2i(\vec U\cdot\vec U)^{1/2}}$ |
| Polar factors from spectrum | $\tilde U=\dfrac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_++\dfrac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-$, then $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ |
| Formal exponent | $\tilde Q_{\log}=\ln r+i\alpha+i\frac{\psi}{2}\vec u_{\mathrm b}+\frac{\theta}{2}\vec u_{\mathrm r}$; its exponential is $\tilde Q$ only when the axes commute or one angle vanishes |
| Parallel axes | $\lambda_\pm=r e^{i\alpha}e^{\pm i\theta/2\mp\psi/2}$ for $\vec u_{\mathrm b}=\vec u_{\mathrm r}$; the signs of $\theta$ are exchanged for $\vec u_{\mathrm b}=-\vec u_{\mathrm r}$ |
| General axes | one real degree of freedom in $\psi,\theta,\vec u_{\mathrm b}\cdot\vec u_{\mathrm r}$ beyond $\lambda_\pm$; the axes carry the rest |
| Domain | polar on all units; spectral only when $Q_x^2+Q_y^2+Q_z^2\neq0$, or $\vec Q=0$ |
| Kernel of $\exp$ | diagonalisable elements with eigenvalues in $2\pi i\mathbb{Z}$; not a subgroup |
| Fibre of $\exp$ | $\mathbb{Z}^2$ in the distinct case; a translate of the kernel in the scalar case; discrete in the Jordan case |
| Zero divisors | spectral, not polar |
| Zero element | spectral, not polar |
| Jordan elements | polar, not spectral |
| Nilpotent elements | no polar word, no spectrum |
| Exponential on eigenprojections | a true logarithm acts by $\lambda_\pm\tilde\Pi_\pm$; the polar exponent does so when the axes commute or one angle vanishes |
| Polar word | a section of the word map, not of the exponential |

### The Dictionary Across the Three Algebras

The table compares the three relation articles; in the split-complex column, $\sigma_\pm=\operatorname{sgn}\lambda_\pm$; in the biquaternion column, $\tilde U=U_te_t+\vec U=\tilde Q/(re^{i\alpha})$ is the unit factor and $\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$.

| Feature | Split-complex | Reduced biquaternion | Biquaternion |
|---|---|---|---|
| Eigenvalues | $\lambda_\pm=q\pm q'$ | $\lambda_\pm=Q_{\blacktriangle}\pm Q_{\blacktriangledown}$ | $\lambda_\pm=Q_t\pm i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ |
| Eigenprojections | fixed $\Pi_\pm$ | fixed $\Pi_\pm$ | variable $\tilde\Pi_\pm$ |
| Polar parameters | $r,\phi,\epsilon$ | $\rho,\phi,\alpha,\beta$ | $r,\alpha,\psi,\theta,\vec u_{\mathrm b},\vec u_{\mathrm r}$ |
| Eigenvalues from polar data | $\sigma_\pm r e^{\pm\phi}$ | $\rho e^{i\alpha}e^{\pm(\phi+i\beta)}$ | $r e^{i\alpha}\bigl(U_t\pm i(\vec U\cdot\vec U)^{1/2}\bigr)$ |
| Polar factors from spectrum | $r$, $\epsilon=\sigma_+\Pi_++\sigma_-\Pi_-$, $e^{\phi j}=e^{\phi}\Pi_++e^{-\phi}\Pi_-$ | $\breve r=\rho_+\Pi_++\rho_-\Pi_-$, $u=e^{i\theta_+}\Pi_++e^{i\theta_-}\Pi_-$ | $\tilde U=\dfrac{\lambda_+}{r e^{i\alpha}}\tilde\Pi_++\dfrac{\lambda_-}{r e^{i\alpha}}\tilde\Pi_-$, $\tilde U_{\mathrm b}=(\tilde U\tilde U^*)^{1/2}$, $\tilde u_{\mathrm r}=\tilde U_{\mathrm b}^{-1}\tilde U$ |
| Discrete data | $\epsilon\in(\mathbb{Z}/2)^2$ | lattice $\Lambda$ in $(\alpha,\beta)$ | none |
| Polar domain | $q^2-q'^2\neq0$ | $Q_{\blacktriangle}^2-Q_{\blacktriangledown}^2\neq0$ | $Q_t^2+Q_x^2+Q_y^2+Q_z^2\neq0$ |
| Spectral domain | all $Q$ | all $\breve Q$ | $Q_x^2+Q_y^2+Q_z^2\neq0$, or $\vec Q=0$ |
| Zero divisors | spectral, no polar word | spectral, no polar word | spectral, no polar word |
| Zero element | spectral, no polar word | spectral, no polar word | spectral, no polar word |
| Jordan elements | absent | absent | polar word, no two-term spectrum |
| Nilpotent elements | absent | absent | no polar word, no spectrum |

Read down a column for one algebra and across a row for one concept. The first three rows are the common pattern: two eigenvalues, two eigenprojections, a polar word. The fourth and fifth rows are the dictionary: explicit in the two commutative cases, and obstructed here by the variable eigenprojections and the scalar-part formula. The last rows record the domain and the degeneracies; the biquaternion column is the only one in which the spectral and polar domains are not nested.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | the biquaternion algebra |
| $\tilde Q=Q_te_t+\vec Q$ | a biquaternion |
| $Q_x^2+Q_y^2+Q_z^2$ | the square of the vector part |
| $\lambda_\pm=Q_t\pm i\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{1/2}$ | the eigenvalues |
| $\tilde\Pi_\pm=\tfrac12(e_t\pm\vec\Xi)$ | the eigenprojections |
| $\vec\Xi=-i\vec Q\bigl(Q_x^2+Q_y^2+Q_z^2\bigr)^{-1/2}$ | the pure root of $+1$ |
| $Q_t^2+Q_x^2+Q_y^2+Q_z^2=\lambda_+\lambda_-$ | the reduced product |
| $r=\bigl\lvert Q_t^2+Q_x^2+Q_y^2+Q_z^2\bigr\rvert^{1/2}$ | the scale |
| $\alpha\in(-\tfrac{\pi}{2},\tfrac{\pi}{2}]$ | the phase |
| $\psi\ge0$ | the rapidity |
| $\theta\in[0,2\pi]$ | the rotor angle |
| $\vec u_{\mathrm b},\vec u_{\mathrm r}$ | the boost and rotor axes |
| $\tilde U=\tilde U_{\mathrm b}\tilde u_{\mathrm r}=\tilde Q/(r e^{i\alpha})$ | the unit factor |
| $\tilde U_{\mathrm b}=\cosh\frac{\psi}{2}e_t+i\sinh\frac{\psi}{2}\vec u_{\mathrm b}$ | the boost |
| $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | the rotor |
| $U_t=\operatorname{Sc}\tilde U$, $\vec U=\operatorname{Vect}\tilde U$ | its scalar and vector parts |
| $\operatorname{Sc}$, $\operatorname{Vect}$ | scalar part, vector part |
| $\operatorname{Arg}$ | the principal argument in $(-\pi,\pi]$ |

## Further Reading

- [Worked Examples of Exponential Polar Decomposition of Biquaternions](worked-examples-of-exponential-polar-decomposition-of-biquaternions.html), for the eight cases, the reconstruction and logarithm tables, and the null cone.
- [Worked Examples of Exponential Polar Decomposition with Eigenbasis of Biquaternions](worked-examples-of-exponential-polar-decomposition-with-eigenbasis-of-biquaternions.html), for the same eight cases read in the eigenbasis, with the nilpotents and the spinors.
- [The Biquaternion Eigenvalue Decomposition](the-biquaternion-eigenvalue-decomposition.html), §*The Eigenvalues* and §*The Eigenprojectors*, for the spectrum and the eigenprojections.
- [Spectral Regularity and Degeneracy in the Biquaternion Algebra](spectral-regularity-and-degeneracy-in-the-biquaternion-algebra.html), §*The Two Cases* and §*The Degenerate Case: The Cone*, for the degenerate case.
- [Biquaternion Elementary Functions](biquaternion-elementary-functions.html), for the exponential, the logarithm, the kernel and the principal branch.
- [Exponential Polar Decomposition of Biquaternions](exponential-polar-decomposition-of-biquaternions.html), for the four-factor word, the Cartan decomposition, existence and uniqueness, the group law and the boundary.
- [The Polar Decomposition of a N-Regular Biquaternion](the-polar-decomposition-of-an-n-regular-biquaternion.html), for the modulus and the unit factor.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Split-Complex Number](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-split-complex-number.html), for the real two-dimensional analogue.
- [Relations between Exponential Polar Decomposition and Eigenbasis a Reduced Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-a-reduced-biquaternion.html), for the commutative four-dimensional analogue.
- [Conventions in Mathematics](conventions-in-mathematics.html), for the notation.
