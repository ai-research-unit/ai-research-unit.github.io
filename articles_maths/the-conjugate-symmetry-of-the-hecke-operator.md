
# __The Conjugate Symmetry of the Hecke Operator__

## Introduction

The Hecke operator $T_n$ on the cusp forms of weight $k$ and level $N$ has a conjugate symmetry: it commutes with the conjugation of the coefficients, and its adjoint for the Petersson form is the conjugate operator when the space carries its natural real structure. This article states that symmetry, proves the identity $T_n^*=\iota T_n\iota$ with $\iota$ the coefficient conjugation, and draws the spectral consequences for the eigenvalues. It is the companion of *The Adjoint of the Hecke Operator*, which computes the adjoint; the Hecke action on the coefficients is *The Shift Operator on the Coefficients*, and the conjugate symmetry of the completed $L$-function is *The Functional Equation and the Conjugate Symmetry of an L-Function*. Nothing here reads a distance as an object.

## The Real Structure

### Definition

**Definition.** On the space $\mathcal{S}_k(\Gamma_0(N))$ the **coefficient conjugation** is the operator
$$
\iota:\sum_{m\ge1}a_mq^m\longmapsto\sum_{m\ge1}\overline{a_m}q^m ,
$$
and the space of the **real forms** is its fixed space, $\mathcal{S}_k(\Gamma_0(N))^\iota$.

**Theorem.** The coefficient conjugation is an anti-linear involution of $\mathcal{S}_k(\Gamma_0(N))$, and it is an isometry of the Petersson form:
$$
\iota^2=\mathrm{id},\qquad \langle\iota f,\iota g\rangle=\overline{\langle f,g\rangle} .
$$
The space of the cusp forms is the complexification of the space of the real forms.

**Proof.** The $q$-expansion coefficients of a cusp form are complex and the conjugation of all of them is again the $q$-expansion of a cusp form, because the functional equation of the automorphy factor is real; the isometry is the reality of the integrand of the Petersson form. The statements are the standard theory of the real structure of the space of modular forms, in *Modular Forms*.

### The symmetry

**Theorem (the conjugate symmetry).** For every $n\ge1$ the Hecke operator commutes with the coefficient conjugation,
$$
\iota\,T_n\,\iota=T_n ,
$$
and consequently the adjoint of $T_n$ satisfies
$$
T_n^*=\iota\,T_n^*\,\iota,\qquad T_n^*=\overline{T_n}\ \text{ in the real basis},
$$
where the bar is the entrywise conjugation in a basis of forms with real $q$-expansion. In particular the matrix of $T_n$ in the basis of the real forms is real, and the characteristic polynomial of $T_n$ has real coefficients.

**Proof.** The action of $T_n$ on the $q$-expansion is the formula $\sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}$, whose coefficients are rational integers; conjugating the coefficients and applying the formula commutes with the operation. The adjoint statement follows from the theorem on the adjoint in *The Adjoint of the Hecke Operator*, because the Fricke involution commutes with $\iota$; the reality of the characteristic polynomial is the consequence that the matrix of $T_n$ in the real basis is real.

**Corollary (the eigenvalues).** The eigenvalues of $T_n$ on $\mathcal{S}_k(\Gamma_0(N))$ are the roots of a real polynomial; they are either real or occur in conjugate pairs; and the eigenforms can be chosen with real coefficients when the eigenvalue is real and with conjugate pairs of coefficients otherwise. The Ramanujan function $\tau(n)$ is real.

**Proof.** The characteristic polynomial is real, so its roots are real or in conjugate pairs; the eigenform of a real eigenvalue can be chosen in the real space, and the eigenforms of a nonreal eigenvalue are the conjugates of one another.

## The Symmetry of the Operators

**Theorem.** The conjugate symmetry holds for the good Hecke operators and for the Atkin–Lehner involutions,
$$
\iota\,T_n\,\iota=T_n\quad(\gcd(n,N)=1),\qquad \iota\,w_d\,\iota=w_d ,
$$
and it intertwines the adjoint and the conjugate:
$$
T_n^*=\iota\,T_n\,\iota
$$
on the subspaces where $T_n$ is self-adjoint. For the ramified operators $U_p$, $p\mid N$, one has $\iota U_p\iota=U_p$ but $U_p^*=\iota U_p^*\iota\ne U_p$, so the symmetry of the operator and its self-adjointness are different properties.

**Proof.** The Atkin–Lehner operators act on the $q$-expansion by a permutation of the coefficients with a root-of-unity factor, real for the appropriate normalisation, so they commute with $\iota$; the ramified case is the computation of the adjoint which is not the operator itself. This is the standard theory of *Modular Forms*.

## Worked Examples

**Example ($N=1$).** The space $\mathcal{S}_{12}(\mathrm{SL}_2(\mathbb{Z}))$ has the real form $\Delta$ with real coefficients and real eigenvalue $\tau(n)$; the operator is self-adjoint and the characteristic polynomial is $x-\tau(n)$.

**Example ($N=11$, $k=2$).** The space $\mathcal{S}_2(\Gamma_0(11))$ has real dimension one, spanned by a newform with real coefficients; its $L$-function has real Dirichlet series and the conjugate symmetry is trivial on the eigenform.

**Example (a nonreal eigenform).** On a higher-dimensional space an eigenform with a nonreal Hecke eigenvalue produces a conjugate eigenform; the pair spans a two-dimensional real subspace on which the operator acts as a rotation-dilation, and the conjugate symmetry exchanges the two.

## Failure of the Degenerate Cases

The conjugate symmetry fails in four degenerate configurations. First, when the weight $k$ is odd the space of cusp forms of level $N$ has a modified real structure and the conjugation is not the coefficient conjugation; the symmetry must be stated with the appropriate sign. Second, the symmetry intertwines the operator with its adjoint only up to the Fricke involution when the level is not one, so on the full space the operator is normal but not self-adjoint; the "conjugate = adjoint" identity holds only after the conjugation by $w_N$. Third, the ramified operators commute with the conjugation but are not self-adjoint, so the coincidence of the two properties fails exactly at the ramified places. Fourth, the Eisenstein series do not have the real structure of the cuspidal space in the same sense, because their constant terms are not cuspidal, and the symmetry applies to the cuspidal part. These are the boundary cases of the conjugate symmetry.

## Summary

The Hecke operator $T_n$ commutes with the coefficient conjugation $\iota$ of the cusp forms, so its matrix in the basis of the real forms is real, its characteristic polynomial has real coefficients and its eigenvalues are real or in conjugate pairs; the adjoint satisfies $T_n^*=\iota T_n\iota$ after the conjugation by the Fricke involution, so the conjugate symmetry and the self-adjointness coincide precisely on the good part of the space. The ramified operators $U_p$ commute with the conjugation but are not self-adjoint, the odd weight requires a modified real structure, and the Eisenstein part is excluded. The conjugate symmetry is the compatibility of the Hecke action with the conjugate symmetry of the associated $L$-functions.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\iota$ | Coefficient conjugation |
| $\mathcal{S}_k(\Gamma_0(N))^\iota$ | Space of the real forms |
| $\iota T_n\iota=T_n$ | The conjugate symmetry |
| $T_n^*=\iota T_n\iota$ | Adjoint as conjugated operator |
| $\overline{T_n}$ | Conjugate matrix in the real basis |
| $w_d$ | Atkin–Lehner involution |
| $U_p$ | Ramified operator |
| $\tau(n)$ | Ramanujan function |

## Further Reading

- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the real structure of the space of cusp forms.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the Hecke operators with real matrices.
- Fred Diamond and Jerry Shurman, *A First Course in Modular Forms* (Springer, 2005), for the newforms and the Atkin–Lehner operators.
- Martin Eichler, *Introduction to the Theory of Algebraic Numbers and Functions* (Academic Press, 1966), for the integral matrices of the Hecke operators.
- Wilfred Kohnen and Don Zagier, *Modular Forms with Rational Periods* (Academic Press, 1981), for the conjugate symmetry and the periods.
