# __Two-Sided Operator and the Polar Decomposition__

## Introduction

The **Hermitian sandwich** of the biquaternion algebra is the operator

$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*},
$$

the two-sided operator whose right factor is the Hermitian conjugate of its left factor. It is the operator that carries the Lorentz group on the algebra: on the norm-one slice it acts on the anti-Hermitian and Hermitian subspaces by the proper orthochronous Lorentz group, and on the full group of units it is that action composed with a dilation.

The polar decomposition writes an element of non-vanishing norm as four factors,

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=r\exp(i\alpha)\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
\qquad \Rho=r\exp(i\alpha),
$$

the four being the scale $r>0$, the central phase $\exp(i\alpha)$ collected in $\Rho$, the Hermitian positive boost $\tilde U_{\mathrm b}$ of rapidity $\psi\ge0$ about the real unit axis $\vec u_{\mathrm b}$, and the rotor $\tilde u_{\mathrm r}$ of angle $\theta\in[0,2\pi]$ about the real unit axis $\vec u_{\mathrm r}$. This article reads the sandwich one factor at a time and answers one question: **what does each factor do to the operator, and what becomes of its exponent?** The answer is a table with one row per factor, and the row that matters is the second. The phase does nothing.

The article is the vector-side companion of *The Polar Decomposition of Biquaternions*, §*The Operator Reading: the Twist*. There the same word acts by left multiplication on the spinor module and all four factors are visible: the scale and the phase form the twist $\chi(\Rho)=\Rho$, and the boost and the rotor form the norm-one operator. Here the action is the sandwich on the algebra, the phase is invisible, and the boost and the rotor are the only factors that act on a vector by a Lorentz transformation. The one-sided companion is *One-Sided Operator and the Polar Decomposition*: there the same word is read through a single left or right multiplication, the phase is visible, and the two real forms $\mathbb{M}_\pm$ are exchanged at $\alpha=\tfrac{\pi}{2}$. **The half-spin is the one-sided operator**: a single slot carries the half-angle $\theta/2$ and the half-rapidity $\psi/2$, and the sandwich of this article is their double, the full angle $\theta$ and the full rapidity $\psi$.

The plan is the following. §*The Sandwich of the Word* proves the multiplicativity and the closed form $\Theta_{\tilde Q}=r^{2}\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}$. §*The Scale* to §*The Rotor* take the four factors in the order of the word. §*The Eigenbasis and the Two Spinor Slots* reads the sandwich as a two-slot operator, computes its spectrum as the four products $\lambda_i\bar\lambda_j$, and identifies the full spin as the double of the one-sided half-spin. §*The Angle Bookkeeping* collects the exponents and states the doubling rule. §*The Image and the Kernel* identifies the image as the conformal Lorentz group and the kernel as the central unit circle. §*The Null Cone* records the degenerate case. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{M}_\pm=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}.
$$

On $\mathbb{M}_-$ an element is $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{M}_+$ an element is $\tilde Q_+=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central.

The **norm** of the polar series is the complex number

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},\qquad \tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,e_t ,
$$

and the **domain** of the polar word is $\langle\tilde Q\rangle_{\natural}\neq0$. The word is

$$
\tilde Q=\Rho\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\Rho=r\exp(i\alpha),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors. The modulus is $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch, so $r=\lvert\Rho\rvert$ and $\alpha=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The factors satisfy

$$
\Rho^{*}=\bar\Rho,\qquad \tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=\langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The sandwich is written $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ throughout. It uses the Hermitian conjugate in the right slot and never the inverse; the two coincide only where $\tilde Q$ is unitary. It is the member $L_{\tilde Q}R_{\tilde Q^{*}}$ of the general two-sided family of *Two-Sided Operators on the Biquaternion Algebra*, with the second parameter fixed at the Hermitian conjugate of the first; the general family allows the two parameters independently.

## The Sandwich of the Word

### Elementary Properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$ and $\tilde X\in\mathbb{B}$. Then:

**(a)** $\Theta_{\tilde Q\tilde Q'}=\Theta_{\tilde Q}\circ\Theta_{\tilde Q'}$;

**(b)** $\Theta_{\tilde Q}$ is $\mathbb{C}$-linear in $\tilde X$;

**(c)** $\Theta_{\tilde Q}$ is invertible if and only if $\tilde Q$ is invertible, and then $\Theta_{\tilde Q}^{-1}=\Theta_{\tilde Q^{-1}}$;

**(d)** $\Theta_{\tilde Q}$ preserves each of $\mathbb{M}_+$ and $\mathbb{M}_-$;

**(e)** $\Theta_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*}$.

*Proof.* (a) $(\tilde Q\tilde Q')\tilde X(\tilde Q\tilde Q')^{*}=\tilde Q(\tilde Q'\tilde X\tilde Q'^{*})\tilde Q^{*}$. (b) The multiplication and the right factor are $\mathbb{C}$-linear. (c) The inverse of $\Theta_{\tilde Q}$ is $\Theta_{\tilde Q^{-1}}$, because $\tilde Q^{-1}\tilde Q\tilde X\tilde Q^{*}\tilde Q^{-*}=\tilde X$ and $(\tilde Q^{-1})^{*}=(\tilde Q^{*})^{-1}$. (d) If $\tilde X^{*}=\pm\tilde X$, then

$$
\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}=\tilde Q\tilde X^{*}\tilde Q^{*}=\pm\tilde Q\tilde X\tilde Q^{*}.
$$

(e) Put $\tilde X=e_t$.

The preservation of the two sectors is the structural reason the action splits into two formulas, one per sector, and the reason a sandwich cannot mix the Hermitian and the anti-Hermitian parts.

**Corollary (the scaling of the norm).** For every unit $\tilde Q$ and every $\tilde X$,

$$
\boxed{\;\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}\;}.
$$

*Proof.* The norm is multiplicative and central, and $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$; hence $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde X\rangle_{\natural}\overline{\langle\tilde Q\rangle_{\natural}}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}$. On the unit-norm slice the sandwich is an isometry of the biquaternion norm.

### The Closed Form

**Theorem (the sandwich of the polar word).** Let $\tilde Q=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\langle\tilde Q\rangle_{\natural}\neq0$. Then

$$ \Theta_{\tilde Q}=\Theta_r\circ\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}}, $$

that is,

$$
\boxed{\;\Theta_{\tilde Q}(\tilde X)=r^{2}\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b}\;},
$$

and $\Theta_{\exp(i\alpha)}=\mathrm{id}$.

*Proof.* The Hermitian conjugate of the word is

$$
\tilde Q^{*}=\bigl(\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)^{*}
=\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}\Rho^{*}
=\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\bar\Rho
=\bar\Rho\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b},
$$

because the scalars are central. Hence

$$
\tilde Q\tilde X\tilde Q^{*}
=\Rho\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\bar\Rho
=\Rho\bar\Rho\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b},
$$

and $\Rho\bar\Rho=r^{2}$. The phase has disappeared in the last step.

**Remark (the order).** The rightmost factor of the word acts first: the rotor, then the boost, then the scale. The phase may be inserted anywhere, and so may the scale, because both are central. The boost and the rotor do not commute, so their order is part of the word and cannot be exchanged.

The theorem is the article in one line. The four sections that follow read its four factors.

## The Scale

### The Factor

The scale is $r=\exp(\ln r)$, a positive real. It is central, real and Hermitian, $r^{*}=r$, and it is the only factor whose exponent is a real scalar.

### The Sandwich

$$
\Theta_r(\tilde X)=r\tilde Xr^{*}=r^{2}\tilde X .
$$

On $\mathbb{M}_-$ and on $\mathbb{M}_+$ alike, every coordinate is multiplied by $r^{2}$: $a\mapsto r^{2}a$ and $\vec b\mapsto r^{2}\vec b$. The scale is a dilation of ratio $r^{2}$ of the whole algebra, and the only factor that changes the norm of the argument,

$$
\langle\Theta_r(\tilde X)\rangle_{\natural}=r^{4}\langle \tilde X\rangle_{\natural}.
$$

### The Exponent

The exponent is $\ln r$, and the sandwich sends it to

$$
\boxed{\;\ln r\longmapsto 2\ln r\;}.
$$

There is no angle. The factor two is nevertheless the same factor two as in the boost and the rotor: the exponent of the factor is half the exponent of its image. The scale is the case in which the doubled parameter is a dilation and not a rotation or a rapidity. The map $r\mapsto r^{2}$ is an isomorphism of $\mathbb{R}_{>0}$, so the scale is recovered from its sandwich; only the sign of the factor is lost, and the polar word has $r>0$.

## The Central Phase

### The Factor

The phase is $P=\exp(i\alpha)$, central and unitary,

$$
P^{*}=P^{-1}=\exp(-i\alpha),\qquad \langle P\rangle_{\natural}=\exp(2i\alpha).
$$

Its exponent is $i\alpha$, purely imaginary and central.

### The Sandwich

$$
\Theta_P(\tilde X)=\exp(i\alpha)\,\tilde X\,\exp(-i\alpha)=\tilde X .
$$

The two scalars commute with $\tilde X$ and with each other, and the second is the inverse of the first, so the product is the identity operator.

**The phase is not a half-angle of the sandwich.** The exponent $i\alpha$ is the full generator of the multiplication by $\exp(i\alpha)$ on the module; the sandwich cancels it. It is already half of the argument of the norm, $\langle\tilde Q\rangle_{\natural}=\Rho^{2}=r^{2}\exp(2i\alpha)$, and that is the only doubling in which it takes part. Writing $\exp(i\alpha/2)$ in the word would not change the sandwich, which is the identity either way; it would only change the meaning of the letter $\alpha$, and it would break $\Rho=\sqrt{\langle\tilde Q\rangle_{\natural}}$ unless $\alpha$ were redefined as $\arg\langle\tilde Q\rangle_{\natural}$.

### Remark (the Cancelled Phase)

This is the central remark of the article. The phase is the only factor of the word whose sandwich is the identity whatever the value of its parameter. It is not halved, not doubled and not shifted: it is annihilated. Six consequences follow.

**First, the cancellation is exact and global.** It holds for every $\tilde X$, not merely on one subspace, and it uses only two properties, centrality and unitarity. Any central factor of modulus one cancels in any sandwich: if $C$ is central and $C^{*}=C^{-1}$, then

$$
C\tilde XC^{*}=\tilde XCC^{-1}=\tilde X .
$$

**Second, two elements that differ by a phase have the same sandwich.** For a central complex $\lambda$,

$$
\Theta_{\lambda\tilde Q}(\tilde X)=\lambda\tilde Q\tilde X\tilde Q^{*}\bar\lambda=|\lambda|^{2}\,\Theta_{\tilde Q}(\tilde X).
$$

On the unit circle $|\lambda|=1$ the two sandwiches are equal, so the whole $U(1)$-orbit of $\tilde Q$ has one sandwich. On the positive real axis the sandwich scales by $\lambda^{2}$, which is the scale row of the table. The phase is the unit-modulus part of the centre, and it is exactly the part that disappears.

**Third, the phase is absent from this action but not from the algebra.** It reappears in three places, and the list is the reason the polar word needs it:

- the norm, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\Rho^{2}=r^{2}\exp(2i\alpha)$;
- the determinant, $\det\mathsf M_2(\tilde Q)=\Rho^{2}=r^{2}\exp(2i\alpha)$;
- the module, where left multiplication by $\tilde Q$ acts on the spinor module by the scalar $\Rho=r\exp(i\alpha)$, the twist $\chi(\Rho)=\Rho$ of *The Polar Decomposition of Biquaternions*, §*The Operator Reading: the Twist*.

The first two are quadratic in $\Rho$ and see $2\alpha$; the third is linear and sees $\alpha$; the sandwich multiplies by $\Rho$ on the left and by $\bar\Rho$ on the right and sees $0$.

**Fourth, the spectral reading confirms it.** The eigenvalues of $\Theta_{\tilde Q}$ are the products $\lambda_i\bar\lambda_j$ of the eigenvalues of $\mathsf M_2(\tilde Q)$, as in §*The Spectrum of the Sandwich*. A phase multiplies every $\lambda_i$ by $\exp(i\alpha)$ and every $\bar\lambda_j$ by $\exp(-i\alpha)$, so every product is unchanged. The cancellation is visible in the spectrum without any computation in coordinates.

**Fifth, the factor $\exp(2i\alpha)$ of the norm is not a doubling by the sandwich.** It is the square of the factor in the product $\tilde Q\tilde Q^{\natural}$: the product has two factors and both carry $\exp(i\alpha)$. The doubling of the boost and the rotor is a different phenomenon, computed in the next two sections. The two must not be conflated: the norm doubles the phase because the product has two factors, while the sandwich doubles the boost because its two slots carry the same exponent, and doubles the rotor because the conjugation is the double cover.

**Sixth, the phase row of the table is zero.** A table that halves every exponent would put $\alpha/2$ in the phase row and would be wrong by the whole phase; a table that repeats the exponent would put $\alpha$ there and would be wrong by the sign of the right factor. The only correct entry is $0$.

## The Boost

### The Factor

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\psi}{2}\,e_t+i\sinh\tfrac{\psi}{2}\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1 .
$$

It is Hermitian and of norm one,

$$
\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=1,
$$

and its square and inverse are

$$
\tilde U_{\mathrm b}^{2}=\exp(i\psi\vec u_{\mathrm b}),\qquad
\tilde U_{\mathrm b}^{-1}=\exp\Bigl(-i\tfrac{\psi}{2}\vec u_{\mathrm b}\Bigr).
$$

The boost is not unitary, because $\tilde U_{\mathrm b}^{-1}\neq\tilde U_{\mathrm b}$ unless $\psi=0$.

### The Sandwich on the Two Sectors

The right slot is $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, so the sandwich is a **congruence**,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\,\tilde X\,\tilde U_{\mathrm b},
$$

and not a conjugation. Write $b_\parallel=\vec u_{\mathrm b}\cdot\vec b$ and $\vec b_\perp=\vec b-b_\parallel\vec u_{\mathrm b}$.

On $\mathbb{M}_-$, for $\tilde X=ia\,e_t+\vec b$,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=ia'\,e_t+\vec b',
\qquad
a'=a\cosh\psi-b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi-a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

On $\mathbb{M}_+$, for $\tilde X=a\,e_t+i\vec b$,

$$
\Theta_{\tilde U_{\mathrm b}}(\tilde X)=a'\,e_t+i\vec b',
\qquad
a'=a\cosh\psi+b_\parallel\sinh\psi,\qquad
b_\parallel'=b_\parallel\cosh\psi+a\sinh\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

The two formulas differ only in the signs of the cross terms. The derivation is one line per piece. For the time piece,

$$
\tilde U_{\mathrm b}\,(ia\,e_t)\,\tilde U_{\mathrm b}=ia\,\tilde U_{\mathrm b}^{2}
=ia\cosh\psi-a\sinh\psi\,\vec u_{\mathrm b},
$$

and for the vector piece the perpendicular part is fixed and the parallel part is stretched by $\cosh\psi$; the cross terms combine into the formulas above. In the coordinates $(a,b_x,b_y,b_z)$ the matrices of the two actions are

$$
B_-(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & -\sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
-\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

$$
B_+(\psi,\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\psi & \sinh\psi\,\vec u_{\mathrm b}^{\,T}\\
\sinh\psi\,\vec u_{\mathrm b} & I_3+(\cosh\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

with $B_+=B_-^{-1}$. Each preserves its form, $B_\pm^{T}G_\pm B_\pm=G_\pm$, where $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+=\operatorname{diag}(-1,1,1,1)$.

### The Exponent and the Rapidity

The exponent is $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ and the output is the rapidity $\psi$. The parameter of the factor is half the parameter of its image, and the doubling is exact. The boost is Hermitian, so both slots carry the exponent with the same sign; the sandwich adds the two exponents instead of cancelling them, and the sum is $2\cdot\tfrac{\psi}{2}=\psi$.

## The Rotor

### The Factor

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta}{2}\,e_t+\sin\tfrac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1 .
$$

It is a real quaternion, of norm one, and unitary,

$$
\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

Unlike the boost, the rotor is both norm-one and unitary, and its right slot is therefore the inverse.

### The Sandwich

$$
\Theta_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\,\tilde X\,\tilde u_{\mathrm r}^{-1}.
$$

The sandwich is a conjugation by an invertible element, hence an algebra automorphism. On a general element $\tilde X=X_te_t+\vec X$ it fixes the scalar part and rotates the vector part,

$$
\Theta_{\tilde u_{\mathrm r}}(\tilde X)=X_te_t+\mathsf R(\theta,\vec u_{\mathrm r})\,\vec X,
$$

where $\mathsf R$ is the Rodrigues rotation

$$
\mathsf R(\theta,\vec u_{\mathrm r})=I_3+\sin\theta\,[\vec u_{\mathrm r}]_\times+(1-\cos\theta)\,[\vec u_{\mathrm r}]_\times^{2},
$$

or, on a vector $\vec X$,

$$
\mathsf R(\theta,\vec u_{\mathrm r})\,\vec X
=\vec X\cos\theta+(\vec u_{\mathrm r}\times\vec X)\sin\theta
+\vec u_{\mathrm r}(\vec u_{\mathrm r}\cdot\vec X)(1-\cos\theta).
$$

On $\mathbb{M}_-$ the rotor fixes the time direction $ie_t$ and rotates $\vec b$; on $\mathbb{M}_+$ it fixes $e_t$ and rotates $i\vec b$. The formula is the same on the two sectors because $i$ is central.

### The Exponent and the Angle

The exponent is $\tfrac{\theta}{2}\vec u_{\mathrm r}$ and the output is the rotation of angle $\theta$ about $\vec u_{\mathrm r}$. The parameter of the factor is half the parameter of its image. The rotor is unitary, so the two slots carry opposite signs; the sandwich conjugates instead of composing the two exponents, and the conjugation by $\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ is the rotation of angle $\theta$. Equivalently, the double cover $SU(2)\to SO(3)$ sends $\pm\tilde u_{\mathrm r}$ to the same rotation, and the parameter $\theta$ of the image is twice the parameter $\theta/2$ of the rotor. The sandwich sees the rotation and not the sign; the sign is the extra data of the one-sided operator.

## The Eigenbasis and the Two Spinor Slots

### The Two Slots of the Sandwich

Assume $B\neq0$ throughout this section. The sandwich is the composite of two one-sided operators,
$$
\Theta_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},
\qquad
\Theta_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$
The left factor acts on the left slot of $\tilde X$ and the right factor on the right slot. In the Q-adapted matrix model $\mathsf M^{\tilde Q}$ of *The Quaternionic Norm-Regular, Spectrally Regular Sector*, §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis* — not the Pauli model $\mathsf M_2$ of §*Conventions* — the element $\tilde Q$ is the diagonal matrix
$$
\Delta=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
\qquad
\lambda_\pm=Q_t\pm iB,
$$
and the left factor is $X\mapsto \Delta X$. The right factor is $X\mapsto X\Delta_*$, where $\Delta_*$ is the matrix of $\tilde Q^{*}$ in the same model. The first slot is the column index, a spinor slot; the second slot is the row index, the dual spinor slot.

In this model the sandwich is $X\mapsto\Delta X\Delta_*$. A first-chirality spinor, in the Peirce sense, is a matrix whose second column is zero; the left factor acts by $\Delta$ on its first column, and the right factor then combines the two columns. A second-chirality spinor, in the Peirce sense, is a matrix whose first column is zero; the left factor acts by $\Delta$ on its second column, and the right factor again combines the columns. The one-sided operator is the column action alone; the sandwich is the column action followed by the row action.

The two slots carry the two eigenvalues separately. The left multiplication $L_{\tilde Q}$ has spectrum $\{\lambda_+,\lambda_-\}$, each with multiplicity two. The right multiplication $R_{\tilde Q^{*}}$ has spectrum $\{\bar\lambda_+,\bar\lambda_-\}$, each with multiplicity two, because the eigenvalues of $\tilde Q^{*}$ are the conjugates of those of $\tilde Q$. The two operators commute,
$$
L_{\tilde Q}R_{\tilde Q^{*}}=R_{\tilde Q^{*}}L_{\tilde Q},
$$
and each is diagonalisable when $B\neq0$. They therefore admit a common eigenbasis, and in that basis the sandwich is diagonal.

*Proof.* The two multiplications commute because both are products in the associative algebra. A commuting family of diagonalisable operators is simultaneously diagonalisable. The eigenvalues of $L_{\tilde Q}$ are $\lambda_\pm$ by the Q-adapted basis. In a matrix model, right multiplication by $A$ is a Kronecker product of $A^{T}$ with the identity, so the eigenvalues of $R_{\tilde Q^{*}}$ are those of $\tilde Q^{*}$, namely $\bar\lambda_\pm$, each with multiplicity two.

### The Spectrum of the Sandwich

In the common eigenbasis the left slot contributes one of $\lambda_+,\lambda_-$ and the right slot one of $\bar\lambda_+,\bar\lambda_-$. The eigenvalue of the sandwich is the product:
$$
\boxed{\;
\operatorname{spec}\Theta_{\tilde Q}
=\bigl\{\lambda_+\bar\lambda_+,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ \lambda_-\bar\lambda_-\bigr\}
\; }.
$$
Equivalently,
$$
\Theta_{\tilde Q}\longleftrightarrow
\operatorname{diag}\bigl(
\lambda_+\bar\lambda_+,\,
\lambda_+\bar\lambda_-,\,
\lambda_-\bar\lambda_+,\,
\lambda_-\bar\lambda_-
\bigr)
$$
in the common eigenbasis. The two diagonal products are the moduli squared:
$$
\lambda_+\bar\lambda_+=|\lambda_+|^{2},
\qquad
\lambda_-\bar\lambda_-=|\lambda_-|^{2}.
$$
The two off-diagonal products are conjugate to each other:
$$
\overline{\lambda_+\bar\lambda_-}=\lambda_-\bar\lambda_+.
$$

This is the precise sense in which the sandwich uses **two slots**. A one-sided operator uses one slot and carries the pair $(\lambda_+,\lambda_-)$; the sandwich uses two slots and carries the four products. The factor attached to a slot is half of the factor attached to the pair of slots, which is the spectral form of the doubling rule.

The common eigenbasis is not the Q-adapted Peirce basis in general. It is the tensor product of a left eigenbasis of $L_{\tilde Q}$ and a right eigenbasis of $R_{\tilde Q^{*}}$. The two agree whenever $\tilde Q^{*}$ is diagonal in the Q-adapted basis; this includes the Hermitian case $\tilde Q^{*}=\tilde Q$, where the four products are the pairings $\lambda_i\lambda_j$, and also the case in which $\tilde Q^{*}$ lies in the span of the two eigenprojections. In general they differ. For a generic polar word the sandwich mixes the two chiral left ideals $S_+$ and $S_-$ of the one-sided reading; the four products are still exact, but they are not the diagonal entries of the Peirce matrix. The pure factors are the exceptions: a pure boost satisfies $\tilde Q^{*}=\tilde Q$, a pure rotor satisfies $\tilde Q^{*}=\tilde Q^{-1}$, and both commute with their own eigenprojections, so their sandwiches preserve $S_+$ and $S_-$. This does not contradict the preservation of the real forms $\mathbb{M}_\pm$: the splitting $\mathbb{B}=S_+\oplus S_-$ is a complex splitting into left ideals, while $\mathbb{B}=\mathbb{M}_+\oplus\mathbb{M}_-$ is a real splitting into Hermitian sectors, and they are different decompositions.

### The Pure Factors and the Full Spin

For each pure factor, read with the other factors absent, the products are elementary. The scale $r$ has $\lambda_\pm=r$ and products $r^{2}$. The central phase has $\lambda_\pm=\exp(i\alpha)$ and products $\exp(i\alpha)\exp(-i\alpha)=1$. The boost has
$$
\lambda_+=e^{-\psi/2},\qquad \lambda_-=e^{\psi/2},
$$
so its products are
$$
e^{-\psi},\quad 1,\quad 1,\quad e^{\psi}.
$$
The rotor has
$$
\lambda_+=e^{i\theta/2},\qquad \lambda_-=e^{-i\theta/2},
$$
so its products are
$$
e^{i\theta},\quad 1,\quad 1,\quad e^{-i\theta}.
$$
The sandwich therefore carries the full rapidity $\psi$ and the full angle $\theta$, while the one-sided operator carries the half-rapidity and the half-angle. The phase cancels and the scale doubles.

**The half-spin is the one-sided operator.** The sandwich has no half-angle of its own: it pairs two one-sided slots, and each slot is the spinor action of *One-Sided Operator and the Polar Decomposition*, §*The Half-Spin: the Eigenbasis and the Two Spinor Spaces*. The half-angle $\theta/2$ and the half-rapidity $\psi/2$ live on a single slot; this article computes their products, which are the full angle $\theta$ and the full rapidity $\psi$.

| factor | one-slot pair $(\lambda_+,\lambda_-)$ | two-slot products | output |
|---|---|---|---|
| scale $r$ | $(r,r)$ | $r^{2},r^{2},r^{2},r^{2}$ | dilation $r^{2}$ |
| phase $\exp(i\alpha)$ | $(e^{i\alpha},e^{i\alpha})$ | $1,1,1,1$ | identity |
| boost $\tilde U_{\mathrm b}$ | $(e^{-\psi/2},e^{\psi/2})$ | $e^{-\psi},1,1,e^{\psi}$ | rapidity $\psi$ |
| rotor $\tilde u_{\mathrm r}$ | $(e^{i\theta/2},e^{-i\theta/2})$ | $e^{i\theta},1,1,e^{-i\theta}$ | angle $\theta$ |

The scale and the phase are central. Their rows are read as scalar multipliers of a word with $B\neq0$; for a purely central element $B=0$ and the spectrum collapses to $Q_t\bar Q_t$.

For a general word the two factors do not commute, and the common eigenbasis is not the Q-adapted one. The product formula for the spectrum remains exact. The splitting of the products into a boost and a rotation is the content of §*The Boost* and §*The Rotor* when the axes commute; in general the effective exponent is the sum of the two slot exponents only after the common eigenbasis is chosen. The relation between the spectral data and the polar parameters is *Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion*, §*The Spectral Data from the Polar Factors*.

**Corollary (the sandwich is the two-slot operator).** The sandwich acts on the left and the right slots of the matrix model. Its spectrum is the four products $\lambda_i\bar\lambda_j$. The one-sided operator is the restriction to one slot; the two-sided operator is the pairing of the two slots. The half-angle of the rotor and the half-rapidity of the boost belong to one slot; their doubles belong to the pair.

### The Vector Representation as the Double of the Half-Spin

The two slots are the two tensor factors of $\mathbb{B}\cong S\otimes S^{*}$, where $S=\mathbb{C}^{2}$ is the spinor space and $S^{*}$ its dual. The left factor acts on $S$, the right on $S^{*}$, and the sandwich is
$$
\Theta_{\tilde Q}=\rho(\tilde Q)\otimes\bar\rho(\tilde Q),
$$
where $\rho$ is the defining representation on $S=\mathbb{C}^{2}$ and $\bar\rho$ its conjugate. The tensor product of the defining representation and its conjugate is the complexified vector representation,
$$
2\otimes\bar 2=4,
$$
so the sandwich is the vector and the one-sided operator, on one slot, is the spinor.

The weights add. For the rotor, $\rho(\tilde u_{\mathrm r})$ has weights $e^{\pm i\theta/2}$ and $\bar\rho(\tilde u_{\mathrm r})$ has weights $e^{\mp i\theta/2}$; the four sums are $\theta,0,0,-\theta$. For the boost, both slots carry $e^{\mp\psi/2}$ because the boost is Hermitian; the four sums are $\psi,0,0,-\psi$. In both cases the vector weights are the sums of the two spinor weights, and each extremal vector weight is twice a spinor weight.

**The sandwich has no half-angle of its own.** It is the vector representation, of dimension four; its weights are the sums. The half-angle $\theta/2$ and the half-rapidity $\psi/2$ live on a single slot, in *One-Sided Operator and the Polar Decomposition*, §*The Half-Spin: the Eigenbasis and the Two Spinor Spaces*. The sandwich is the double of the half-spin, not a half-spin itself.

**The two Peirce chiralities are not the two Lorentz chiralities.** The two columns $S_+$ and $S_-$ carry the same Weyl representation $\rho$; the two Lorentz chiralities are the two tensor slots $S$ and $S^{*}$, that is the left and right slots.

**The addition is at the level of generators.** For a general word the two slot exponents do not combine into one rapidity and one angle unless the axes commute. The four products $\lambda_i\bar\lambda_j$ remain exact; the split into a boost and a rotation is the content of §*The Boost* and §*The Rotor* for commuting axes. For a pure non-central factor the eigenvalue $1$ occurs twice in the list; for the scale the value $r^{2}$ occurs four times, and for the phase the value $1$ occurs four times.

The whole section assumes $B\neq0$. When $B=0$ and $\vec Q\neq0$, $L_{\tilde Q}$ is a Jordan block, the common eigenbasis of $L_{\tilde Q}$ and $R_{\tilde Q^{*}}$ does not exist, and the spectral formula is unavailable; the sandwich itself remains defined. This is the degenerate case of *Spectral Regularity and Degeneracy in the Biquaternion Algebra*, §*The Degenerate Case: The Cone and Its Three Regimes*.

## The Angle Bookkeeping

### The Table

| factor | exponent | kind of exponent | sandwich | output parameter | angle |
|---|---|---|---|---|---|
| scale $r$ | $\ln r$ | real scalar | $r^{2}\tilde X$ | $2\ln r$ | none |
| phase $\exp(i\alpha)$ | $i\alpha$ | imaginary scalar | $\tilde X$ | $0$ | none |
| boost $\tilde U_{\mathrm b}$ | $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | imaginary vector | congruence | rapidity $\psi$ | rapidity |
| rotor $\tilde u_{\mathrm r}$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | real vector | automorphism | angle $\theta$ | rotation |

The table is a table of exponents, not of angles alone. The scale doubles its exponent and produces no angle; the phase produces no exponent and no angle; the boost and the rotor double theirs and produce a rapidity and a rotation.

### The Doubling Rule

**Proposition (the doubling rule).** Write each factor as $F=\exp(tA)$, where $t$ is its scalar parameter and $A$ its generator: $A=e_t$ for the scale, $A=i$ for the phase, $A=i\vec u_{\mathrm b}$ for the boost and $A=\vec u_{\mathrm r}$ for the rotor. Then

$$
\Theta_F(\tilde X)=\exp(tA)\,\tilde X\,\exp(tA^{*}).
$$

Three cases exhaust the word:

**(a)** $A^{*}=A$ (Hermitian). The two slots carry the same exponent $+tA$. If $A$ is central, as for the scale with $A=e_t$, the sandwich is multiplication by $\exp(2tA)$; if $A$ is non-central, as for the boost with $A=i\vec u_{\mathrm b}$, the sandwich is the congruence whose parameter is $2t$. In both cases the output parameter is $2t$.

**(b)** $A^{*}=-A$ and $A$ non-central (the rotor, $A=\vec u_{\mathrm r}$). The two slots carry opposite exponents, so the sandwich is the conjugation $\exp(t\,\mathrm{ad}_A)$, whose vector action is the rotation of angle $2t$; the output parameter is $2t$.

**(c)** $A^{*}=-A$ and $A$ central (the phase, $A=i$). The two slots carry opposite exponents and $A$ commutes with everything, so $\mathrm{ad}_A=0$ and the output parameter is $0$.

In one formula,

$$
\text{output parameter}=
\begin{cases}
2t, & A^{*}=A,\\
2t, & A^{*}=-A\ \text{and}\ A\ \text{non-central},\\
0, & A^{*}=-A\ \text{and}\ A\ \text{central}.
\end{cases}
$$

The doubling is therefore a property of the non-central factors, and of the Hermitian central one; the cancellation is a property of the skew-Hermitian central one. "Half-angle" is the name of the boost and rotor rows; it is not a property of the phase.

## The Image and the Kernel

**Theorem.** Let $\Theta:\mathbb{B}^{\times}\to GL_{\mathbb{R}}(\mathbb{B})$ be the sandwich map $\tilde Q\mapsto\Theta_{\tilde Q}$.

**(a)** The kernel is the central unit circle,
$$
\ker\Theta=U(1)=\{\lambda e_t:\lambda\in\mathbb{C},\ \lvert\lambda\rvert=1\}.
$$

**(b)** The image is the linear conformal Lorentz group,
$$
\boxed{\;\operatorname{im}\Theta\cong CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)\;},
$$
acting on $\mathbb{M}_-$ by a dilation of ratio $r^{2}$ composed with a proper orthochronous Lorentz transformation.

**(c)** On the modulus-one slice $r=1$, the image is $SO^{+}(1,3)$ and the kernel is $U(1)$.

**(d)** On the norm-one slice $\langle\tilde Q\rangle_{\natural}=1$, the image is $SO^{+}(1,3)$ and the kernel is $\{\pm e_t\}$; the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$.

*Proof.* (a) If $\Theta_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde Q^{*}=e_t$ by evaluating at $e_t$, so $\tilde Q^{*}=\tilde Q^{-1}$ and $\tilde Q\tilde X\tilde Q^{-1}=\tilde X$ for every $\tilde X$. Hence $\tilde Q$ is central, $\tilde Q=\lambda e_t$, and $\lvert\lambda\rvert=1$. Conversely, a central $\lambda e_t$ with $\lvert\lambda\rvert=1$ gives the identity, by the computation of §*The Central Phase*.

(b) Every unit is $\Rho U$ with $\Rho\in\mathbb{C}^{\times}$ and $U\in SL(2,\mathbb{C})$, the pair unique up to $(\Rho,U)\mapsto(-\Rho,-U)$. The kernel (a) is the unit circle in the first factor, so after that quotient the first factor is $\mathbb{R}_{>0}$ and the second is $SL(2,\mathbb{C})/\{\pm e_t\}=PSL(2,\mathbb{C})\cong SO^{+}(1,3)$:

$$
\operatorname{im}\Theta\cong\mathbb{R}_{>0}\times SO^{+}(1,3)=CO^{+}(1,3).
$$

(c) At $r=1$ the element is $\exp(i\alpha)U$ with $U\in SL(2,\mathbb{C})$, the pair unique up to $(\alpha,U)\mapsto(\alpha+\pi,-U)$. The kernel is still $U(1)$, and the quotient is $SO^{+}(1,3)$.

(d) At $\langle\tilde Q\rangle_{\natural}=1$ the element lies in $SL(2,\mathbb{C})$ and the kernel of the action on $\mathbb{M}_-$ is $\{\pm e_t\}$.

**Corollary (the isometry slice).** The sandwich is an isometry of the Lorentzian norm on $\mathbb{M}_-$ exactly when $r=1$. For general $r$,

$$ L^{T}G_-L=r^{4}G_-,\qquad \det L=r^{8}, $$

so the form is multiplied by $r^{4}$ and the volume by $r^{8}$; the causal type is preserved and the transformation is a similarity of ratio $r^{2}$.

**Remark (what the image is not).** The image is not the unitary group and not $GL(2,\mathbb{C})$. The unitary group acts on the spinor module and sees the phase; the sandwich sees only the conformal Lorentz group. The two readings of the same word are the subject of *The Polar Decomposition of Biquaternions*, §*The Operator Reading: the Twist*, and of this article.

## The Null Cone

On the null cone $\langle\tilde Q\rangle_{\natural}=0$ the polar word does not exist, but the sandwich does. If $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, the matrix $\mathsf M_2(\tilde Q)$ is a nonzero $2\times2$ matrix of determinant zero, hence of complex rank one. The sandwich therefore has complex rank one, and its image is the complex line spanned by $\tilde Q\tilde Q^{*}$: writing $\mathsf M_2(\tilde Q)=uv^{*}$ with column $u$ and row $v^{*}$,

$$
\mathsf M_2(\tilde Q)\,X\,\mathsf M_2(\tilde Q)^{*}
=u\,(v^{*}Xv)\,u^{*},
$$

which is a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. The element $\tilde Q\tilde Q^{*}$ is nonzero because its trace in the matrix model is the squared Frobenius norm of $\mathsf M_2(\tilde Q)$. The action collapses the eight-dimensional algebra onto one complex line; it is not invertible, and it has no polar reading because the scale, the phase, the boost and the rotor are not available on the cone.

**The degenerate case in coordinates.** Write $\tilde Q=Q^0e_t+Q^k\vec e_k$ and $\vec Q^\natural=(\overline{Q^1},\overline{Q^2},\overline{Q^3})$. For $k=1,2,3$ the scalar component of the image of a vector basis element is

$$
\Theta_{\tilde Q}(\vec e_k)^0 = 2i\,\mathrm{Im}\bigl(Q^0\overline{Q^k}\bigr) - \bigl(\vec Q\times\vec Q^\natural\bigr)^k ,
$$

which vanishes when all four coefficients of $\tilde Q$ are real, and when $\tilde Q$ is central. On the cone the trace of the rank-one operator is $4\lvert Q^0\rvert^2$, so

$$
\Theta_{\tilde Q}\circ\Theta_{\tilde Q}=4\lvert Q^0\rvert^{2}\,\Theta_{\tilde Q} .
$$

The operator is therefore nilpotent exactly when $Q^0=0$, and for $Q^0\neq0$ it is a projection up to the scalar $4\lvert Q^0\rvert^{2}$.

## Summary

The Hermitian sandwich of the polar word is read factor by factor. The closed form is

$$
\Theta_{\tilde Q}=r^{2}\,\Theta_{\tilde U_{\mathrm b}}\circ\Theta_{\tilde u_{\mathrm r}},
\qquad
\Theta_{\exp(i\alpha)}=\mathrm{id}.
$$

The scale dilates by $r^{2}$ and doubles its exponent $\ln r$ to $2\ln r$. The phase cancels: its exponent $i\alpha$ produces nothing, because it is central and unitary, and the whole $U(1)$-orbit of an element has one sandwich. The boost is a congruence by the Hermitian positive $\tilde U_{\mathrm b}$; its exponent $i\tfrac{\psi}{2}\vec u_{\mathrm b}$ produces the rapidity $\psi$. The rotor is an inner automorphism; its exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ produces the rotation of angle $\theta$. The doubling rule is that a Hermitian exponent and a non-central skew-Hermitian exponent double, while a central skew-Hermitian exponent cancels. The norm scales by $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$, so the sandwich is an isometry on the unit-norm slice.

The spectral form of the rule is the product formula. The left and right slots commute, and their eigenvalues are $\lambda_\pm$ and $\bar\lambda_\pm$. The spectrum of the sandwich is
$$
\operatorname{spec}\Theta_{\tilde Q}
=\bigl\{\lambda_+\bar\lambda_+,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ \lambda_-\bar\lambda_-\bigr\}.
$$
The one-slot pair of the rotor is $(e^{i\theta/2},e^{-i\theta/2})$ and the two-slot products are $e^{\pm i\theta}$; the one-slot pair of the boost is $(e^{-\psi/2},e^{\psi/2})$ and the products are $e^{\pm\psi}$; the scale gives $r^{2}$ and the phase gives $1$. The sandwich is therefore the two-slot operator: its spectrum is the four products, not the two eigenvalues. In representation-theoretic terms it is $\rho\otimes\bar\rho$, the complexified vector representation: the vector weights are the sums of the two spinor weights, so the sandwich is the double of the half-spin, not a half-spin itself. **The half-spin is the one-sided operator**: the half-angle and the half-rapidity are carried by one slot, and the full angle and the full rapidity are their products over the two slots.

The image of the sandwich on the group of units is $CO^{+}(1,3)$, the kernel is $U(1)$, and the isometry slice is $r=1$, where the image is $SO^{+}(1,3)$. On the norm-one slice the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$. On the null cone the sandwich survives as an operator of complex rank one, with image the line spanned by $\tilde Q\tilde Q^{*}$.

The phase is the one factor that the sandwich does not see. It is visible to the norm, to the determinant and to the module, which is why the polar word carries it; it is invisible to the vector action, which is why the sandwich is a representation whose image is the conformal Lorentz group and not the full group of units.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian subspaces, $\tilde Q^{*}=\pm\tilde Q$ |
| $\Theta_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian sandwich |
| $\langle\Theta_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}$ | the scaling of the norm; an isometry on the unit-norm slice |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm of the polar series |
| $\Rho=r\exp(i\alpha)$ | the complex modulus, the principal square root of $\langle\tilde Q\rangle_{\natural}$ |
| $P=\exp(i\alpha)$ | the central phase factor |
| $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\lambda_\pm=Q_t\pm iB$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the two eigenvalues of $L_{\tilde Q}$, and of $R_{\tilde Q}$ |
| $\lambda_i\bar\lambda_j$ | the four eigenvalues of the sandwich in its common eigenbasis |
| $\Delta=\operatorname{diag}(\lambda_+,\lambda_-)$ | the matrix of $\tilde Q$ in the Q-adapted matrix model |
| $S,S^{*}$ | the spinor space $\mathbb{C}^{2}$ and its dual, with $\mathbb{B}\cong S\otimes S^{*}$ |
| $\rho,\bar\rho$ | the defining representation on $S$ and its conjugate |
| $\mathsf M^{\tilde Q}$ | the Q-adapted matrix model, not the Pauli model $\mathsf M_2$ |
| $\tilde\Pi_\pm$, $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the eigenprojections and the two left ideals of the one-sided reading (Peirce chirality) |
| $\psi\ge0$, $\theta\in[0,2\pi]$ | the rapidity and the rotation angle |
| $B_\pm$ | the $4\times4$ matrices of the boost on $\mathbb{M}_\pm$ |
| $\mathsf R(\theta,\vec u_{\mathrm r})$ | the Rodrigues rotation matrix of the rotor |
| $G_\pm$ | the matrices of the norm on the two sectors, $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+$ |
| $CO^{+}(1,3)$ | the linear conformal Lorentz group, the image of the sandwich |
| $U(1)$ | the kernel of the sandwich, the central unit circle |
| $\langle\tilde Q\rangle_{\natural}=1$ | the norm-one slice, $SL(2,\mathbb{C})$ |

## Further Reading

- [One-Sided Operator and the Polar Decomposition](one-sided-operator-and-the-polar-decomposition.html), for the one-sided companion: the left and right multiplications, the sector decomposition and the exchange $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$ by the phase $i$.
- [The Quaternionic Norm-Regular, Spectrally Regular Sector](the-quaternionic-norm-regular-spectrally-regular-sector.html), §*The Q-Adapted Peirce Basis, the Nilpotents, and the Eigenbasis*, for the basis, the two chiral spinor spaces and the diagonal action of $\tilde Q$.
- [Relations between Exponential Polar Decomposition and Eigenbasis of a Biquaternion](relations-between-exponential-polar-decomposition-and-eigenbasis-of-a-biquaternion.html), for the general dictionary between the spectral data and the polar angles when the axes do not commute.
- [The Polar Decomposition of Biquaternions](modulus-unit-polar-decomposition-of-biquaternions.html), for the four factors, the modulus, the branch and the domain, and §*The Operator Reading: the Twist*, for the same word read on the spinor module.
- [The Polar Decomposition and Remarkable Subspaces](the-polar-decomposition-and-remarkable-subspaces.html), §*The Action on the Two Halves*, for the detailed action on the two sectors, the boost matrices and the comparison of the two signs.
- [The Cartan Hermitian Pairing of the Polar Decomposition of Biquaternions](the-cartan-hermitian-pairing-of-the-polar-decomposition-of-biquaternions.html), for the Hermitian positive and unitary factors and the equation $\tilde Q\tilde Q^{*}=\tilde H^{2}$.
- [The Quaternion Pairing of the Polar Decomposition of Biquaternions](the-quaternion-pairing-of-the-polar-decomposition-of-biquaternions.html) and [The Hamilton Root Pairing of the Polar Decomposition of Biquaternions](the-hamilton-root-pairing-of-the-polar-decomposition-of-biquaternions.html), for the two partial two-factor groupings.
- [Introduction to the 4×4 Matrix Element Representation $M_4(\mathbb{C})_L$ of Biquaternions](introduction-to-the-4x4-matrix-element-representation-of-biquaternions.html), §*The Sandwich in the Regular Basis*, for the sandwich as a product of the two regular maps.
- [Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint](completely-positive-maps-of-a-hermitian-algebra-with-hermitian-adjoint.html), for the sandwich as a completely positive map and its rank-one place among the completely positive maps.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group in biquaternionic form and the double cover.
- [Operator and the Polar Decomposition of a Split-Complex Number](operator-and-the-polar-decomposition-of-a-split-complex-number.html), for the commutative case where the sandwich collapses to $\langle Q\rangle_{*}$ times the identity.
- [Operator and the Polar Decomposition of a Reduced Biquaternion](operator-and-the-polar-decomposition-of-a-reduced-biquaternion.html), for the commutative case where the sandwich collapses to multiplication by the modulus squared and the phases cancel.
