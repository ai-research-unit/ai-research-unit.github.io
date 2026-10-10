
# __Split-Biquaternion Regular Functions__

## Introduction

This article studies **regular** (equivalently **monogenic**) split-biquaternion-valued functions, that is, the solutions of the first-order system $\tilde{\nabla}\tilde{F} = 0$ defined by the split biquaternion Cauchy–Riemann operator on a four-dimensional real subspace. It follows *Split-Biquaternion Analysis*, where the operator and its conjugate are constructed, and it records the system of equations, the examples, the harmonicity and factorization of the d'Alembertian, the role of the zero divisors, and the relations to the biquaternion regular functions and to Clifford analysis. The treatment is purely mathematical; no physical interpretation is used, and the operator is only ever called the **Cauchy–Riemann operator**, never by any older name.

Throughout, $\tilde{Q} = \sum_{\mu=0}^{3} Q_\mu e_\mu$ with $Q_\mu = q_\mu + jq'_\mu \in \mathbb{D}$, the units satisfy $e_0 = 1$, $e_1^2 = e_2^2 = e_3^2 = -e_0$ and $e_1e_2 = e_3$, and $j$ is the central split complex unit with $j^2 = +e_0$. On a four-dimensional real subspace $V \subset \mathbb{H}_{\mathbb{D}}$ with real coordinates $Q_0,Q_1,Q_2,Q_3$ we write $\partial_\mu = \partial/\partial Q_\mu$.

## The Variable and Its Structure

A **complex structure** on a real vector space is a real-linear map $J$ with $J^2 = -\mathrm{id}$. The split biquaternion algebra carries the two commuting structures

$$
J_j(\tilde{Q}) = j\tilde{Q} , \qquad J_1(\tilde{Q}) = e_1\tilde{Q} ,
$$

but they are not interchangeable: $J_j$ is the coefficient structure and it does not complexify the algebra, since $j^2 = +e_0$ and the coefficients lie in the split complex algebra $\mathbb{D}$. The genuinely complex structure is $J_1$, which complexifies the plane spanned by $e_0, e_1$ and singles out the commutative subalgebra

$$
\mathbb{D}[e_1] = \{a e_0 + b e_1 : a, b \in \mathbb{D}\} \cong \mathbb{D} \otimes \mathbb{C} ,
$$

in which $e_1$ is the imaginary unit. Restricting to real coefficients, the subalgebra $\mathbb{R}[e_1] = \mathrm{span}_{\mathbb{R}}\{e_0, e_1\} \cong \mathbb{C}$ is the classical complex plane of quaternionic analysis.

## The Cauchy–Riemann Operator and Its Conjugate

**Definition.** The **split biquaternion Cauchy–Riemann operator** on $V$ and its **quaternion conjugate** are

$$
\tilde{\nabla} = \sum_{\mu=0}^{3} e_\mu \frac{\partial}{\partial Q_\mu} , \qquad \tilde{\nabla}^{\natural} = e_0 \frac{\partial}{\partial Q_0} - \sum_{k=1}^{3} e_k \frac{\partial}{\partial Q_k} .
$$

On the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ this is the quaternion Cauchy–Riemann operator of Fueter's theory; on the full algebra it acts coefficientwise, and on the idempotent decomposition it splits as

$$
\tilde{\nabla}\tilde{F} = \left(\tilde{\nabla}\tilde{F}_+\right)\tilde\Pi_1 + \left(\tilde{\nabla}\tilde{F}_-\right)\tilde\Pi_2 ,
$$

where on the right $\tilde{\nabla}$ is the quaternion operator acting on each idempotent component.

**Theorem.** The operator factors the scalar d'Alembertian:

$$
\tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = \Box := \left(\partial_0^2 + \partial_1^2 + \partial_2^2 + \partial_3^2\right) e_0 .
$$

**Proof.** The units satisfy $e_\mu e_\nu^{\natural} + e_\nu e_\mu^{\natural} = 2\delta_{\mu\nu}e_0$, so the cross terms cancel in the product, leaving the sum of the second derivatives.

The operator $\tilde{\nabla}$ is the first-order operator whose fundamental solution is the Cauchy kernel; it must not be confused with $\tilde{\nabla}^2 = (\partial_0^2-\Delta) + 2\sum_k e_k\partial_0\partial_k$, which is split-biquaternion-valued and is not the d'Alembertian.

## Regular Functions and the System of Equations

**Definition.** Let $\Omega$ be open in $V$ and let $\tilde{F} : \Omega \to \mathbb{H}_{\mathbb{D}}$ be continuously differentiable. Then $\tilde{F}$ is **left-regular** if $\tilde{\nabla}\tilde{F} = 0$ on $\Omega$, and **right-regular** if $\tilde{F}\tilde{\nabla} = 0$ on $\Omega$. A function regular with respect to $\tilde{\nabla}^{\natural}$ is **anti-regular**.

**Convention.** In this category **regular** without qualification means **left-regular**, $\tilde{\nabla}\tilde{F} = 0$; the operator inverted in the integral theory is the first-order operator $\tilde{\nabla}$, not $\Box$ and not $\tilde{\nabla}^2$.

**Theorem (regularity system).** Writing $\tilde{F} = F_0 + \mathbf{F}$ with $\mathbf{F} = F_1e_1 + F_2e_2 + F_3e_3$, the function $\tilde{F}$ is left-regular if and only if

$$
\partial_0 F_0 = \mathrm{div}\,\mathbf{F} , \qquad \partial_0\mathbf{F} + \mathrm{grad}\,F_0 + \mathrm{rot}\,\mathbf{F} = 0 ,
$$

a system of four first-order equations coupling the scalar part $F_0$ to the vector part $\mathbf{F}$.

**Proof.** Expanding $\tilde{\nabla}\tilde{F} = \sum_\mu\sum_\nu (\partial_\mu F_\nu)e_\mu e_\nu$ and separating the scalar and vector parts of the quaternion product gives the displayed system, the same computation as for the quaternions (see *Split-Biquaternion Analysis*).

On the quaternion subspace, where the coefficients are real, the principal symbol $s(\xi) = \sum_\mu \xi_\mu e_\mu$ satisfies $s(\xi)s^{\natural}(\xi) = |\xi|^2 e_0$, so the system is elliptic and its regular functions are real-analytic. On an indefinite four-dimensional subspace, where the coordinate along the split direction enters the symbol with the opposite sign, the principal symbol degenerates on the null cone and the system is no longer elliptic.

## Examples and Basic Properties

**Constants.** A constant $\tilde{F} = \tilde{C}$ is regular on any subspace, and the constants form an eight-dimensional real space of regular functions.

**Powers of a single-plane variable.** On the quaternion subspace, with $A = Q_0 + Q_1 e_1$, every classical holomorphic function of $A$, extended by constancy in $Q_2, Q_3$, is regular; in particular $\tilde{\nabla} A = e_0 e_0 + e_1 e_1 = 0$.

**The coordinate function is not regular.** $\tilde{\nabla}\tilde{Q} = \sum_\mu e_\mu e_\mu = e_0 - 3e_0 = -2e_0 \neq 0$, so the identity function is not regular, in contrast with the complex case.

**The Cauchy kernel.** On the quaternion subspace $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$, which is a division algebra, the function

$$
\tilde{G}(\tilde{Q}) = \frac{\tilde{Q}^{\natural}}{\|\tilde{Q}\|_E^4}
$$

is regular for $\tilde{Q} \neq 0$ and is the fundamental solution of $\tilde{\nabla}$; the proof uses $\tilde{Q}^{\natural}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$ and therefore needs the real coefficients of that subspace. On the full algebra, where the coefficients lie in $\mathbb{D}$, this identity fails because the coefficient part of $\tilde{Q}^{\natural}\tilde{Q}$ is $N(\tilde{Q})$, a split complex number rather than a positive real one.

**Closure.** Regular functions are closed under addition and under right multiplication by constants, $\tilde{\nabla}(\tilde{F}\tilde{C}) = (\tilde{\nabla}\tilde{F})\tilde{C} = 0$; they are stable under right multiplication by constants but not under left multiplication, because left multiplication by a general constant does not commute past the units.

## Harmonicity and the Factorization of the Laplacian

**Theorem.** Every left-regular function is harmonic for the d'Alembertian:

$$
\Box\tilde{F} = \tilde{\nabla}^{\natural}\left(\tilde{\nabla}\tilde{F}\right) = 0 , \qquad \Box = \left(\partial_0^2 + \partial_1^2 + \partial_2^2 + \partial_3^2\right)e_0 .
$$

**Proof.** Apply $\tilde{\nabla}^{\natural}$ to $\tilde{\nabla}\tilde{F} = 0$ and use the factorization.

The converse fails: $Q_0$ is harmonic but $\tilde{\nabla}Q_0 = e_0 \neq 0$. On the quaternion subspace the d'Alembertian is the ordinary Laplacian in four real variables, so every regular function there is harmonic in the classical sense; on an indefinite subspace it is a wave operator, and the elliptic tools of the complex theory — the mean value property, the maximum principle and Liouville's theorem — are not available.

**Corollary.** The idempotent components of a regular function are separately regular, $\tilde{\nabla}\tilde{F}_\pm = 0$, and hence separately harmonic; regularity on the full algebra is thus the pair of quaternionic regularities, and the theory splits along the two halves. This is the analytic form of the algebra decomposition, and it is a genuine difference from the biquaternion case, where the algebra is simple and no such splitting exists.

## The Role of the Zero Divisors

In the complex theory the variable ranges over a field and every nonzero element is invertible; in the split biquaternion algebra this fails, and every failure of the complex analogy on the full algebra is traceable to the zero divisors.

**The inverse is local.** The naive quotient $\tilde{A}/\tilde{Q} = \tilde{A}\tilde{Q}^{\natural}N(\tilde{Q})^{-1}$ requires $N(\tilde{Q})$ to be a unit of $\mathbb{D}$, that is requires $\tilde{Q}$ to lie off the zero divisor locus $Z = \mathbb{H}\tilde\Pi_1\cup\mathbb{H}\tilde\Pi_2$, the union of the two four-dimensional ideals. On $Z$ there is no inverse and no difference quotient, and since $Z$ has dimension four rather than being a hypersurface, the naive definition of differentiability with respect to the variable fails on a positive-dimensional set. This is the reason the standard definition of regularity uses four real variables rather than one algebra variable, exactly as in the biquaternion case.

**The kernel is local.** The Cauchy kernel $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ is defined off the origin, but its regularity rests on the identity $\tilde{Q}^{\natural}\tilde{Q} = \|\tilde{Q}\|_E^2 e_0$ which holds only where the coefficients are real. On the full algebra, where $N(\tilde{Q})$ is split complex, the corresponding homogeneous kernel is $\tilde{Q}^{\natural}N(\tilde{Q})^{-1}$ up to a power, and it is undefined on the zero divisor locus; on an indefinite subspace it is not a fundamental solution, and the characteristic set of the operator is the null cone there.

**The characteristic set.** On an indefinite subspace the principal symbol vanishes on the null cone of the relevant real form, so the operator factors a wave operator there rather than the Laplacian; the null cone is simultaneously the characteristic set, a subset of the zero divisor locus, and the place where the kernel ceases to be regular. Every regular function on the full algebra therefore obeys its equations on the complement of $Z$, and any integral representation must restrict either to the quaternion subspace, where $Z$ is empty, or to domains avoiding $Z$.

## The Relation to the Biquaternion Case and to Clifford Analysis

Restricting to real quaternion-valued functions on the quaternion subspace recovers Fueter's quaternionic analysis in full, since that subspace is a division algebra; the split biquaternion theory is the extension obtained by allowing the coefficients to run over $\mathbb{D}$. The biquaternion case replaces $\mathbb{D}$ by $\mathbb{C}$: the norm there is complex, the zero divisors are the null quadric of an isotropic form and form a hypersurface, and the Cauchy kernel $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ is a genuine fundamental solution on the whole algebra off the origin. In the split biquaternion case the split-biquaternion norm is anisotropic and the zero divisors form the union of two linear subspaces, so the singular set of the naive inverse is a union of two four-dimensional subspaces rather than a quadric hypersurface. The regularity system, the harmonicity and the factorization of the d'Alembertian are formally identical in the two cases, since both rest on the same Clifford relation among $e_0,e_1,e_2,e_3$; what differs is the coefficient algebra and hence the invertibility.

The general setting is Clifford analysis. On the subsystem generated by $e_0,e_1,e_2,e_3$ with the negative definite relations, the regular functions are the monogenic functions of the Clifford algebra $\mathrm{Cl}_{0,3}$; allowing the coefficients to be split complex replaces the complex coefficient field by $\mathbb{D}$ and introduces the zero divisors. The bridge between the single-plane and the hypercomplex notions is the Fueter–Sce construction, in which the appropriate power of the Laplacian converts a slice-regular function of one complex variable into a monogenic function of four real variables; for the split biquaternion setting this is treated in *Fueter Theory for Split-Biquaternions*.

## Summary

The split biquaternion Cauchy–Riemann operator $\tilde{\nabla} = \sum_\mu e_\mu\partial_\mu$ and its quaternion conjugate $\tilde{\nabla}^{\natural}$ act on a four-dimensional real subspace, factor the scalar d'Alembertian $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = (\partial_0^2+\Delta)e_0$, and define left-regular and right-regular functions by $\tilde{\nabla}\tilde{F} = 0$ and $\tilde{F}\tilde{\nabla} = 0$. Regularity is equivalent to the four-equation Cauchy–Riemann–Fueter system coupling the scalar and vector parts through divergence, gradient and curl, which is elliptic on the quaternion subspace and degenerate on the indefinite subspaces, where its characteristic set is the null cone. Every regular function is harmonic, the converse failing already for $Q_0$; and because the algebra is a product of two quaternion algebras, regularity is the pair of quaternionic regularities on the two idempotent components, a splitting that has no counterpart in the simple biquaternion algebra. The zero divisors, which form the union of the two four-dimensional ideals rather than a quadric hypersurface, make the inverse and the difference quotient local, since $N(\tilde{Q})$ must be a unit of $\mathbb{D}$; they are the analytic obstruction on the full algebra and on the indefinite sectors, while on the quaternion subspace, a division algebra, the Cauchy kernel $\tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ is a genuine regular fundamental solution. The theory recovers Fueter's quaternionic analysis on the quaternion subspace and is the $\mathbb{D}$-coefficient case of Clifford analysis; the transition from single-plane holomorphy is the Fueter–Sce construction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{H}_{\mathbb{D}} = \mathbb{D}\otimes_{\mathbb{R}}\mathbb{H} \cong \mathbb{H}\oplus\mathbb{H}$ | Split biquaternion algebra |
| $e_0,e_1,e_2,e_3$ | Algebra basis, $e_0 = 1$, $e_k^2 = -e_0$ |
| $j$ | Central split complex unit, $j^2 = +e_0$ |
| $V$ | Four-dimensional real subspace with coordinates $Q_0,\dots,Q_3$ |
| $\tilde{\nabla} = \sum_\mu e_\mu\partial_\mu$ | Split biquaternion Cauchy–Riemann operator |
| $\tilde{\nabla}^{\natural}$ | Quaternion conjugate of $\tilde{\nabla}$ |
| $\Box = \tilde{\nabla}\tilde{\nabla}^{\natural} = \tilde{\nabla}^{\natural}\tilde{\nabla} = (\partial_0^2+\Delta)e_0$ | d'Alembertian, scalar |
| $\tilde{\nabla}^2 = (\partial_0^2-\Delta) + 2\sum_k e_k\partial_0\partial_k$ | Square of the operator, not the d'Alembertian |
| $\tilde{\nabla}\tilde{F} = 0$ | Left-regular (monogenic) condition |
| $\tilde{G} = \tilde{Q}^{\natural}/\|\tilde{Q}\|_E^4$ | Cauchy kernel on the quaternion subspace |
| $\|\tilde{Q}\|_E^2 = \sum_\mu(q_\mu^2+q'^2_\mu)$ | Euclidean norm squared |
| $Z = \mathbb{H}\tilde\Pi_1\cup\mathbb{H}\tilde\Pi_2$ | Zero divisor locus |
| $\mathbb{H}_{\mathbb{H}_{\mathbb{D}}}$ | Quaternion subspace, a division algebra |

## Further Reading

- R. Fueter, "Die Funktionentheorie der Differentialgleichungen $\Delta u = 0$ und $\Delta\Delta u = 0$ mit vier reellen Variablen", *Commentarii Mathematici Helvetici* 7 (1934), for the origin of the quaternionic regularity system.
- F. Brackx, R. Delanghe and F. Sommen, *Clifford Analysis*, Research Notes in Mathematics 76 (Pitman, 1982), for the Cauchy–Riemann operator, monogenic functions and the Cauchy integral formula.
- Klaus Gürlebeck and Wolfgang Sprößig, *Quaternionic and Clifford Calculus for Physicists and Engineers* (Wiley, 1997), for the componentwise regularity system and its elliptic theory.
- Pertti Lounesto, *Clifford Algebras and Spinors*, 2nd edition (Cambridge University Press, 2001), for the Clifford relation among the units and the factorization of the Laplacian.
