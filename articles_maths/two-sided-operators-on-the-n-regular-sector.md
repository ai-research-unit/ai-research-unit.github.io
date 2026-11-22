# __Two-Sided Operators on the N-Regular Sector__

## Introduction

Throughout this article $\tilde Q$ lies in the **N-regular sector**, so $N\neq0$ and $\tilde Q$ is invertible. The **Hermitian pair** of the biquaternion algebra, also called the **bilinear two-sided operator**, is the operator

$$
\mathrm{Sd}_{\tilde Q}:\mathbb{B}\longrightarrow\mathbb{B},\qquad \mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*},
$$

the two-sided operator — the default two-sided operator of the corpus — whose right factor is the Hermitian conjugate of its left factor. It is the operator that carries the Lorentz group on the algebra: on the norm-one slice it acts on the anti-Hermitian and Hermitian subspaces by the proper orthochronous Lorentz group, and on the full group of invertibles it is that action composed with a dilation.

**What the norm decides, and what the vector form decides.** The norm decides everything global, and the vector form $B^{2}$ decides only the Jordan type. On the whole N-regular sector the operator is invertible, of rank four, with the whole algebra as image and the central circle $U(1)$ as kernel. The wall $B^{2}=0$ changes the spectrum from the four products $\lambda_i\bar\lambda_j$ of two distinct eigenvalues to a single repeated eigenvalue, and on the Jordan part of the wall it changes the Jordan type from semisimple to one block of size three and one of size one. That is the whole difference, and it is the reason the wall is a part of this article.

The complete polar decomposition writes an element of non-vanishing norm as four factors,

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r}
=\varrho\exp(i\theta_{\mathrm{pha}})\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
\qquad \varrho\exp(i\theta_{\mathrm{pha}}),
$$

the four being the scale $\varrho>0$, the central phase $\exp(i\theta_{\mathrm{pha}})$ collected in $\varrho\,e^{i\theta_{\mathrm{pha}}}$, the Hermitian positive boost $\tilde U_{\mathrm b}$ of rapidity $\theta_{\mathrm{rpd}}\ge0$ about the real unit axis $\vec u_{\mathrm b}$, and the rotor $\tilde u_{\mathrm r}$ of angle $\theta_{\mathrm{axr}}\in[0,2\pi]$ about the real unit axis $\vec u_{\mathrm r}$. This article reads the two-sided operator one factor at a time and answers one question: **what does each factor do to the operator?** The answer is read one factor at a time, and the phase does nothing.

The article is the vector-side companion of *The Complete Polar Decomposition of an N-Regular Biquaternion*, §*The Operator Reading: the Twist*. There the same word acts by left multiplication on the spinor module and all four factors are visible: the scale and the phase form the twist $\chi(\varrho\,e^{i\theta_{\mathrm{pha}}})=\varrho\,e^{i\theta_{\mathrm{pha}}}$, and the boost and the rotor form the norm-one operator. Here the action is the two-sided operator on the algebra, the phase is invisible, and the boost and the rotor are the only factors that act on a vector by a Lorentz transformation. The one-sided companion is *One-Sided Operators on the N-Regular Sector*: there the same word is read through a single left or right multiplication, the phase is visible, and the two real forms $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ are exchanged at $\theta_{\mathrm{pha}}=\tfrac{\pi}{2}$. The exponent reading of the two slots is §*The Doubling Rule* below.

The plan is the following. §*The Two-Sided Operator of the Word* proves the multiplicativity and the closed form $\mathrm{Sd}_{\tilde Q}=\varrho^{2}\mathrm{Sd}_{\tilde U_{\mathrm b}}\circ\mathrm{Sd}_{\tilde u_{\mathrm r}}$. §*The Scale* to §*The Rotor* take the four factors in the order of the word. §*The Eigenbasis and the Two Spinor Slots* reads the two-sided operator as a two-slot operator, computes its spectrum as the four products $\lambda_i\bar\lambda_j$, and identifies the four products. §*The Exponential of the Two-Sided Operator* reads the one-parameter group, the pure-factor table, the doubling rule and the vector representation. §*The Image and the Kernel* identifies the image as the conformal Lorentz group and the kernel as the central unit circle. §*The Wall $B^{2}=0$* treats the unipotent case, its $3+1$ Jordan structure, the null rotation that its exponential produces and its fixed directions. §*The Boundary: the Null Cone* records the comparison with the N-degenerate article. The article closes with the summary, the notation and the readings.

## Conventions

The algebra is $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, with basis $e_t,\vec e_x,\vec e_y,\vec e_z$, the product $\vec e_x\vec e_y=\vec e_z$ and the squares $\vec e_x^{2}=\vec e_y^{2}=\vec e_z^{2}=-e_t$. The scalar imaginary is $i$, central, $i^{2}=-1$. An element is $\tilde Q=Q_te_t+\vec Q$ with the four coefficients $Q_\mu$ complex.

The three conjugations are the quaternion conjugation $\natural$, the coefficient conjugation $\bar\cdot$ and their composite, the **Hermitian conjugation**

$$
\tilde Q^{*}=\overline{\tilde Q^{\natural}}=\bar Q_te_t-\bar Q_x\vec e_x-\bar Q_y\vec e_y-\bar Q_z\vec e_z .
$$

The Hermitian and anti-Hermitian subspaces are

$$
\mathbb{B}_{\Psi}\cup\mathbb{B}_{\Phi}=\{\tilde Q:\tilde Q^{*}=\pm\tilde Q\}.
$$

On $\mathbb{B}_{\Phi}$ an element is $\tilde Q_-=ia\,e_t+\vec b$ with $a\in\mathbb{R}$ and $\vec b$ a real vector; on $\mathbb{B}_{\Psi}$ an element is $\tilde Q_+=a\,e_t+i\vec b$ with the same real data. The two sectors are exchanged by multiplication by $i$, which is central.

The **norm** of the polar series is the complex number

$$
\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_{\mu\in\{t,x,y,z\}}Q_\mu^{2},\qquad \tilde Q\tilde Q^{\natural}=\langle\tilde Q\rangle_{\natural}\,e_t ,
$$

and the **domain** of the complete polar decomposition is $\langle\tilde Q\rangle_{\natural}\neq0$. The word is

$$
\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\,\tilde u_{\mathrm r},\qquad
\varrho\exp(i\theta_{\mathrm{pha}}),\qquad
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr),\qquad
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr),
$$

with $\varrho>0$, $\theta_{\mathrm{pha}}\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$, $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$, and $\vec u_{\mathrm b},\vec u_{\mathrm r}$ real unit vectors. The modulus is $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}$ on the principal branch, so $\varrho=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{1/2}$ and $\theta_{\mathrm{pha}}=\tfrac12\arg \langle\tilde Q\rangle_{\natural}$. The factors satisfy

$$
\varrho^{*}=\varrho,\qquad \tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=\langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

The matrix model is $\mathsf M_2:\mathbb{B}\to M_2(\mathbb{C})$, with $\mathsf M_2(e_t)=I_2$ and $\mathsf M_2(\vec e_k)=-i\sigma_k$, the $\sigma_k$ being the Pauli matrices. It is $\mathbb{C}$-linear and satisfies $\mathsf M_2(\tilde Q^{*})=\mathsf M_2(\tilde Q)^{\dagger}$, and its determinant is the norm, $\det\mathsf M_2(\tilde Q)=\langle\tilde Q\rangle_{\natural}$.

The two-sided operator is written $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ throughout. It uses the Hermitian conjugate in the right slot and never the inverse; the two coincide only where $\tilde Q$ is $*$-unitary. It is the member $L_{\tilde Q}R_{\tilde Q^{*}}$ of the general two-sided family of *Operators Acting on Two Sides*, with the second parameter fixed at the Hermitian conjugate of the first; the general family allows the two parameters independently.

## The Two-Sided Operator of the Word

### Elementary Properties

**Proposition.** Let $\tilde Q,\tilde Q'\in\mathbb{B}$ and $\tilde X\in\mathbb{B}$. Then:

**(a)** $\mathrm{Sd}_{\tilde Q\tilde Q'}=\mathrm{Sd}_{\tilde Q}\circ\mathrm{Sd}_{\tilde Q'}$;

**(b)** $\mathrm{Sd}_{\tilde Q}$ is $\mathbb{C}$-linear in $\tilde X$;

**(c)** $\mathrm{Sd}_{\tilde Q}$ is invertible if and only if $\tilde Q$ is invertible, and then $\mathrm{Sd}_{\tilde Q}^{-1}=\mathrm{Sd}_{\tilde Q^{-1}}$;

**(d)** $\mathrm{Sd}_{\tilde Q}$ preserves each of $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$;

**(e)** $\mathrm{Sd}_{\tilde Q}(e_t)=\tilde Q\tilde Q^{*}$.

*Proof.* (a) $(\tilde Q\tilde Q')\tilde X(\tilde Q\tilde Q')^{*}=\tilde Q(\tilde Q'\tilde X\tilde Q'^{*})\tilde Q^{*}$. (b) The multiplication and the right factor are $\mathbb{C}$-linear. (c) The inverse of $\mathrm{Sd}_{\tilde Q}$ is $\mathrm{Sd}_{\tilde Q^{-1}}$, because $\tilde Q^{-1}\tilde Q\tilde X\tilde Q^{*}\tilde Q^{-*}=\tilde X$ and $(\tilde Q^{-1})^{*}=(\tilde Q^{*})^{-1}$. (d) If $\tilde X^{*}=\pm\tilde X$, then

$$
\bigl(\tilde Q\tilde X\tilde Q^{*}\bigr)^{*}=\tilde Q\tilde X^{*}\tilde Q^{*}=\pm\tilde Q\tilde X\tilde Q^{*}.
$$

(e) Put $\tilde X=e_t$.

The preservation of the two sectors is the structural reason the action splits into two formulas, one per sector, and the reason a two-sided operator cannot mix the Hermitian and the anti-Hermitian parts.

**Corollary (the scaling of the norm).** For every invertible $\tilde Q$ and every $\tilde X$,

$$
\boxed{\;\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}\;}.
$$

*Proof.* The norm is multiplicative and central, and $\langle\tilde Q^{*}\rangle_{\natural}=\overline{\langle\tilde Q\rangle_{\natural}}$; hence $\langle\tilde Q\tilde X\tilde Q^{*}\rangle_{\natural}=\langle\tilde Q\rangle_{\natural}\langle\tilde X\rangle_{\natural}\overline{\langle\tilde Q\rangle_{\natural}}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}$. On the unit-norm slice the two-sided operator is an isometry of the biquaternion norm.

### The Closed Form

**Theorem (the two-sided operator of the polar word).** Let $\tilde Q=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}$ with $\langle\tilde Q\rangle_{\natural}\neq0$. Then

$$ \mathrm{Sd}_{\tilde Q}=\mathrm{Sd}_r\circ\mathrm{Sd}_{\tilde U_{\mathrm b}}\circ\mathrm{Sd}_{\tilde u_{\mathrm r}}, $$

that is,

$$
\boxed{\;\mathrm{Sd}_{\tilde Q}(\tilde X)=\varrho^{2}\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b}\;},
$$

and $\mathrm{Sd}_{\exp(i\theta_{\mathrm{pha}})}=\mathrm{id}$.

*Proof.* The Hermitian conjugate of the word is

$$
\tilde Q^{*}=\bigl(\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\bigr)^{*}
=\tilde u_{\mathrm r}^{*}\tilde U_{\mathrm b}^{*}\varrho\,e^{-i\theta_{\mathrm{pha}}}
=\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\varrho\,e^{-i\theta_{\mathrm{pha}}}
=\varrho\,e^{-i\theta_{\mathrm{pha}}}\,\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b},
$$

because the scalars are central. Hence

$$
\tilde Q\tilde X\tilde Q^{*}
=\varrho\,e^{i\theta_{\mathrm{pha}}}\tilde U_{\mathrm b}\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\tilde U_{\mathrm b}\varrho\,e^{-i\theta_{\mathrm{pha}}}
=\varrho\,e^{i\theta_{\mathrm{pha}}}\varrho\,e^{-i\theta_{\mathrm{pha}}}\,\tilde U_{\mathrm b}\bigl(\tilde u_{\mathrm r}\tilde X\tilde u_{\mathrm r}^{-1}\bigr)\tilde U_{\mathrm b},
$$

and $\varrho\,e^{i\theta_{\mathrm{pha}}}\varrho\,e^{-i\theta_{\mathrm{pha}}}=\varrho^{2}$. The phase has disappeared in the last step.

**Remark (the order).** The rightmost factor of the word acts first: the rotor, then the boost, then the scale. The phase may be inserted anywhere, and so may the scale, because both are central. The boost and the rotor do not commute, so their order is part of the word and cannot be exchanged.

The theorem is the article in one line. The four sections that follow read its four factors.

## The Scale

### The Factor

The scale is $\varrho=\exp(\ln \varrho)$, a positive real. It is central, real and Hermitian, $\varrho^{*}=\varrho$, and it is the only factor whose exponent is a real scalar.

### The Two-Sided Operator

$$
\mathrm{Sd}_r(\tilde X)=\varrho\tilde X\varrho^{*}=\varrho^{2}\tilde X .
$$

On $\mathbb{B}_{\Phi}$ and on $\mathbb{B}_{\Psi}$ alike, every coordinate is multiplied by $\varrho^{2}$: $a\mapsto \varrho^{2}a$ and $\vec b\mapsto \varrho^{2}\vec b$. The scale is a dilation of ratio $\varrho^{2}$ of the whole algebra, and the only factor that changes the norm of the argument,

$$
\langle\mathrm{Sd}_r(\tilde X)\rangle_{\natural}=\varrho^{4}\langle \tilde X\rangle_{\natural}.
$$

## The Central Phase

### The Factor

The phase is $P=\exp(i\theta_{\mathrm{pha}})$, central and $*$-unitary,

$$
P^{*}=P^{-1}=\exp(-i\theta_{\mathrm{pha}}),\qquad \langle P\rangle_{\natural}=\exp(2i\theta_{\mathrm{pha}}).
$$

Its exponent is $i\theta_{\mathrm{pha}}$, purely imaginary and central.

### The Two-Sided Operator

$$
\mathrm{Sd}_P(\tilde X)=\exp(i\theta_{\mathrm{pha}})\,\tilde X\,\exp(-i\theta_{\mathrm{pha}})=\tilde X .
$$

The two scalars commute with $\tilde X$ and with each other, and the second is the inverse of the first, so the product is the identity operator.

**The phase is not a half-angle of the two-sided operator.** The exponent $i\theta_{\mathrm{pha}}$ is the full generator of the multiplication by $\exp(i\theta_{\mathrm{pha}})$ on the module; the two-sided operator cancels it. It is already half of the argument of the norm, $\langle\tilde Q\rangle_{\natural}=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}=\varrho^{2}\exp(2i\theta_{\mathrm{pha}})$, and that is the only doubling in which it takes part. Writing $\exp(i\theta_{\mathrm{pha}}/2)$ in the word would not change the two-sided operator, which is the identity either way; it would only change the meaning of the letter $\theta_{\mathrm{pha}}$, and it would break $\varrho\,e^{i\theta_{\mathrm{pha}}}=\sqrt{\langle\tilde Q\rangle_{\natural}}$ unless $\theta_{\mathrm{pha}}$ were redefined as $\arg\langle\tilde Q\rangle_{\natural}$.

### Remark (the Cancelled Phase)

This is the central remark of the article. The phase is the only factor of the word whose two-sided operator is the identity whatever the value of its parameter. It is not halved, not doubled and not shifted: it is annihilated. Four consequences follow.

**First, the cancellation is exact and global.** It holds for every $\tilde X$, not merely on one subspace, and it uses only two properties, centrality and unitarity. Any central factor of modulus one cancels in any two-sided operator: if $C$ is central and $C^{*}=C^{-1}$, then

$$
C\tilde XC^{*}=\tilde XCC^{-1}=\tilde X .
$$

**Second, two elements that differ by a phase have the same two-sided operator.** For a central complex $\lambda$,

$$
\mathrm{Sd}_{\lambda\tilde Q}(\tilde X)=\lambda\tilde Q\tilde X\tilde Q^{*}\bar\lambda=|\lambda|^{2}\,\mathrm{Sd}_{\tilde Q}(\tilde X).
$$

On the unit circle $|\lambda|=1$ the two such operators are equal, so the whole $U(1)$-orbit of $\tilde Q$ has one two-sided operator. On the positive real axis the two-sided operator scales by $\lambda^{2}$, which is the scale row of the table. The phase is the unit-modulus part of the centre, and it is exactly the part that disappears.

**Third, the phase is absent from this action but not from the algebra.** It reappears in three places, and the list is the reason the polar word needs it:

- the norm, $\langle\tilde Q\rangle_{\natural}=\tilde Q\tilde Q^{\natural}=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}=\varrho^{2}\exp(2i\theta_{\mathrm{pha}})$;
- the determinant, $\det\mathsf M_2(\tilde Q)=\varrho^{2}e^{2i\theta_{\mathrm{pha}}}=\varrho^{2}\exp(2i\theta_{\mathrm{pha}})$;
- the module, where left multiplication by $\tilde Q$ acts on the spinor module by the scalar $\varrho\exp(i\theta_{\mathrm{pha}})$, the twist $\chi(\varrho\,e^{i\theta_{\mathrm{pha}}})=\varrho\,e^{i\theta_{\mathrm{pha}}}$ of *The Complete Polar Decomposition of an N-Regular Biquaternion*, §*The Operator Reading: the Twist*.

The first two are quadratic in $\varrho\,e^{i\theta_{\mathrm{pha}}}$ and see $2\theta_{\mathrm{pha}}$; the third is linear and sees $\theta_{\mathrm{pha}}$; the two-sided operator multiplies by $\varrho\,e^{i\theta_{\mathrm{pha}}}$ on the left and by $\varrho\,e^{-i\theta_{\mathrm{pha}}}$ on the right and sees $0$.

**Fourth, the spectral reading confirms it.** The eigenvalues of $\mathrm{Sd}_{\tilde Q}$ are the products $\lambda_i\bar\lambda_j$ of the eigenvalues of $\mathsf M_2(\tilde Q)$, as in §*The Spectrum of the Two-Sided Operator*. A phase multiplies every $\lambda_i$ by $\exp(i\theta_{\mathrm{pha}})$ and every $\bar\lambda_j$ by $\exp(-i\theta_{\mathrm{pha}})$, so every product is unchanged. The cancellation is visible in the spectrum without any computation in coordinates.

## The Boost

### The Factor

The boost is

$$
\tilde U_{\mathrm b}=\exp\Bigl(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr)
=\cosh\tfrac{\theta_{\mathrm{rpd}}}{2}\,e_t+i\sinh\tfrac{\theta_{\mathrm{rpd}}}{2}\,\vec u_{\mathrm b},
\qquad \theta_{\mathrm{rpd}}\ge0,\qquad \lvert\vec u_{\mathrm b}\rvert=1 .
$$

It is Hermitian and of norm one,

$$
\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b},\qquad \langle\tilde U_{\mathrm b}\rangle_{\natural}=1,
$$

and its square and inverse are

$$
\tilde U_{\mathrm b}^{2}=\exp(i\theta_{\mathrm{rpd}}\vec u_{\mathrm b}),\qquad
\tilde U_{\mathrm b}^{-1}=\exp\Bigl(-i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}\Bigr).
$$

The boost is not $*$-unitary, because $\tilde U_{\mathrm b}^{-1}\neq\tilde U_{\mathrm b}$ unless $\theta_{\mathrm{rpd}}=0$.

### The Two-Sided Operator on the Two Sectors

The right slot is $\tilde U_{\mathrm b}^{*}=\tilde U_{\mathrm b}$, so the two-sided operator is a **congruence**,

$$
\mathrm{Sd}_{\tilde U_{\mathrm b}}(\tilde X)=\tilde U_{\mathrm b}\,\tilde X\,\tilde U_{\mathrm b},
$$

and not a conjugation. Write $b_\parallel=\vec u_{\mathrm b}\cdot\vec b$ and $\vec b_\perp=\vec b-b_\parallel\vec u_{\mathrm b}$.

On $\mathbb{B}_{\Phi}$, for $\tilde X=ia\,e_t+\vec b$,

$$
\mathrm{Sd}_{\tilde U_{\mathrm b}}(\tilde X)=ia'\,e_t+\vec b',
\qquad
a'=a\cosh\theta_{\mathrm{rpd}}-b_\parallel\sinh\theta_{\mathrm{rpd}},\qquad
b_\parallel'=b_\parallel\cosh\theta_{\mathrm{rpd}}-a\sinh\theta_{\mathrm{rpd}},\qquad
\vec b_\perp'=\vec b_\perp .
$$

On $\mathbb{B}_{\Psi}$, for $\tilde X=a\,e_t+i\vec b$,

$$
\mathrm{Sd}_{\tilde U_{\mathrm b}}(\tilde X)=a'\,e_t+i\vec b',
\qquad
a'=a\cosh\theta_{\mathrm{rpd}}+b_\parallel\sinh\theta_{\mathrm{rpd}},\qquad
b_\parallel'=b_\parallel\cosh\theta_{\mathrm{rpd}}+a\sinh\theta_{\mathrm{rpd}},\qquad
\vec b_\perp'=\vec b_\perp .
$$

The two formulas differ only in the signs of the cross terms. The derivation is one line per piece. For the time piece,

$$
\tilde U_{\mathrm b}\,(ia\,e_t)\,\tilde U_{\mathrm b}=ia\,\tilde U_{\mathrm b}^{2}
=ia\cosh\theta_{\mathrm{rpd}}-a\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b},
$$

and for the vector piece the perpendicular part is fixed and the parallel part is stretched by $\cosh\theta_{\mathrm{rpd}}$; the cross terms combine into the formulas above. In the coordinates $(a,b_x,b_y,b_z)$ the matrices of the two actions are

$$
B_-(\theta_{\mathrm{rpd}},\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\theta_{\mathrm{rpd}} & -\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}^{\,T}\\
-\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b} & I_3+(\cosh\theta_{\mathrm{rpd}}-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

$$
B_+(\theta_{\mathrm{rpd}},\vec u_{\mathrm b})=
\begin{pmatrix}
\cosh\theta_{\mathrm{rpd}} & \sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b}^{\,T}\\
\sinh\theta_{\mathrm{rpd}}\,\vec u_{\mathrm b} & I_3+(\cosh\theta_{\mathrm{rpd}}-1)\vec u_{\mathrm b}\vec u_{\mathrm b}^{\,T}
\end{pmatrix},
$$

with $B_+=B_-^{-1}$. Each preserves its form, $B_\pm^{T}G_\pm B_\pm=G_\pm$, where $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+=\operatorname{diag}(-1,1,1,1)$.

## The Rotor

### The Factor

The rotor is

$$
\tilde u_{\mathrm r}=\exp\Bigl(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}\Bigr)
=\cos\tfrac{\theta_{\mathrm{axr}}}{2}\,e_t+\sin\tfrac{\theta_{\mathrm{axr}}}{2}\,\vec u_{\mathrm r},
\qquad \theta_{\mathrm{axr}}\in[0,2\pi],\qquad \lvert\vec u_{\mathrm r}\rvert=1 .
$$

It is a real quaternion, of norm one, and $*$-unitary,

$$
\tilde u_{\mathrm r}^{*}=\tilde u_{\mathrm r}^{\natural}=\tilde u_{\mathrm r}^{-1},\qquad \langle\tilde u_{\mathrm r}\rangle_{\natural}=1 .
$$

Unlike the boost, the rotor is both norm-one and $*$-unitary, and its right slot is therefore the inverse.

### The Two-Sided Operator

$$
\mathrm{Sd}_{\tilde u_{\mathrm r}}(\tilde X)=\tilde u_{\mathrm r}\,\tilde X\,\tilde u_{\mathrm r}^{-1}.
$$

The two-sided operator is a conjugation by an invertible element, hence an algebra automorphism. On a general element $\tilde X=X_te_t+\vec X$ it fixes the scalar part and rotates the vector part,

$$
\mathrm{Sd}_{\tilde u_{\mathrm r}}(\tilde X)=X_te_t+\mathsf R(\theta_{\mathrm{axr}},\vec u_{\mathrm r})\,\vec X,
$$

where $\mathsf R$ is the Rodrigues rotation

$$
\mathsf R(\theta_{\mathrm{axr}},\vec u_{\mathrm r})=I_3+\sin\theta_{\mathrm{axr}}\,[\vec u_{\mathrm r}]_\times+(1-\cos\theta_{\mathrm{axr}})\,[\vec u_{\mathrm r}]_\times^{2},
$$

or, on a vector $\vec X$,

$$
\mathsf R(\theta_{\mathrm{axr}},\vec u_{\mathrm r})\,\vec X
=\vec X\cos\theta_{\mathrm{axr}}+(\vec u_{\mathrm r}\times\vec X)\sin\theta_{\mathrm{axr}}
+\vec u_{\mathrm r}(\vec u_{\mathrm r}\cdot\vec X)(1-\cos\theta_{\mathrm{axr}}).
$$

On $\mathbb{B}_{\Phi}$ the rotor fixes the time direction $ie_t$ and rotates $\vec b$; on $\mathbb{B}_{\Psi}$ it fixes $e_t$ and rotates $i\vec b$. The formula is the same on the two sectors because $i$ is central.

## The Eigenbasis and the Two Spinor Slots

### The Two Slots of the Two-Sided Operator

Assume $B\neq0$ throughout this section. The two-sided operator is the composite of two one-sided operators,
$$
\mathrm{Sd}_{\tilde Q}=R_{\tilde Q^{*}}\circ L_{\tilde Q},
\qquad
\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\,\tilde X\,\tilde Q^{*}.
$$
The left factor acts on the left slot of $\tilde X$ and the right factor on the right slot. In the eigenbasis matrix model $\mathsf M^{\tilde Q}$ of *The N-Regular, Spectrally Regular Sector*, §*The Eigenbasis, the Nilpotents, and the Peirce Corners* — not the Pauli model $\mathsf M_2$ of §*Conventions* — the element $\tilde Q$ is the diagonal matrix
$$
\Delta=\begin{pmatrix}\lambda_+&0\\0&\lambda_-\end{pmatrix},
\qquad
\lambda_\pm=Q_t\pm iB,
$$
and the left factor is $X\mapsto \Delta X$. The right factor is $X\mapsto X\Delta_*$, where $\Delta_*$ is the matrix of $\tilde Q^{*}$ in the same model. The first slot is the column index, a spinor slot; the second slot is the row index, the dual spinor slot.

In this model the two-sided operator is $X\mapsto\Delta X\Delta_*$. A first-copy spinor, in the Peirce sense, is a matrix whose second column is zero; the left factor acts by $\Delta$ on its first column, and the right factor then combines the two columns. A second-copy spinor, in the Peirce sense, is a matrix whose first column is zero; the left factor acts by $\Delta$ on its second column, and the right factor again combines the columns. The one-sided operator is the column action alone; the two-sided operator is the column action followed by the row action.

The two slots carry the two eigenvalues separately. The left multiplication $L_{\tilde Q}$ has spectrum $\{\lambda_+,\lambda_-\}$, each with multiplicity two. The right multiplication $R_{\tilde Q^{*}}$ has spectrum $\{\bar\lambda_+,\bar\lambda_-\}$, each with multiplicity two, because the eigenvalues of $\tilde Q^{*}$ are the conjugates of those of $\tilde Q$. The two operators commute,
$$
L_{\tilde Q}R_{\tilde Q^{*}}=R_{\tilde Q^{*}}L_{\tilde Q},
$$
and each is diagonalisable when $B\neq0$. They therefore admit a common eigenbasis, and in that basis the two-sided operator is diagonal.

*Proof.* The two multiplications commute because both are products in the associative algebra. A commuting family of diagonalisable operators is simultaneously diagonalisable. The eigenvalues of $L_{\tilde Q}$ are $\lambda_\pm$ by the eigenbasis. In a matrix model, right multiplication by $A$ is a Kronecker product of $A^{T}$ with the identity, so the eigenvalues of $R_{\tilde Q^{*}}$ are those of $\tilde Q^{*}$, namely $\bar\lambda_\pm$, each with multiplicity two.

### The Spectrum of the Two-Sided Operator

In the common eigenbasis the left slot contributes one of $\lambda_+,\lambda_-$ and the right slot one of $\bar\lambda_+,\bar\lambda_-$. The eigenvalue of the two-sided operator is the product:
$$
\boxed{\;
\operatorname{spec}\mathrm{Sd}_{\tilde Q}
=\bigl\{\lambda_+\bar\lambda_+,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ \lambda_-\bar\lambda_-\bigr\}
\; }.
$$
Equivalently,
$$
\mathrm{Sd}_{\tilde Q}\longleftrightarrow
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

This is the precise sense in which the two-sided operator uses **two slots**. A one-sided operator uses one slot and carries the pair $(\lambda_+,\lambda_-)$; the two-sided operator uses two slots and carries the four products. The factor attached to a slot is the square root of the corresponding product; the exponent reading of that relation is §*The Doubling Rule*.

The common eigenbasis is not the eigenbasis of $L_{\tilde Q}$ in general. It is the tensor product of a left eigenbasis of $L_{\tilde Q}$ and a right eigenbasis of $R_{\tilde Q^{*}}$. The two agree whenever $\tilde Q^{*}$ is diagonal in the eigenbasis of $L_{\tilde Q}$; this includes the Hermitian case $\tilde Q^{*}=\tilde Q$, where the four products are the pairings $\lambda_i\lambda_j$, and also the case in which $\tilde Q^{*}$ lies in the span of the two eigenprojections. In general they differ. For a generic polar word the two-sided operator mixes the two chiral left ideals $S_+$ and $S_-$ of the one-sided reading; the four products are still exact, but they are not the diagonal entries of the Peirce matrix. The pure factors are the exceptions: a pure boost satisfies $\tilde Q^{*}=\tilde Q$, a pure rotor satisfies $\tilde Q^{*}=\tilde Q^{-1}$, and both commute with their own eigenprojections, so their two-sided operators preserve $S_+$ and $S_-$. This does not contradict the preservation of the real forms $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$: the splitting $\mathbb{B}=S_+\oplus S_-$ is a complex splitting into left ideals, while $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$ is a real splitting into Hermitian sectors, and they are different decompositions.

## The Exponential of the Two-Sided Operator

### The Spectral Form

**Proposition.** On $\Sigma_{11}$ the operator is diagonalisable, with the eigenvalues $\lambda_i\bar\lambda_j$ of §*The Spectrum of the Two-Sided Operator*. Its exponential is diagonalisable, with the eigenvalues
$$
e^{t\lambda_+\bar\lambda_+},\quad
e^{t\lambda_+\bar\lambda_-},\quad
e^{t\lambda_-\bar\lambda_+},\quad
e^{t\lambda_-\bar\lambda_-},
$$
and determinant
$$
\boxed{\;\det\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=\exp\bigl(t\operatorname{tr}\mathrm{Sd}_{\tilde Q}\bigr)
=\exp\bigl(4t\lvert Q_t\rvert^{2}\bigr).\;}
$$

*Proof.* The operator is diagonalisable in the common eigenbasis of §*The Two Slots of the Two-Sided Operator*, and the exponential of a diagonal operator is the diagonal of the exponentials. The trace is the sum of the four products,
$$
\lambda_+\bar\lambda_++\lambda_+\bar\lambda_-+\lambda_-\bar\lambda_++\lambda_-\bar\lambda_-
=(\lambda_++\lambda_-)(\bar\lambda_++\bar\lambda_-)
=4\lvert Q_t\rvert^{2},
$$
and $\det\exp(tA)=\exp(t\operatorname{tr}A)$.

**Remark (no element identity).** There is no identity of the form $\exp(t\,\mathrm{Sd}_{\tilde Q})=\mathrm{Sd}_{\exp(t\tilde Q)}$: the operator is quadratic in the parameter. For a central element $\tilde Q=c\,e_t$ the operator is $\lvert c\rvert^{2}\mathrm{id}$, so $\exp(t\mathrm{Sd}_{\tilde Q})=e^{t\lvert c\rvert^{2}}\mathrm{id}$, while $\mathrm{Sd}_{\exp(t\tilde Q)}=e^{2t\operatorname{Re}c}\mathrm{id}$. The two agree only when $\lvert c\rvert^{2}=2\operatorname{Re}c$. The two-sided operator exponentiates its image, not its parameter. The one-sided operator, being a representation, does satisfy the element identity (§*The Element Identity* of *One-Sided Operators on the N-Regular Sector*).

### The Pure Factors and the Full Rotor

For each pure factor, read with the other factors absent, the products are elementary. The scale $\varrho$ has $\lambda_\pm=\varrho$ and products $\varrho^{2}$. The central phase has $\lambda_\pm=\exp(i\theta_{\mathrm{pha}})$ and products $\exp(i\theta_{\mathrm{pha}})\exp(-i\theta_{\mathrm{pha}})=1$. The boost has
$$
\lambda_+=e^{-\theta_{\mathrm{rpd}}/2},\qquad \lambda_-=e^{\theta_{\mathrm{rpd}}/2},
$$
so its products are $e^{-\theta_{\mathrm{rpd}}},1,1,e^{\theta_{\mathrm{rpd}}}$. The rotor has
$$
\lambda_+=e^{i\theta_{\mathrm{axr}}/2},\qquad \lambda_-=e^{-i\theta_{\mathrm{axr}}/2},
$$
so its products are $e^{i\theta_{\mathrm{axr}}},1,1,e^{-i\theta_{\mathrm{axr}}}$. The two-sided operator therefore carries the full rapidity $\theta_{\mathrm{rpd}}$ and the full angle $\theta_{\mathrm{axr}}$, while the one-sided operator carries the half-rapidity and the half-angle. The phase cancels and the scale doubles.

| factor | exponent | kind of exponent | two-slot products | output |
|---|---|---|---|---|
| scale $\varrho$ | $\ln\varrho$ | real scalar | $\varrho^{2},\varrho^{2},\varrho^{2},\varrho^{2}$ | dilation $\varrho^{2}$ |
| phase $\exp(i\theta_{\mathrm{pha}})$ | $i\theta_{\mathrm{pha}}$ | imaginary scalar | $1,1,1,1$ | identity |
| boost $\tilde U_{\mathrm b}$ | $i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b}$ | imaginary vector | $e^{-\theta_{\mathrm{rpd}}},1,1,e^{\theta_{\mathrm{rpd}}}$ | rapidity $\theta_{\mathrm{rpd}}$ |
| rotor $\tilde u_{\mathrm r}$ | $\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r}$ | real vector | $e^{i\theta_{\mathrm{axr}}},1,1,e^{-i\theta_{\mathrm{axr}}}$ | angle $\theta_{\mathrm{axr}}$ |

The scale and the phase are central. Their rows are read as scalar multipliers of a word with $B\neq0$; for a purely central element $B=0$ and the spectrum collapses to $Q_t\bar Q_t$.

**The one-sided operator is the spinor action.** The two-sided operator has no half-angle of its own: it pairs two one-sided slots, and each slot is the spinor action of §*The Polar Word on a Spinor* of *One-Sided Operators on the N-Regular Sector*. The half-angle $\theta_{\mathrm{axr}}/2$ and the half-rapidity $\theta_{\mathrm{rpd}}/2$ live on a single slot; this article computes their products, which are the full angle $\theta_{\mathrm{axr}}$ and the full rapidity $\theta_{\mathrm{rpd}}$.

For a general word the two factors do not commute, and the common eigenbasis is not the eigenbasis of $L_{\tilde Q}$. The product formula for the spectrum remains exact. The splitting of the products into a boost and a rotation is the content of §*The Boost* and §*The Rotor* when the axes commute; in general the effective exponent is the sum of the two slot exponents only after the common eigenbasis is chosen. The relation between the spectral data and the polar parameters is *Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion*, §*The Spectral Data from the Polar Factors*.

### The Vector Representation as the Double of the Half-Angle

The two slots are the two tensor factors of $\mathbb{B}\cong S\otimes S^{*}$, where $S=\mathbb{C}^{2}$ is the spinor space and $S^{*}$ its dual. The left factor acts on $S$, the right on $S^{*}$, and the two-sided operator is
$$
\mathrm{Sd}_{\tilde Q}=\Delta_{\mathrm{rep}}(\tilde Q)\otimes\bar\Delta_{\mathrm{rep}}(\tilde Q),
$$
where $\Delta_{\mathrm{rep}}$ is the defining representation on $S$ and $\bar\Delta_{\mathrm{rep}}$ its conjugate. The tensor product of the defining representation and its conjugate is the complexified vector representation, $2\otimes\bar 2=4$, so the two-sided operator is the vector and the one-sided operator, on one slot, is the spinor.

The weights add. For the rotor, $\Delta_{\mathrm{rep}}(\tilde u_{\mathrm r})$ has weights $e^{\pm i\theta_{\mathrm{axr}}/2}$ and $\bar\Delta_{\mathrm{rep}}(\tilde u_{\mathrm r})$ has weights $e^{\mp i\theta_{\mathrm{axr}}/2}$, and the four sums are $\theta_{\mathrm{axr}},0,0,-\theta_{\mathrm{axr}}$. For the boost, both slots carry $e^{\mp\theta_{\mathrm{rpd}}/2}$ because the boost is Hermitian, and the four sums are $\theta_{\mathrm{rpd}},0,0,-\theta_{\mathrm{rpd}}$. In both cases the vector weights are the sums of the two spinor weights, and each extremal vector weight is twice a spinor weight.

**The two-sided operator has no half-angle of its own.** It is the vector representation, of dimension four; its weights are the sums. The half-angle $\theta_{\mathrm{axr}}/2$ and the half-rapidity $\theta_{\mathrm{rpd}}/2$ live on a single slot. The two-sided operator is the double of the half-spin, not a half-spin itself.

**The two Peirce copies are not the two Lorentz chiralities.** The two columns $S_+$ and $S_-$ carry the same Weyl representation $\Delta_{\mathrm{rep}}$; the two Lorentz chiralities are the two tensor slots $S$ and $S^{*}$, that is the left and right slots.

For a pure non-central factor the eigenvalue $1$ occurs twice in the list; for the scale the value $\varrho^{2}$ occurs four times, and for the phase the value $1$ occurs four times.

The whole section assumes $B\neq0$. When $B=0$ and $\vec Q\neq0$, $L_{\tilde Q}$ is defective, with two Jordan blocks of size two, the common eigenbasis of $L_{\tilde Q}$ and $R_{\tilde Q^{*}}$ does not exist, and the spectral formula is unavailable; the two-sided operator itself remains defined. This is the degenerate case of *The Spectrum of a Biquaternion*, §*The Degenerate Case: The Spectral-Degenerate Cone*.

### The Doubling Rule

**Proposition (the doubling rule).** Write each factor as $F=\exp(tA)$, where $t$ is its scalar parameter and $A$ its generator: $A=e_t$ for the scale, $A=i$ for the phase, $A=i\vec u_{\mathrm b}$ for the boost and $A=\vec u_{\mathrm r}$ for the rotor. Then
$$
\mathrm{Sd}_F(\tilde X)=\exp(tA)\,\tilde X\,\exp(tA^{*}).
$$
Three cases exhaust the word:

**(a)** $A^{*}=A$ (Hermitian). The two slots carry the same exponent $+tA$. If $A$ is central, as for the scale with $A=e_t$, the two-sided operator is multiplication by $\exp(2tA)$; if $A$ is non-central, as for the boost with $A=i\vec u_{\mathrm b}$, the two-sided operator is the congruence whose parameter is $2t$. In both cases the output parameter is $2t$.

**(b)** $A^{*}=-A$ and $A$ non-central (the rotor, $A=\vec u_{\mathrm r}$). The two slots carry opposite exponents, so the two-sided operator is the conjugation $\exp(t\,\mathrm{ad}_A)$, whose vector action is the rotation of angle $2t$; the output parameter is $2t$.

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
The doubling is therefore a property of the non-central factors and of the Hermitian central one; the cancellation is a property of the anti-Hermitian central one. "Half-angle" is the name of the boost and rotor rows; it is not a property of the phase.

## The Image and the Kernel

**Theorem.** Let $\mathrm{J}:\mathbb{B}^{\times}\to GL_{\mathbb{R}}(\mathbb{B})$ be the two-sided map $\tilde Q\mapsto\mathrm{Sd}_{\tilde Q}$.

**(a)** The kernel is the central unit circle,
$$
\ker\Theta=U(1)=\{\lambda e_t:\lambda\in\mathbb{C},\ \lvert\lambda\rvert=1\}.
$$

**(b)** The image is the linear conformal Lorentz group,
$$
\boxed{\;\operatorname{im}\Theta\cong CO^{+}(1,3)=\mathbb{R}_{>0}\cdot SO^{+}(1,3)\;},
$$
acting on $\mathbb{B}_{\Phi}$ by a dilation of ratio $\varrho^{2}$ composed with a proper orthochronous Lorentz transformation.

**(c)** On the modulus-one slice $\varrho=1$, the image is $SO^{+}(1,3)$ and the kernel is $U(1)$.

**(d)** On the norm-one slice $\langle\tilde Q\rangle_{\natural}=1$, the image is $SO^{+}(1,3)$ and the kernel is $\{\pm e_t\}$; the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$.

*Proof.* (a) If $\mathrm{Sd}_{\tilde Q}=\mathrm{id}$, then $\tilde Q\tilde Q^{*}=e_t$ by evaluating at $e_t$, so $\tilde Q^{*}=\tilde Q^{-1}$ and $\tilde Q\tilde X\tilde Q^{-1}=\tilde X$ for every $\tilde X$. Hence $\tilde Q$ is central, $\tilde Q=\lambda e_t$, and $\lvert\lambda\rvert=1$. Conversely, a central $\lambda e_t$ with $\lvert\lambda\rvert=1$ gives the identity, by the computation of §*The Central Phase*.

(b) Every unit is $\varrho\,e^{i\theta_{\mathrm{pha}}} U$ with $\varrho\,e^{i\theta_{\mathrm{pha}}}\in\mathbb{C}^{\times}$ and $U\in SL(2,\mathbb{C})$, the pair unique up to $(\varrho\,e^{i\theta_{\mathrm{pha}}},U)\mapsto(-\varrho\,e^{i\theta_{\mathrm{pha}}},-U)$. The kernel (a) is the unit circle in the first factor, so after that quotient the first factor is $\mathbb{R}_{>0}$ and the second is $SL(2,\mathbb{C})/\{\pm e_t\}=PSL(2,\mathbb{C})\cong SO^{+}(1,3)$:

$$
\operatorname{im}\Theta\cong\mathbb{R}_{>0}\times SO^{+}(1,3)=CO^{+}(1,3).
$$

(c) At $\varrho=1$ the element is $\exp(i\theta_{\mathrm{pha}})U$ with $U\in SL(2,\mathbb{C})$, the pair unique up to $(\theta_{\mathrm{pha}},U)\mapsto(\theta_{\mathrm{pha}}+\pi,-U)$. The kernel is still $U(1)$, and the quotient is $SO^{+}(1,3)$.

(d) At $\langle\tilde Q\rangle_{\natural}=1$ the element lies in $SL(2,\mathbb{C})$ and the kernel of the action on $\mathbb{B}_{\Phi}$ is $\{\pm e_t\}$.

**Corollary (the isometry slice).** The two-sided operator is an isometry of the Lorentzian norm on $\mathbb{B}_{\Phi}$ exactly when $\varrho=1$. For general $\varrho$,

$$ L^{T}G_-L=\varrho^{4}G_-,\qquad \det L=\varrho^{8}, $$

so the form is multiplied by $\varrho^{4}$ and the volume by $\varrho^{8}$; the causal type is preserved and the transformation is a similarity of ratio $\varrho^{2}$.

**Remark (what the image is not).** The image is not the $*$-unitary group and not $GL(2,\mathbb{C})$. The $*$-unitary group acts on the spinor module and sees the phase; the two-sided operator sees only the conformal Lorentz group. The two readings of the same word are the subject of *The Complete Polar Decomposition of an N-Regular Biquaternion*, §*The Operator Reading: the Twist*, and of this article.

## The Wall $B^{2}=0$: the Unipotent Case

On the wall the element is $\tilde Q=Q_t(e_t+\vec\Upsilon)$ with $\vec\Upsilon^{2}=0$, and the operator is a positive scalar times a unipotent operator: $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}\,\mathrm{Sd}_{\tilde Q_0}$ with $\tilde Q_0=e_t+\vec\Upsilon$. The scalar is $\lvert Q_t\rvert^{2}$, not $Q_t^{2}$, because the operator carries the Hermitian conjugate on the right. The scalar line $\vec\Upsilon=0$ is the case $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}\mathrm{id}$, with geometric multiplicity four and Jordan type $1+1+1+1$; the sections below describe the Jordan part $\vec\Upsilon\neq0$.

### The Unipotent Operator

Let $A=L_{\vec\Upsilon}$ and $B=R_{\vec\Upsilon^{*}}$, the left multiplication by $\vec\Upsilon$ and the right multiplication by $\vec\Upsilon^{*}$. They commute, and

$$
A^2=0,
\qquad
B^2=0,
\qquad
\mathrm{Sd}_{\tilde U}=I+A+B+AB.
$$

**Proposition (the Jordan structure).** On the Jordan part, $\mathrm{Sd}_{\tilde U}$ has the single eigenvalue $1$, and its nilpotent part

$$
\mathsf N=\mathrm{Sd}_{\tilde U}-I=A+B+AB
$$

satisfies $\mathsf N^2=2AB$, $\mathsf N^3=0$, with $\operatorname{rank}\mathsf N=2$ and $\operatorname{rank}\mathsf N^2=1$. The Jordan form is one block of size three and one block of size one.

*Proof.* The operators $A$ and $B$ commute and square to zero, so

$$
\mathsf N^2=2AB,
\qquad
\mathsf N^3=3AB(A+B)=0,
$$

because $A^2=B^2=0$. The rank of $A$ is two, and the rank of $B$ is two; their product $AB$ has rank one because the image of $B$ is the right ideal $\vec\Upsilon^{*}\mathbb{B}$ and the kernel of $A$ is the right annihilator of $\vec\Upsilon$, whose intersection with that image is one complex line. Hence $\operatorname{rank}\mathsf N=2$ and $\operatorname{rank}\mathsf N^2=1$. A nilpotent on a four-dimensional space with $\mathsf N^3=0$ and $\operatorname{rank}\mathsf N^2=1$ has one block of size three and one of size one.

Consequently $\mathrm{Sd}_{\tilde Q}$ has the single eigenvalue $|Q_t|^2$, with one $3\times3$ Jordan block and one $1\times1$ block. Its determinant is

$$
\det\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{8},
$$

the fourth power of the element determinant, as in the regular sector.

The fixed subspace of $\mathrm{Sd}_{\tilde U}$ is two-dimensional. It is not the centralizer of $\tilde U$: the norm-one element is not $*$-unitary, and $\mathrm{Sd}_{\tilde U}$ is not a conjugation. One fixed vector comes from the $3\times3$ block and one from the $1\times1$ block; both are written explicitly in §*The Fixed Directions*.

### The Exponential at the Wall

**The exponent of the two-sided operator.** Write $\vec\Upsilon=\vec A+i\vec B$ with $\vec A$ and $\vec B$ real, so that $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$, and put $P=L_{\vec\Upsilon}$ and $Q=R_{\vec\Upsilon^{*}}$, the two operators called $A$ and $B$ in §*The Unipotent Operator*. They commute and square to zero. Since $\tilde U=e^{\vec\Upsilon}$ and $\tilde U^{*}=e^{\vec\Upsilon^{*}}$,
$$
\mathrm{Sd}_{\tilde U}=L_{e^{\vec\Upsilon}}\circ R_{e^{\vec\Upsilon^{*}}}=e^{P}e^{Q}=e^{P+Q},
$$
and $(P+Q)^2=2PQ$ and $(P+Q)^3=0$, as §*The Unipotent Operator* proves. Hence
$$
\boxed{\;\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}\mathrm{Sd}_{\tilde U}
=\lvert Q_t\rvert^{2}e^{P+Q}
=\lvert Q_t\rvert^{2}(I+\mathsf N),\qquad \mathsf N=P+Q+PQ.\;}
$$

**The one-parameter group.** Since $\mathsf N^2=2PQ$ and $\mathsf N^3=0$,
$$
\boxed{\;\exp\bigl(t\mathrm{Sd}_{\tilde Q}\bigr)
=e^{t\lvert Q_t\rvert^{2}}
\Bigl(I+t\lvert Q_t\rvert^{2}\mathsf N+\frac{t^{2}\lvert Q_t\rvert^{4}}{2}\mathsf N^{2}\Bigr)\;}
$$
for every complex $t$.

*Proof.* $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}(I+\mathsf N)$, and $I$ commutes with $\mathsf N$; hence the exponential is $e^{t\lvert Q_t\rvert^{2}}\exp(t\lvert Q_t\rvert^{2}\mathsf N)$, and the second factor truncates at $\mathsf N^3=0$.

**A null rotation.** On $\mathbb{B}_{\Phi}$ the factor $\tilde U$ has norm one, so $\mathrm{Sd}_{\tilde U}$ preserves the Minkowski form $\langle X\rangle_{\natural}$; the path $\mathrm{Sd}_{e^{t\vec\Upsilon}}$, $0\le t\le1$, connects it to the identity, so it is a proper orthochronous Lorentz transformation. Its single eigenvalue is $1$, and its Jordan form is one block of size three and one of size one. A Lorentz transformation of that type is a **null rotation** (a parabolic element): it fixes a null direction and shears the two transverse directions. The exponential displays the finite shear as $I+s\mathsf N+\frac{s^2}{2}\mathsf N^2$ with $s=t\lvert Q_t\rvert^2$. It contains no rotation angle and no rapidity; the two are locked to the single null parameter $a$, with $\varepsilon\tan\frac{\theta_{\mathrm{axr}}}{2}=\sinh\frac{\theta_{\mathrm{rpd}}}{2}=a$. The modulus scales the shear, and the phase cancels.

**The rate is the square of the one-sided rate.** The two-sided operator carries $\vec\Upsilon$ in its left slot and $\vec\Upsilon^{*}$ in its right slot, so the scalar $Q_t$ appears once on each side and the modulus is squared; the one-sided operator carries the left slot only. This is the wall form of the doubling rule: on a vector the two slots add their exponents, and at the wall they add $\vec\Upsilon$ and $\vec\Upsilon^{*}$.


### The Polar Decomposition of the Two-Sided Operator

Write the Cartan pairing of the element as $\tilde Q=\tilde H\tilde V$ with $\tilde H=\varrho\tilde U_{\mathrm b}$ positive and $\tilde V=e^{i\theta_{\mathrm{pha}}}\tilde u_{\mathrm r}$ $*$-unitary. Then

$$
\mathrm{Sd}_{\tilde Q}=\mathrm{Sd}_{\tilde H}\circ\mathrm{Sd}_{\tilde V},
\qquad
\mathrm{Sd}_{\tilde H}(\tilde X)=\tilde H\tilde X\tilde H^{*},
\qquad
\mathrm{Sd}_{\tilde V}(\tilde X)=\tilde V\tilde X\tilde V^{*}.
$$

The first factor is a positive operator on $\mathbb{B}$, because $\tilde H$ is positive. The second is a $*$-unitary operator, because $\tilde V$ is $*$-unitary. This is the polar decomposition of the operator $\mathrm{Sd}_{\tilde Q}$.

The product $\mathrm{Sd}_{\tilde Q}$ is $\lvert Q_t\rvert^{2}$ times a unipotent operator, while the two factors are not unipotent. The positive factor has eigenvalues $\varrho^{2}e^{\pm\theta_{\mathrm{rpd}}}$ on the two spinor slots, and the $*$-unitary factor has eigenvalues $e^{\pm i\theta}$ after the phase cancels. The product has the single eigenvalue $\lvert Q_t\rvert^{2}$. The factors do not commute, and the non-commutativity is the Jordan defect of the two-sided operator.

### The Coalescence of the Two Slots

In the regular sector the two-sided operator has two spinor slots, and the rotor angle and the rapidity are doubled on them. On the wall the slots do not disappear; they coalesce into the Jordan chain. The $3\times3$ block and the $1\times1$ block are the remnants of the two slots: one slot keeps a fixed vector, and the other carries the nilpotent chain of length three.

The central phase is invisible in the two-sided operator, as in the regular sector: $\mathrm{Sd}_{e^{i\theta_{\mathrm{pha}}}}=\mathrm{id}$. The phase is visible only in the one-sided operator. The sector therefore preserves the one-sided/two-sided operator contrast: the phase is a one-sided datum, and the two-sided operator sees only the scale, the boost and the rotor.

### The Fixed Directions

The fixed subspace is $\ker\mathsf N$, of dimension two. Put $\vec c=\vec A\times\vec B/a^2$, so that $\lvert\vec c\rvert=1$, and $X=e_t+i\vec c$.

*Proposition.* $\mathrm{Sd}_{\tilde U}$ fixes $\vec A$ and $X$. These two vectors span the fixed subspace. On $\mathbb{B}_{\Phi}$ the fixed null vector is $iX=ie_t-\vec c$.

*Proof.* From $\vec A\cdot\vec B=0$ and $\lvert\vec A\rvert=\lvert\vec B\rvert=a$,

$$
\Upsilon\vec A=-a^2-i\vec A\times\vec B=\vec A\bar\Upsilon,\qquad
\bar\Upsilon^2=0,
$$

and

$$
\Upsilon\vec c=-\vec B+i\vec A,\qquad
\vec c\bar\Upsilon=\vec B+i\vec A.
$$

Hence $\Upsilon X=\Upsilon+i\Upsilon\vec c=0$ and $X\bar\Upsilon=\bar\Upsilon+i\vec c\bar\Upsilon=0$. Therefore

$$
\mathrm{Sd}_{\tilde U}(\vec A)
=\vec A+\Upsilon\vec A-\vec A\bar\Upsilon-\Upsilon\vec A\bar\Upsilon=\vec A,
$$

because the two middle terms are equal and cancel, and $\Upsilon\vec A\bar\Upsilon=\vec A\bar\Upsilon^2=0$; and

$$
\mathrm{Sd}_{\tilde U}(X)
=X+\Upsilon X-X\bar\Upsilon-\Upsilon X\bar\Upsilon=X.
$$

The vector $\vec A$ has zero scalar part and $X$ has scalar part one, so they are independent. Since $\ker\mathsf N$ is two-dimensional, they span it.

The vector $X$ is null, $\langle X\rangle_{\natural}=1-\lvert\vec c\rvert^2=0$, so the fixed line is the null line of the rotation. The vector $\vec A$ is spacelike, of norm $-a^2$.

### Worked Example on the Wall

Take $\tilde Q=e_t+\vec e_x+i\vec e_y$. In the basis $(e_t,\vec e_x,\vec e_y,\vec e_z)$,

$$
\mathsf M(\mathrm{Sd}_{\tilde Q})=
\begin{pmatrix}
3 & 0 & -2i & 2i\\
0 & 1 & 0 & 0\\
2i & 0 & 1 & -2\\
2i & 0 & 2 & -1
\end{pmatrix}.
$$

The matrix is the identity plus

$$
\mathsf N=
\begin{pmatrix}
2 & 0 & -2i & 2i\\
0 & 0 & 0 & 0\\
2i & 0 & 0 & -2\\
2i & 0 & 2 & -2
\end{pmatrix}.
$$

The rank of $\mathsf N$ is two, the rank of $\mathsf N^2$ is one, and $\mathsf N^3=0$. The second coordinate is fixed, and the remaining three coordinates carry one Jordan block of size three. The determinant is one.

The Cartan factors are

$$
\tilde H=\sqrt2\,e_t+i\frac{\vec e_y+\vec e_z}{\sqrt2},
\qquad
\tilde V=\frac{e_t+\vec e_x}{\sqrt2},
$$

and the two-sided operator is the composition of the positive operator $\mathrm{Sd}_{\tilde H}$ and the $*$-unitary operator $\mathrm{Sd}_{\tilde V}$. The example shows the general structure: the product is unipotent, the factors are not, and the fixed coordinate is the remnant of the $1\times1$ block.

## The Boundary: the Null Cone

The null cone $N=0$ is the subject of *Two-Sided Operators on the N-Degenerate Sector*. Only the two identities that connect the operator on the cone to the operator on the sector are recorded here. On the cone the polar word does not exist, but the two-sided operator does. If $\tilde Q\neq0$ and $\langle\tilde Q\rangle_{\natural}=0$, the matrix $\mathsf M_2(\tilde Q)$ is a nonzero $2\times2$ matrix of determinant zero, hence of complex rank one. The two-sided operator therefore has complex rank one, and its image is the complex line spanned by $\tilde Q\tilde Q^{*}$: writing $\mathsf M_2(\tilde Q)=uv^{*}$ with column $u$ and row $v^{*}$,

$$
\mathsf M_2(\tilde Q)\,X\,\mathsf M_2(\tilde Q)^{*}
=u\,(v^{*}Xv)\,u^{*},
$$

which is a multiple of $uu^{*}=\mathsf M_2(\tilde Q\tilde Q^{*})$. The element $\tilde Q\tilde Q^{*}$ is nonzero because its trace in the matrix model is the squared Frobenius norm of $\mathsf M_2(\tilde Q)$. The action collapses the eight-dimensional algebra onto one complex line; it is not invertible, and it has no polar reading because the scale, the phase, the boost and the rotor are not available on the cone.

**The degenerate case in coordinates.** Write $\tilde Q=Q^0e_t+Q^k\vec e_k$ and $\vec Q^\natural=(\overline{Q^1},\overline{Q^2},\overline{Q^3})$. For $k=1,2,3$ the scalar component of the image of a vector basis element is

$$
\mathrm{Sd}_{\tilde Q}(\vec e_k)^0 = 2i\,\mathrm{Im}\bigl(Q^0\overline{Q^k}\bigr) - \bigl(\vec Q\times\vec Q^\natural\bigr)^k ,
$$

which vanishes when all four coefficients of $\tilde Q$ are real, and when $\tilde Q$ is central. On the cone the trace of the rank-one operator is $4\lvert Q^0\rvert^2$, so

$$
\mathrm{Sd}_{\tilde Q}\circ\mathrm{Sd}_{\tilde Q}=4\lvert Q^0\rvert^{2}\,\mathrm{Sd}_{\tilde Q} .
$$

The operator is therefore nilpotent exactly when $Q^0=0$, and for $Q^0\neq0$ it is a projection up to the scalar $4\lvert Q^0\rvert^{2}$.

## Summary

The Hermitian pair of the polar word is read factor by factor. The closed form is

$$
\mathrm{Sd}_{\tilde Q}=\varrho^{2}\,\mathrm{Sd}_{\tilde U_{\mathrm b}}\circ\mathrm{Sd}_{\tilde u_{\mathrm r}},
\qquad
\mathrm{Sd}_{\exp(i\theta_{\mathrm{pha}})}=\mathrm{id}.
$$

The scale dilates by $\varrho^{2}$. The phase cancels: the whole $U(1)$-orbit of an element has one two-sided operator, because the phase is central and $*$-unitary. The boost is a congruence by the Hermitian positive $\tilde U_{\mathrm b}$, and the rotor is an inner automorphism; on the norm-one slice they produce the rapidity $\theta_{\mathrm{rpd}}$ and the rotation of angle $\theta_{\mathrm{axr}}$. The norm scales by $\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}$, so the two-sided operator is an isometry on the unit-norm slice.

The spectral form of the pairing is the product formula. The left and right slots commute, and their eigenvalues are $\lambda_\pm$ and $\bar\lambda_\pm$. The spectrum of the two-sided operator is
$$
\operatorname{spec}\mathrm{Sd}_{\tilde Q}
=\bigl\{\lambda_+\bar\lambda_+,\ \lambda_+\bar\lambda_-,\ \lambda_-\bar\lambda_+,\ \lambda_-\bar\lambda_-\bigr\}.
$$
The two-sided operator is therefore the two-slot operator: its spectrum is the four products, not the two eigenvalues. In representation-theoretic terms it is $\Delta_{\mathrm{rep}}\otimes\bar\Delta_{\mathrm{rep}}$, the complexified vector representation: the vector weights are the sums of the two spinor weights. The exponent reading of this doubling is §*The Doubling Rule*.

The image of the two-sided operator on the group of invertibles is $CO^{+}(1,3)$, the kernel is $U(1)$, and the isometry slice is $\varrho=1$, where the image is $SO^{+}(1,3)$. On the norm-one slice the map is the double cover $SL(2,\mathbb{C})\to SO^{+}(1,3)$. On the null cone the two-sided operator survives as an operator of complex rank one, with image the line spanned by $\tilde Q\tilde Q^{*}$.

The phase is the one factor that the two-sided operator does not see. It is visible to the norm, to the determinant and to the module, which is why the polar word carries it; it is invisible to the vector action, which is why the two-sided operator is a representation whose image is the conformal Lorentz group and not the full group of invertibles.

Off the wall the exponential is diagonalisable, with the eigenvalues $e^{t\lambda_i\bar\lambda_j}$, and its determinant is $\exp(4t\lvert Q_t\rvert^{2})$.

On the wall $B^{2}=0$ the element is $\tilde Q=Q_t(e_t+\vec\Upsilon)$ and $\mathrm{Sd}_{\tilde Q}=\lvert Q_t\rvert^{2}\mathrm{Sd}_{e_t+\vec\Upsilon}$. The exponential is $\exp(t\mathrm{Sd}_{\tilde Q})=e^{t\lvert Q_t\rvert^{2}}\bigl(I+t\lvert Q_t\rvert^{2}\mathsf N+\tfrac{t^{2}\lvert Q_t\rvert^{4}}{2}\mathsf N^{2}\bigr)$, a null rotation with the single eigenvalue $1$. The nilpotent part $\mathsf N=\mathrm{Sd}_{e_t+\vec\Upsilon}-I=A+B+AB$, with $A=L_{\vec\Upsilon}$ and $B=R_{\vec\Upsilon^{*}}$, satisfies $\mathsf N^{2}=2AB$, $\mathsf N^{3}=0$, $\operatorname{rank}\mathsf N=2$ and $\operatorname{rank}\mathsf N^{2}=1$: one Jordan block of size three and one of size one, eigenvalue $\lvert Q_t\rvert^{2}$, determinant $\lvert Q_t\rvert^{8}$. The fixed subspace is two-dimensional, spanned by the spacelike vector $\vec A$ and the null vector $e_t+i\vec c$ with $\vec c=\vec A\times\vec B/a^{2}$. The two spinor slots coalesce into the Jordan chain.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}$ | the biquaternion algebra $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $\vec e_k^{2}=-e_t$ and $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | the central scalar imaginary, $i^{2}=-1$ |
| $\tilde Q^{*}$ | the Hermitian conjugation $\overline{\tilde Q^{\natural}}$ |
| $\natural$, $\bar\cdot$ | the quaternion and coefficient conjugations |
| $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ | the Hermitian and anti-Hermitian subspaces, $\tilde Q^{*}=\pm\tilde Q$ |
| $\mathrm{Sd}_{\tilde Q}(\tilde X)=\tilde Q\tilde X\tilde Q^{*}$ | the Hermitian pair |
| $\langle\mathrm{Sd}_{\tilde Q}(\tilde X)\rangle_{\natural}=\lvert\langle\tilde Q\rangle_{\natural}\rvert^{2}\langle\tilde X\rangle_{\natural}$ | the scaling of the norm; an isometry on the unit-norm slice |
| $\langle\tilde Q\rangle_{\natural}=\langle\tilde Q,\tilde Q\rangle_{\natural}=\sum_\mu Q_\mu^{2}$ | the complex norm of the polar series |
| $\varrho\exp(i\theta_{\mathrm{pha}})$ | the complex modulus, the principal square root of $\langle\tilde Q\rangle_{\natural}$ |
| $P=\exp(i\theta_{\mathrm{pha}})$ | the central phase factor |
| $\varrho>0$, $\theta_{\mathrm{pha}}\in\left(-\tfrac{\pi}{2},\tfrac{\pi}{2}\right]$ | the scale and the phase angle |
| $\tilde U_{\mathrm b}=\exp(i\tfrac{\theta_{\mathrm{rpd}}}{2}\vec u_{\mathrm b})$ | the Hermitian positive unit-norm boost |
| $\tilde u_{\mathrm r}=\exp(\tfrac{\theta_{\mathrm{axr}}}{2}\vec u_{\mathrm r})$ | the unit real quaternion rotor |
| $\lambda_\pm=Q_t\pm iB$, $B^{2}=Q_x^{2}+Q_y^{2}+Q_z^{2}$ | the two eigenvalues of $L_{\tilde Q}$, and of $R_{\tilde Q}$ |
| $\lambda_i\bar\lambda_j$ | the four eigenvalues of the two-sided operator in its common eigenbasis |
| $\Delta=\operatorname{diag}(\lambda_+,\lambda_-)$ | the matrix of $\tilde Q$ in the eigenbasis matrix model |
| $S,S^{*}$ | the spinor space $\mathbb{C}^{2}$ and its dual, with $\mathbb{B}\cong S\otimes S^{*}$ |
| $\Delta_{\mathrm{rep}},\bar\Delta_{\mathrm{rep}}$ | the defining representation on $S$ and its conjugate |
| $A$ in the doubling rule | the generator of the factor, $\mathrm{Sd}_F(\tilde X)=\exp(tA)\tilde X\exp(tA^{*})$ |
| $\mathsf M^{\tilde Q}$ | the eigenbasis matrix model, not the Pauli model $\mathsf M_2$ |
| $\tilde\Pi_\pm$, $S_\pm=\mathbb{B}\tilde\Pi_\pm$ | the eigenprojections and the two left ideals of the one-sided reading (Peirce index) |
| $\theta_{\mathrm{rpd}}\ge0$, $\theta_{\mathrm{axr}}\in[0,2\pi]$ | the rapidity and the rotation angle |
| $B_\pm$ | the $4\times4$ matrices of the boost on $\mathbb{B}_{\Psi}$ and $\mathbb{B}_{\Phi}$ |
| $\mathsf R(\theta_{\mathrm{axr}},\vec u_{\mathrm r})$ | the Rodrigues rotation matrix of the rotor |
| $G_\pm$ | the matrices of the norm on the two sectors, $G_+=\operatorname{diag}(1,-1,-1,-1)$ and $G_-=-G_+$ |
| $CO^{+}(1,3)$ | the linear conformal Lorentz group, the image of the two-sided operator |
| $U(1)$ | the kernel of the two-sided operator, the central unit circle |
| $\langle\tilde Q\rangle_{\natural}=1$ | the norm-one slice, $SL(2,\mathbb{C})$ |

## Further Reading

- [One-Sided Operators on the N-Regular Sector](one-sided-operators-on-the-n-regular-sector.html), for the one-sided companion: the left and right multiplications, the sector decomposition and the exchange $\mathbb{B}_{\Phi}\leftrightarrow\mathbb{B}_{\Psi}$ by the phase $i$.
- [The N-Regular, Spectrally Regular Sector](the-n-regular-spectrally-regular-sector.html), §*The Eigenbasis, the Nilpotents, and the Peirce Corners*, for the basis, the two chiral spinor spaces and the diagonal action of $\tilde Q$.
- [Relations between the Complete Polar Decomposition and Eigenbasis of an N-Regular Biquaternion](relations-between-the-complete-polar-decomposition-and-eigenbasis-of-an-n-regular-biquaternion.html), for the general dictionary between the spectral data and the polar angles when the axes do not commute.
- [The Complete Polar Decomposition of an N-Regular Biquaternion](the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the four factors, the modulus, the branch and the domain, and §*The Operator Reading: the Twist*, for the same word read on the spinor module.
- [The Complete Polar Decomposition and Remarkable Subspaces](the-complete-polar-decomposition-and-remarkable-subspaces.html), §*The Action on the Two Halves*, for the detailed action on the two sectors, the boost matrices and the comparison of the two signs.
- [The Cartan Hermitian Pairing of the Complete Polar Decomposition of an N-Regular Biquaternion](the-cartan-hermitian-pairing-of-the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the Hermitian positive and $*$-unitary factors and the equation $\tilde Q\tilde Q^{*}=\tilde H^{2}$.
- [The Quaternion Pairing of the Complete Polar Decomposition of an N-Regular Biquaternion](the-quaternion-pairing-of-the-complete-polar-decomposition-of-an-n-regular-biquaternion.html) and [The Hamilton Root Pairing of the Complete Polar Decomposition of an N-Regular Biquaternion](the-hamilton-root-pairing-of-the-complete-polar-decomposition-of-an-n-regular-biquaternion.html), for the two partial two-factor groupings.
- [The Hermitian Pair of Operators Acting on Two Sides](the-hermitian-pair-of-operators-acting-on-two-sides.html), for the two-sided operator as a product of the two regular maps, its spectrum, determinant, trace and rank.
- [Completely Positive Maps of a Hermitian Algebra with Hermitian Adjoint](completely-positive-maps-of-a-hermitian-algebra-with-hermitian-adjoint.html), for the two-sided operator as a completely positive map and its rank-one place among the completely positive maps.
- [Biquaternion Rotations and Lorentz Transformations](biquaternion-rotations-and-lorentz-transformations.html), for the Lorentz group in biquaternionic form and the double cover.
- [$M_2(\mathbb{R})$ Hyperbolic Representation : Operators](m2r-hyperbolic-representation-operators.html), for the commutative case where the two-sided operator collapses to $\langle Q\rangle_{*}$ times the identity.
- [$M_2(\mathbb{C})$ Reduced Representation : Operators](m2c-reduced-representation-operators.html), for the commutative case where the two-sided operator collapses to multiplication by the modulus squared and the phases cancel.
