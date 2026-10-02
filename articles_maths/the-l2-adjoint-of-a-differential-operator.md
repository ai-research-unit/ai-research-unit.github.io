# __The L2 Adjoint of a Differential Operator__

## Introduction

The **$L^2$ adjoint** of a differential operator is its adjoint as an unbounded operator on a Hilbert space of square-integrable sections. It is the global object for which the **formal adjoint** of the operator group is the local shadow: the two agree on the smooth compactly supported sections, and the difference between them is exactly the boundary term of the Lagrange identity, read as the choice of a **domain**. The passage from the formal to the global adjoint is therefore the passage from a formula to an operator with a domain, a closure and possibly boundary conditions, and it is the point where analysis enters the differential geometry.

The article develops the $L^2$ adjoint. It defines the Hilbert space of sections, the operator determined by a differential operator on the smooth compactly supported sections, and its adjoint, and proves that the adjoint exists and is closed as soon as the initial operator is densely defined. It relates the global adjoint to the formal adjoint, showing that the boundary term of Green's formula is precisely the obstruction to equality, and identifies the **minimal** and **maximal** operators whose adjoint pair the formal and the global adjoints are. It develops the closedness, the symmetry, the self-adjointness and the essential self-adjointness of the operators defined by $P$ and $P^*$, and it treats the Laplace-type operators as the model, with the variational characterisation of the spectrum and the Friedrichs extension as the closing of the theory.

The article assumes the Hilbert spaces, the unbounded operators, the adjoints, the closed operators and the spectral theorem of *Hilbert Spaces* and *Unbounded Operators and Spectral Measures*; the metric and measure foundations of *Metric, Uniform and Complete Spaces* and *Measure Theory and Integration*; the Sobolev spaces, the weak derivatives and the elliptic regularity of *Partial Differential Equations* and *Pseudodifferential Operators*; the $L^2$ sections, the pairing, the Lagrange identity and Green's formula of *The Formal Adjoint of a Differential Operator*, the previous entry of this group; the density, the Hodge star, the codifferential, the Laplace–Beltrami operator and the Hodge decomposition of *Hermitian Metrics and the Levi-Civita Connection*, *The Codifferential* and *Differential Forms and Stokes' Theorem*; and the connection Laplacian of *Hermitian Connections and the Adjoint*. The Hodge theory of the de Rham complex on a compact manifold, the harmonic forms and the Betti numbers are *Differential Forms and Stokes' Theorem* and *Sheaves and the de Rham Complex* in this Part; the index theory is *The Atiyah–Singer Index Theorem and K-Theory*. No physics is invoked.

## The Hilbert Space and the Operator

### The Space of Sections

Let $E \to M$ be a vector bundle with a fibrewise inner product $\langle\cdot,\cdot\rangle$ over a smooth manifold with a positive density $d\mu$. The **space of $L^2$ sections** is the completion

$$
L^2(M;E) = \overline{\Gamma_c(E)}^{\ \lVert\cdot\rVert_{L^2}}, \qquad \lVert u\rVert_{L^2}^2 = \int_M \langle u,u\rangle\,d\mu,
$$

of the compactly supported smooth sections with respect to the norm; it is a real or complex Hilbert space, depending on whether the fibres are real or Hermitian, by the standard completeness of the $L^2$ spaces of *Measure Theory and Integration*, applied fibrewise. The inner product extends the pairing $\langle u,v\rangle_{L^2}=\int_M\langle u,v\rangle\,d\mu$ of the previous entry, and $L^2(M;E)$ is the space on which the adjoint is taken.

### Differential Operators as Unbounded Operators

**Definition.** A differential operator $P : \Gamma(E)\to\Gamma(F)$ of order at most $k$ with smooth coefficients, together with a choice of **domain** $\mathcal{D}\subseteq L^2(M;E)$, defines an unbounded operator, also written $P$, with

$$
\mathrm{dom}(P) = \mathcal{D}, \qquad Pu = P u \ \text{for } u \in \mathcal{D}.
$$

The standard choices are the **minimal domain** $\mathcal{D}_{\min} = C_c^\infty(M;E) = \Gamma_c(E)$, dense in $L^2$, and the **maximal domain**

$$
\mathcal{D}_{\max} = \{u \in L^2(M;E) : Pu \in L^2(M;F) \ \text{in the sense of distributions}\},
$$

which contains $\mathcal{D}_{\min}$ and is the largest possible domain on which $P$ maps into $L^2$. The operator with the minimal domain is densely defined; that with the maximal domain contains all the weak solutions of the equation. The distinction between the domains is the whole content of the global theory: the same differential expression defines many operators, one for each domain between the minimal and the maximal, and the adjoint depends on the choice.

## The Adjoint Operator

### The Definition

**Definition.** Let $T : L^2(M;E)\supseteq\mathrm{dom}(T)\to L^2(M;F)$ be a densely defined unbounded operator. Its **adjoint** $T^*$ is defined by

$$
\mathrm{dom}(T^*) = \bigl\{v \in L^2(M;F) : \exists\, w \in L^2(M;E) \ \text{with } \langle Tu,v\rangle_{L^2}=\langle u,w\rangle_{L^2} \ \forall u \in \mathrm{dom}(T)\bigr\},
$$

and $T^*v = w$ for the unique such $w$; the uniqueness is the density of $\mathrm{dom}(T)$, and the existence is the Riesz representation of the bounded functional $u\mapsto\langle Tu,v\rangle_{L^2}$ when it is bounded.

**Theorem (existence and closedness).** If $T$ is densely defined, its adjoint $T^*$ is a closed operator, and $T$ is closable with closure $\bar T = (T^*)^*$. In particular the adjoint of the differential operator with the minimal domain is a closed operator, and the adjoint of the maximal domain operator is the closure of the minimal one.

*Proof.* The existence of $w$ when the functional is bounded is the Riesz representation theorem of *Hilbert Spaces*; the graph of $T^*$ is the annihilator of the graph of $T$ under the pairing $\langle(u,Tu),(v,w)\rangle = \langle u,w\rangle - \langle Tu,v\rangle$, and the annihilator of a subspace is closed, so $T^*$ is closed. The identity $\bar T=(T^*)^*$ is the standard double-commutant argument: the graph of $(T^*)^*$ is the closure of the graph of $T$ when $T$ is closable, and a densely defined operator with closed adjoint is closable.

### The Boundary Conditions and the Formal Adjoint

**Theorem (the formal and the global adjoint).** Let $P$ be a differential operator and let $P^{\dagger}$ be its formal adjoint, defined by the pairing on $\Gamma_c(F)$ with $P$ acting on $\Gamma_c(E)$. Then the adjoint of $P$ with the minimal domain contains the operator $P^{\dagger}$ with the minimal domain,

$$
P_{\min}^{\ *} \supseteq P^{\dagger}_{\min},
$$

with equality if and only if the boundary term of Green's formula vanishes for all compactly supported sections, which holds automatically when $M$ is closed; and the density of the maximal domain makes the maximal operator the adjoint of $P^{\dagger}_{\min}$,

$$
(P^{\dagger}_{\min})^* = P_{\max}, \qquad (P_{\min})^* = P^{\dagger}_{\max},
$$

on a manifold without boundary, up to the closures. On a manifold with boundary the maximal domain is cut down by the boundary conditions, and the adjoint of a boundary-value problem is another boundary-value problem, whose boundary conditions are read from the Green formula.

*Proof.* For $u,v\in\Gamma_c$ the integration by parts gives $\langle Pu,v\rangle_{L^2}=\langle u,P^{\dagger}v\rangle_{L^2}$ with no boundary term, so $P^{\dagger}$ acts on $\Gamma_c(F)$ as a restriction of $P^*_{\min}$. Conversely, if $v\in\mathrm{dom}(P^*_{\min})$ with $P^*v=w$, then $w-P^{\dagger}v$ is a distribution vanishing on the test sections $\Gamma_c(E)$, hence $w=P^{\dagger}v$ in the distribution sense. The characterisation of the maximal domain of $P$ as the domain of the adjoint of $P^{\dagger}_{\min}$ is the standard computation with the distributional pairing: the condition $\langle Pu,v\rangle=\langle u,w\rangle$ for all test $u$ says exactly that the distribution $P^{\dagger}v$ is represented by the $L^2$ function $w$, which is the definition of the maximal domain. The boundary case reduces to the vanishing of the boundary term of Green's formula, which is the statement that the adjoint boundary conditions are the orthogonal complement of the given ones.

## Closedness, Symmetry and Self-Adjointness

**Definition.** An operator $T$ is **symmetric** if $\langle Tu,v\rangle=\langle u,Tv\rangle$ for all $u,v\in\mathrm{dom}(T)$, equivalently $T\subseteq T^*$; it is **self-adjoint** if $T=T^*$, which includes the equality of the domains; it is **essentially self-adjoint** if its closure is self-adjoint, or equivalently if $T$ has a unique self-adjoint extension. A symmetric operator is closable and its closure is symmetric.

**Theorem (the criterion of self-adjointness).** A symmetric operator $T$ is self-adjoint if and only if $\ker(T^*\pm i)=0$; more precisely, with the **deficiency subspaces** $K_\pm=\ker(T^*\mp i)$ and the **deficiency indices** $n_\pm=\dim K_\pm$, the operator is essentially self-adjoint if and only if $n_+=n_-=0$, it has self-adjoint extensions if and only if $n_+=n_-$, and the self-adjoint extensions are parametrised by the partial isometries $K_+\to K_-$.

*Proof.* This is the von Neumann theory of the deficiency indices of a symmetric operator, proved in *Unbounded Operators and Spectral Measures*; the criterion $\ker(T^*\pm i)=0$ for self-adjointness is the special case of the projection onto the eigenspaces of the Cayley transform, whose domain is all of the Hilbert space exactly when the two deficiency indices vanish. The parametrisation of the extensions is the parametrisation of the isometric isomorphisms between the deficiency subspaces, and the boundary conditions of the previous section are the differential-geometric realisation of these extensions.

**Proposition (the variational characterisation of the spectrum).** Let $T$ be self-adjoint and bounded below, with the associated quadratic form $Q(u)=\langle Tu,u\rangle$ on $\mathrm{dom}(T)$. Then the bottom of the spectrum is

$$
\inf\sigma(T) = \inf_{u\neq0}\frac{Q(u)}{\lVert u\rVert_{L^2}^2},
$$

the **Rayleigh quotient**; if $T$ has compact resolvent, its spectrum is discrete, $\lambda_1\le\lambda_2\le\cdots$, and the eigenvalues are characterised by the min–max principle.

*Proof.* The min–max principle and the Rayleigh quotient are the spectral theorem for a self-adjoint operator bounded below, as in *Unbounded Operators and Spectral Measures*; the compactness of the resolvent makes the spectrum discrete and the eigenvalues accumulate only at infinity.

## The Laplace-Type Operators

**Theorem.** Let $P$ be a second-order differential operator with the formal self-adjointness $P=P^{\dagger}$ and the ellipticity of its principal symbol, and suppose $P$ is bounded below on the compactly supported sections, $Q(u)\ge -c\lVert u\rVert^2$. Then the operator $P$ with the minimal domain is symmetric and bounded below, and it has a unique self-adjoint extension bounded below, the **Friedrichs extension**; its domain is the closure of the minimal domain in the **form norm** $\lVert u\rVert_Q^2=Q(u)+(c+1)\lVert u\rVert^2$, and on a closed manifold the extension is self-adjoint with domain the Sobolev space $H^2(M;E)$ intersected with the boundary conditions.

*Proof.* The construction of the Friedrichs extension uses the quadratic form: the form $Q$ is closed and bounded below on its domain with the form norm, and the representation theorem for closed forms produces the self-adjoint operator associated with the form; this is the **Friedrichs extension** of *Unbounded Operators and Spectral Measures* and *Pseudodifferential Operators*. The identifications of the domain with the Sobolev space and the boundary conditions follow from elliptic regularity: a distribution in the domain of a self-adjoint elliptic operator is a Sobolev section of the corresponding order.

**Example (the Laplace–Beltrami operator).** On a closed Riemannian manifold the Laplace–Beltrami operator $\Delta$ is formally self-adjoint and nonnegative on the compactly supported sections, $Q(\alpha)=\lVert d\alpha\rVert_{L^2}^2\ge0$ on the forms of the operator group, so it is essentially self-adjoint and its self-adjoint closure has a discrete spectrum $0=\lambda_1\le\lambda_2\le\cdots$; the eigenforms of eigenvalue zero are the **harmonic forms**, $\ker\Delta=\ker d\cap\ker\delta$, and this is the Hodge theory of the de Rham complex on a compact manifold, the content of *Differential Forms and Stokes' Theorem* and *Sheaves and the de Rham Complex* in this Part. On a manifold with boundary the same operator with the minimal domain is symmetric but not self-adjoint, and its self-adjoint extensions are the boundary-value problems — the Dirichlet, the Neumann and the mixed conditions — whose deficiency indices are computed from the boundary term.

**Example (the connection Laplacian).** The connection Laplacian $\nabla^*\nabla$ of *Hermitian Connections and the Adjoint* is formally self-adjoint and nonnegative, with the same theory; on a closed manifold it is self-adjoint with discrete spectrum, and its kernel is the space of parallel sections.

## Summary

The $L^2$ adjoint of a differential operator is its adjoint as an unbounded operator on the Hilbert space of square-integrable sections. It exists and is closed as soon as the operator is densely defined; the minimal and maximal domains are the two extremes, and the adjoint of one is the other up to the closures. The formal adjoint is a restriction of the global adjoint on the smooth compactly supported sections, and the two agree exactly when the boundary term of Green's formula vanishes, which holds on a closed manifold and fails on a manifold with boundary, where the difference is the choice of boundary conditions.

A symmetric operator has $T\subseteq T^*$; it is self-adjoint when the domains are equal, and essentially self-adjoint when the deficiency indices $n_+=n_-=0$ vanish. The self-adjoint extensions are parametrised by the deficiency subspaces, and the Rayleigh quotient and the min–max principle characterise the spectrum of a self-adjoint operator bounded below. The Laplace-type operators — the Laplace–Beltrami operator of the de Rham complex, the connection Laplacian, the Laplace operators of a Hermitian manifold — are symmetric on the compactly supported sections, bounded below and elliptic, and their Friedrichs extension is the self-adjoint operator with domain the corresponding Sobolev space and boundary conditions; the harmonic forms and the Hodge decomposition of the compact case are the spectral shadow of this construction.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $L^2(M;E)$, $\lVert u\rVert_{L^2}^2=\int_M\langle u,u\rangle\,d\mu$ | Hilbert space of square-integrable sections |
| $\mathrm{dom}(P)$, minimal $\Gamma_c(E)$, maximal $\{u : Pu\in L^2\}$ | The choice of domain of a differential operator |
| $T^*$, $\mathrm{dom}(T^*)$ | Adjoint of an unbounded operator |
| $T^*$ closed, $\bar T=(T^*)^*$ | Closedness of the adjoint; the closure of a closable operator |
| $P^{\dagger}$ | Formal adjoint of the previous entry |
| $P_{\min}$, $P_{\max}$; $(P^{\dagger}_{\min})^*=P_{\max}$ | The adjoint pair of the minimal and maximal operators |
| Boundary term of Green's formula | The obstruction to the equality of the formal and global adjoints |
| Symmetric, self-adjoint, essentially self-adjoint | $T\subseteq T^*$; $T=T^*$; $\bar T=\bar T^*$ |
| Deficiency indices $n_\pm=\dim\ker(T^*\mp i)$ | Essential self-adjointness iff $n_+=n_-=0$ |
| $Q(u)=\langle Tu,u\rangle$, Rayleigh quotient | Variational characterisation of the bottom of the spectrum |
| Friedrichs extension, form norm | The self-adjoint extension of a bounded-below symmetric operator |
| $\ker\Delta=\ker d\cap\ker\delta$, Hodge theory | Harmonic forms of a compact Riemannian manifold |

## Further Reading

- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics*, vol. I and II (Academic Press, 1972, 1975), for the unbounded operators, the adjoints, the deficiency indices and the spectral theorem.
- Michael E. Taylor, *Partial Differential Equations*, vol. I and II (Springer, 2nd ed. 2011), for the $L^2$ theory, the Sobolev spaces, the elliptic regularity and the self-adjoint extensions.
- David Gilbarg and Neil S. Trudinger, *Elliptic Partial Differential Equations of Second Order* (Springer, 2001), for the boundary-value problems and their adjoints.
- John M. Lee, *Introduction to Riemannian Manifolds*, 2nd ed. (Springer, 2018), for the Laplace–Beltrami operator on a compact manifold and the Hodge theory.
- Tosio Kato, *Perturbation Theory for Linear Operators* (Springer, 1995), for the self-adjointness criteria, the quadratic forms and the Friedrichs extension.
