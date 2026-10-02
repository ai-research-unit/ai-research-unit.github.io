
# __The Adjoint of the Signature Operator__

## Introduction

An operator on the differential forms has a formal adjoint with respect to the metric inner product, and the signature operator $D=d+d^{*}$ is its own adjoint: the adjoint of the exterior derivative is the codifferential, and the adjoint of the codifferential is the exterior derivative, so $D^{*}=D$. The self-adjointness is what makes the operator an index-theoretic object of the simplest kind — the index of its positive half is the difference of the dimensions of the two kernels, and it is the signature of the Hermitian form that the inner product and the chirality define on the kernel. The Hodge star is the isometry that intertwines the operator with the adjoint, the chiral halves are mutually adjoint, and the whole index theory of the signature is the spectral theory of a self-adjoint operator and its order-two symmetry.

The article treats the metric inner product and the formal adjoint, the self-adjointness of the signature operator, the adjoint of its chiral halves and the resulting form of the index, the role of the Hodge star as the intertwining isometry, and the interpretation of the index as the signature of the Hermitian form on the kernel. The index itself is that of *The Signature Operator*; the harmonic forms are those of *The Hodge Laplacian*; the action of an involution on a pairing and the signature of the fixed part are those of *Hermitian Pairings on a Topological Space*; and the general adjoint of a differential operator is that of the Part III article *The Formal Adjoint of a Differential Operator* and *The L2 Adjoint of a Differential Operator*.

The prerequisites are *The Formal Adjoint of a Differential Operator* and *The L2 Adjoint of a Differential Operator* for the formal and $L^{2}$ adjoints and their domains; *The Codifferential* for the adjoint of $d$; *The Hodge Laplacian* for the Laplacian and the harmonic forms; *The Signature Operator* for the operator, its chirality and the signature theorem; *Hermitian Pairings on a Topological Space* and the Part I articles *Bilinear Forms* and *Indefinite Inner Product Spaces* for the Hermitian and bilinear forms and the signature; and *Spectral Theory* and the self-adjoint operator theory of Part III for the Fredholm alternative. The metric is chosen, and the adjoint is taken with respect to it; the analytic domain theory belongs to Part III and is cited. No physics is invoked.

## The Inner Product and the Formal Adjoint

Let $(M,g)$ be a closed oriented Riemannian manifold of dimension $n$, with $\Omega^{k}(M)$ the smooth complexified $k$-forms, with the Hodge star $\star$ and the $L^{2}$ inner product

$$
(\alpha,\beta)=\int_{M}\alpha\wedge\star\bar\beta ,
$$

which is a positive definite Hermitian form on $\Omega^{k}(M)$ and makes the completion $L^{2}\Omega^{k}(M)$ a Hilbert space.

**Definition.** The **formal adjoint** of a differential operator $P:\Omega^{k}\to\Omega^{l}$ is the operator $P^{*}:\Omega^{l}\to\Omega^{k}$ satisfying

$$
(P\alpha,\beta)=(\alpha,P^{*}\beta)
$$

for all smooth forms, the identity of integration by parts; the **$L^{2}$ adjoint** is the corresponding adjoint of the closed densely defined operator on the Hilbert space, whose domain is the set of $\beta$ for which the functional $\alpha\mapsto(P\alpha,\beta)$ is bounded.

**Theorem.** For the exterior derivative $d:\Omega^{k}\to\Omega^{k+1}$ the formal adjoint is the **codifferential** $d^{*}:\Omega^{k+1}\to\Omega^{k}$,

$$
(d\alpha,\beta)=(\alpha,d^{*}\beta),\qquad
d^{*}=(-1)^{k}\star^{-1}d\star
$$

up to the degree and dimension sign, and the formal adjoints of $d$ and $d^{*}$ are mutual: $(d^{*})^{*}=d$ on the appropriate domains. On a closed manifold the formal adjoint and the $L^{2}$ adjoint coincide on the smooth forms.

**Proof.** The adjointness is integration by parts: $\int d(\alpha\wedge\star\bar\beta)=\int d\alpha\wedge\star\bar\beta+(-1)^{k}\int\alpha\wedge d\star\bar\beta$, and the left-hand side vanishes on a closed manifold by Stokes' theorem, so the two boundary-free terms are equal up to sign, and the identification of the result with $d^{*}\beta$ gives the formula; the mutual adjointness follows by applying the identity twice. The equality of the formal and $L^{2}$ adjoints on smooth forms is the density of the smooth forms and the ellipticity. $\square$

## Self-Adjointness of the Signature Operator

**Definition.** The **signature operator** is $D=d+d^{*}:\Omega^{\bullet}(M)\to\Omega^{\bullet}(M)$, a formally self-adjoint elliptic operator of order one, with the chirality $\tau=i^{k(k-1)+m}\star$ and the splitting $\Omega^{\pm}(M)$ of its eigenspaces when $n=2m$ is even.

**Theorem.** The signature operator is formally self-adjoint, $D^{*}=D$, and on the closed manifold it is self-adjoint as an unbounded operator on $L^{2}\Omega^{\bullet}(M)$ with domain the Sobolev space of forms in $H^{1}$; its spectrum is real and discrete, it has a complete orthonormal basis of eigenforms, and the Fredholm alternative holds at $\lambda=0$.

**Proof.** The adjoint of $d+d^{*}$ is $d^{*}+d=D$ by the mutual adjointness of $d$ and $d^{*}$; the self-adjointness as a closed operator follows from the ellipticity and the completeness, and the discreteness of the spectrum is the compactness of the resolvent of an elliptic self-adjoint operator on a closed manifold. The analytic domain theory is that of *The L2 Adjoint of a Differential Operator* and of the spectral theory of Part III. $\square$

**Corollary (the chiral halves).** On an even-dimensional closed manifold the operator is odd for the chirality, so it restricts to a pair of mutually adjoint operators

$$
D^{+}:\Omega^{+}(M)\to\Omega^{-}(M),\qquad
(D^{+})^{*}=D^{-}:\Omega^{-}(M)\to\Omega^{+}(M),
$$

and the **cokernel of $D^{+}$** is the kernel of $D^{-}$,

$$
\operatorname{coker}D^{+}=\ker(D^{+})^{*}=\ker D^{-} .
$$

Both $D^{\pm}$ are Fredholm of index

$$
\operatorname{ind}D^{+}=\dim\ker D^{+}-\dim\ker D^{-}=b_{+}-b_{-}=\sigma(M),
$$

the signature of the manifold, by *The Signature Operator*.

**Proof.** The oddness of $D$ was established with the chirality, and the adjoint of an odd self-adjoint operator has the stated chiral form; the cokernel of $D^{+}$ is the kernel of its adjoint $D^{-}$ by the Fredholm alternative, and the index is the difference of the two kernel dimensions; the identification with the signature is the theorem of the signature article. $\square$

## The Adjoint and the Chirality

**Theorem.** The adjoint operation and the chirality are related by

$$
(D^{+})^{*}=D^{-},\qquad
\tau D \tau^{-1}=-D,\qquad
\tau (D^{+})^{*}\tau^{-1}=D^{+},
$$

so that conjugation by the chirality sends the positive half of the operator to the negative of the adjoint of its own negative half; equivalently, the chirality exchanges the two halves of the self-adjoint operator and conjugates the index problem into its dual. The self-adjointness is therefore the statement that the index of the positive half and the index of the negative half are opposite, $\operatorname{ind}D^{+}=-\operatorname{ind}D^{-}$, so that the index of the self-adjoint operator is well defined as the signature, with no dependence on the choice of the half.

**Proof.** The relation $\tau D\tau^{-1}=-D$ was proved in *The Signature Operator*; multiplying it by $\tau$ gives $D\tau=-\tau D$, and the restriction to the halves gives $D^{+}\tau=\tau D^{-}$ and $D^{-}\tau=\tau D^{+}$, so conjugation by $\tau$ identifies the two adjoint operators and their index difference is the signature. $\square$

**Corollary.** The index of the signature operator is the trace of the chirality on the kernel,

$$
\sigma(M)=\operatorname{ind}D^{+}=\operatorname{tr}\bigl(\tau\mid\ker D\bigr),
$$

the difference of the dimensions of the $\pm1$ eigenspaces of $\tau$ on the harmonic forms; the index is thus the **signature** of the involution $\tau$ on the finite-dimensional kernel, in the sense of *Hermitian Pairings on a Topological Space*. This is the operator-theoretic form of the statement that the signature is the signature of the intersection form.

## The Star as the Intertwining Isometry

**Theorem.** The chirality is the normalized Hodge star, $\tau=i^{k(k-1)+m}\star$ on $\Omega^{k}$ for $n=2m$, and it satisfies

$$
\tau^{2}=\mathrm{id},\qquad
\tau d\,\tau^{-1}=-d^{*},\qquad
\tau D\,\tau^{-1}=-D ,
$$

so the star, normalized by the degree-dependent phase, intertwines the exterior derivative with its adjoint; the phase is exactly what absorbs the degree dependence of the Hodge identity $d^{*}=\pm\star d\star$, and the normalized star is the isometry $(\tau\alpha,\tau\beta)=(\alpha,\beta)$ that conjugates the operator to its adjoint. Concretely, on the middle forms of a $4k$-manifold the phase is $1$, the chirality is the star itself, and the Poincaré dual of a harmonic anti-self-dual form is a harmonic self-dual form, with the pairing between them the intersection form.

**Proof.** The square and the conjugation of $d$ are those of *The Signature Operator*; the phase in $\tau$ is chosen so that the degree-dependent sign of $\star d\star^{-1}$ is normalized to $-1$, and $\tau$ is unitary because the star is, $(\star\alpha,\star\beta)=(\alpha,\beta)$. The concrete statement on the middle forms is that $\tau=\star$ there, with $\star^2=1$, and Poincaré duality for the harmonic forms is that of *The Hodge Laplacian* and *Hermitian Pairings on a Topological Space*. $\square$

**Remark.** The star is the object that makes the index of the signature operator a **Hermitian** index: it is the isometry that computes the adjoint, and the chirality it defines splits the kernel into the positive and negative definite parts of the intersection form. Without the metric there is no star, hence no adjoint and no index; the operator, its adjoint and its index are all metric objects, and the theorem that the index is the signature is the statement that the metric cancels out of the answer.

## The Index as the Signature of the Kernel Pairing

**Theorem.** Let $V=\ker D$ be the finite-dimensional kernel of the signature operator on a closed oriented manifold of dimension $4k$, and let $(\cdot,\cdot)$ be the metric inner product and $Q(\alpha,\beta)=\int_{M}\alpha\wedge\beta$ the intersection form, related by $Q(\alpha,\beta)=(\alpha,\star\beta)$ on the middle forms. Then

- the metric form $(\cdot,\cdot)$ is positive definite on $V$, and
- the chirality acts on $V$ with the trace the index, and the non-middle harmonic forms cancel in that trace: the chirality maps $\mathcal{H}^{j}$ to $\mathcal{H}^{n-j}$, so its trace on the sum $\mathcal{H}^{j}\oplus\mathcal{H}^{n-j}$ is $0$ for $j\neq n-j$, and only the middle harmonic forms contribute, with

$$
\operatorname{tr}(\tau\mid V)=\operatorname{tr}(\tau\mid\mathcal{H}^{2k})=b_{+}-b_{-}=\sigma(M),
$$

the **signature** of the middle intersection form.

The index of the self-adjoint operator is therefore the signature of the restriction of the Hermitian pairing to the middle part of the kernel: the positive definite metric form and the indefinite intersection form differ by the star, $Q(\alpha,\beta)=(\alpha,\star\beta)$, and the index is the difference of the dimensions of the two star eigenspaces on the middle harmonic forms, the non-middle forms contributing nothing.

**Proof.** The kernel of $D$ consists of the harmonic forms, on which $d$ and $d^{*}$ vanish; the metric form is positive definite there, and the intersection form on the middle degree is nondegenerate by Poincaré duality; the star preserves the middle forms and squares to $+1$ there, so it splits them into the self-dual and anti-self-dual parts, the positive and negative definite parts of $Q$, and their dimensions differ by $\sigma(M)$. For $j\neq n-j$ the chirality exchanges $\mathcal{H}^{j}$ and $\mathcal{H}^{n-j}$, so the trace picks up no contribution from them, and its total value is the middle signature. $\square$

**Corollary (the Hermitian structure of the index).** The index of the signature operator is the Hermitian pairing of *Hermitian Pairings on a Topological Space* evaluated on the chirality, and the operation of taking the adjoint is the operator-theoretic form of the involution on the pairing: the involution $\tau$ acts on the kernel, its middle fixed and anti-fixed parts are the positive and negative definite subspaces, and its non-middle action pairs the two sides. The self-adjointness of the operator is the compatibility of the pairing with the involution in the sense that $(D\alpha,\beta)=(\alpha,D\beta)$, and the index is the invariant of the pair (operator, chirality) that the adjoint operation preserves.

## Examples

**Example (the four-sphere).** The kernel of the signature operator on $S^{4}$ is the space of harmonic forms, which spans the constant functions and the volume form, of total dimension two; the middle cohomology vanishes. The chirality exchanges the constant function with minus the volume form, so on the two-dimensional kernel it has one $+1$ and one $-1$ eigenvector: the trace is $0$ and the index is $\sigma(S^{4})=0$. The adjoint of $D^{+}$ is $D^{-}$, both kernels have dimension one and the intersection form on the middle cohomology is the zero form; the example shows the cancellation of the non-middle harmonic forms.

**Example (the complex projective plane).** On $\mathbb{CP}^{2}$ the middle cohomology is one-dimensional and self-dual, and the harmonic forms in degrees $0$ and $2$ contribute a pair of chirality eigenvectors with trace zero as for the sphere; the total trace of the chirality on the kernel is $1$, the index of $D^{+}$, and the intersection form on the middle cohomology is the positive form $(1)$. The full kernel of $D^{+}$ has dimension $2$ and that of $D^{-}$ has dimension $1$, the difference being the signature; the example shows that the index is a difference and not the dimension of a kernel.

**Example (the $K3$ surface).** On a $K3$ surface the harmonic forms in degrees $0$ and $4$ contribute one chirality eigenvalue $+1$ and one $-1$, and the middle harmonic forms have dimension $22$, split into the self-dual part of dimension $3$ and the anti-self-dual part of dimension $19$; the total trace of the chirality on the kernel is $1+3-1-19=-16=\sigma(K3)$, so the kernels of $D^{+}$ and $D^{-}$ have dimensions $4$ and $20$ and the Hermitian form of the middle kernel has signature $-16$. The example shows that the index of a self-adjoint operator is the signature of its middle kernel pairing and can be negative.

**Example (the flat torus).** On $T^{n}$ with the flat metric the harmonic forms are the constant-coefficient forms; the signature operator is the square root of the flat Laplacian, its index is the signature of the middle intersection form for $n=4k$ and vanishes for $n\equiv2\pmod4$; the adjoint is the operator itself and the chirality is the star, and the plane-wave eigenforms compute the spectrum.

## Summary

The signature operator $D=d+d^{*}$ on a closed oriented Riemannian manifold is **formally self-adjoint** with respect to the metric inner product $(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta$, because the adjoint of the exterior derivative is the codifferential and the two are mutually adjoint; as an unbounded operator it is self-adjoint with discrete real spectrum and complete eigenforms. On an even-dimensional manifold the chirality $\tau$ makes the operator odd, so it splits into the mutually adjoint halves $(D^{+})^{*}=D^{-}$, and the **cokernel of $D^{+}$ is the kernel of $D^{-}$**; the index is the signature $\sigma(M)$ of the manifold. The adjoint operation is the operator-theoretic form of the involution on the pairing: the chirality conjugates the operator to the negative of its adjoint, $\tau D\tau^{-1}=-D$, and the **chirality is the normalized Hodge star**, the isometry that computes the adjoint. The index is the trace of the chirality on the kernel; the non-middle harmonic forms are exchanged by the chirality and cancel, so the index is equivalently the signature of the intersection pairing on the middle harmonic forms, whose positive part is the self-dual and whose negative part the anti-self-dual middle forms; the index of a self-adjoint operator is thus the signature of its middle kernel pairing, the Hermitian statement of *Hermitian Pairings on a Topological Space*. The examples $S^{4}$, $\mathbb{CP}^{2}$ and the $K3$ surface show the index $0$, $1$ and $-16$.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $(\alpha,\beta)=\int_M\alpha\wedge\star\bar\beta$ | Metric $L^2$ inner product on forms |
| $P^{*}$ | Formal adjoint, $(P\alpha,\beta)=(\alpha,P^{*}\beta)$ |
| $d^{*}$, $(d^{*})^{*}=d$ | Codifferential, adjoint of the exterior derivative |
| $D=d+d^{*}=D^{*}$ | Signature operator, self-adjoint |
| $\Omega^{\pm}$, $D^{\pm}:\Omega^{\pm}\to\Omega^{\mp}$ | Chirality eigenspaces and the chiral halves |
| $(D^{+})^{*}=D^{-}$, $\operatorname{coker}D^{+}=\ker D^{-}$ | Adjoint of the positive half |
| $\tau D\tau^{-1}=-D$ | Chirality conjugates the operator to the negative of its adjoint |
| $\tau=i^{k(k-1)+m}\star$, $\tau^2=\mathrm{id}$ | Chirality as the normalized star, the intertwining isometry |
| $\sigma(M)=\operatorname{ind}D^{+}=\operatorname{tr}(\tau\mid\ker D)$ | Index as the chirality trace |
| $Q(\alpha,\beta)=\int_M\alpha\wedge\beta$ | Intersection form; on the middle harmonic forms its signature is $\sigma(M)$ |

## Further Reading

- Michael Reed and Barry Simon, *Methods of Modern Mathematical Physics I: Functional Analysis* and *II: Fourier Analysis, Self-Adjointness* (Academic Press, 1972–1975), for the self-adjointness, the spectrum and the Fredholm alternative.
- Tosio Kato, *Perturbation Theory for Linear Operators*, Classics in Mathematics (Springer, 1995), for the closed operators, the adjoints and the domains.
- Michael F. Atiyah and Isadore M. Singer, "The index of elliptic operators I," *Annals of Mathematics* **87** (1968), 484–530, for the index of a self-adjoint elliptic operator and the chiral splitting.
- H. Blaine Lawson and Marie-Louise Michelsohn, *Spin Geometry* (Princeton University Press, 1989), for the self-adjointness of the Dirac-type operators and the role of the Hermitian structure.
- Phillip A. Griffiths and Joseph Harris, *Principles of Algebraic Geometry* (Wiley, 1978), for the intersection form, the positivity and the signature of the Hermitian pairing on the harmonic forms.
- Peter D. Lax, *Functional Analysis* (Wiley, 2002), for the formal adjoint, the integration by parts and the unbounded operators.
