# __The Friedrichs Extension of a Hermitian Form__

## Introduction

A semi-bounded Hermitian form is one whose diagonal is bounded below, $\langle Tu,u\rangle\ge m\|u\|^2$, but which need not be closed and need not be coercive. The Friedrichs construction manufactures a self-adjoint operator out of it anyway. The device is to shift the form into a positive one, $a(u,u)+(1-m)\|u\|^2$, to complete the given domain in the resulting norm, and to pick out the operator whose action is given by the form on the vectors of the completion that lie in $H$. The resulting **Friedrichs extension** is the self-adjoint operator associated with the smallest closed extension of the form, and among all self-adjoint extensions of the given symmetric operator it is the one whose form domain is smallest; at the other extreme sits the **Krein–von Neumann extension**, whose form domain is largest. This is the theorem that gives the Dirichlet Laplacian its boundary conditions and the Sturm–Liouville operators their self-adjointness, and it is the reason a boundary-value problem can be posed by a form and a domain alone, with no reference to the differential expression.

This article fixes the semi-bounded Hermitian forms, the form norm and its completion, the Friedrichs extension and its maximality, the operator version for a semi-bounded symmetric operator, and the examples. The closed and coercive forms and the Dirichlet principle are *Dirichlet Forms and the Hermitian Dirichlet Principle*; the representation theorem is *Sesquilinear Forms and the Lax–Milgram Theorem*; the self-adjointness and the square root are *Self-Adjoint Operators and the Spectral Theorem* and *Positive Operators and the Square Root*; the deficiency indices and the symmetric operators are *The Adjoint of an Unbounded Operator*.

Throughout, $H$ is a complex Hilbert space with inner product linear in the first argument, and $t$ is a **Hermitian form** with dense domain $\mathcal{D}(t)\subseteq H$; the form is **semi-bounded below** with bound $m$ if

$$
t(u,u)\ge m\|u\|^2\qquad(u\in\mathcal{D}(t)),
$$

and the **shifted form** is $t_1(u,v)=t(u,v)+(1-m)\langle u,v\rangle$, which is nonnegative.

## Semi-Bounded Forms

**Definition.** A Hermitian form $t$ is **bounded below** by $m\in\mathbb{R}$ if $t(u,u)\ge m\|u\|^2$ for $u\in\mathcal{D}(t)$; the largest such $m$ is the **lower bound**, and the form is **semibounded** if it has one.

**Proposition (the shifted form is an inner product).** If $t$ is semibounded below by $m$ then $t_1(u,v)=t(u,v)+(1-m)\langle u,v\rangle$ satisfies $t_1(u,u)\ge\|u\|^2$; it is a positive definite Hermitian form, hence an inner product on $\mathcal{D}(t)$, and the associated norm

$$
\|u\|_1=\sqrt{t(u,u)+(1-m)\|u\|^2}
$$

dominates the original norm, $\|u\|_1\ge\|u\|$.

*Proof.* The shift makes the diagonal at least $\|u\|^2$; the form is sesquilinear and Hermitian, so it is an inner product, and the dominance is immediate.

**Proposition (the form need not be closed).** The form $t$ is **closed** if $\mathcal{D}(t)$ is complete for $\|\cdot\|_1$ and **closable** if it has a closed extension; a semibounded closable form has a smallest closed extension, the **closure** $\bar t$, obtained by completing the domain and extending the form by continuity.

*Proof.* The form is continuous for the form norm, so it extends uniquely to the completion of its domain; the extension is a Hermitian form with domain the completion, and it is the smallest closed extension because any closed extension must contain the closure of the domain and be continuous on it.

## The Form Norm and Its Completion

**Definition.** For a semibounded Hermitian form $t$ the **form space** $H_t$ is the completion of $\mathcal{D}(t)$ for the norm $\|\cdot\|_1$, and the **form domain** of the closure is $H_t$ with the form extended by continuity.

**Proposition (the form space and its embedding).** $H_t$ is a Hilbert space and the inclusion $\mathcal{D}(t)\hookrightarrow H$ extends to a contraction $H_t\to H$ of norm at most $1$, which need not be injective when $t$ is not closable; when $t$ is closable the map is injective and $H_t$ is canonically a dense subspace of $H$.

*Proof.* The completion of an inner product space is a Hilbert space, and the identity map on $\mathcal{D}(t)$ is continuous because $\|u\|\le\|u\|_1$, so it extends by continuity to a contraction; injectivity fails exactly when there is a nonzero element of $H_t$ with $\|u\|_1$-limit zero in $H$, which is the non-closability of $t$.

**Example (the Dirichlet form).** For $\Omega\subseteq\mathbb{R}^d$ open and bounded the form

$$
t(u,v)=\int_\Omega\nabla u\cdot\nabla\bar v
$$

on $\mathcal{D}(t)=C_c^\infty(\Omega)$ is Hermitian and bounded below by $0$; its form space is the Sobolev space $H^1_0(\Omega)$, obtained by completing the smooth compactly supported functions in the norm $\|u\|_1=\bigl(\int|\nabla u|^2+\int|u|^2\bigr)^{1/2}$, and the Poincaré inequality makes the gradient term alone a norm on this space.

## The Friedrichs Extension

**Theorem (Friedrichs).** Let $t$ be a densely defined semibounded Hermitian form with lower bound $m$, and let $H_t$ be its form space. Then there is a self-adjoint operator $A_F$ with

$$
D(A_F)=\{u\in H_t: v\mapsto t(u,v)\ \text{is }H\text{-bounded on}\ \mathcal{D}(t)\},
$$

characterised by

$$
t(u,v)=\langle A_Fu,v\rangle\qquad(u\in D(A_F),\ v\in H_t),
$$

and $A_F$ is bounded below by $m$. The operator $A_F$ is the **Friedrichs extension** of $t$; its form domain is $H_t$, so $\mathcal{D}(A_F^{1/2})=H_t$, and

$$
t(u,v)=\langle A_F^{1/2}u,A_F^{1/2}v\rangle\qquad(u,v\in H_t).
$$

*Proof.* The shifted form $t_1$ is a bounded coercive Hermitian form on the Hilbert space $H_t$, so by Lax–Milgram it is represented by a bounded operator $B$ on $H_t$; the vectors of $D(A_F)$ are those for which the functional $v\mapsto t_1(u,v)$ is bounded in the original norm, and on them $A_Fu=B u-(1-m)u$ shifted back. The operator is symmetric and, being the restriction of the representing operator of a coercive form, it is self-adjoint by the representation theorem for forms; the identification of the form domain with the domain of the square root is then the standard statement that the form is the form of its own square root.

**Theorem (maximality).** Among all self-adjoint operators $A$ that represent the form $t$, the Friedrichs extension is the largest: if $A$ represents $t$ then

$$
A\le A_F
$$

in the order of self-adjoint operators, equivalently $A_F^{-1}\le A^{-1}$ on the positive part; and the Friedrichs extension is the unique self-adjoint extension of $t$ whose operator domain is contained in $H_t$, the smallest possible form domain.

*Proof.* A representing operator $A$ has form domain contained in $H_t$, because the form domain contains $\mathcal{D}(t)$ and is complete for the form norm, hence lies in the completion $H_t$, and the form of $A$ agrees with $t$ there. Comparing the two forms and using the resolvent identity gives $A\le A_F$. For the uniqueness, if $D(A)\subseteq H_t$ then for $u\in D(A)$ the identity $t(u,v)=\langle Au,v\rangle$ holds on $\mathcal{D}(t)$ and extends to $H_t$ by continuity in $v$; so $v\mapsto t(u,v)$ is $H$-bounded, $u\in D(A_F)$ and $A_Fu=Au$, whence $A\subseteq A_F$; both are self-adjoint, so $A=A_F$.

**Remark.** The naming is by the form domain: the Friedrichs extension has the smallest form domain among the self-adjoint extensions, hence the largest operator, and the other extreme, with the largest form domain and hence the smallest operator, is the Krein–von Neumann extension treated below. The two coincide exactly when the form is already closed and the original operator self-adjoint.

## The Operator Version

**Theorem (Friedrichs extension of a symmetric operator).** Let $T$ be a densely defined symmetric operator bounded below by $m$, and let $t_T(u,v)=\langle Tu,v\rangle$ on $D(T)$. Then $T$ has a self-adjoint extension bounded below by $m$, and among the self-adjoint extensions of $T$ there is exactly one whose operator domain is contained in the form domain $H_{t_T}$; it is the Friedrichs extension, and it is the largest self-adjoint extension of $T$ in the operator order.

*Proof.* The form $t_T$ is semibounded on the dense domain $D(T)$, so the previous theorem applies and produces $A_F$; the operator $A_F$ extends $T$ because on $D(T)$ the form $t_T$ is represented by $T$; the maximality among extensions of $T$ is the maximality among extensions of the form, since an extension of $T$ defines an extension of the form. The extension is bounded below by $m$ by the corresponding statement for the form.

**Proposition (the extension and the deficiency indices).** If $T$ is symmetric with deficiency indices $n_+=n_-=n>0$ then $T$ has a $U(n)$-family of self-adjoint extensions; the Friedrichs extension is the one whose form domain is smallest, the Krein–von Neumann extension is the one whose form domain is largest, and every other self-adjoint extension has a form domain between them.

*Proof.* The self-adjoint extensions are parametrised by the unitary maps between the deficiency subspaces, as in von Neumann's criterion; the order on the extensions is the inclusion of form domains, and the two extreme extensions are the Friedrichs and the Krein–von Neumann ones.

## The Krein–von Neumann Extension

**Definition.** The **Krein–von Neumann extension** $A_N$ of a semibounded symmetric operator $T$ is the smallest self-adjoint extension in the operator order, equivalently the one whose form domain is the largest.

**Proposition (characterisation).** $A_N$ is the self-adjoint extension of $T$ with $\ker A_N=\ker A_F$, and it is the unique extension whose form domain contains all the other form domains; for every self-adjoint extension $A$ of $T$,

$$
A_N\le A\le A_F ,
$$

so the Krein–von Neumann extension is the smallest and the Friedrichs extension the largest in the operator order.

*Proof.* The Krein–von Neumann extension is defined by the boundary condition that the extension annihilates the kernel of the Friedrichs extension; the order statement is the translation of the form-domain inclusion, and the two extreme extensions sandwich all others because every form domain lies between the smallest and the largest, with the operator order reversed.

**Example (the Laplacian on a bounded domain).** For $\Omega$ a bounded smooth domain the operator $-\Delta$ on $C_c^\infty(\Omega)$ has deficiency indices $(n,n)$ with $n$ infinite; its Friedrichs extension is the Dirichlet Laplacian $-\Delta_D$ with form domain $H^1_0(\Omega)$, and its Krein–von Neumann extension is the operator whose form domain is $H^1(\Omega)$ with the boundary condition $\partial_\nu u=0$ replaced by the vanishing of $A_N$ on the harmonic functions; the Robin problems interpolate between the two extremes, and this is the standard spectral picture of the extension theory.

**Example (Sturm–Liouville).** For the Sturm–Liouville expression $-(pu')'+qu$ on a finite interval with $p>0$ and $q$ bounded below, the minimal operator on compactly supported smooth functions has deficiency indices $(2,2)$; the Friedrichs extension realises the Dirichlet boundary conditions, the other self-adjoint extensions are the separated and coupled boundary conditions, and the Friedrichs extension is the one selected by the quadratic form $\int p|u'|^2+q|u|^2$ on $H^1_0(a,b)$.

## Summary

A Hermitian form $t$ is semibounded below by $m$ if $t(u,u)\ge m\|u\|^2$, and the shifted form $t+ (1-m)\langle\cdot,\cdot\rangle$ is then an inner product whose completion $H_t$ is the form space; the identity of $H_t$ with a subspace of $H$ fails exactly when $t$ is not closable. The Friedrichs extension $A_F$ is the self-adjoint operator represented by the form, with domain the vectors of $H_t$ whose representing functional is bounded in $H$ and with form domain $H_t$, so $\mathcal{D}(A_F^{1/2})=H_t$ and $t(u,v)=\langle A_F^{1/2}u,A_F^{1/2}v\rangle$; it is bounded below by the same constant $m$. It is the largest self-adjoint extension of the form in the operator order, equivalently the one whose form domain is smallest and contained in every other, and for a semibounded symmetric operator it is the unique self-adjoint extension with operator domain contained in the form domain of the given form. When the deficiency indices are equal and positive the extensions form a $U(n)$-family; the Friedrichs extension is one extreme, the Krein–von Neumann extension is the other, and every self-adjoint extension lies between them, $A_N\le A\le A_F$. The Dirichlet Laplacian and the Sturm–Liouville problems with separated boundary conditions are the standard realisations, and the Robin problems interpolate between the two extremes.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $t(u,v)$ | Hermitian form on a dense domain $\mathcal{D}(t)$ |
| $t(u,u)\ge m\|u\|^2$ | semibounded below |
| $t_1=t+(1-m)\langle\cdot,\cdot\rangle$ | the shifted positive form |
| $\|u\|_1^2=t(u,u)+(1-m)\|u\|^2$ | the form norm |
| $H_t$ | form space, the completion of $\mathcal{D}(t)$ |
| $t(u,v)=\langle A_Fu,v\rangle$ | the Friedrichs extension |
| $\mathcal{D}(A_F^{1/2})=H_t$ | form domain is the domain of the square root |
| $A_N\le A\le A_F$ | Friedrichs and Krein–von Neumann extensions sandwich the rest |
| $H^1_0(\Omega)$ | form space of the Dirichlet form |
| Dirichlet Laplacian | Friedrichs extension of $-\Delta$ on $C_c^\infty(\Omega)$ |

## Further Reading

- Kurt Friedrichs, "Spektraltheorie halbbeschränkter Operatoren und Anwendung auf die Spektralzerlegung von Differentialoperatoren", *Mathematische Annalen* **109** (1934), 465–487, for the original construction.
- Mark G. Krein, "The Theory of Self-Adjoint Extensions of Semi-Bounded Hermitian Transformations and its Applications", *Matematicheskii Sbornik* **20** (1947), 431–495, for the Krein–von Neumann extension and the comparison with Friedrichs.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 2nd ed. 1976), for the form representation, the semibounded forms and the extension theory.
- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics II: Fourier Analysis, Self-Adjointness* (Academic Press, 1975), for the Friedrichs extension, the deficiency indices and the examples.
- Joachim Weidmann, *Spectral Theory of Ordinary Differential Operators* (Springer, 1987), for the Sturm–Liouville realisations and the boundary conditions.

