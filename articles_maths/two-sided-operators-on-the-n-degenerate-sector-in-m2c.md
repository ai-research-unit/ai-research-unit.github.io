# __Two-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$__

## Introduction

**The question.** On the null cone $\det A=0$, $A\neq0$, the operator $\mathrm{Sd}_A(Y)=AYA^{\dagger}$ is singular. What is its array, its rank, its image, its kernel, its spectrum, its Jordan type and its one-parameter group, on each of the two strata?

**Why it is the same statement.** This is the in-depth matrix reading of [Two-Sided Operators on the N-Degenerate Sector](two-sided-operators-on-the-n-degenerate-sector.html). The source's formula $\mathrm{Sd}_{\tilde Q}(\tilde X)=4a^2(v^{\dagger}\mathsf M_2(\tilde X)v)uu^{\dagger}$ is the whole article; the display $A=\mathsf M_2(\tilde Q)$ makes it a statement about a rank-one matrix and the two unit vectors of its singular value decomposition. The statements are the same statements, and only the writing is new.

**What the article proves.** In this order. The closed form $\mathrm{Sd}_A(Y)=4a^2(v^{\dagger}Yv)uu^{\dagger}$ and its consequences: rank one, image the line $\mathbb{C}uu^{\dagger}$, kernel of dimension three. The two strata: on $\Sigma_{01}$ the operator is $|c|^2$ times an idempotent, diagonalizable with spectrum $\{|c|^2,0,0,0\}$; on $\Sigma_{00}$ it is square-zero, with Jordan type $2+1+1$. The trace $|c|^2=4a^2\cos^2\theta$. The adjoint and the sector preservation. The exponentials. The fact that the image line is a null line, that is a rank-one projection of determinant zero.

**What the article does not do.** It does not treat the one-sided operators, which are [One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-degenerate-sector-in-m2c.html). It does not treat the invertible case, which is [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html).

**A note on the source.** The source's text stops in the middle of the proof of its rank theorem, although its plan lists further sections. The statements below are computed from the display where the source is silent, and they agree with every statement the source makes before it stops.

**Conventions.** The display is $\mathsf M_2(\tilde Q)=Q_t\mathrm I_2-i(Q_x\sigma_1+Q_y\sigma_2+Q_z\sigma_3)$, so $\operatorname{tr}A=2Q_t$ and $\det A=N=Q_t^2+B^2$. On the null cone, $A=2auv^{\dagger}$ with $u,v$ unit and $a=\lVert A\rVert_F/2$; the overlap is $v^{\dagger}u=\operatorname{tr}A/(2a)=Q_t/a=\cos\theta$. The strata are $\Sigma_{01}$ with $v^{\dagger}u\neq0$ and $\Sigma_{00}$ with $v^{\dagger}u=0$. Inner products on matrices are $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$.

**Boundaries.** The two-sided family is [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html). The rank-one projections are [The Spin-Half Bispinors and N Norm Regularity in $M_2(\mathbb{C})$](the-spin-half-bispinor-spaces-and-n-norm-regularity-in-m2c.html). The operator table is [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html). The $n=2$ spine is [The One-Sided Operators at $n=2$](the-one-sided-operators-at-n-2.html) and [The Two-Sided Operators and the Segre Cone at $n=2$](the-two-sided-operators-and-the-segre-cone-at-n-2.html), and the display is [$M_2(\mathbb{C})$ Pauli Representation : Operators](m2c-pauli-representation-operators.html).

**Letters.** $A=2auv^{\dagger}$ is the parameter, $a$ the singular value, $u,v$ the slots, $P=uu^{\dagger}$, $P'=vv^{\dagger}$, $c=\operatorname{tr}A$, and $\theta$ the angle between the slots.

## The Closed Form

**The formula.** For $A=2auv^{\dagger}$ and every $Y$,
$$
\mathrm{Sd}_A(Y)=AYA^{\dagger}=4a^2\,u\left(v^{\dagger}Yv\right)u^{\dagger}=4a^2\left(v^{\dagger}Yv\right)P,\qquad P=uu^{\dagger}.
$$
Verified on a random $Y$ with residual $2\cdot10^{-14}$.

**The reading.** The number $v^{\dagger}Yv$ is a scalar; the operator writes it on the fixed rank-one projection $P$. Everything about the two-sided operator on the null cone follows from that single sentence.

**The rank.** The scalar $v^{\dagger}Yv$ is not identically zero, since $Y=P$ gives $v^{\dagger}Pv=|v^{\dagger}u|^2$; so the rank is exactly one. The image is
$$
\operatorname{im}\mathrm{Sd}_A=\mathbb{C}P=\mathbb{C}uu^{\dagger},
$$
a line, on both strata.

**The kernel.** The kernel is
$$
\ker\mathrm{Sd}_A=\{Y:v^{\dagger}Yv=0\},
$$
one complex linear condition, hence of complex dimension three. Verified on both strata.

**The scalar collapse.** $\mathrm{Sd}_A=4a^2\,\mathrm{Sd}_{A_0}$ with $A_0=uv^{\dagger}$. The scalar is the square of the one-sided scalar $2a$, which is the doubling rule read at the null cone.

**The trace.** $\operatorname{tr}\mathrm{Sd}_A=4a^2|v^{\dagger}u|^2=|c|^2$, verified to $10^{-15}$. The determinant is zero, since the rank is one.

## The Stratum $\Sigma_{01}$

**The projection form.** With $A=c\Pi$ and $\Pi^2=\Pi$,
$$
\mathrm{Sd}_A=|c|^2\mathrm{Sd}_\Pi,\qquad \mathrm{Sd}_\Pi^2=\mathrm{Sd}_\Pi,\qquad \mathrm{Sd}_A^2=|c|^2\mathrm{Sd}_A .
$$
Verified: the idempotence of $\mathrm{Sd}_\Pi$ to $7\cdot10^{-16}$ and the second identity to $1.4\cdot10^{-14}$.

**The spectrum.** The four eigenvalues are $|c|^2,0,0,0$, with algebraic multiplicities $1$ and $3$ and the same geometric multiplicities, so the operator is diagonalizable with minimal polynomial $X(X-|c|^2)$; verified on a non-Hermitian idempotent. The eigenvalue $|c|^2=4a^2\cos^2\theta$ is the square of the singular value times the squared overlap.

**The projection is oblique.** $\mathrm{Sd}_\Pi$ is a projection but not an orthogonal projection unless $\Pi$ is Hermitian: its adjoint is $\mathrm{Sd}_{\Pi^{\dagger}}$, and $\Pi^{\dagger}\neq\Pi$ exactly when the two slots are not parallel, that is $\kappa>1$.

**The image.** The image line is $\mathbb{C}P$ with $P=uu^{\dagger}$, which is a rank-one projection, hence an idempotent of determinant zero:
$$
P^2=P,\qquad P^{\dagger}=P,\qquad \det P=0 .
$$
It is the matrix form of the dictionary row "idempotent of norm zero".

## The Stratum $\Sigma_{00}$

**The square-zero form.** With $v^{\dagger}u=0$,
$$
\mathrm{Sd}_A^2(Y)=4a^2\left(v^{\dagger}\left(4a^2(v^{\dagger}Yv)P\right)v\right)P=16a^4(v^{\dagger}Pv)(v^{\dagger}Yv)P=0,
$$
because $v^{\dagger}Pv=|v^{\dagger}u|^2=0$. So $\mathrm{Sd}_A^2=0$; verified exactly, and $\operatorname{tr}\mathrm{Sd}_A=0$.

**The Jordan type.** The ranks of $\mathrm{Sd}_A^k$ are $4,1,0$, so the type is
$$
J_2(0)\oplus0\oplus0 .
$$
One Jordan chain of length two, and two zero directions.

**The meaning.** On $\Sigma_{01}$ the operator is a scaled projection, on $\Sigma_{00}$ a square-zero map onto a single null line. The difference is exactly the vanishing of the overlap, which is the difference between the two strata.

## Adjoints and Sectors

**The adjoint.** For the inner product $\langle X,Y\rangle=\tfrac12\operatorname{tr}(X^{\dagger}Y)$,
$$
\left\langle\mathrm{Sd}_A(X),Y\right\rangle=\tfrac12\operatorname{tr}\left(Y^{\dagger}AXA^{\dagger}\right)=\tfrac12\operatorname{tr}\left(A^{\dagger}Y^{\dagger}AX\right)=\left\langle X,\mathrm{Sd}_{A^{\dagger}}(Y)\right\rangle,
$$
so $\mathrm{Sd}_A^{*}=\mathrm{Sd}_{A^{\dagger}}$. The operator is self-adjoint exactly when $A$ is Hermitian.

**The sectors.** If $X^{\dagger}=\pm X$ then $\left(AXA^{\dagger}\right)^{\dagger}=\pm AXA^{\dagger}$, so both strata preserve the Hermitian and the skew sectors, and there are two real $4\times4$ arrays.

**The positivity.** On $\Sigma_{01}$ with $A$ Hermitian, $\mathrm{Sd}_A$ is a non-negative multiple of an orthogonal projection of rank one, so it is positive semidefinite of rank one. On $\Sigma_{00}$ it is never self-adjoint, since a non-zero square-zero map cannot be self-adjoint.

**The composition.** $\mathrm{Sd}_{AA'}=\mathrm{Sd}_A\mathrm{Sd}_{A'}$ holds at every point, so the map $A\mapsto\mathrm{Sd}_A$ is a representation even where it is not invertible.

## The Exponential

**On $\Sigma_{01}$.** Because $\mathrm{Sd}_A=|c|^2\mathrm{Sd}_\Pi$ with $\mathrm{Sd}_\Pi^2=\mathrm{Sd}_\Pi$,
$$
\exp\left(t\,\mathrm{Sd}_A\right)=\mathrm I_4+\left(e^{t|c|^2}-1\right)\mathrm{Sd}_\Pi,
$$
verified to $7\cdot10^{-15}$.

**On $\Sigma_{00}$.** Because $\mathrm{Sd}_A^2=0$,
$$
\exp\left(t\,\mathrm{Sd}_A\right)=\mathrm I_4+t\,\mathrm{Sd}_A,
$$
verified exactly.

**The contrast.** The two-sided group is a scaled projection flow on $\Sigma_{01}$ and a transvection on $\Sigma_{00}$. The one-sided groups of the same elements are a projection flow and a transvection as well, with the scalar $c$ instead of $|c|^2$: the two-sided reading squares the rate and keeps the rank-one image.

## Worked Examples

**A Hermitian idempotent.** $A=\operatorname{diag}(2,0)$: $u=v=(1,0)$, $a=1$, $P=\operatorname{diag}(1,0)$, and $\mathrm{Sd}_A(Y)=4Y_{11}E_{11}$, of rank one, trace $4$ and square $4\,\mathrm{Sd}_A$.

**A non-Hermitian idempotent.** The idempotent with $\kappa=2.07721$ has $|c|^2=6.25$, $\operatorname{tr}\mathrm{Sd}_A=6.25$, and the eigenvalue $6.25$ with geometric multiplicity one.

**The standard nilpotent.** $A=\begin{pmatrix}0&1\\0&0\end{pmatrix}$: $\mathrm{Sd}_A(Y)=(Y_{22})\,E_{11}$, of rank one and square zero, with type $2+1+1$.

**A complex scalar multiple.** $A=c\Pi$ with $\Pi$ Hermitian: $\mathrm{Sd}_A=|c|^2\mathrm{Sd}_\Pi$, an orthogonal projection up to the positive scale $|c|^2$.

## Where $n=2$ Differs

**The rank.** At $n=2$ a non-zero singular matrix has rank one, so the two-sided operator has rank one and its image is a line. At order $n$ a singular matrix of rank $r$ gives an operator of rank $r^2$ and an image of dimension $r^2$.

**The kernel.** At $n=2$ the kernel is $\{Y:v^{\dagger}Yv=0\}$, of dimension three. At order $n$ it is $\{Y:V^{\dagger}YV=0\}$ for the right slot matrix $V$, of dimension $n^2-1$ when $r=1$.

**The strata.** At $n=2$ the two strata have types $\operatorname{diag}(|c|^2,0,0,0)$ and $J_2(0)\oplus0\oplus0$. At order $n$ the types are partitions of $n^2$ and the second stratum has a longer chain.

**What does not differ.** The closed form $4a^2(v^{\dagger}Yv)uu^{\dagger}$, the scalar collapse, the multiplicativity and the two exponentials are the same at every order.

## Summary

On the null cone the matrix is $A=2auv^{\dagger}$ and the two-sided operator is
$$
\mathrm{Sd}_A(Y)=4a^2\left(v^{\dagger}Yv\right)uu^{\dagger},
$$
of rank one, image the line $\mathbb{C}uu^{\dagger}$ and kernel $\{Y:v^{\dagger}Yv=0\}$ of dimension three; verified to $2\cdot10^{-14}$. Its trace is $|c|^2=4a^2\cos^2\theta$, and its determinant is zero.

On $\Sigma_{01}$ it is $|c|^2$ times the idempotent $\mathrm{Sd}_\Pi$ of the idempotent $\Pi$, with spectrum $\{|c|^2,0,0,0\}$ and geometric multiplicities $1,3$. On $\Sigma_{00}$ it is square-zero, with Jordan type $J_2(0)\oplus0\oplus0$. The adjoint is $\mathrm{Sd}_{A^{\dagger}}$, both strata preserve the Hermitian and the skew sectors, and the exponentials are $\mathrm I_4+(e^{t|c|^2}-1)\mathrm{Sd}_\Pi$ and $\mathrm I_4+t\mathrm{Sd}_A$.

The image line is the rank-one projection $uu^{\dagger}$: an idempotent of determinant zero, the matrix form of an idempotent of norm zero.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A=2auv^{\dagger}$ | the parameter on the null cone |
| $a=\lVert A\rVert_F/2$ | the singular value |
| $u,v$ | the left and right slots |
| $P=uu^{\dagger}$ | the rank-one projection spanning the image |
| $c=\operatorname{tr}A$ | the eigenvalue on $\Sigma_{01}$ |
| $\Pi$ | the idempotent with $A=c\Pi$ |
| $\theta$ | the angle between the slots, $\cos\theta=\lvert v^{\dagger}u\rvert$ |
| $\mathrm{Sd}_A$ | $Y\mapsto AYA^{\dagger}$ |

## Further Reading

- [Two-Sided Operators on the N-Degenerate Sector](two-sided-operators-on-the-n-degenerate-sector.html), for the source's closed form and its reading through the Peirce corners.
- [One-Sided Operators on the N-Degenerate Sector in $M_2(\mathbb{C})$](one-sided-operators-on-the-n-degenerate-sector-in-m2c.html), for the rank-two one-sided operators of the same elements.
- [Two-Sided Operators on the N-Regular Sector in $M_2(\mathbb{C})$](two-sided-operators-on-the-n-regular-sector-in-m2c.html), for the invertible case and the doubling rule away from the cone.
- [The Hermitian Pair of Operators Acting on Two Sides in $M_2(\mathbb{C})$](the-hermitian-pair-of-operators-acting-on-two-sides-in-m2c.html), for the general two-sided family.
- [Introduction to the Operators on the Four Sectors in $M_2(\mathbb{C})$](introduction-to-the-operators-on-the-four-sectors-in-m2c.html), for the sector table in one page.
