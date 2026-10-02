
# __Involutions of the Twistor Operator__

## Introduction

The twistor operator $\mathcal{T}=\pi\circ\nabla^{\mathcal{S}}$ of *The Twistor Operator* is built from the covariant derivative and the orthogonal projection $\pi$ onto the kernel of the Clifford contraction; it is a first-order operator $\Gamma(\mathcal{S})\to\Gamma(T^*M\otimes\mathcal{S})$ with the twistor equation $\mathcal{T}\sigma=0$ as its kernel equation. The spinor bundle carries canonical **involutions** — the chirality $\Pi$, the volume element $\omega$ in odd dimension, and the anti-linear charge conjugation $\kappa$ — and each of them either commutes or anticommutes with the Clifford multiplication by a vector. The article computes the effect of that sign on the twistor operator, and the outcome is uniform: **the projection is quadratic in the Clifford multiplication**, so all three involutions commute with $\mathcal{T}$, and the kernel of the twistor operator decomposes into their joint eigenspaces. The commuting of the anti-linear involution is the **conjugate symmetry** of the operator, and it produces the Hermitian pairing on the kernel whose Hermitian character is the **self-adjointness** statement of the article.

**The boundaries.** The operator, its symbol and its conformal covariance are *The Twistor Operator* and *The Penrose Operator*; the fibre form, the charge conjugation and the reality structure are *Hermitian Clifford Structures* and *Spin Geometry*; the formal adjoint operator, the identity $\nabla^*\nabla=\mathcal{T}^*\mathcal{T}+\frac1nD^2$ and the twistor equation as an equation for $\nabla\sigma$ are *The Adjoint of the Twistor Operator*, the next entry of the group, and are quoted here. The analytic completions of the eigenspaces and the spectral theory belong to Part III and are named only. The body is a Riemannian spin manifold with the fibre form $h$, $c(v)^*=-c(v)$, and the operator $\mathcal{T}$ of *The Twistor Operator*.

## The Involutions of the Spinor Bundle

**Definition.** The **chirality** is the endomorphism $\Pi$ of the spinor bundle which in even dimension $n=2m$ is the Clifford product $\Pi=c(e_1)\cdots c(e_n)$ of a local orthonormal frame, normalised by a scalar so that $\Pi^2=\mathrm{id}$; the **volume involution** in odd dimension $n=2m+1$ is $\omega=c(e_1)\cdots c(e_n)$; the **charge conjugation** $\kappa : \mathcal{S}\to\mathcal{S}$ is the anti-linear map induced by the conjugation of the spin representation with respect to the fibre form $h$ of *Hermitian Clifford Structures*.

**Proposition.** The three maps satisfy the following, pointwise and globally.

**(a)** $\Pi^2=\mathrm{id}$ and $\Pi$ is self-adjoint and unitary for $h$; in odd dimension $\omega^2=\mathrm{id}$ and $\omega$ is self-adjoint and unitary.

**(b)** $\Pi c(v)=-c(v)\Pi$ in even dimension; $\omega c(v)=(-1)^{m}c(v)\omega$ in dimension $n=2m+1$.

**(c)** $\kappa$ is anti-linear, $\kappa^2=\pm\mathrm{id}$ according to $n\bmod 8$, and $c(v)\kappa=\kappa c(v)$ for a real vector $v$.

**(d)** $\Pi,\omega,\kappa$ are parallel for the spin connection, hence are global sections of the endomorphism bundle with $\nabla\Pi=\nabla\omega=\nabla\kappa=0$.

**Proof.** (a) is the standard computation of the chirality from the Clifford relations and the reality of the fibrewise form; (b) moving a vector past the product of $n$ vectors changes the number of sign changes by $n-1$, and the normalisation gives the stated signs; (c) the conjugation is anti-linear by construction and squares to a sign recorded by the real spinor type, and it commutes with $c(v)$ because the fibrewise form is invariant; (d) the spin connection is the lift of the Levi-Civita connection and the three endomorphisms are defined by the parallel Clifford structure, so they are annihilated by it. The sign table is that of *Spin Geometry*.

## Intertwining with the Twistor Operator

**Theorem.** The twistor operator commutes with each of the three involutions:

$$
\mathcal{T}\Pi=\Pi\mathcal{T} , \qquad \mathcal{T}\omega=\omega\mathcal{T} , \qquad \mathcal{T}\kappa=\kappa\mathcal{T} .
$$

**Proof.** Write $\mathcal{T}=\pi\circ\nabla$ with $\pi=\mathrm{id}-\frac1nc^*c$ the orthogonal projection onto $\ker c$ and $c^*$ the adjoint of the contraction, of *The Twistor Operator*. Since $\Pi$ anticommutes with every $c(v)$ by (b) of the previous proposition, it commutes with $c^*$, hence with the product $c^*c$ and with $\pi$; and $\Pi$ commutes with $\nabla$ by parallelness, so $\mathcal{T}\Pi=\pi\nabla\Pi=\pi\Pi\nabla=\Pi\pi\nabla=\Pi\mathcal{T}$. The same computation with $\omega$ uses $\omega c(v)=(-1)^mc(v)\omega$ and the antisymmetry of the sign in the two factors of $c^*c$, which cancels; the computation with $\kappa$ uses its anti-linearity and its commutation with $c(v)$ and with $\nabla$, so $\mathcal{T}\kappa=\pi\nabla\kappa=\pi\kappa\nabla=\kappa\pi\nabla=\kappa\mathcal{T}$.

**Remark (why no sign survives).** For the individual Clifford multiplications the signs of $\Pi$ and $\omega$ are non-trivial, and they are the content of the chirality splitting of the spinor bundle; for the twistor operator the two factors of $c^*c$ carry opposite signs, cancel, and the projection is in fact a combination of the identity and an even element of the Clifford algebra. The uniform commutation is therefore not an accident of the signs but the statement that $\mathcal{T}$ is built from **even** elements of the Clifford algebra, and it holds for every involution $\varepsilon$ with $\varepsilon c(v)=\lambda(v)c(v)\varepsilon$.

**Corollary.** The kernel of $\mathcal{T}$ is stable under $\Pi$, $\omega$ and $\kappa$; since $\kappa$ is anti-linear, its kernel is a real structure of the solution space, and the space of twistor spinors is a module over the algebra generated by $\Pi,\omega$ and $\kappa$.

**Proof.** An intertwining operator maps solutions to solutions; the anti-linearity of $\kappa$ makes the fixed set of $\kappa^2$ a real form of the solution space in the sense of *Hermitian Clifford Structures*; the module statement is the associativity of the composition.

## The Joint Decomposition of the Kernel

**Proposition.** The space $\mathcal{K}=\ker\mathcal{T}$ decomposes into the joint eigenspaces of the commuting involutions $\Pi$ and $\omega$ (the relevant one according to the parity of $n$), and the charge conjugation $\kappa$ pairs the eigenspaces according to the reality type of the spinor module:

$$
\mathcal{K}=\bigoplus_{\varepsilon=\pm1}\mathcal{K}^{\varepsilon} , \qquad \Pi\,\mathcal{K}^{\varepsilon}=\varepsilon\mathcal{K}^{\varepsilon} , \qquad \kappa : \mathcal{K}^{\varepsilon}\longrightarrow \mathcal{K}^{\varepsilon} ,
$$

with $\kappa$ acting anti-linearly on each summand.

**Proof.** Commuting involutions are simultaneously diagonalisable in characteristic not two, which gives the decomposition; $\kappa$ commutes with $\Pi$ (it commutes with $c(v)$ and hence with the volume element), so it preserves each summand; its anti-linearity is (c) above.

**Theorem (quoted).** In even dimension the twistor operator splits as

$$
\mathcal{T} = \mathcal{T}^+\oplus\mathcal{T}^- : \Gamma(\mathcal{S}^\pm)\longrightarrow\Gamma(T^*M\otimes\mathcal{S}^\pm) ,
$$

each summand is itself a twistor operator, and the twistor spinors of *The Penrose Operator* satisfy $D^2\sigma=\frac{n}{4(n-1)}\operatorname{scal}\sigma$; the two chiral components of a twistor spinor are independent, and on an Einstein manifold the twistor equation is equivalent to the Killing spinor equation with the appropriate constant.

**Proof sketch.** The splitting is the commutation with $\Pi$; the scalar identity follows from $\mathcal{T}\sigma=0$ combined with the identity $\nabla^*\nabla=\mathcal{T}^*\mathcal{T}+\frac1nD^2$ and the Lichnerowicz formula, both of *The Adjoint of the Twistor Operator* and *The Spinor Operator*; the Einstein equivalence is the standard statement quoted from the twistor-spinor literature.

## Conjugate Symmetry and Self-Adjointness

**Definition.** The **conjugate symmetry** of the twistor operator is the identity $\mathcal{T}\kappa=\kappa\mathcal{T}$: the operator is real for the charge conjugation, so it maps the conjugate spinor of a solution to the conjugate spinor of the solution.

**Proposition (the Hermitian pairing of the kernel).** The restriction of the pointwise Hermitian form $h$ of *Hermitian Clifford Structures* to the kernel of $\mathcal{T}$,

$$
\Sigma(\sigma,\tau) = \int_M h(\sigma,\tau)\,\mu_g ,
$$

is a Hermitian form on $\mathcal{K}$, conjugate-symmetric, and the current

$$
X_{\sigma,\tau} = \sum_i h(\sigma,c(e_i)\tau)\,\theta^i
$$

of *The Penrose Operator* satisfies $\operatorname{div}X_{\sigma,\tau}=0$ for twistor spinors $\sigma,\tau$, so the pairing is independent of the conformal factor in the sense recorded there; the eigenspaces $\mathcal{K}^\pm$ are orthogonal for $\Sigma$, and $\Sigma$ is non-degenerate exactly where the reality type of the spinor module permits it.

**Proof.** The Hermitian character is (a) of *Hermitian Clifford Structures*; the divergence identity is the pairing of the twistor equation with the conjugate equation, which is the statement of the invariance of the current in *The Penrose Operator*; the orthogonality of the chiral summands is the self-adjointness of $\Pi$; the non-degeneracy statement is the restriction of the fibre form, and its failure in the quaternionic type is the reason the pairing is indefinite there.

**Remark (the sense of self-adjointness).** The twistor operator itself is not a self-adjoint operator on a single bundle: it maps $\Gamma(\mathcal{S})$ to $\Gamma(T^*M\otimes\mathcal{S})$, and its formal adjoint is the operator of *The Adjoint of the Twistor Operator*. What is self-adjoint is the **twistor Laplacian** $\mathcal{T}^*\mathcal{T}$, a non-negative operator on $\Gamma(\mathcal{S})$, and its kernel is that of $\mathcal{T}$; the conjugate symmetry of $\mathcal{T}$ is what makes $\mathcal{T}^*\mathcal{T}$ a real operator and the pairing $\Sigma$ Hermitian rather than merely sesquilinear. The analytic theory of $\mathcal{T}^*\mathcal{T}$ belongs to Part III.

## Summary

The spinor bundle carries the commuting involutions $\Pi$ (chirality), $\omega$ (volume involution) and the anti-linear charge conjugation $\kappa$; each anticommutes or commutes with the Clifford multiplication by a vector, but because the twistor operator $\mathcal{T}=\pi\circ\nabla$ is quadratic in the Clifford multiplication through $\pi=\mathrm{id}-\frac1nc^*c$, **all three commute with** $\mathcal{T}$: $\mathcal{T}\Pi=\Pi\mathcal{T}$, $\mathcal{T}\omega=\omega\mathcal{T}$, $\mathcal{T}\kappa=\kappa\mathcal{T}$. The kernel decomposes into the joint eigenspaces of the commuting involutions, the anti-linear $\kappa$ acting on each summand and giving a real structure; in even dimension the twistor operator splits chirally, $\mathcal{T}=\mathcal{T}^+\oplus\mathcal{T}^-$. The **conjugate symmetry** $\mathcal{T}\kappa=\kappa\mathcal{T}$ makes the pointwise Hermitian form restricted to the kernel a Hermitian pairing with the conserved current $X_{\sigma,\tau}$ of *The Penrose Operator*, and the **self-adjointness** that survives is that of the twistor Laplacian $\mathcal{T}^*\mathcal{T}$, whose kernel is the space of twistor spinors. The formal adjoint is *The Adjoint of the Twistor Operator*; the form and the charge conjugation are *Hermitian Clifford Structures* and *Spin Geometry*; the analytic theory is Part III.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{T}=\pi\circ\nabla$, $\pi=\mathrm{id}-\frac1nc^*c$ | Twistor operator and the projection onto $\ker c$ |
| $\Pi$ | Chirality; $\Pi^2=\mathrm{id}$, $\Pi c(v)=-c(v)\Pi$ |
| $\omega$ | Volume involution in odd dimension |
| $\kappa$ | Anti-linear charge conjugation; $c(v)\kappa=\kappa c(v)$ |
| $\mathcal{T}\Pi=\Pi\mathcal{T}$, $\mathcal{T}\omega=\omega\mathcal{T}$, $\mathcal{T}\kappa=\kappa\mathcal{T}$ | The intertwining identities |
| $\mathcal{K}=\ker\mathcal{T}$ | Space of twistor spinors |
| $\mathcal{K}^\pm$ | Joint eigenspaces of the commuting involutions |
| $X_{\sigma,\tau}=\sum_ih(\sigma,c(e_i)\tau)\theta^i$ | Conserved current of *The Penrose Operator* |
| $\Sigma(\sigma,\tau)=\int_Mh(\sigma,\tau)\mu_g$ | Hermitian pairing of the kernel |

## Further Reading

- Helga Baum, Thomas Friedrich, Ralf Grunewald and Ines Kath, *Twistors and Killing Spinors on Riemannian Manifolds* (Teubner, 1991), for the chirality splitting of the twistor operator, the charge conjugation and the conjugate symmetry.
- Thomas Friedrich, *Dirac Operators in Riemannian Geometry* (American Mathematical Society, 2000), for the twistor equation, the Lichnerowicz formula and the scalar identity for twistor spinors.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the chirality, the volume element, the charge conjugation and their sign tables.
- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time, Volume 2* (Cambridge University Press, 1986), for the conjugate symmetry of the twistor equation and the conserved currents.
