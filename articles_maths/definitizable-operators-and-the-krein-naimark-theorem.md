# __Definitizable Operators and the Krein–Naĭmark Theorem__

## Introduction

A $J$-self-adjoint operator can have non-real spectrum, and the first question of the spectral theory is whether the operator is nevertheless controlled by a self-adjoint one in some other Hilbert structure. The answer is given by **definitizability**: an operator is definitizable when some nonzero real polynomial in it is positive definite for the indefinite form, $[p(T)x,x]\geq0$ for every $x$. Definitizability replaces the semi-boundedness of a self-adjoint operator by the requirement that a polynomial of the operator be semi-bounded, and it is the condition under which the spectral function exists.

The **Krein–Naĭmark theorem** is the theorem that a definitizable operator with a uniformly positive polynomial is **similar to a self-adjoint operator**: there is a bounded invertible operator $V$ such that $V^{-1}TV$ is self-adjoint for a Hilbert-space structure. When the polynomial is only semi-definite, the similarity is not available in general and the failures are concentrated at the finitely many **critical points** of the operator, where the quadratic form $[p(T)\cdot,\cdot]$ degenerates and the spectral function acquires singularities. So the theory is a two-case theory: away from the critical points a definitizable operator is spectrally indistinguishable from a self-adjoint one, and at the critical points the indefinite form makes itself felt.

This article fixes definitizability, the critical points, the Krein–Naĭmark similarity theorem with its proof, the existence of the spectral function, and the place of the unbounded theory in Part III.

The indefinite adjoint and $J$-self-adjointness are *J-Self-Adjoint and J-Unitary Operators*; the spectral data is *Spectral Theory on Krein Spaces*; the space, the rank and the form are *Indefinite Inner Product Spaces*, *Pontryagin Spaces* and *Krein Spaces*; the positivity is *The J-Positive Cone and the J-Order*; the quadratic forms and the polarisation are *Quadratic Forms and Polarisation* and *Bilinear Forms*. Those are cited. The operator is bounded and $J$-self-adjoint on a Krein space $K$.

## Definitizable Operators

**Definition.** A bounded $J$-self-adjoint operator $T$ is **definitizable** when there is a real polynomial $p\neq0$ with

$$
[p(T)x,x]\ \geq\ 0 \qquad \text{for every } x\in K ,
$$

and **uniformly definitizable** when moreover $[p(T)x,x]\geq c\|x\|^{2}$ for some $c>0$.

**Proposition (the class is stable under the natural operations).** A uniformly definitizable operator has real spectrum; a definitizable operator with $p(T)$ invertible is uniformly definitizable; and if $T$ is definitizable with polynomial $p$ and $S$ is a $J$-unitary conjugation, then $S^{-1}TS$ is definitizable with the same polynomial.

**Proof.** If $[p(T)x,x]\geq c\|x\|^{2}$ then $\mu - p(T)$ is, for $\mu$ small and of the appropriate sign, positive definite; the spectrum of $p(T)$ is then real and encloses no loop, whence the spectrum of $T$ is real; the invertibility statement is the nondegeneracy of an invertible $J$-self-adjoint operator's form; the stability statement is the $J$-unitarity of $S$, which preserves the form.

**Theorem (spectral consequences of definitizability).** If $T$ is definitizable then its non-real spectrum is finite, consisting of eigenvalues with finite-dimensional root subspaces paired by conjugation; all but finitely many points of the real spectrum are of definite type; and the exceptional real points are the zeros of the polynomial.

**Proof.** The polynomial $p(T)$ is $J$-self-adjoint with $[p(T)x,x]\geq0$; the degeneracy set of the form $[p(T)\cdot,\cdot]$ on the real spectrum is finite by the finite-dimensionality of the root subspaces at the exceptional points, and the non-real spectrum is finite by the argument of *Spectral Theory on Krein Spaces* combined with the semi-definiteness of $p(T)$.

## Critical Points

**Definition.** Let $T$ be definitizable with polynomial $p$. A real point $\lambda$ is a **critical point** of $T$ (with respect to $p$) when $p(\lambda) = 0$ and the form $[p(T)\cdot,\cdot]$ is degenerate on the root subspace of $T$ at $\lambda$; the set $\Sigma$ of critical points is finite.

**Proposition (the polynomial can be chosen with simple behaviour at the critical points).** There is a polynomial $p$ for $T$ whose real zeros are exactly the critical points of $T$, and each such zero of $p$ can be taken of multiplicity at most two; the critical points are independent of the choice of $p$ in the sense that two polynomials exhibit the same finite set of points at which the spectral function may fail to be bounded.

**Proof.** For a polynomial semidefinite in the Krein sense the zeros on the real spectrum are exactly the points at which the form degenerates in a first or second order; the construction is the standard normalisation of the polynomial and the uniqueness of the critical set is the comparison of two such polynomials.

**Proposition (definite points behave as in Hilbert space).** At a real point $\lambda\notin\Sigma$ the operator is of definite type, the spectral projection onto a neighbourhood of $\lambda$ is $J$-self-adjoint and definite, and the functional calculus of $T$ is defined near $\lambda$ as in the Hilbert theory.

**Proof.** Nondegeneracy of $[p(T)\cdot,\cdot]$ at $\lambda$ means the root subspace is a definite subspace of $K$; on a definite subspace the form has a sign, and the operator restricted to it is similar to a self-adjoint operator by the sign of the form.

**Remark (what a critical point is).** A critical point is a point of the real spectrum where the indefinite form degenerates on the root subspace. It is not a point of non-real spectrum; it is the place where a real eigenvalue has an isotropic eigenvector or an isotropic root subspace, and it is the precise obstruction to the similarity established in the next section. In a Pontryagin space every bounded $J$-self-adjoint operator with real spectrum is definitizable, so the critical points are the only phenomenon that the definiteness of the real spectrum does not exclude.

## The Krein–Naĭmark Theorem

**Theorem (uniform case).** Let $T$ be a bounded $J$-self-adjoint operator on a Krein space and suppose there are a real polynomial $p\neq0$ and $c>0$ with $[p(T)x,x]\geq c\|x\|^{2}$ for every $x$. Then

$$
\langle x,y\rangle_{K,p} := [p(T)x,y]
$$

is an inner product defining a norm equivalent to the Hilbert norm of $K$, and $T$ is self-adjoint for it. Consequently there is a bounded invertible operator $V$ with

$$
V^{-1}TV\ \text{self-adjoint in the transported Hilbert structure},
$$

so $T$ is **similar to a self-adjoint operator**.

**Proof.** The form $\langle\cdot,\cdot\rangle_{K,p}$ is sesquilinear, and it is an inner product because $[p(T)x,x]\geq c\|x\|^{2}$ and the form $[p(T)x,y]$ is Hermitian by the $J$-self-adjointness of $p(T)$; its norm is equivalent to the Hilbert norm by the same inequality and the boundedness of $p(T)$. For the symmetry of $T$, $\langle Tx,y\rangle_{K,p} = [p(T)Tx,y]$ and $\langle x,Ty\rangle_{K,p} = [p(T)x,Ty] = [T^{\dagger}p(T)x,y] = [Tp(T)x,y] = [p(T)Tx,y]$, using that $p$ has real coefficients and that $T$ commutes with $p(T)$; so $T$ is symmetric, hence self-adjoint, for the new inner product. The operator $V$ is the positive square root of the operator implementing the equivalence of the two inner products.

**Corollary (the definitizable case away from the critical set).** A definitizable operator whose polynomial can be chosen so that the form $[p(T)\cdot,\cdot]$ is nondegenerate is similar to a self-adjoint operator; in the presence of critical points the similarity still holds on each definite invariant part and may fail on the sum of the critical root subspaces.

**Proof.** The complement of the critical set is a union of definite invariant parts on each of which the uniform hypothesis holds; on the critical root subspaces the form is degenerate and the preceding proof does not apply.

**Remark (the theorem is sharp).** The hypothesis of uniform positivity is used twice: once to obtain an equivalent inner product and once to make $T$ symmetric for it. When only semi-definiteness holds, the form $[p(T)\cdot,\cdot]$ has an isotropic part, and examples of definitizable operators with singular critical points that are not similar to any self-adjoint operator show that the similarity is genuinely lost there.

## The Definite Parts and the Deferral

**Proposition (the definite parts).** Let $\Sigma$ be the critical set of a definitizable operator $T$, the finitely many points at which the form $[p(T)\cdot,\cdot]$ degenerates. On every open interval of $\mathbb{R}\setminus\Sigma$ the operator has a definite invariant part, on which it is an ordinary Hilbert-space self-adjoint operator; on the isotropic part the form degenerates and no such statement holds.

**Proof.** The positivity of $[p(T)\cdot,\cdot]$ on the invariant subspace attached to an interval away from $\Sigma$ makes the form definite there, and a definite form is an inner product equivalent to the original one; on that subspace $T$ is symmetric for an equivalent positive inner product and therefore Hilbert-self-adjoint, and the definite case is the Hilbert case.

**Remark (the boundary of Part II, and the deferral of the spectral function).** The **spectral function** of a definitizable operator — the object that plays the role of a resolution of the identity when the form degenerates at the critical points, together with the functional calculus it defines — is *not* developed here. Its construction and the operator-valued calculus built from it are the content of *Analysis on Linear Spaces* (Part III), which owns the spectral theorem, the resolvent and the analytic machinery; the Kreĭn–Langer construction of the singular part at the critical points is cited from there and not reproved. What Part II keeps is the **bounded** account above: the polynomial criterion of definitizability, the critical set, the definite parts, and the similarity theorem, none of which uses the analytic theory.

## Worked Cases

### The Fundamental Symmetry

$T = J$ is $J$-self-adjoint with $p(t) = t$, since $[Jx,x] = \langle x,x\rangle>0$ for $x\neq0$; the operator is uniformly definitizable, similar to the identity under the appropriate $V$, so its only critical point is $+1$ and the renormalised inner product makes the operator the identity there.

### The Two-Dimensional Example

$T = \left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ on $\mathbb{C}^{1,1}$ has non-real spectrum $\{i,-i\}$ and satisfies $[p(T)x,x]$ with $p(t) = t^{2} + 1$ equal to $0$, so it is definitizable only with the zero form and its critical set is the whole real axis; the operator is not similar to a self-adjoint one, since its spectrum is not real. This is the borderline case of the theory.

### A Hilbert-Self-Adjoint Operator

If $T$ commutes with $J$ and is Hilbert-self-adjoint with real spectrum, then $p(T) = T$ is $J$-positive definite only when $T$ is definite; in general $T$ is definitizable with a polynomial chosen by the sign of $T$ on its spectral intervals, and the similarity theorem recovers the Hilbert self-adjointness.

## Summary

A bounded $J$-self-adjoint operator is **definitizable** when some nonzero real polynomial $p$ makes $[p(T)x,x]\geq0$, and **uniformly definitizable** when $[p(T)x,x]\geq c\|x\|^{2}$; definitizability forces the non-real spectrum to be finite and all but finitely many real points to be of definite type, and it isolates the finitely many **critical points** at which the quadratic form degenerates. The **Krein–Naĭmark theorem** states that a uniformly definitizable operator is similar to a self-adjoint operator: the form $\langle x,y\rangle_{K,p} = [p(T)x,y]$ is an equivalent inner product for which $T$ is symmetric, and the equivalence is implemented by a bounded invertible $V$; the similarity may fail at singular critical points, which is why the theorem is sharp. Away from its finite critical set the operator has definite invariant parts on which it is an ordinary Hilbert-space self-adjoint operator, and the **spectral function** that replaces a resolution of the identity when the form degenerates, with the functional calculus it defines, is deferred to *Analysis on Linear Spaces* (Part III), which owns the spectral theorem and the resolvent. The indefinite adjoint is *J-Self-Adjoint and J-Unitary Operators*, the spectrum is *Spectral Theory on Krein Spaces*, the spaces are *Krein Spaces* and *Pontryagin Spaces*, and the positivity is *The J-Positive Cone and the J-Order*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $[p(T)x,x]\geq0$ | Definitizability |
| $[p(T)x,x]\geq c\|x\|^{2}$ | Uniform definitizability |
| $\Sigma$ | Finite set of critical points |
| $\langle x,y\rangle_{K,p} = [p(T)x,y]$ | Equivalent inner product of the theorem |
| $V^{-1}TV$ self-adjoint | Similarity, the Krein–Naĭmark conclusion |
| $E(\cdot)$, $T = \int\lambda\,E(d\lambda)$ | The spectral function |
| Definite type off $\Sigma$ | Hilbert-like behaviour |
| $\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$ | Borderline case, spectrum $\{i,-i\}$ |

## Further Reading

- Mark G. Kreĭn and Mark A. Naĭmark, "The method of symmetric and Hermitian forms in the theory of the separation of the roots of algebraic equations" (1936) and the later theory, for the similarity method.
- Heinz Langer, "Spectral functions of definitizable operators in Krein spaces", in *Functional Analysis*, Lecture Notes in Mathematics 948 (Springer, 1982), for the spectral function.
- Mark G. Kreĭn and Heinz Langer, "On the spectral function of a self-adjoint operator in a space with indefinite metric", *Doklady Akademii Nauk SSSR* **211** (1973), 1027–1030, for the original construction.
- Tomas Ya. Azizov and I. S. Iokhvidov, *Linear Operators in Spaces with an Indefinite Metric* (Wiley, 1989), for definitizable operators and the similarity theorem.
- Peter Jonas, "On the spectral theory of operators on Krein spaces", in *Operator Theory: Advances and Applications* (Birkhäuser), for critical points and the modern formulation.
