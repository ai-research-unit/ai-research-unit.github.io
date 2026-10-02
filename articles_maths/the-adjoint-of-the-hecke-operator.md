
# __The Adjoint of the Hecke Operator__

## Introduction

The Hecke operator $T_n$ acts on the space of cusp forms of weight $k$ and level $N$, and the space carries the Petersson inner product, which is the Hermitian form of this article. The operator is normal, and the whole spectral theory of the Hecke eigenforms rests on that fact; the adjoint $T_n^*$ is again a Hecke operator when $\gcd(n,N)=1$, and it is exactly of the ramified type when $\gcd(n,N)>1$. This article defines the operators, computes the adjoint with respect to the Petersson form, states the self-adjointness criterion, and records the failure of the criterion for the ramified operators $U_p$. The coefficient form on the $q$-expansion is the form of the category, and the comparison between the two forms is *Multiplication Operators on an L-Function*; the conjugate symmetry is *The Conjugate Symmetry of the Hecke Operator*. Nothing here reads a distance as an object.

## The Petersson Form and the Hecke Operators

### The form

**Definition.** The **Petersson inner product** on the space $\mathcal{S}_k(\Gamma_0(N))$ of cusp forms is
$$
\langle f,g\rangle=\int_{\Gamma_0(N)\backslash\mathfrak{H}}f(z)\overline{g(z)}\,y^{k}\,\frac{dx\,dy}{y^2},\qquad z=x+iy ,
$$
and the **Petersson norm** is $\|f\|^2=\langle f,f\rangle$.

**Theorem.** The Petersson form is a positive definite Hermitian form on $\mathcal{S}_k(\Gamma_0(N))$; it is invariant under the action of $\mathrm{SL}_2(\mathbb{Z})$ by the slash operator, and the space is a finite-dimensional Hilbert space with this form.

**Proof.** The integrand is invariant under $\Gamma_0(N)$ because the factor $y^k$ compensates the automorphy factors of weight $k$; the integral converges absolutely because $f$ and $g$ are cuspidal, and it is positive definite because the integrand is $|f|^2y^k>0$ off the zeros. This is the standard Petersson theory of *Modular Forms*.

### The operators

**Definition.** For $n\ge1$ the **Hecke operator** is
$$
(T_nf)(z)=n^{k-1}\sum_{d\mid n}d^{-k}\sum_{b\bmod d}f\!\Bigl(\frac{nz+b}{d}\Bigr),
$$
and on the $q$-expansion $f=\sum_{m\ge1}a_mq^m$ it acts by
$$
T_nf=\sum_{m\ge1}\Bigl(\sum_{d\mid\gcd(m,n)}d^{k-1}a_{mn/d^2}\Bigr)q^m .
$$
For $p\mid N$ the operator is written $U_p$ and for $p\nmid N$ the operator $T_p$ is the **good Hecke operator**.

**Theorem.** The operators $T_n$ preserve $\mathcal{S}_k(\Gamma_0(N))$, they commute pairwise, and they are multiplicative in $n$: $T_{mn}=T_mT_n$ for $\gcd(m,n)=1$. They preserve the space of newforms and the space of oldforms separately when $\gcd(n,N)=1$.

**Proof.** The action on the $q$-expansion is the classical formula, in *Modular Forms*; the commutativity and the multiplicativity follow from the double-coset computation and the moduli interpretation of the Hecke correspondence, and the newform statement is the Atkin–Lehner theory.

## The Adjoint

### The formula

**Theorem (the adjoint).** Let $\gcd(n,N)=1$. With respect to the Petersson form and the Fricke involution $w_N$,
$$
T_n^*=w_N^{-1}T_nw_N=w_NT_nw_N ,
$$
and $T_n$ is normal, $T_nT_n^*=T_n^*T_n$. In particular $T_n^*=T_n$ for $\gcd(n,N)=1$ on the whole space when the Fricke involution acts trivially on the space, and always on the subspace of the forms fixed by $w_N$.

**Proof.** The adjoint is computed from the definition by the change of variable $z\mapsto-1/(Nz)$ implementing the Fricke involution; the conjugation by $w_N$ inverts the double coset, and the double coset of $T_n$ is its own inverse under the transpose when $\gcd(n,N)=1$, so the conjugation is the identity on the operator. This is the standard computation of *Modular Forms* and *Hecke Algebras*.

**Corollary (self-adjointness and normality).** For $\gcd(n,N)=1$ the operator $T_n$ is self-adjoint on the space of cusp forms when $N=1$ or when $T_n$ is restricted to the $w_N$-fixed part; in general $T_n$ is normal, hence diagonalisable with an orthonormal basis of eigenforms, and its eigenvalues are real on the self-adjoint subspace.

**Proof.** The normality is from the theorem; a normal operator on a finite-dimensional Hilbert space is unitarily diagonalisable, and a self-adjoint operator has real eigenvalues, by *Spectral Theory*.

### The ramified case

**Theorem.** For $p\mid N$ the operator $U_p$ is not self-adjoint and not normal in general; its adjoint is
$$
U_p^*=w_N^{-1}\widetilde{U}_p\,w_N ,
$$
where $\widetilde U_p$ is the Hecke operator of the dual double coset, and the deviation from self-adjointness is measured by the Atkin–Lehner theory. On the newforms of level $N$ the operator $U_p$ has the eigenvalue $a_p$ with $|a_p|\le2p^{(k-1)/2}$ in the analytic normalisation.

**Proof.** The double coset of $U_p$ is not symmetric because $p\mid N$; the conjugation by the Fricke involution replaces the coset by its adjoint, which is a different operator. The eigenvalue bound is the Deligne bound, in *Modular Forms*.

## Worked Examples

**Example ($N=1$, $k=12$).** The space $\mathcal{S}_{12}(\mathrm{SL}_2(\mathbb{Z}))$ is one-dimensional, spanned by $\Delta$, and $T_n\Delta=\tau(n)\Delta$ with the Ramanujan function; the operator is self-adjoint and the eigenvalues $\tau(n)$ are real.

**Example ($N=p$, $k=2$).** The Atkin–Lehner involution $w_p$ acts on $\mathcal{S}_2(\Gamma_0(p))$ with the $+1$ and $-1$ eigenspaces; the operator $U_p$ is self-adjoint on neither, and its adjoint is $w_p^{-1}U_pw_p$, which is a different operator; the newforms of level $p$ are the eigenvectors of the good $T_n$.

**Example (the Eisenstein series).** On the noncuspidal Eisenstein series the Petersson integral diverges, so the form of the article is not defined and the adjoint computation is replaced by the constant-term pairing; the operator on the Eisenstein part is not the topic of this article.

## Failure of the Degenerate Cases

The adjoint theory of the Hecke operators fails in four degenerate configurations. First, for $p\mid N$ the operator $U_p$ is not normal, so it need not be diagonalisable, and the spectral theorem does not apply; its eigenvalue spectrum is the spectrum of a nonnormal operator, and the eigenforms need not be orthogonal. Second, the Petersson form is not invariant under $\mathrm{SL}_2(\mathbb{Z})$ when the weight is odd, and the space of cusp forms of odd weight and level $N$ has a different structure; the adjoint must be computed with the modified form. Third, the new/old decomposition is preserved by the good Hecke operators but not by the ramified ones, so the adjoint of $U_p$ mixes the new and the old parts; the operator is not block diagonal. Fourth, on the larger space of all modular forms, including the Eisenstein series, the Petersson form diverges and the adjoint is not defined; the theory of the article is the cuspidal theory. These are the boundary cases of the adjoint of the Hecke operator.

## Summary

The Hecke operator $T_n$ acting on the cusp forms of weight $k$ and level $N$ is normal for $\gcd(n,N)=1$, with adjoint $T_n^*=w_N^{-1}T_nw_N$ computed from the Petersson inner product; it is self-adjoint on the $w_N$-fixed part and on the level-one space, so the eigenvalues of the eigenforms are real and the eigenforms form an orthonormal basis. For $p\mid N$ the operator $U_p$ is neither self-adjoint nor normal, its adjoint is the conjugate by the Fricke involution of the dual Hecke operator, and the new/old decomposition is mixed. The degenerate cases are the ramified operators, the odd weight, the noncuspidal Eisenstein series and the mixing of the new and the old parts.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{S}_k(\Gamma_0(N))$ | Space of cusp forms |
| $\langle f,g\rangle$ | Petersson inner product |
| $T_n$ | Hecke operator, $\gcd(n,N)=1$ |
| $U_p$ | Ramified operator, $p\mid N$ |
| $w_N$ | Fricke involution |
| $T_n^*=w_N^{-1}T_nw_N$ | The adjoint |
| $T_nT_n^*=T_n^*T_n$ | Normality |
| $T_n^*=T_n$ | Self-adjointness |
| $a_p$ | Hecke eigenvalue |

## Further Reading

- Martin Eichler, *Introduction to the Theory of Algebraic Numbers and Functions* (Academic Press, 1966), for the Hecke operators and their matrices.
- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the Petersson form and the adjoint.
- Jean-Pierre Serre, *A Course in Arithmetic* (Springer, 1973), for the Hecke operators in the $q$-expansion.
- Wilfred Kohnen and Don Zagier, *Modular Forms with Rational Periods* (Academic Press, 1981), for the newforms and the adjoint operators.
- Fred Diamond and Jerry Shurman, *A First Course in Modular Forms* (Springer, 2005), for a modern treatment of the Hecke operators and the Petersson form.
