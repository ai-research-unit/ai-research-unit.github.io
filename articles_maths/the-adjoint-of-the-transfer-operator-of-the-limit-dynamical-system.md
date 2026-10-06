# __The Adjoint of the Transfer Operator of the Limit Dynamical System__

## Introduction

The transfer operator $L_\varphi$ of the limit dynamical system pushes functions along the dynamics, and its adjoint in the Hermitian metric of the invariant measure pulls them back. The computation of that adjoint is the content of this article, and its answer is the swap of the operators of Part III: the adjoint of the transfer operator is the **Koopman operator** $U_\varphi f=f\circ\varphi$, exactly as the adjoint of the Koopman operator is the transfer operator in *The Adjoint of the Koopman Operator*. The two are not inverses — the limit map is $d$-to-one — and the difference is measured by the local degree; the reversal of *Reversible Iterated Function Systems and the Involution* enters as the operator that interchanges the two kernels, $R_*L_\varphi^*R_*$, and for a reversible system it identifies the adjoint with the transfer operator read with the permuted branches. The eigenvalues of the two operators are conjugate, their eigenfunctions are paired, and the decay of correlations is the estimate on the powers of the adjoint.

The article sets up the Hilbert space $L^2(\mu)$ of the invariant measure and the transfer operator as a bounded operator on it, computes its adjoint and proves that the adjoint is the Koopman operator, and expresses the adjoint through the **reversed kernel** $R_*L_\varphi^*R_*$, which requires the reversibility of the previous article. It draws the spectral consequences: the adjoint has the conjugate spectrum, the complex eigenvalues occur in conjugate pairs, the reversibility makes the transfer operator self-adjoint in the Hermitian form twisted by $R$, and the Perron eigenvalue one is real and simple. It computes the decay of correlations through the duality $\langle L_\varphi^{\,n}f,g\rangle=\langle f,U_\varphi^{\,n}g\rangle$ and the spectral gap of the previous articles. It closes with the two-sided limit — the natural extension of $\varphi$ with the reverse-time dynamics $\hat R$ — and with the comparison with *The Adjoint of the Koopman Operator*, in which the two roles are exchanged.

The transfer operator, the pressure and the invariant density are *The Transfer Operator of the Limit Dynamical System*; the involution, the exchange relation and the fixed tiles are *Reversible Iterated Function Systems and the Involution*; the reversible measure and its decomposition are *The Self-Similar Measure and the Involution*; the adjoint of the Koopman operator, the transfer operator of a reversible system and the time reversal are *The Adjoint of the Koopman Operator*, *The Transfer Operator* and *Time Reversal and the Transfer Operator*, in Part III; the spectral gap, the correlations and the conjugate spectra are the operator theory of Part III. No physics is invoked.

## The Transfer Operator on the Limit Space

### The Hilbert Space and the Action

**Definition.** Let $\mu$ be the invariant measure of the limit dynamical system on $\mathcal{J}_G$ of *The Transfer Operator of the Limit Dynamical System*, and let $L^2(\mu)$ be the Hilbert space of the complex functions of integrable square with the inner product
$$
\langle f,g\rangle=\int f\,\bar g\,d\mu .
$$
The **transfer operator** acts on the bounded functions by
$$
(L_\varphi f)(x)=\sum_{\varphi(y)=x}\delta(y)\,f(y),
$$
with $\delta(y)$ the local degree, and it extends to a bounded operator on $L^2(\mu)$ because $\delta$ is bounded and the measure is finite.

**Proposition (the reduction of the operator).** On the branch $\sigma_x$ the sum defining $L_\varphi$ has exactly one term, so that
$$
L_\varphi f\bigl(\sigma_x(z)\bigr)=d\bigl(\sigma_x(z)\bigr)\,f\bigl(\sigma_x(z)\bigr)+\sum_{x'\ne x}d\bigl(\sigma_{x'}(z')\bigr)f\bigl(\sigma_{x'}(z')\bigr)
$$
with the second sum over the other branches, and in the uniform case, $d\equiv d$, $L_\varphi f=d\sum_{x'}f\circ\sigma_{x'}$: the transfer operator is the sum of the composition operators with the contractions.

### The Adjoint in the Hermitian Metric

**Theorem (the adjoint is the Koopman operator).** The adjoint of the transfer operator with respect to the invariant measure is the **Koopman operator**,
$$
L_\varphi^{\,*}=U_\varphi,\qquad U_\varphi f=f\circ\varphi ,
$$
so that $\langle L_\varphi f,g\rangle=\langle f,U_\varphi g\rangle$ for all $f,g\in L^2(\mu)$.

*Proof.* This is the transpose relation of *The Transfer Operator of the Limit Dynamical System*: changing the variable $x=\varphi(y)$ in the integral $\int(L_\varphi f)\bar g\,d\mu$ and using the invariance of $\mu$ with the unit Jacobian normalisation turns the sum over the preimage into the single value of $g$ at $\varphi(y)$; hence the pairing with $L_\varphi f$ equals the pairing of $f$ with $U_\varphi g$. The general case carries the Radon–Nikodym factor of the invariant measure, which is one in the normalisation.

**Corollary (the shift of the roles).** The computation is the mirror image of *The Adjoint of the Koopman Operator*: there the adjoint of the Koopman operator is the transfer operator of the inverse system, here the adjoint of the transfer operator is the Koopman operator; the difference between the two directions is the non-invertibility of $\varphi$, which makes $U_\varphi$ an isometry but not unitary and $L_\varphi$ a contraction but not an isometry.

*Proof.* $U_\varphi$ is an isometry because $\mu$ is invariant, $\|U_\varphi f\|^2=\int|f|^2\circ\varphi\,d\mu=\int|f|^2\,d(\varphi_*\mu)=\|f\|^2$; it is not onto on the constant functions when $d>1$, because $U_\varphi f=1$ requires $f$ to be constant on the fibres, and the fibres have $d$ points; hence the adjoint $L_\varphi$ cannot be an isometry either, and $L_\varphi U_\varphi=d\,\mathrm{id}$ on the fibres as in the previous article.

**Corollary (the spectra are conjugate).** The spectra of $L_\varphi$ and of $L_\varphi^*=U_\varphi$ are complex conjugate: $\operatorname{spec}L_\varphi=\overline{\operatorname{spec}U_\varphi}$, and the eigenvalues occur in conjugate pairs with the eigenfunctions paired by the adjoint.

*Proof.* The general operator identity: the spectrum of the adjoint is the conjugate of the spectrum. The eigenfunctions: if $U_\varphi g=\lambda g$ and $L_\varphi f=\mu f$, then $\mu\bar\lambda\langle f,g\rangle=\langle L_\varphi f,g\rangle=\langle f,U_\varphi g\rangle=\bar\lambda\langle f,g\rangle$, so the pairing vanishes unless $\mu=\bar\lambda$.

## The Reversed Kernel and the Involution

### The Reversed Kernel

**Definition.** Let $R$ be the involution of *Reversible Iterated Function Systems and the Involution* and let $R_*f=f\circ R$ be the induced operator on functions, a unitary self-adjoint involution because $R_*\mu=\mu$. The **reversed transfer operator** is
$$
\tilde L_\varphi=R_*\,L_\varphi^{\,*}\,R_*=R_*U_\varphi R_* ,
$$
the transfer operator read through the reversal of the kernel.

**Theorem (the reversed kernel).** With $R\varphi=\varphi R$ and $R_*\mu=\mu$, the adjoint $L_\varphi^*=U_\varphi$ commutes with the involutive unitary $R_*$:
$$
R_*U_\varphi R_*=U_{R\varphi R}=U_\varphi=L_\varphi^{\,*},
$$
so the **reversed kernel** $R_*L_\varphi^*R_*$ is the adjoint itself; the transfer operator, being its adjoint, commutes with $R_*$ as well, $R_*L_\varphi R_*=L_\varphi$; and $L_\varphi$ is **self-adjoint up to the involution**,
$$
\langle R_*L_\varphi f,g\rangle=\langle R_*f,L_\varphi g\rangle ,
$$
that is, symmetric for the **twisted Hermitian form** $\langle f,g\rangle_R=\langle R_*f,g\rangle$. The branch exchange $R_*\sigma_xR_*=\sigma_{\rho(x)}$ is the visible form of the same commutation on the tiles.

*Proof.* The commutation $R_*U_\varphi R_*=U_{R\varphi R}=U_\varphi$ holds because $R\varphi=\varphi R$ and $R^2=\mathrm{id}$; the transfer operator is the adjoint of the Koopman operator and commutes with any operator that commutes with the Koopman operator, hence with $R_*$. For the twisted form, $\langle R_*L_\varphi f,g\rangle=\langle L_\varphi f,R_*g\rangle=\langle f,U_\varphi R_*g\rangle=\langle f,R_*U_\varphi g\rangle$ using $R_*^2=\mathrm{id}$ and $R_*U_\varphi=U_\varphi R_*$; on the other side $\langle R_*f,L_\varphi g\rangle=\langle R_*f,U_\varphi^{\,*}g\rangle=\langle U_\varphi R_*f,g\rangle=\langle R_*U_\varphi f,g\rangle=\langle f,U_\varphi R_*g\rangle$, the same value. Hence the symmetry, which is the defining relation of the twisted form.

### Self-Adjointness up to the Involution

**Corollary (the Hermitian form twisted by the reversal).** The form $\langle f,g\rangle_R=\langle R_*f,g\rangle$ is a Hermitian form invariant under $L_\varphi$ in the sense of the previous theorem, and on the symmetric part it agrees with $\langle f,g\rangle$; the antisymmetric part is the negative-definite part of the form, and the two parts are the ones of *The Self-Similar Measure and the Involution*.

*Proof.* The form is sesquilinear and conjugated-symmetric because $R_*$ is Hermitian; the invariance under $L_\varphi$ is the theorem; the splitting into the symmetric and antisymmetric parts comes from the eigenvalues $\pm1$ of $R_*$, and on the latter the form is minus the usual inner product.

## The Spectral Consequences

### The Complex Eigenvalues and the Covariance

**Theorem (the pairing of the eigenvalues).** If $L_\varphi f=\lambda f$ and $f\ne0$ then there is a function $\tilde f$ with $L_\varphi^*\tilde f=\bar\lambda\tilde f$ and $\tilde f=R_*f$ in the reversible case; the spectrum of $L_\varphi$ is invariant under the conjugation $\lambda\mapsto\bar\lambda$, and under the reversal $\lambda\mapsto\bar\lambda$ it is also mapped to the spectrum of the reversed kernel; the Perron eigenvalue $1$ is real, simple and equal to its own conjugate.

*Proof.* The conjugation pairing is the corollary above; the reversal pairing is the theorem on the reversed kernel, which identifies $L_\varphi^*$ with its own reversal, so a $\lambda$-eigenfunction of $L_\varphi$ produces a $\bar\lambda$-eigenfunction of the reversed kernel related by $R_*$. The Perron eigenvalue is real by the Perron–Frobenius theorem of *The Transfer Operator*.

**Corollary (the non-real eigenvalues in pairs).** In the reversible case the non-real eigenvalues of the transfer operator of the limit system occur in conjugate pairs $\lambda,\bar\lambda$ with the eigenfunctions paired by the reversal, and the corresponding eigenfunctions vanish on the fixed set $\mathrm{Fix}(R)$ when they are antisymmetric.

*Proof.* The conjugate pairing of the spectrum and the vanishing of the antisymmetric densities on the fixed set from *The Self-Similar Measure and the Involution*.

### The Adjoint, the Correlations and the Decay

**Theorem (the duality of the correlations).** The correlations of the limit dynamical system are computed through the adjoint:
$$
C_n(f,g)=\int f\circ\varphi^n\,\bar g\,d\mu-\Bigl(\int f\,d\mu\Bigr)\Bigl(\int\bar g\,d\mu\Bigr)=\langle L_\varphi^{\,n}f,g\rangle-\langle f,1\rangle\langle1,g\rangle ,
$$
and when the spectral gap of *The Transfer Operator of the Limit Dynamical System* holds the decay is exponential, $|C_n(f,g)|\le C\theta^n$, for $f$ and $g$ in the H\"older class.

*Proof.* The first identity is the definition of the correlation and the duality $\langle L_\varphi^{\,n}f,g\rangle=\langle f,U_\varphi^{\,n}g\rangle$ of the adjoint; the decay is the spectral gap applied to the shifted operator $L_\varphi-\Pi$ with $\Pi f=\langle f,1\rangle$ the rank-one projection on the invariant function, whose powers decay by $\theta^n$. The central limit theorem follows from the same gap by the standard argument of *The Transfer Operator*.

## The Two-Sided Limit

### The Natural Extension and the Reverse-Time Dynamics

**Definition.** The **natural extension** of the limit dynamical system is the two-sided shift $\Phi$ on the two-sided codes and the **reverse-time dynamics** is the involution $\hat R$ of the natural extension of *Reversible Iterated Function Systems and the Involution*;
$$
\hat R(x_n)_{n\in\mathbb{Z}}=(Rx_{-n})_{n\in\mathbb{Z}},\qquad \hat R\Phi=\Phi^{-1}\hat R .
$$

**Theorem (the adjoint as the reverse-time transfer operator).** On the natural extension the Koopman operator $U_\Phi$ is unitary, its adjoint is the transfer operator $U_\Phi^*=U_\Phi^{-1}=U_{\Phi^{-1}}$, and the one-sided adjoint $L_\varphi^*=U_\varphi$ is the compression of the reverse-time transfer operator:
$$
L_\varphi^*=\mathbb{E}\,U_{\Phi^{-1}}\,\mathbb{E}^{*} ,
$$
where $\mathbb{E}$ is the conditional expectation from the two-sided to the one-sided space.

*Proof sketch.* The natural extension is invertible, so the standard Part III relation $U_\Phi^*=U_\Phi^{-1}$ applies, and the one-sided operator is recovered by conditioning on the future; the compression of a unitary by the conditional expectation is a contraction whose adjoint is the transfer operator. The construction is the reversible version of *The Adjoint of the Koopman Operator*; the details are the operator-theoretic treatment of the natural extensions of Part III.

### The Comparison with the Adjoint of the Koopman Operator

**Remark (the mirror of Part III).** In *The Adjoint of the Koopman Operator* the adjoint of $U$ is the transfer operator of the inverse system; in the present article the adjoint of the transfer operator is the Koopman operator, and the reversed kernel $R_*L_\varphi^*R_*$ is the involution-corrected form of the same identity. The two articles are the two sides of the same duality, and the reversibility of *Reversible Iterated Function Systems and the Involution* is what makes the kernel symmetric: the non-invertibility of the limit map is the entire analytic content of the difference, and the local degree is measured by the failure of the transfer operator to be an isometry, $L_\varphi U_\varphi=d$ on the fibres.

## Summary

The transfer operator $L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)f(y)$ is bounded on $L^2(\mu)$ and its adjoint is the **Koopman operator**, $L_\varphi^*=U_\varphi$, $U_\varphi f=f\circ\varphi$: the mirror of *The Adjoint of the Koopman Operator*. The Koopman operator is an isometry but not unitary and the transfer operator is a contraction but not an isometry, the discrepancy being the local degree, $L_\varphi U_\varphi=d$ on the fibres. The **reversed kernel** is the operator $R_*L_\varphi^*R_*=R_*U_\varphi R_*$, which equals $L_\varphi^*$ itself because the adjoint commutes with the involutive unitary $R_*$, so the adjoint is its own reversal; the transfer operator is then self-adjoint for the **twisted Hermitian form** $\langle f,g\rangle_R=\langle R_*f,g\rangle$, which is positive on the symmetric part and negative on the antisymmetric part. The spectra of $L_\varphi$ and $U_\varphi$ are conjugate, the non-real eigenvalues occur in conjugate pairs related by the reversal, the Perron eigenvalue $1$ is real and simple, and the correlations are the duality $\langle L_\varphi^{\,n}f,g\rangle=\langle f,U_\varphi^{\,n}g\rangle$, decaying exponentially by the spectral gap. On the natural extension the reverse-time transfer operator $U_{\Phi^{-1}}$ is the unitary whose compression to the one-sided space is the adjoint $L_\varphi^*$. The identities $L_\varphi^*=U_\varphi$, $L_\varphi U_\varphi=d$ and the reversal relation were derived from the transpose theorem of *The Transfer Operator of the Limit Dynamical System*; the spectral gap, the decay and the natural extension are quoted from Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle f,g\rangle=\int f\bar g\,d\mu$ | The Hermitian metric of $L^2(\mu)$ |
| $L_\varphi f(x)=\sum_{\varphi(y)=x}\delta(y)f(y)$ | The transfer operator |
| $L_\varphi^*=U_\varphi$, $f\mapsto f\circ\varphi$ | The adjoint, the Koopman operator |
| $L_\varphi U_\varphi=d$ on the fibres | The failure of the isometry |
| $R_*f=f\circ R$ | The operator of the involution |
| $\tilde L_\varphi=R_*L_\varphi^*R_*$ | The reversed kernel |
| $\langle f,g\rangle_R=\langle R_*f,g\rangle$ | The twisted Hermitian form |
| $\operatorname{spec}L_\varphi=\overline{\operatorname{spec}U_\varphi}$ | The conjugate spectra |
| $C_n(f,g)=\langle L_\varphi^{\,n}f,g\rangle-\ldots$ | The correlation and its decay |
| $\hat R(x_n)=(Rx_{-n})$, $\hat R\Phi=\Phi^{-1}\hat R$ | The reverse-time dynamics on the natural extension |

## Further Reading

- Viviane Baladi, *Positive Transfer Operators and Decay of Correlations* (World Scientific, 2000), for the transfer operator, the spectral gap, the correlations and the central limit theorem.
- Michael C. Mackey and Andrzej Lasota, *Chaos, Fractals, and Noise* (Springer, 2nd ed. 1994), for the Perron–Frobenius operator and the invariant densities.
- David Ruelle, *Thermodynamic Formalism* (Addison-Wesley, 1978), for the transfer operator of a reversible system and the pressure.
- Peter Walters, *An Introduction to Ergodic Theory* (Springer, 1982), for the natural extension, the reversible systems and the Koopman operator.
- Kôsaku Yosida, *Functional Analysis* (Springer, 6th ed. 1980), for the adjoint of a bounded operator, the spectra and the compressions by conditional expectations.
- Volodymyr Nekrashevych, *Self-similar groups*, Mathematical Surveys and Monographs **117** (American Mathematical Society, 2005), for the limit dynamical system and the natural extension.
