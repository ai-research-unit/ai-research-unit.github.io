
# __Hermitian Pairings of an L-Function__

## Introduction

An $L$-function carries two natural Hermitian pairings: the coefficient pairing on its Dirichlet coefficients, and the completed pairing obtained from the Rankin–Selberg convolution of the function with the conjugate of another. The first makes the space of coefficients a Hilbert space and gives the adjoint of the local operators; the second is the pairing whose analytic continuation and functional equation encode the analytic behaviour of the product. This article defines the two pairings, proves their Hermitian properties, states the positivity of the coefficient pairing and the adjoint relation of the Hecke operators, and identifies the degenerate cases in which the pairings diverge. The operators acting on the pairings are *Multiplication Operators on an L-Function* and *The Adjoint of the Hecke Operator*; the completion is *The Functional Equation and the Conjugate Symmetry of an L-Function*. Nothing here reads a distance as an object.

## The Coefficient Pairing

### Definition

**Definition.** For arithmetic functions $f,g$ with finite norm at the abscissa $\sigma$, the **coefficient pairing** is
$$
\langle f,g\rangle_\sigma=\sum_{n\ge1}f(n)\overline{g(n)}\,n^{-\sigma},
$$
and for $\sigma=0$ it is the form of the category, $\langle f,g\rangle_0=\sum_nf(n)\overline{g(n)}$, on $\mathcal{H}=\ell^2$. The associated norm is $\|f\|_\sigma$.

**Theorem.** The coefficient pairing is a positive definite Hermitian form on the space of the functions of finite norm; it is the $L^2$ form of the multiplicative monoid, and the operators of the algebra of arithmetic functions act on it with the adjoints computed in *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*. The pairing is invariant under the shift $\Sigma_{-\sigma}$ in the sense that $\langle f,g\rangle_\sigma=\langle\Sigma_{\sigma/2}f,\Sigma_{\sigma/2}g\rangle_0$.

**Proof.** Positive definiteness is the positivity of the sum of the moduli; the Hermitian property is $\overline{g(n)}f(n)$ conjugated; the shift statement is the definition of $\Sigma_t$ of *The Shift Operator on a Dirichlet Series*.

### The adjoint relation

**Theorem.** For the local operator $M_h$ of multiplication by $h$, the adjoint with respect to the coefficient pairing is
$$
\langle M_hf,g\rangle_\sigma=\langle f,\Theta_hg\rangle_\sigma ,
$$
with $(\Theta_hg)(k)=\sum_m\overline{h(m)}g(mk)$; the adjoint of the multiplication by a completely multiplicative function $h$ with $|h(p)|=1$ is the multiplication by $\overline h$ composed with the transposed operator, and on the space of the functions supported on the squarefree integers with $|h(p)|=1$ the operator $M_h$ is unitary.

**Proof.** The first statement is the definition of the transposed multiplication; the second is the computation for the unitary case, in which the two sums coincide after the change of variables $n\mapsto mk$. The details are in *The Adjoint of the Left Multiplication on the Algebra of Arithmetic Functions*.

## The Completed Pairing

### The Rankin–Selberg convolution

**Definition.** For two $L$-functions $L(f,s)$, $L(g,s)$ with the local factors $L_p(f,s)$, $L_p(g,s)$ and the local gamma factors, the **Rankin–Selberg convolution** is
$$
L(f\times\bar g,s)=\prod_pL_p(f\times\bar g,s),\qquad L_p(f\times\bar g,s)=L_p(f,s)\,\overline{L_p(g,\bar s)} ,
$$
with the completed form $\Lambda(f\times\bar g,s)$.

**Theorem.** The completed Rankin–Selberg convolution has an analytic continuation with finitely many poles, satisfies a functional equation with conductor the product of the conductors, and its value at the centre is the **completed pairing**
$$
\langle f,g\rangle_{\mathrm{RS}}=\Lambda(f\times\bar g,\tfrac12) ,
$$
a Hermitian pairing on the space of the $L$-functions for which the convolution converges. The pairing is positive definite on the space of the cuspidal $L$-functions and its positivity is the Hermitian form whose associated operator theory is in *Hermitian Forms and the Zeta Function*.

**Proof.** The local factors multiply because the coefficients are multiplicative; the analytic continuation and the functional equation are the Rankin–Selberg theory, with the archimedean factors and the conductor as in *L-Functions*; the positivity on the cuspidal part is the statement that the Petersson inner product is recovered as the residue of the convolution at the edge of the critical strip, in *Modular Forms*.

### The functional equation as an isometry

**Theorem.** The completed pairing satisfies
$$
\langle f,g\rangle_{\mathrm{RS}}=\epsilon\,\overline{\langle f^*,g^*\rangle_{\mathrm{RS}}}
$$
with the root number $\epsilon$, so the involution $s\mapsto1-\bar s$ acts on the pairing as an anti-isometry; the pairing is Hermitian and the functional equation is its compatibility with the conjugate symmetry.

**Proof.** The functional equation of the convolution is the product of the functional equations of the two factors with the root numbers multiplied; the conjugation of the pairing is the conjugation of the completion, and the reflection $s\mapsto1-\bar s$ is the substitution that defines the equation. This is the standard compatibility in *L-Functions*.

## Worked Examples

**Example (the zeta pairing).** For $f=g=\mathbf 1$ the coefficient pairing at $\sigma>1$ is $\zeta(\sigma)$ and the completed pairing is $\Lambda(\zeta\times\zeta,s)$, whose pole structure gives the classical Rankin–Selberg identity; the pairing diverges at $\sigma=1$.

**Example (a Dirichlet character).** For $f=\chi$ and $g=\chi$ the coefficient pairing at $\sigma=1$ is the squared norm of the character, and the completed pairing is the product $L(\chi,s)L(\bar\chi,s)$, whose value at the centre is the central value of a self-dual product.

**Example (a normalised eigenform).** For $f=g$ a newform of level $N$ and weight $k$ the completed pairing is the symmetric square $L$-function, and the positivity of the pairing is the statement that the Petersson norm is positive; the adjoint of the Hecke operator is the self-adjointness of $T_p$ for $p\nmid N$.

## Failure of the Degenerate Cases

The pairings fail in four degenerate configurations. First, the coefficient pairing converges only for $\sigma$ larger than the abscissa of the square-integrability, and at the critical line it may diverge; the pairing must then be defined by the analytic continuation of the completed convolution. Second, the Rankin–Selberg convolution has a pole when the two $L$-functions are not orthogonal, and the pairing is then not finite; the pairing of a form with itself has the pole that computes the Petersson norm, and the pole is removed by the regularisation. Third, the positivity of the completed pairing requires the cuspidality of the forms; for the Eisenstein series the convolution has extra poles and the pairing is not positive definite. Fourth, when the conductors are not coprime the local factors can share a ramified component and the product of the $L$-functions is not the $L$-function of a single object; the pairing is then the pairing of a non-primitive product and its functional equation has an extra factor. These are the boundary cases of the Hermitian pairings.

## Summary

Every $L$-function carries the coefficient Hermitian pairing $\langle f,g\rangle_\sigma=\sum_nf(n)\overline{g(n)}n^{-\sigma}$, positive definite on the functions of finite norm and invariant under the shift, whose local adjoints are the transposed multiplications $\Theta_h$; and the completed pairing $\langle f,g\rangle_{\mathrm{RS}}=\Lambda(f\times\bar g,\frac12)$ defined by the Rankin–Selberg convolution, Hermitian, positive definite on the cuspidal part, and compatible with the conjugate symmetry up to the root number. The rank-one and primitive cases recover the classical pairings, and the degenerate cases are the divergence at the critical line, the pole of the self-convolution, the non-cuspidal Eisenstein part and the shared ramified factors.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle f,g\rangle_\sigma=\sum_nf(n)\overline{g(n)}n^{-\sigma}$ | Coefficient pairing |
| $\mathcal{H}=\ell^2$ | Space of the form at $\sigma=0$ |
| $\Theta_h$ | Transposed multiplication |
| $L(f\times\bar g,s)$ | Rankin–Selberg convolution |
| $\Lambda(f\times\bar g,s)$ | Completed convolution |
| $\langle f,g\rangle_{\mathrm{RS}}=\Lambda(f\times\bar g,\frac12)$ | Completed pairing |
| $\epsilon$ | Root number |
| $s\mapsto1-\bar s$ | Conjugate symmetry |
| $f^*,g^*$ | Coefficient conjugates |

## Further Reading

- Robert Rankin, *Contributions to the theory of Ramanujan's function and similar arithmetical functions* (Proceedings of the Cambridge Philosophical Society, 1939), for the original convolution.
- Atle Selberg, *Bemerkungen über eine Dirichletsche Reihe* (Archiv for Mathematik og Naturvidenskab, 1940), for the Selberg convolution.
- Goro Shimura, *Introduction to the Arithmetic Theory of Automorphic Functions* (Princeton University Press, 1971), for the completed pairing and the Petersson norm.
- Henryk Iwaniec and Emmanuel Kowalski, *Analytic Number Theory* (American Mathematical Society, 2004), for the Rankin–Selberg theory.
- Jean-Pierre Serre, *Abelian $\ell$-adic Representations and Elliptic Curves* (Benjamin, 1968), for the compatibility with the conjugate symmetry.
