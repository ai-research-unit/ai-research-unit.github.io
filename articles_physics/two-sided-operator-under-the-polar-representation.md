# __Two-Sided Operator Under the Polar Representation__

## Introduction

The **Hermitian sandwich** of the biquaternion algebra is the operator

$$
\Theta_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad
\Theta_{\tilde Q}(X)=\tilde Q\,X\,\tilde Q^{*},
$$

the two-sided operator whose right factor is the Hermitian conjugate of its left factor. It is the operator that carries the Lorentz group on the algebra: on the norm-one slice it acts on the anti-Hermitian and Hermitian subspaces by the proper orthochronous Lorentz group, and on the full group of units it is that action composed with a dilation.

The polar element representation writes an element of non-vanishing norm as four factors. In the physics normalization of the corpus the word is

$$
\tilde Q=r\exp(i\alpha)\,B\,\tilde q,\qquad
B=\exp(-i\psi\vec u_{\mathrm b}),\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and real unit axes $\vec u_{\mathrm b},\vec u_{\mathrm r}$.

The factor $B$ is the **positive Hermitian boost factor**, and it is not the factor that acts physically on a four-vector. The physical factor is its inverse square root, the **frame rotor**

$$
\tilde U_{\mathrm L}=B^{-1/2}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\qquad
B=\tilde U_{\mathrm L}^{-2}.
$$

This is the one point where the present article differs from its mathematics companion, and it is the point of the article. The sandwich by $B$ is the inverse of the Lorentz boost of rapidity $2\psi$; the sandwich by $\tilde U_{\mathrm L}$ is the Lorentz boost of rapidity $\psi$. The word stores the boost as the inverse square of the physical factor, so the operator of the word and the physical four-vector operator are two readings of the same data, related by the square root in the boost slot.

The article reads both. The operator of the word is

$$
\Theta_{\tilde Q}=r^{2}\,\Theta_B\circ\Theta_{\tilde q}
=r^{2}\,\Theta_{\tilde U_{\mathrm L}}^{-2}\circ\Theta_{\tilde q},
$$

and the physical four-vector operator is

$$
\Theta_{\tilde Q_L}=r^{2}\,\Theta_{\tilde U_{\mathrm L}}\circ\Theta_{\tilde q},
\qquad
\tilde Q_L=r\exp(i\alpha)\tilde U_{\mathrm L}\tilde q.
$$

For each factor the article answers one question: what does the factor do to the operator, and what becomes of its exponent? The answer is a table with one row per factor. The phase row is zero. The boost row is the square-root rule.

The plan is the following. §*The Sandwich of the Word* proves the multiplicativity and the closed form. §*The Scale* to §*The Rotor* take the four factors in the order of the word. §*The Angle Bookkeeping* collects the exponents and states the doubling rule, with the square-root rule for the boost. §*The Image and the Kernel* identifies the image as the conformal Lorentz group and the kernel as the central unit circle. §*The Null Cone* records the degenerate case. §*Worked Numbers* fixes one element and checks the formulas. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^2=\vec e_y^2=\vec e_z^2=-e_t$. The scalar imaginary is $i$, central, $i^2=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z.
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{M}_\pm=\{X\in\mathbb{B}:X^{*}=\pm X\}.
$$

On $\mathbb{M}_-$ an element is $X=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{M}_+$ an element is $X=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central. In the physical reading $\mathbb{M}_-$ is the material sector and $\mathbb{M}_+$ the informational sector.

The **norm** is the complex number

$$
N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}
=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},
$$

and the **domain** of the polar word is $N(\tilde Q)\neq0$. The word is

$$
\tilde Q=r\exp(i\alpha)B\tilde q,\qquad
B=\exp(-i\psi\vec u_{\mathrm b}),\qquad
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr),
$$

with $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\psi\ge0$, $\theta\in[0,2\pi]$, and real unit vectors $\vec u_{\mathrm b},\vec u_{\mathrm r}$. The modulus is $\rho=r\exp(i\alpha)=\sqrt{N(\tilde Q)}$ on the principal branch, so $r=\lvert\rho\rvert$ and $\alpha=\tfrac12\arg N(\tilde Q)$. The factors satisfy

$$
B^{*}=B,\qquad N(B)=1,\qquad B=\tilde U_{\mathrm L}^{-2},\qquad
\tilde U_{\mathrm L}=B^{-1/2}=\exp\Bigl(i\frac{\psi}{2}\vec u_{\mathrm b}\Bigr),
\qquad
\tilde U_{\mathrm L}^{*}=\tilde U_{\mathrm L},\qquad N(\tilde U_{\mathrm L})=1,
$$

and

$$
\tilde q^{*}=\tilde q^{\natural}=\tilde q^{-1},\qquad N(\tilde q)=1.
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=N(\tilde Q)$.

The sandwich is written $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ throughout. It uses the Hermitian conjugate in the right slot and never the inverse; the two coincide only where $\tilde Q$ is unitary. The word's boost factor is $B$; the frame rotor is $\tilde U_{\mathrm L}$; the two are related by $B=\tilde U_{\mathrm L}^{-2}$.

## The Sandwich of the Word

### Elementary Properties

**Proposition.** Let $\tilde Q_1,\tilde Q_2\in\mathbb{B}$ and $X\in\mathbb{B}$. Then:

**(a)** $\Theta_{\tilde Q_1\tilde Q_2}=\Theta_{\tilde Q_1}\circ\Theta_{\tilde Q_2}$;

**(b)** $\Theta_{\tilde Q_1}$ is $\mathbb{C}$-linear in $X$;

**(c)** $\Theta_{\tilde Q_1}$ is invertible if and only if $\tilde Q_1$ is a unit, and then $\Theta_{\tilde Q_1}^{-1}=\Theta_{\tilde Q_1^{-1}}$;

**(d)** $\Theta_{\tilde Q_1}$ preserves each of $\mathbb{M}_+$ and $\mathbb{M}_-$;

**(e)** $\Theta_{\tilde Q_1}(e_t)=\tilde Q_1\tilde Q_1^{*}$.

*Proof.* (a) $(\tilde Q_1\tilde Q_2)X(\tilde Q_1\tilde Q_2)^{*}=\tilde Q_1(\tilde Q_2X\tilde Q_2^{*})\tilde Q_1^{*}$. (b) The multiplication and the right factor are $\mathbb{C}$-linear. (c) The inverse of $\Theta_{\tilde Q_1}$ is $\Theta_{\tilde Q_1^{-1}}$, because $\tilde Q_1^{-1}\tilde Q_1X\tilde Q_1^{*}\tilde Q_1^{-*}=X$ and $(\tilde Q_1^{-1})^{*}=(\tilde Q_1^{*})^{-1}$. (d) If $X^{*}=\pm X$, then

$$
\bigl(\tilde Q_1X\tilde Q_1^{*}\bigr)^{*}
=\tilde Q_1X^{*}\tilde Q_1^{*}
=\pm\tilde Q_1X\tilde Q_1^{*}.
$$

(e) Put $X=e_t$.

The preservation of the two sectors is the structural reason the action splits into two formulas, one per sector, and the reason a sandwich cannot mix the Hermitian and the anti-Hermitian parts.

### The Closed Form

**Theorem (the sandwich of the polar word).** Let $\tilde Q=r\exp(i\alpha)B\tilde q$ with $N(\tilde Q)\neq0$. Then

$$
\Theta_{\tilde Q}=r^{2}\,\Theta_B\circ\Theta_{\tilde q}
=r^{2}\,\Theta_{\tilde U_{\mathrm L}}^{-2}\circ\Theta_{\tilde q},
\qquad
\Theta_{\exp(i\alpha)}=\mathrm{id},
$$

that is,

$$
\Theta_{\tilde Q}(X)=r^{2}\,B\,\tilde q\,X\,\tilde q^{-1}B.
$$

The physical four-vector operator is

$$
\Theta_{\tilde Q_L}=r^{2}\,\Theta_{\tilde U_{\mathrm L}}\circ\Theta_{\tilde q},
\qquad
\tilde Q_L=r\exp(i\alpha)\tilde U_{\mathrm L}\tilde q.
$$

*Proof.* The Hermitian conjugate of the word is

$$
\tilde Q^{*}
=\bigl(r\exp(i\alpha)B\tilde q\bigr)^{*}
=\tilde q^{*}B^{*}\bigl(r\exp(i\alpha)\bigr)^{*}
=\tilde q^{-1}B\,r\exp(-i\alpha)
=r\exp(-i\alpha)\,\tilde q^{-1}B,
$$

because the scalars are central. Hence

$$
\tilde QX\tilde Q^{*}
=r\exp(i\alpha)B\tilde q\,X\,\tilde q^{-1}B\,r\exp(-i\alpha)
=r^{2}\,B\bigl(\tilde qX\tilde q^{-1}\bigr)B,
$$

and $\exp(i\alpha)\exp(-i\alpha)=1$. The identity $\Theta_{\exp(i\alpha)}=\mathrm{id}$ is the central-phase computation of §*The Central Phase*. The last formula is the same computation with $B$ replaced by $\tilde U_{\mathrm L}$.

**Remark (the order).** The rightmost factor of the word acts first: the rotor, then the boost factor, then the scale. The phase may be inserted anywhere, and so may the scale, because both are central. The boost factor and the rotor do not commute, so their order is part of the word and cannot be exchanged. In the physical reading the rightmost factor is the spin rotation and the next is the boost, so the operator rotates and then boosts; a boost followed by a rotation would differ by the Thomas–Wigner rotation.

**Remark (the square-root rule).** The word's boost factor is the inverse square of the frame rotor, $B=\tilde U_{\mathrm L}^{-2}$. Hence $\Theta_B=\Theta_{\tilde U_{\mathrm L}}^{-2}$, and the sandwich of the word acts in the boost slot by the inverse square of the physical boost. The physical operator replaces $\Theta_B$ by $\Theta_{\tilde U_{\mathrm L}}$; the scale and the rotor are unchanged. In the matrix model

$$
\mathsf M_2(B)=\exp(-\psi\,\sigma_{\mathrm b}),\qquad
\mathsf M_2(\tilde U_{\mathrm L})=\exp\Bigl(+\frac{\psi}{2}\sigma_{\mathrm b}\Bigr),
\qquad
\sigma_{\mathrm b}=\vec u_{\mathrm b}\cdot\vec\sigma,
$$

so the physical Lorentz transformation is the congruence by $\exp(+\tfrac{\psi}{2}\sigma_{\mathrm b})$, of rapidity $+\psi$, while the word's factor is the congruence by $\exp(-\psi\sigma_{\mathrm b})$, of rapidity $-2\psi$. The exponent of $B$ is $-i\psi\vec u_{\mathrm b}$; the exponent of $\tilde U_{\mathrm L}$ is $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$. The two differ by the sign and the factor two. The square-root rule is not a convention of the algebra: it is the statement that the word stores the boost as the inverse square of the physical factor, and that the physical operator takes the inverse square root.

## The Scale

### The Factor

The scale is $r=\exp(\ln r)$, a positive real. It is central, real and Hermitian, $r^{*}=r$, and it is the only factor whose exponent is a real scalar.

### The Sandwich

$$
\Theta_r(X)=rXr^{*}=r^{2}X.
$$

On $\mathbb{M}_-$ and on $\mathbb{M}_+$ alike, every coordinate is multiplied by $r^{2}$: $a\mapsto r^{2}a$ and $\vec b\mapsto r^{2}\vec b$. The scale is a dilation of ratio $r^{2}$ of the whole algebra, and the only factor that changes the norm of the argument,

$$
N\bigl(\Theta_r(X)\bigr)=r^{4}N(X).
$$

### The Exponent

The exponent is $\ln r$, and the sandwich sends it to

$$
\ln r\longmapsto 2\ln r.
$$

There is no angle. The factor two is the same factor two as in the boost and the rotor: the exponent of the factor is half the exponent of its image. The scale is the case in which the doubled parameter is a dilation and not a rotation or a rapidity. The map $r\mapsto r^{2}$ is an isomorphism of $\mathbb{R}_{>0}$, so the scale is recovered from its sandwich; only the sign of the factor is lost, and the polar word has $r>0$.

## The Central Phase

### The Factor

The phase is $P=\exp(i\alpha)$, central and unitary,

$$
P^{*}=P^{-1}=\exp(-i\alpha),\qquad N(P)=\exp(2i\alpha).
$$

Its exponent is $i\alpha$, purely imaginary and central.

### The Sandwich

$$
\Theta_P(X)=\exp(i\alpha)\,X\,\exp(-i\alpha)=X.
$$

The two scalars commute with $X$ and with each other, and the second is the inverse of the first, so the product is the identity operator.

**The phase is not a half-angle of the sandwich.** The exponent $i\alpha$ is the full generator of the multiplication by $\exp(i\alpha)$ on the module; the sandwich cancels it. It is already half of the argument of the norm, $N=\rho^{2}=r^{2}\exp(2i\alpha)$, and that is the only doubling in which it takes part. Writing $\exp(i\alpha/2)$ in the word would not change the sandwich, which is the identity either way; it would only change the meaning of the letter $\alpha$, and it would break $\rho=\sqrt N$ unless $\alpha$ were redefined as $\arg N$.

### The Cancelled Phase

This is the central remark of the article. The phase is the only factor of the word whose sandwich is the identity whatever the value of its parameter. It is not halved, not doubled and not shifted: it is annihilated.

**First, the cancellation is exact and global.** It holds for every $X$, not merely on one subspace, and it uses only two properties, centrality and unitarity. Any central factor of modulus one cancels in any sandwich: if $C$ is central and $C^{*}=C^{-1}$, then

$$
CXC^{*}=XCC^{-1}=X.
$$

**Second, two elements that differ by a phase have the same sandwich.** For a central complex $\lambda$,

$$
\Theta_{\lambda\tilde Q}(X)=\lambda\tilde QX\tilde Q^{*}\bar\lambda
=\lvert\lambda\rvert^{2}\Theta_{\tilde Q}(X).
$$

On the unit circle $\lvert\lambda\rvert=1$ the two sandwiches are equal, so the whole $U(1)$-orbit of $\tilde Q$ has one sandwich. On the positive real axis the sandwich scales by $\lambda^{2}$, which is the scale row of the table. The phase is the unit-modulus part of the centre, and it is exactly the part that disappears.

**Third, the phase is absent from this action but not from the algebra.** It reappears in three places, and the list is the reason the polar word needs it:

- the norm, $N(\tilde Q)=\tilde Q\tilde Q^{\natural}=\rho^{2}=r^{2}\exp(2i\alpha)$;
- the determinant, $\det\mathsf M_2(\tilde Q)=\rho^{2}=r^{2}\exp(2i\alpha)$;
- the module, where left multiplication by $\tilde Q$ acts on the spinor module by the scalar $\rho=r\exp(i\alpha)$.

The first two are quadratic in $\rho$ and see $2\alpha$; the third is linear and sees $\alpha$; the sandwich multiplies by $\rho$ on the left and by $\bar\rho$ on the right and sees $0$. The ladder of the phase is therefore $2,2,1,0$.

**Fourth, the spectral reading confirms it.** In the spectra of the operators on the biquaternion algebra with Hermitian adjoint, the eigenvalues of $\Theta_{\tilde Q}$ are the products $\lambda_i\bar\lambda_j$ of the eigenvalues of $\mathsf M_2(\tilde Q)$. A phase multiplies every $\lambda_i$ by $\exp(i\alpha)$ and every $\bar\lambda_j$ by $\exp(-i\alpha)$, so every product is unchanged. The cancellation is visible in the spectrum without any computation in coordinates.

**Fifth, the phase row of the table is zero.** A table that halves every exponent would put $\alpha/2$ in the phase row and would be wrong by the whole phase; a table that repeats the exponent would put $\alpha$ there and would be wrong by the sign of the right factor. The only correct entry is $0$.

**Physical reading.** The phase is the $ict$ phase of the corpus and the sector label. The sandwich is the four-vector action, and a four-vector has no memory of the phase: the material and informational sectors are acted on by the same Lorentz transformation, and the phase only decides which sector the element belongs to. The phase is the kernel of the sandwich, and the kernel is the central unit circle.

## The Boost Factor

### The Factor

The boost factor is

$$
B=\exp(-i\psi\vec u_{\mathrm b})
=\cosh\psi\,e_t-i\sinh\psi\,\vec u_{\mathrm b},
\qquad \psi\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1.
$$

It is Hermitian and of norm one,

$$
B^{*}=B,\qquad N(B)=1,
$$

and its inverse and square are

$$
B^{-1}=\exp(i\psi\vec u_{\mathrm b})=\tilde U_{\mathrm L}^{2},
\qquad
B^{2}=\exp(-2i\psi\vec u_{\mathrm b}).
$$

The boost factor is not unitary: $B^{-1}\neq B^{*}$ unless $\psi=0$.

### The Sandwich on the Two Sectors

The right slot is $B^{*}=B$, so the sandwich is a **congruence**,

$$
\Theta_B(X)=B\,X\,B,
$$

and not a conjugation. Write $b_\parallel=\vec u_{\mathrm b}\cdot\vec b$ and $\vec b_\perp=\vec b-b_\parallel\vec u_{\mathrm b}$.

On $\mathbb{M}_-$, for $X=ia\,e_t+\vec b$,

$$
\Theta_B(X)=ia'\,e_t+\vec b',
\qquad
a'=a\cosh 2\psi+b_\parallel\sinh 2\psi,\qquad
b_\parallel'=b_\parallel\cosh 2\psi+a\sinh 2\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

On $\mathbb{M}_+$, for $X=a\,e_t+i\vec b$,

$$
\Theta_B(X)=a'\,e_t+i\vec b',
\qquad
a'=a\cosh 2\psi-b_\parallel\sinh 2\psi,\qquad
b_\parallel'=b_\parallel\cosh 2\psi-a\sinh 2\psi,\qquad
\vec b_\perp'=\vec b_\perp .
$$

The two formulas differ only in the signs of the cross terms. The derivation is one line per piece. For the time piece,

$$
B\,(ia\,e_t)\,B=ia\,B^{2}
=ia\cosh 2\psi+a\sinh 2\psi\,\vec u_{\mathrm b},
$$

and for the vector piece the perpendicular part is fixed and the parallel part is stretched by $\cosh 2\psi$; the cross terms combine into the formulas above. In the coordinates $(a,b_x,b_y,b_z)$ the matrices of the two actions are

$$
B_-(\psi)=
\begin{pmatrix}
\cosh 2\psi & \sinh 2\psi\,\vec u_{\mathrm b}^{\,T}\\
\sinh 2\psi\,\vec u_{\mathrm b} & I_3+(\cosh 2\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

$$
B_+(\psi)=
\begin{pmatrix}
\cosh 2\psi & -\sinh 2\psi\,\vec u_{\mathrm b}^{\,T}\\
-\sinh 2\psi\,\vec u_{\mathrm b} & I_3+(\cosh 2\psi-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

with $B_+(\psi)=B_-(\psi)^{-1}$. Each preserves its form, $B_\pm^{T}G_\pm B_\pm=G_\pm$, where $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+=\operatorname{diag}(-1,1,1,1)$.

### The Exponent and the Rapidity

The exponent is $-i\psi\vec u_{\mathrm b}$ and the output is the rapidity $-2\psi$, that is, the inverse of the boost of rapidity $2\psi$. The parameter of the factor is half the parameter of its image in absolute value, and the sign is the sign of the exponent. The boost factor is Hermitian, so both slots carry the exponent with the same sign; the sandwich adds the two exponents instead of cancelling them, and the sum is $2\cdot(-\psi)=-2\psi$.

**Physical reading.** The word's factor $B$ is the positive Hermitian square of the inverse frame rotor. The physical boost on a four-vector is the congruence by $\tilde U_{\mathrm L}=B^{-1/2}$, whose exponent is $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$ and whose output is the rapidity $+\psi$. The word stores the boost as the inverse square, so the sandwich of the word doubles the rapidity and reverses its sign; the physical operator takes the inverse square root and restores the physical value. The two statements are one statement about the same rapidity $\psi$, read at the two levels of the word.

## The Rotor

### The Factor

The rotor is

$$
\tilde q=\exp\Bigl(\frac{\theta}{2}\vec u_{\mathrm r}\Bigr)
=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\,\vec u_{\mathrm r},
\qquad \theta\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1.
$$

It is a real quaternion, of norm one, and unitary,

$$
\tilde q^{*}=\tilde q^{\natural}=\tilde q^{-1},\qquad N(\tilde q)=1.
$$

Unlike the boost factor, the rotor is both norm-one and unitary, and its right slot is therefore the inverse.

### The Sandwich

$$
\Theta_{\tilde q}(X)=\tilde q\,X\,\tilde q^{-1}.
$$

The sandwich is a conjugation by an invertible element, hence an algebra automorphism. On a general element $X=X_te_t+\vec X$ it fixes the scalar part and rotates the vector part,

$$
\Theta_{\tilde q}(X)=X_te_t+\mathsf R(\theta,\vec u_{\mathrm r})\,\vec X,
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

The exponent is $\tfrac{\theta}{2}\vec u_{\mathrm r}$ and the output is the rotation of angle $\theta$ about $\vec u_{\mathrm r}$. The parameter of the factor is half the parameter of its image. The rotor is unitary, so the two slots carry opposite signs; the sandwich conjugates instead of composing the two exponents, and the conjugation by $\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ is the rotation of angle $\theta$. Equivalently, the double cover $SU(2)\to SO(3)$ sends $\pm\tilde q$ to the same rotation, and the parameter $\theta$ of the image is twice the parameter $\theta/2$ of the rotor.

**Physical reading.** The rotor is the spatial rotation of the four-vector's vector part and the spin rotation of the spinor. It does not touch the time component. Its order with the boost is the physical order because the two do not commute; the commutator is the Thomas–Wigner rotation of the composition.

## The Angle Bookkeeping

### The Table

| factor | exponent | kind of exponent | sandwich | output parameter | physical name |
|---|---|---|---|---|---|
| scale $r$ | $\ln r$ | real scalar | $r^{2}X$ | $2\ln r$ | dilation |
| phase $\exp(i\alpha)$ | $i\alpha$ | imaginary scalar | $X$ | $0$ | $ict$ phase, sector |
| boost $B$ | $-i\psi\vec u_{\mathrm b}$ | imaginary vector, Hermitian | $BXB$ | $-2\psi$ | inverse square of the boost |
| frame rotor $\tilde U_{\mathrm L}$ | $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$ | imaginary vector, Hermitian | $\tilde U_{\mathrm L}X\tilde U_{\mathrm L}$ | $+\psi$ | boost |
| rotor $\tilde q$ | $\tfrac{\theta}{2}\vec u_{\mathrm r}$ | real vector | $\tilde qX\tilde q^{-1}$ | $\theta$ | rotation |

The table is a table of exponents, not of angles alone. The scale doubles its exponent and produces no angle; the phase produces no exponent and no angle; the boost factor and the frame rotor double theirs and produce a rapidity; the rotor doubles its and produces a rotation. The boost row and the frame-rotor row are the two normalizations of the same physical boost.

### The Doubling Rule

**Proposition (the doubling rule).** Write each factor as $F=\exp(tA)$, where $t$ is its scalar parameter and $A$ its generator: $A=e_t$ for the scale, $A=i$ for the phase, $A=-i\vec u_{\mathrm b}$ for the boost factor, $A=+i\vec u_{\mathrm b}$ for the frame rotor and $A=\vec u_{\mathrm r}$ for the rotor. Then

$$
\Theta_F(X)=\exp(tA)\,X\,\exp(tA^{*}).
$$

Three cases exhaust the word:

**(a)** $A^{*}=A$ (Hermitian). The two slots carry the same exponent $+tA$. If $A$ is central, as for the scale with $A=e_t$, the sandwich is multiplication by $\exp(2tA)$; if $A$ is non-central, as for the boost factor and the frame rotor with $A=\mp i\vec u_{\mathrm b}$, the sandwich is the congruence whose parameter is $2t$. In both cases the output exponent is $2tA$.

**(b)** $A^{*}=-A$ and $A$ non-central (the rotor, $A=\vec u_{\mathrm r}$). The two slots carry opposite exponents, so the sandwich is the conjugation $\exp(t\,\mathrm{ad}_A)$, whose vector action is the rotation of angle $2t$; the output parameter is $2t$.

**(c)** $A^{*}=-A$ and $A$ central (the phase, $A=i$). The two slots carry opposite exponents and $A$ commutes with everything, so $\mathrm{ad}_A=0$ and the output parameter is $0$.

In one formula, for the scalar output parameter,

$$
\text{output parameter}=
\begin{cases}
2t, & A^{*}=A,\\[2pt]
2t, & A^{*}=-A\ \text{and}\ A\ \text{non-central},\\[2pt]
0, & A^{*}=-A\ \text{and}\ A\ \text{central}.
\end{cases}
$$

The doubling is therefore a property of the non-central factors and of the Hermitian central one; the cancellation is a property of the skew-Hermitian central one. "Half-angle" is the name of the rotor row and, in the physics normalization, of the frame-rotor row; it is not a property of the phase. For the boost factor $A=-i\vec u_{\mathrm b}$ and $t=\psi$, so the output exponent is $-2i\psi\vec u_{\mathrm b}$ and the rapidity is $-2\psi$; for the frame rotor $A=+i\vec u_{\mathrm b}$ and $t=\psi/2$, so the output exponent is $+i\psi\vec u_{\mathrm b}$ and the rapidity is $+\psi$.

## The Image and the Kernel

**Theorem.** Let $\Theta:\mathbb{B}^{\times}\to GL_{\mathbb{R}}(\mathbb{B})$ be the sandwich map $\tilde Q\mapsto\Theta_{\tilde Q}$.

**(a)** The kernel is the central unit circle,
$$
\ker\Theta=U(1)=\{\lambda e_t:\lambda\in\mathbb{C},\ \lvert\lambda\rvert=1\}.
$$

**(b)** The image is the linear conformal Lorentz group,
$$
\operatorname{im}\Theta\cong CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3),
$$
acting on $\mathbb{M}_-$ by a dilation of ratio $r^{2}$ composed with a proper orthochronous Lorentz transformation.

**(c)** On the modulus-one slice $r=1$, the image is $SO^{+}(1,3)$ and the kernel is $U(1)$.

**(d)** On the norm-one slice $N=1$, the image is $SO^{+}(1,3)$ and the kernel is $\{\pm e_t\}$; the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$.

*Proof.* (a) If $\Theta_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde Q^{*}=e_t$ by evaluating at $e_t$, so $\tilde Q^{*}=\tilde Q^{-1}$ and $\tilde QX\tilde Q^{-1}=X$ for every $X$. Hence $\tilde Q$ is central, $\tilde Q=\lambda e_t$, and $\lvert\lambda\rvert=1$. Conversely, a central $\lambda e_t$ with $\lvert\lambda\rvert=1$ gives the identity, by §*The Central Phase*.

(b) Every unit is $\rho U$ with $\rho\in\mathbb{C}^{\times}$ and $U\in SL(2,\mathbb{C})$, the pair unique up to $(\rho,U)\mapsto(-\rho,-U)$. The kernel (a) is the unit circle in the first factor, so after that quotient the first factor is $\mathbb{R}_{>0}$ and the second is $SL(2,\mathbb{C})/\{\pm e_t\}=PSL(2,\mathbb{C})\cong SO^{+}(1,3)$:

$$
\operatorname{im}\Theta\cong\mathbb{R}_{>0}\times SO^{+}(1,3)=CO^{+}(1,3).
$$

(c) At $r=1$ the element is $\exp(i\alpha)U$ with $U\in SL(2,\mathbb{C})$, the pair unique up to $(\alpha,U)\mapsto(\alpha+\pi,-U)$. The kernel is still $U(1)$, and the quotient is $SO^{+}(1,3)$.

(d) At $N=1$ the element lies in $SL(2,\mathbb{C})$ and the kernel of the action on $\mathbb{M}_-$ is $\{\pm e_t\}$.

**Corollary (the isometry slice).** The sandwich is an isometry of the Minkowski norm on $\mathbb{M}_-$ exactly when $r=1$. For general $r$,

$$
L^{T}G_-L=r^{4}G_-,\qquad \det L=r^{8},
$$

so the form is multiplied by $r^{4}$ and the volume by $r^{8}$; the causal type is preserved and the transformation is a similarity of ratio $r^{2}$.

**Remark (what the image is not).** The image is not the unitary group and not $GL(2,\mathbb{C})$. The unitary group acts on the spinor module and sees the phase; the sandwich sees only the conformal Lorentz group. The two readings of the same word are the subject of *One-Sided Operator Under the Polar Representation*.

**Physical reading.** The word's sandwich and the physical sandwich have the same image, because $B$ and $\tilde U_{\mathrm L}$ are both in $SL(2,\mathbb{C})$. They differ in the parameter of the boost, not in the group. The kernel is the central unit circle, which is the phase; the image is the conformal Lorentz group, of real dimension seven. The group of units has real dimension eight; the missing dimension is the phase. The physical four-vector action is the image, and the phase freedom that the four-vector cannot see.

## The Null Cone

On the null cone $N(\tilde Q)=0$ the polar word does not exist, but the sandwich does. If $\tilde Q\neq0$ and $N(\tilde Q)=0$, the matrix $\mathsf M_2(\tilde Q)$ is a nonzero $2\times2$ matrix of determinant zero, hence of complex rank one. The sandwich therefore has complex rank one, and its image is the complex line spanned by $\tilde Q\tilde Q^{*}$: writing $\mathsf M_2(\tilde Q)=uv^{*}$ with column $u$ and row $v^{*}$,

$$
\mathsf M_2(\tilde Q)\,X\,\mathsf M_2(\tilde Q)^{*}
=u\,(v^{*}Xv)\,u^{*},
$$

which is a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. The element $\tilde Q\tilde Q^{*}$ is nonzero because its trace in the matrix model is the squared Frobenius norm of $\mathsf M_2(\tilde Q)$. The action collapses the eight-dimensional algebra onto one complex line; it is not invertible, and it has no polar reading because the scale, the phase, the boost and the rotor are not available on the cone.

For the example $\tilde Q_0=e_t+i\vec e_x$ one has $N(\tilde Q_0)=0$, $\mathsf M_2(\tilde Q_0)=\begin{pmatrix}1&1\\1&1\end{pmatrix}$ of rank one, and $\tilde Q_0\tilde Q_0^{*}=2\tilde Q_0$; the image of the sandwich is the line $\mathbb{C}\tilde Q_0$.

**Physical reading.** A lightlike four-momentum has no rest frame and no polar data: the scale, the rapidity and the phase cannot be separated. The sandwich survives as a degenerate operator of rank one.

## Worked Numbers

Take

$$
r=1.25,\qquad \alpha=0.3,\qquad \psi=0.5,\qquad \theta=0.7,
\qquad \vec u_{\mathrm b}=\vec e_x,\qquad \vec u_{\mathrm r}=\vec e_z,
$$

and the element $\tilde Q=r\exp(i\alpha)B\tilde q$ with coordinates

$$
Q_t=1.264938430+0.391291310i,\qquad
Q_x=0.180822428-0.584549751i,
$$

$$
Q_y=-0.066005339+0.213377316i,\qquad
Q_z=0.461738571+0.142832478i.
$$

The norm is $N(\tilde Q)=1.289586898+0.882253865i$, so $\rho=1.194170611+0.369400258i$, $r=1.25$ and $\alpha=0.3$, as required.

Take the anti-Hermitian element $X=i e_t+0.6\vec e_x$. The rotor acts first:

$$
\Theta_{\tilde q}(X)=i e_t+0.458905312\vec e_x+0.386530612\vec e_y,
$$

the boost factor acts next:

$$
\Theta_B\bigl(\Theta_{\tilde q}(X)\bigr)
=2.082386706\,i e_t+1.883329094\vec e_x+0.386530612\vec e_y,
$$

and the scale multiplies by $r^{2}=1.5625$:

$$
\Theta_{\tilde Q}(X)
=3.253729228\,i e_t+2.942701710\vec e_x+0.603954082\vec e_y.
$$

The last line is also the direct computation $\tilde QX\tilde Q^{*}$, and it agrees with the chain to the displayed digits.

The two boost normalizations are visible separately. The frame rotor gives

$$
\Theta_{\tilde U_{\mathrm L}}(X)=0.814968782\,i e_t+0.155480274\vec e_x,
$$

which is the boost of rapidity $+0.5$, and the word's factor gives

$$
\Theta_B(X)=2.248201351\,i e_t+2.101049575\vec e_x,
$$

which is the boost of rapidity $-1.0$. Since $B=\tilde U_{\mathrm L}^{-2}$, two applications of $\Theta_{\tilde U_{\mathrm L}}$ to $\Theta_B(X)$ return $X$; the check is

$$
\Theta_{\tilde U_{\mathrm L}}^{2}\bigl(\Theta_B(X)\bigr)=X.
$$

Finally, the phase is invisible:

$$
\Theta_{\exp(i\alpha)}(X)=X,
\qquad
\Theta_{\tilde Q}(X)=\Theta_{rB\tilde q}(X).
$$

## Summary

The Hermitian sandwich of the polar word is read factor by factor. The closed form is

$$
\Theta_{\tilde Q}=r^{2}\,\Theta_B\circ\Theta_{\tilde q}
=r^{2}\,\Theta_{\tilde U_{\mathrm L}}^{-2}\circ\Theta_{\tilde q},
\qquad
\Theta_{\exp(i\alpha)}=\mathrm{id}.
$$

The scale dilates by $r^{2}$ and doubles its exponent $\ln r$ to $2\ln r$. The phase cancels: its exponent $i\alpha$ produces nothing, because it is central and unitary, and the whole $U(1)$-orbit of an element has one sandwich. The boost factor $B$ is Hermitian and of norm one; its sandwich is a congruence, and its exponent $-i\psi\vec u_{\mathrm b}$ produces the rapidity $-2\psi$. The frame rotor $\tilde U_{\mathrm L}=B^{-1/2}$ is the physical boost; its exponent $+i\tfrac{\psi}{2}\vec u_{\mathrm b}$ produces the rapidity $+\psi$. The rotor is an inner automorphism; its exponent $\tfrac{\theta}{2}\vec u_{\mathrm r}$ produces the rotation of angle $\theta$. The doubling rule is that a Hermitian exponent and a non-central skew-Hermitian exponent double, while a central skew-Hermitian exponent cancels.

The image of the sandwich on the group of units is $CO^{+}(1,3)$, the kernel is $U(1)$, and the isometry slice is $r=1$, where the image is $SO^{+}(1,3)$. On the norm-one slice the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$. On the null cone the sandwich survives as an operator of complex rank one, with image the line spanned by $\tilde Q\tilde Q^{*}$.

The phase is the one factor that the sandwich does not see. It is visible to the norm, to the determinant and to the module, which is why the polar word carries it; it is invisible to the vector action, which is why the sandwich is a representation whose image is the conformal Lorentz group and not the full group of units. The word stores the boost as the inverse square of the physical factor; the physical operator takes the inverse square root, and the two readings are the same rapidity at the two levels of the word.

## Summary of Notation

| symbol | meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{M}_\pm$ | the Hermitian and anti-Hermitian subspaces, $X^{*}=\pm X$ |
| $\Theta_{\tilde Q}(X)=\tilde QX\tilde Q^{*}$ | the Hermitian sandwich |
| $N(\tilde Q)=\langle\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm of the polar series |
| $\rho=r\exp(i\alpha)$ | the complex modulus, the principal square root of $N$ |
| $r>0$, $\alpha\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $B=\exp(-i\psi\vec u_{\mathrm b})$ | the positive Hermitian boost factor |
| $\tilde U_{\mathrm L}=B^{-1/2}=\exp(i\tfrac{\psi}{2}\vec u_{\mathrm b})$ | the frame rotor |
| $\tilde q=\exp(\tfrac{\theta}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\psi\ge0$, $\theta\in[0,2\pi]$ | the rapidity and the rotation angle |
| $\tilde Q_L=r\exp(i\alpha)\tilde U_{\mathrm L}\tilde q$ | the frame word of the physical four-vector operator |
| $B_\pm(\psi)$ | the $4\times4$ matrices of the boost factor on $\mathbb{M}_\pm$ |
| $\mathsf R(\theta,\vec u_{\mathrm r})$ | the Rodrigues rotation matrix of the rotor |
| $G_\pm$ | the matrices of the norm on the two sectors, $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+$ |
| $CO^{+}(1,3)$ | the linear conformal Lorentz group, the image of the sandwich |
| $U(1)$ | the kernel of the sandwich, the central unit circle |
| $N=1$ | the norm-one slice, $SL(2,\mathbb{C})$ |

## Further Reading

- *One-Sided Operator Under the Polar Representation* (`articles_physics/one-sided-operator-under-the-polar-representation.md`), for the one-sided companion: the left and right multiplications, the sector decomposition and the exchange $\mathbb{M}_-\leftrightarrow\mathbb{M}_+$ by the phase $i$.
- *The Action of the Polar Element Representation on the Hermitian and Anti-Hermitian Subspaces* (`articles_physics/the-action-of-the-polar-element-representation-on-the-hermitian-and-anti-hermitian-subspaces.md`), for the detailed action on the two sectors, the boost matrices and the frame rotor.
- *The Polar Decomposition of Biquaternions in Practice* (`articles_physics/the-polar-decomposition-of-biquaternions-in-practice.md`), for the algorithm that produces the four factors.
- *The Cartan Hermitian Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-cartan-hermitian-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the Hermitian positive and unitary factors and the equation $\tilde Q\tilde Q^{*}=\tilde H^{2}$.
- *The Polar Element Representation of Biquaternions* (`articles_maths/the-polar-element-representation-of-biquaternions.md`), for the four factors, the modulus, the branch and the domain.
- *Two-Sided Operator Under the Polar Representation* (`articles_maths/two-sided-operator-under-the-polar-representation.md`), for the mathematics reference in the normalization $B=\tilde U_{\mathrm b}$.
- *The Quaternion Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-quaternion-pairing-of-the-polar-element-representation-of-biquaternions.md`) and *The Hamilton Root Pairing of the Polar Element Representation of Biquaternions* (`articles_physics/the-hamilton-root-pairing-of-the-polar-element-representation-of-biquaternions.md`), for the two partial two-factor groupings.
- *The Spectra of the Operators on the Biquaternion Algebra with Hermitian Adjoint* (`articles_maths/the-spectra-of-the-operators-on-the-biquaternion-algebra-with-hermitian-adjoint.md`), for the eigenvalues $\lambda_i\bar\lambda_j$ of the sandwich and the spectral proof of the phase cancellation.
- *The Four-Vector Operator Representation of Biquaternions* (`articles_physics/the-four-vector-operator-representation-of-biquaternions.md`), for the sandwich written in the four complex coefficients and its degenerate image on the cone.
- *The Lorentz Group in Biquaternionic Form — Structure and Representations* (`articles_physics/the-lorentz-group-in-biquaternionic-form-structure-and-representations.md`), for the Lorentz group in biquaternionic form and the double cover.
