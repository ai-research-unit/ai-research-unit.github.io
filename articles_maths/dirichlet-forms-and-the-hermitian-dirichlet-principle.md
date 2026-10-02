# __Dirichlet Forms and the Hermitian Dirichlet Principle__

## Introduction

A Dirichlet form is a closed coercive Hermitian form on a Hilbert space together with a contraction property: the form is not increased by truncating a function at $0$ and $1$. The two halves of the definition play different roles. The closedness and coercivity make the form the inner product of a new Hilbert space, and by the Lax–Milgram theorem they associate to it a self-adjoint operator — the **generator** — through the identity $a(u,v)=\langle Au,v\rangle$; the Markov contraction, which is the analytic form of the maximum principle, makes that operator the generator of a positivity-preserving contraction semigroup. The **Dirichlet principle** is the variational statement that goes with the coercivity: the unique solution of the variational equation is the unique minimiser of the energy functional, and it is the Hermitian case of the principle that the form itself is the energy.

This article fixes the closed and coercive Hermitian forms, the associated operator, the Dirichlet principle, the Markov property and the contraction semigroup, and the generator of a Dirichlet form. The forms and the representation theorem are *Sesquilinear Forms and the Lax–Milgram Theorem*; the self-adjointness and the positivity of the generator are *Self-Adjoint Operators and the Spectral Theorem* and *Positive Operators and the Square Root*; the semi-bounded forms that are not coercive are handled by *The Friedrichs Extension of a Hermitian Form*; the Hilbert-space background is *Hilbert Spaces*, and the integration is *Measure Theory and Integration*.

Throughout, $H$ is a complex Hilbert space with inner product $\langle\cdot,\cdot\rangle$ linear in the first argument, and $a$ is a **Hermitian form** with domain $\mathcal{D}(a)\subseteq H$ a dense linear subspace, linear in the first argument and conjugate-linear in the second, with $a(u,v)=\overline{a(v,u)}$; the form is **closed** if $\mathcal{D}(a)$ is complete for the norm $u\mapsto\sqrt{a(u,u)+\|u\|^2}$, **coercive** if $a(u,u)\ge c\|u\|^2$ for some $c>0$, and **Markovian** if $u\in\mathcal{D}(a)$ implies $(0\vee u)\wedge1\in\mathcal{D}(a)$ with $a\bigl((0\vee u)\wedge1,(0\vee u)\wedge1\bigr)\le a(u,u)$. The **energy** of $u\in\mathcal{D}(a)$ against $f\in H$ is $E_f(u)=a(u,u)-2\operatorname{Re}\langle f,u\rangle$.

## Closed Forms and the Associated Operator

**Definition.** A **closed Hermitian form** is a Hermitian form whose domain is complete for the form norm $\|u\|_a=\sqrt{a(u,u)+\|u\|^2}$; a **Dirichlet form** is a closed coercive Markovian Hermitian form on $H$.

**Proposition (the form domain is a Hilbert space).** If $a$ is closed and Hermitian then $\mathcal{D}(a)$ with $\langle u,v\rangle_a=a(u,v)+\langle u,v\rangle$ is a Hilbert space continuously embedded in $H$; if $a$ is coercive with constant $c$ then the form norm is equivalent to $u\mapsto\sqrt{a(u,u)}$ and $\mathcal{D}(a)$ is complete for that norm as well.

*Proof.* Closedness is the completeness of the form norm; the embedding is the inequality $\|u\|\le\|u\|_a$, and coercivity gives $a(u,u)\le\|u\|_a^2\le(1+\|a\|/c)a(u,u)$ when the form is bounded by $\|a\|$, so the two norms are equivalent.

**Theorem (the generator).** Let $a$ be a closed coercive Hermitian form. Then there is a unique self-adjoint positive operator $A$ with domain

$$
\mathcal{D}(A)=\{u\in\mathcal{D}(a):v\mapsto a(u,v)\ \text{is bounded in }H\}\subseteq\mathcal{D}(a)
$$

such that

$$
a(u,v)=\langle Au,v\rangle\qquad(u\in\mathcal{D}(A),\ v\in\mathcal{D}(a)).
$$

The operator $A$ is boundedly invertible with $\|A^{-1}\|\le1/c$, its form domain contains the domain of $A$, and $a$ is the closure of the form $u,v\mapsto\langle Au,v\rangle$ on $\mathcal{D}(A)\times\mathcal{D}(A)$.

*Proof.* On the Hilbert space $(\mathcal{D}(a),\langle\cdot,\cdot\rangle_a)$ the pairing $a$ is bounded and coercive, so by Lax–Milgram it is represented by a bounded operator; restricting the representing operator to the vectors whose representing functional is bounded in $H$ gives a symmetric operator, and the representation theorem for forms on the dense subspace $H$ produces $A$. The inverse bound is Lax–Milgram on the form, and the closure statement is the density of $\mathcal{D}(A)$ in $\mathcal{D}(a)$ for the form norm.

**Proposition (the resolvent and the square root).** With $A$ as above, the resolvent $(\lambda+A)^{-1}$ is bounded for $\lambda>0$, and $A$ has a positive square root; the **form domain** of $a$ is the domain of $A^{1/2}$,

$$
\mathcal{D}(a)=\mathcal{D}(A^{1/2}),\qquad a(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle ,
$$

so the Dirichlet form is the Dirichlet form of its own square root.

*Proof.* The identification of the form domain with $\mathcal{D}(A^{1/2})$ is the standard spectral-theoretic statement for a positive self-adjoint operator; the factorisation is $a(u,v)=\langle Au,v\rangle=\langle A^{1/2}u,A^{1/2}v\rangle$ on the operator domain, extended by closure to the form domain.

## The Dirichlet Principle

**Theorem (the Hermitian Dirichlet principle).** Let $a$ be a closed coercive Hermitian form on $H$ and let $f\in H$. Then the energy $E_f$ is bounded below on $\mathcal{D}(a)$ and has a unique minimiser $u_0$, which is exactly the unique solution of the variational equation

$$
a(u_0,v)=\langle f,v\rangle\qquad(v\in\mathcal{D}(a)),
$$

and the minimum value is

$$
\inf_{u\in\mathcal{D}(a)}E_f(u)=E_f(u_0)=-a(u_0,u_0)=-\langle f,u_0\rangle .
$$

*Proof.* Completing the square, $E_f(u)=a(u-u_0,u-u_0)-a(u_0,u_0)$ for the solution $u_0$ of the variational equation, which exists and is unique by Lax–Milgram applied to the Hilbert space $(\mathcal{D}(a),\langle\cdot,\cdot\rangle_a)$; the first term is nonnegative and vanishes exactly at $u=u_0$, so $u_0$ is the unique minimiser and the minimum value is $-a(u_0,u_0)$.

**Corollary (the linear dependence on the data).** The minimiser depends linearly on $f$: the map $f\mapsto u_0=A^{-1}f$ is linear and bounded with norm at most $1/c$, and it is the inverse of the generator.

*Proof.* The variational equation reads $a(u_0,v)=\langle f,v\rangle$ for all $v$, which is $\langle Au_0,v\rangle=\langle f,v\rangle$ on the operator domain and extends by continuity; so $u_0=A^{-1}f$, and $A^{-1}$ is bounded with norm at most $1/c$.

**Proposition (the energy identity).** For the minimiser of $E_f$,

$$
E_f(u)=a(u,u)-2\operatorname{Re}\langle f,u\rangle = \|u-u_0\|_a^2-a(u_0,u_0) ,
$$

for every $u\in\mathcal{D}(a)$, and the energy is strictly convex: for $u\neq v$ and $0<t<1$,

$$
E_f\bigl(tu+(1-t)v\bigr)<tE_f(u)+(1-t)E_f(v) .
$$

*Proof.* The identity is the completed square written with the form norm; strict convexity is the strict positivity $a(u-v,u-v)>0$ of the Hermitian form on a nonzero difference, together with the linearity of the term $\operatorname{Re}\langle f,\cdot\rangle$.

**Example (the classical Dirichlet principle).** For a bounded open $\Omega$ the form $a(u,v)=\int_\Omega\nabla u\cdot\nabla\bar v$ on $H^1_0(\Omega)$ is a closed coercive Hermitian form, and the Dirichlet principle recovers the classical statement that the function minimising $\int|\nabla u|^2-2\operatorname{Re}\int f\bar u$ among functions vanishing on the boundary is the weak solution of $-\Delta u=f$.

## The Markov Property and the Semigroup

**Theorem (the Markov property is a contraction).** A closed coercive Hermitian form $a$ is Markovian if and only if the associated semigroup $T_t=e^{-tA}$, $t\ge0$, is submarkovian: $0\le u\le1$ implies $0\le T_tu\le1$ for every $t\ge0$. Equivalently, the Markov property is the statement that the truncations $(0\vee u)\wedge1$ are contractions for the form.

*Proof.* The equivalence is the Beurling–Deny criterion: the normal contractions operate on the form domain and contract the form exactly when the semigroup is submarkovian, and the truncation $u\mapsto(0\vee u)\wedge1$ is the basic normal contraction from which the others are generated.

**Theorem (the contraction semigroup).** Let $a$ be a Dirichlet form with generator $A$. Then $A$ is self-adjoint, positive and boundedly invertible, the semigroup $T_t=e^{-tA}$ is a strongly continuous contraction semigroup of self-adjoint operators, and

$$
a(u,v)=\lim_{t\downarrow0}\frac1t\langle u-T_tu,v\rangle
$$

for $u\in\mathcal{D}(A)$ and all $v\in\mathcal{D}(a)$; conversely a strongly continuous contraction semigroup generated by a self-adjoint operator produces a closed coercive Hermitian form through this limit, and the form is Markovian exactly when the semigroup is submarkovian.

*Proof.* The spectral theorem makes $e^{-tA}$ a contraction for the positive self-adjoint $A$, and strong continuity is the spectral calculus; the limit formula is the differential version of the semigroup equation $\frac{d}{dt}T_tu=-AT_tu$ evaluated at $t=0$; the converse and the Markov equivalence are the Beurling–Deny theorem.

**Proposition (the maximum principle).** A submarkovian semigroup preserves positivity and the bound $\|T_tu\|_\infty\le\|u\|_\infty$ in the ordered setting: if $u\ge0$ then $T_tu\ge0$, and if $u\le1$ then $T_tu\le1$. This is the analytic form of the maximum principle, and it is the reason the Dirichlet form is the variational object of a positivity-preserving contraction semigroup.

*Proof.* The truncation $u\wedge0$ has form no larger than $u$, so the semigroup does not increase it, giving positivity; the upper bound is the same statement applied to $1-u$.

## The Generator

**Definition.** The **generator** of a Dirichlet form $a$ is the operator $A$ of the representation theorem, characterised by $a(u,v)=\langle Au,v\rangle$ for $u\in\mathcal{D}(A)$ and $v\in\mathcal{D}(a)$.

**Proposition (the generator is determined by the form on a core).** If $\mathcal{C}\subseteq\mathcal{D}(A)$ is dense in $\mathcal{D}(a)$ for the form norm and $A_0=A|_{\mathcal{C}}$ is essentially self-adjoint, then the closure of $A_0$ is $A$ and the closure of the form $u,v\mapsto\langle A_0u,v\rangle$ is $a$; so the Dirichlet form and its generator determine each other.

*Proof.* Density in the form norm makes the closure of the form equal to $a$; essential self-adjointness makes the closure of $A_0$ the self-adjoint generator of that form, and uniqueness of the representation gives $A$.

**Example (the Laplacian).** For $\Omega=\mathbb{R}^d$ the form $a(u,v)=\int\nabla u\cdot\nabla\bar v$ on $H^1(\mathbb{R}^d)$ has generator the Laplacian $A=-\Delta$ on $H^2(\mathbb{R}^d)$, the associated semigroup is $e^{-tA}=e^{t\Delta}$, and the Markov property is the maximum principle for the generator. For a finite graph the form $a(u,v)=\sum_{x\sim y}(u(x)-u(y))(\bar v(x)-\bar v(y))$ on the vertex space is a Dirichlet form with generator the graph Laplacian and associated semigroup $e^{-tA}$; these two examples are the continuous and the discrete ends of the theory.

## Summary

A Dirichlet form is a closed coercive Hermitian form on a Hilbert space that is Markovian, meaning that truncating a function at $0$ and $1$ does not increase the form. Closedness and coercivity make the form domain a Hilbert space and produce, by Lax–Milgram, a unique self-adjoint positive invertible **generator** $A$ with $a(u,v)=\langle Au,v\rangle$ for $u$ in the operator domain and $v$ in the form domain, the form domain being that of $A^{1/2}$ and the form being the Dirichlet form of its own square root. The **Hermitian Dirichlet principle** states that the energy $E_f(u)=a(u,u)-2\operatorname{Re}\langle f,u\rangle$ has a unique minimiser, which is the solution of the variational equation and equals $A^{-1}f$, with minimum value $-a(u_0,u_0)$ and with the energy equal to $\|u-u_0\|_a^2-\|u_0\|_a^2$. The Markov property is equivalent to the semigroup $e^{-tA}$ being submarkovian, so a Dirichlet form is the variational object behind a positivity-preserving contraction semigroup; the Laplacian on a domain and the graph Laplacian on a finite graph are the standard examples.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $a(u,v)$ | closed coercive Hermitian form, linear in the first argument |
| $\mathcal{D}(a)$ | form domain, a Hilbert space for $\|u\|_a$ |
| $\|u\|_a^2=a(u,u)+\|u\|^2$ | the form norm |
| $a(u,v)=\langle Au,v\rangle$ | the generator $A$ |
| $\mathcal{D}(a)=\mathcal{D}(A^{1/2})$ | form domain as the domain of the square root |
| $E_f(u)=a(u,u)-2\operatorname{Re}\langle f,u\rangle$ | the energy functional |
| $E_f(u_0)=-a(u_0,u_0)$ | minimum value of the Dirichlet principle |
| $T_t=e^{-tA}$ | the contraction semigroup |
| Markovian | $(0\vee u)\wedge1$ contracts the form |
| submarkovian | $0\le u\le1\Rightarrow 0\le T_tu\le1$ |

## Further Reading

- Masatoshi Fukushima, Yoichi Oshima and Masayoshi Takeda, *Dirichlet Forms and Symmetric Markov Processes* (De Gruyter, 2nd ed. 2011), for the Markov property, the Beurling–Deny criterion and the semigroup.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics IV: Analysis of Operators* (Academic Press, 1978), for the form representation of a self-adjoint operator and the semigroup.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for closed forms, the form domain and the square root.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2nd ed. 1983), for the classical Dirichlet principle and the maximum principle.
- Zhi-Ming Ma and Michael Röckner, *Introduction to the Theory of (Non-Symmetric) Dirichlet Forms* (Springer, 1992), for the general theory and the analytic characterisation.
