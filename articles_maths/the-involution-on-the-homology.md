
# __The Involution on the Homology__

## Introduction

An involution of a manifold acts on the homology, and this article reads the action as a structure on the homology module itself: the involution makes $H_*(M;k)$ a module over the group ring $k[\mathbb{Z}/2]$, and its decomposition into the **fixed part** and the **anti-fixed part** is the refinement that the intersection form sees. The point of the article is the interaction: the intersection form of *Poincaré Duality* is compatible with the involution, and the compatibility decides whether the two parts are orthogonal or dual, and what the signature does.

The two cases are the whole content. An **orientation-preserving** involution leaves the intersection form invariant, the fixed and the anti-fixed parts are orthogonal and nondegenerate for the form separately, and the signature of the manifold is the sum of the signatures of the two parts. An **orientation-reversing** involution negates the form, the two parts are isotropic and are placed in perfect duality by the form, and the signature of the manifold must vanish. This dichotomy is the source of the equivariant signature and of the fixed-point formulae of the later articles.

**The article assumes** the homology and cohomology of a manifold, the cup and cap products, Poincaré duality and the intersection form and its signature, all of *Algebraic Topology* in this Part, and the elementary operator theory of *The Involution as an Operator on the Homology*.

**The boundaries of the article.** The operator on the homology — the group ring, the transfer and the Smith theory — is *The Involution as an Operator on the Homology*, and its results are used here without repetition. The fixed set as a manifold, the equivariant surgery and the classification of involutions are the group `- * Theory`. The operators built from the involution, with the adjoint as their archetype, and the equivariant signature are the group `- * Operator Theory`; in particular the $G$-signature theorem is *Hermitian Pairings and the Equivariant Signature*, and the present article stops at the algebraic consequence $\sigma(M)=0$ for an orientation-reversing involution. No analysis and no smooth structure is used.

## The Involution on the Homology and the Cohomology

**Definition.** Let $M$ be a finite CW complex and let $T : M \to M$ be an involution. The induced maps are
$$
T_* : H_*(M;k)\to H_*(M;k), \qquad T^{*} : H^{*}(M;k)\to H^{*}(M;k), \qquad T_*^2 = \mathrm{id}, \quad (T^{*})^2 = \mathrm{id}.
$$
The **fixed part** and the **anti-fixed part** of the homology are
$$
H_*^{+} = \ker\bigl(T_* - \mathrm{id}\bigr), \qquad H_*^{-} = \ker\bigl(T_* + \mathrm{id}\bigr),
$$
and similarly for the cohomology, with $H^{*,\pm}$. When $2$ is invertible in $k$ these are the images of the projections $P_\pm = \tfrac12(1\pm T_*)$ and $H_* = H_*^{+}\oplus H_*^{-}$.

**Proposition (the involution is a ring map on the cohomology).** The induced map $T^{*}$ is a unital ring automorphism of $H^{*}(M;k)$: it preserves the cup product, $T^{*}(x\smile y) = T^{*}x \smile T^{*}y$, and it commutes with the cap product against the fundamental class when $M$ is a closed oriented manifold. Consequently the fixed subring $H^{*}(M;k)^{T}$ — the elements fixed by $T^{*}$ — is a subring, and the anti-fixed part is a module over it.

**Proof.** $T$ is a map of spaces, so the induced map on cohomology preserves the cup product by naturality of the product of *Cup and Cap Products*; the same naturality applied to the fundamental class gives $T^{*}(x)\frown T_*[M] = T_*(x \frown [M])$, and $T_*[M] = \deg(T)[M]$ with $\deg(T) = \pm1$.

**Definition.** The **degree** of the involution is the sign $\deg(T)\in\{\pm1\}$ by which it acts on the top homology $H_n(M;\mathbb{Z})\cong\mathbb{Z}$ of a closed connected orientable $n$-manifold, that is, $T_*[M] = \deg(T)[M]$; the involution is **orientation-preserving** when $\deg(T) = +1$ and **orientation-reversing** when $\deg(T) = -1$.

## The Fixed and the Anti-Fixed Parts

**Proposition (the two parts in terms of the transfer).** Let $k$ be a ring in which $2$ is invertible and let $p : M \to M/T$ be the orbit map. Then $H_*(M;k)^{+}\cong H_*(M/T;k)$ via the induced map of the quotient, and the anti-fixed part $H_*^{-}$ is the kernel of the transfer, so that there is a natural splitting
$$
H_*(M;k) = H_*^{+}\oplus H_*^{-}, \qquad H_*^{+}\cong H_*(M/T;k).
$$

**Proof.** The statement that the fixed part is the homology of the quotient is the transfer theorem of *The Involution as an Operator on the Homology*; the anti-fixed part is its complementary summand and hence the kernel of the transfer, by the same splitting.

**Remark (the anti-fixed part as the sign representation).** The anti-fixed part is the part of the homology on which $\mathbb{Z}/2$ acts by the sign representation. Writing $k_{\mathrm{sgn}}$ for the module $k$ with $t$ acting by $-1$, one has
$$
H_*^{-} \;\cong\; H_*(M;k\otimes_{\mathbb{Z}} k_{\mathrm{sgn}})^{\mathbb{Z}/2},
$$
the invariants of the homology with coefficients in the sign representation; equivalently, the anti-fixed part is the "twisted" or sign-isotypic component of the module. This is the module-theoretic way to state that $H_*^{-}$ is not computed by the ordinary quotient but by the quotient twisted by the orientation.

**Example (the anti-fixed part of the torus).** For $T^2$ with the orientation-preserving involution $-I$ of *The Involution as an Operator on the Homology*, the anti-fixed part is one-dimensional in degree $1$ (the space on which $-I$ acts by $-1$) and the fixed part is one-dimensional in degrees $0$ and $2$; the sum reproduces $H_*(T^2;\mathbb{Q})$.

## The Intersection Form and the Involution

Let $M$ be a closed connected orientable manifold of dimension $n = 2m$, with intersection form
$$
Q : H^m(M;\mathbb{Z})\times H^m(M;\mathbb{Z})\to\mathbb{Z}, \qquad Q(x,y) = \bigl\langle x\smile y,[M]\bigr\rangle,
$$
which is nondegenerate and is symmetric or alternating according to the parity of $m$. The involution acts on the middle-dimensional homology and the form is compatible with it in one of the two ways above.

**Theorem (the form is invariant or anti-invariant).** For every $x,y\in H^m(M;\mathbb{Q})$,
$$
Q\bigl(T_*x, T_*y\bigr) = \deg(T)\, Q(x,y).
$$
So an orientation-preserving involution leaves the form invariant and an orientation-reversing involution negates it.

**Proof.** $Q(T_*x,T_*y) = \langle T^{*}(x\smile y),[M]\rangle = \langle x\smile y, T_*[M]\rangle = \deg(T)\langle x\smile y,[M]\rangle$, using the naturality of the evaluation pairing and the definition of the degree.

**Theorem (the orientation-preserving case: orthogonal splitting).** Let $\deg(T) = +1$ and let $2$ be invertible. Then the fixed and anti-fixed parts are orthogonal for $Q$,
$$
Q\bigl(H_m^{+}, H_m^{-}\bigr) = 0,
$$
and the form restricts to a nondegenerate form on each part; consequently
$$
Q = Q^{+}\oplus Q^{-}, \qquad \sigma(M) = \sigma(M^{+}) + \sigma(M^{-}),
$$
where $\sigma(M^{\pm})$ is the signature of the form restricted to the $\pm$-part.

**Proof.** For $x\in H_m^{+}$ and $y\in H_m^{-}$ one has $Q(x,y) = Q(T_*x,T_*y) = Q(x,-y) = -Q(x,y)$, so $2Q(x,y)=0$ and the orthogonality follows from the invertibility of $2$. Orthogonal summands of a nondegenerate form are nondegenerate on each summand: a class in the radical of $Q^{+}$ pairs trivially with $H_m^{+}$ and, by orthogonality, with $H_m^{-}$ as well, hence with all of $H_m$, and vanishes by the nondegeneracy of $Q$. The signature is additive over an orthogonal direct sum.

**Theorem (the orientation-reversing case: isotropic duality and vanishing signature).** Let $\deg(T) = -1$ and let $2$ be invertible. Then each part is isotropic for $Q$,
$$
Q\bigl(H_m^{+}, H_m^{+}\bigr) = 0, \qquad Q\bigl(H_m^{-}, H_m^{-}\bigr) = 0,
$$
and $Q$ places the two parts in perfect duality:
$$
Q : H_m^{+}\times H_m^{-}\to\mathbb{Q} \ \text{is nondegenerate}.
$$
Consequently the signature of $M$ vanishes, $\sigma(M) = 0$, and the form is the hyperbolic form attached to the pair of dual isotropic subspaces.

**Proof.** For $x,y\in H_m^{+}$ one has $Q(x,y) = Q(T_*x,T_*y) = -Q(x,y)$, since $T_*x = x$ and $T_*y = y$; so $2Q(x,y)=0$ and $Q$ vanishes on $H_m^{+}$, and symmetrically on $H_m^{-}$. If $x\in H_m^{+}$ pairs trivially with all of $H_m^{-}$, then by isotropy it pairs trivially with all of $H_m$, so $x = 0$ by nondegeneracy of $Q$; thus the pairing between the two parts is nondegenerate. The vanishing of the signature also follows directly: an orientation-reversing homeomorphism identifies $M$ with $\overline M$, whence $\sigma(M) = \sigma(\overline M) = -\sigma(M)$.

**Example (complex projective space admits no orientation-reversing involution).** The form on $H^2(\mathbb{CP}^2;\mathbb{Z})$ is $\langle1\rangle$, of signature $1$, so $\mathbb{CP}^2$ admits no orientation-reversing self-homeomorphism: if it did, the signature would vanish. Complex conjugation, the standard candidate, is indeed orientation-preserving, acting by $-1$ on $H^2$ and by $+1$ on $H^4$, so that the form is invariant in the required way.

**Example (a torus reflection).** On $T^2 = S^1\times S^1$ the involution $\tau(z,w) = (\bar z, w)$ reverses orientation. The middle-dimensional homology is $H_1(T^2;\mathbb{Z})\cong\mathbb{Z}^2$, and the anti-fixed part of the form is the part on which $\tau_*$ acts by $-1$; the form is alternating on $H_1$, and the fixed and anti-fixed parts are isotropic and dual, as the theorem states. The signature of $T^2$ vanishes, consistently.

## The Involution and Poincaré Duality

Poincaré duality couples the involution in complementary degrees, and the coupling is the reason the middle-dimensional statement is enough.

**Theorem (the duality is equivariant).** Let $M$ be a closed connected orientable $n$-manifold with an involution preserving the orientation. Then the cap product with the fundamental class is an isomorphism of $\mathbb{Z}[\mathbb{Z}/2]$-modules,
$$
-\frown[M] : H^{k}(M;\mathbb{Z})\xrightarrow{\ \cong\ }H_{n-k}(M;\mathbb{Z}),
$$
so that it maps the fixed part of $H^{k}$ onto the fixed part of $H_{n-k}$ and the anti-fixed part onto the anti-fixed part. If the involution reverses the orientation, the same holds with the two parts interchanged: the fixed part of $H^{k}$ is identified with the anti-fixed part of $H_{n-k}$.

**Proof.** The cap product is natural for maps of spaces, so $T_*(x\frown[M]) = T^{*}x\frown T_*[M] = \deg(T)\,T^{*}x\frown[M]$. If $\deg(T) = +1$ the isomorphism intertwines the two involutions, hence preserves the eigenspaces; if $\deg(T) = -1$ it intertwines $T^{*}$ with $-T_* = T_*$ on the anti-fixed part, hence exchanges the two eigenspaces.

**Corollary (the Euler characteristic and the equivariant Euler characteristic).** For an orientation-preserving involution of a closed orientable manifold, the equivariant Poincaré duality gives $\dim H_k^{\pm} = \dim H_{n-k}^{\pm}$, hence
$$
\sum_k(-1)^k\dim H_k^{\pm} = (-1)^n \sum_k(-1)^k\dim H_k^{\pm},
$$
so that each part has vanishing Euler characteristic when $n$ is odd. The alternating sum of the fixed part is the Euler characteristic $\chi(M/T)$ of the quotient, by the transfer, and the alternating sum of the anti-fixed part is $\chi(M)-\chi(M/T)$.

## The Module Structure and the Hermitian Pairing

The interaction of the involution with the form is expressed algebraically by pairing the form against the involution.

**Definition.** Let $k$ be a field of characteristic not two and let $A = k[\mathbb{Z}/2]$ with the involution $\overline{t} = t^{-1} = t$. A **Hermitian form** on an $A$-module $V$ is a form $\langle-,-\rangle$ that is $A$-linear in the first variable and satisfies
$$
\langle y,x\rangle = \overline{\langle x,y\rangle}, \qquad \langle t x, y\rangle = \langle x, t y\rangle ,
$$
the second condition saying that the form is invariant under the involution. A form with $\langle y,x\rangle = -\overline{\langle x,y\rangle}$ is **anti-Hermitian**.

**Proposition (the intersection form is Hermitian for an orientation-preserving involution).** Let $T$ preserve the orientation and define the sesquilinear form
$$
\langle x, y\rangle = Q(x, T_*y), \qquad x,y\in H_m(M;\mathbb{Q}).
$$
Then $\langle-,-\rangle$ satisfies
$$
\text{(a)}\quad \langle y,x\rangle = \varepsilon\,\langle x,y\rangle, \qquad \varepsilon = (-1)^m\deg(T); \qquad\qquad
\text{(b)}\quad \langle T_*x, y\rangle = \deg(T)\,\langle x, T_*y\rangle ,
$$
so that it is $\varepsilon$-Hermitian and compatible with the involution up to the degree sign. On the fixed part it agrees with $Q$ and on the anti-fixed part it agrees with $-Q$, because $T_*y = \pm y$ there. The classification of such forms is the subject of *Hermitian Pairings and the Signature*.

**Proof.** (b) is the compatibility of $Q$ with the involution: $\langle T_*x,y\rangle = Q(T_*x,T_*y) = \deg(T)Q(x,y)$ and $\langle x,T_*y\rangle = Q(x,T_*^2y) = Q(x,y)$. For (a), the same compatibility applied to $Q(T_*y,x)$ together with the middle-degree symmetry $Q(u,v) = (-1)^mQ(v,u)$ gives $Q(T_*y,x) = \deg(T)Q(y,T_*x)$ and $Q(T_*y,x) = (-1)^mQ(x,T_*y)$, so that $(-1)^m\langle x,y\rangle = \deg(T)\langle y,x\rangle$. Part (c) is immediate from $T_*y = \pm y$ on the two parts.

**Remark (the Witt groups and the obstruction).** The classification of the forms that occur is the content of *Hermitian Pairings and the Signature*, where the Witt group of Hermitian forms over a ring with involution and the Wall surgery groups are developed. The module structure here is the geometric input to that classification, and the elementary operations on the form are the ones induced by surgery, as in *The Surgery Operator*.

## Examples

**Example (the sphere with the reflection and with the antipodal map).** On $S^2$ the reflection in a plane is orientation-reversing with fixed set a circle; the middle-dimensional homology $H_1(S^2) = 0$ carries the zero form, and the theorem is vacuous. On $S^{2m}$ the same holds for $m \geq 1$ because $H_m(S^{2m}) = 0$ for $m\neq 0, 2m$. The first nontrivial case is a four-manifold.

**Example (a free orientation-reversing involution).** On $M = S^2\times S^2$ the involution $T(x,y) = (x,-y)$, with $-y$ the antipode on the second factor, is orientation-reversing (the antipodal map has degree $-1$ on the two-dimensional factor) and free. On $H_2(M;\mathbb{Z})$ with generators $a = [\mathrm{pt}\times S^2]$ and $b = [S^2\times\mathrm{pt}]$ it acts by $-1$ on $a$ and by $+1$ on $b$, so that the anti-fixed part is the line spanned by $a$ and the fixed part the line spanned by $b$; both are isotropic for the form and $Q(a,b) = 1$, so the form places them in perfect duality and the signature vanishes, in agreement with the theorem.

**Example (the swap of the two factors of $S^2\times S^2$).** On $M = S^2\times S^2$ the involution $T(x,y) = (y,x)$ swaps the factors; it is orientation-preserving, with fixed set the diagonal $S^2$. On $H_2(M;\mathbb{Z})\cong\mathbb{Z}^2$ with generators $a = [\mathrm{pt}\times S^2]$ and $b = [S^2\times\mathrm{pt}]$, the form is $Q(a,a) = Q(b,b) = 0$, $Q(a,b) = 1$. The involution exchanges $a$ and $b$, so the fixed part is spanned by $a+b$ and the anti-fixed part by $a-b$; the two parts are orthogonal, of dimensions one and one, and the form restricts to the values $Q(a+b,a+b) = 2$ and $Q(a-b,a-b) = -2$, so the signatures are $+1$ and $-1$ and the total signature of $M$ is $0$, in agreement with the orthogonal splitting theorem.

## Summary

An involution of a manifold induces an involution of the homology and of the cohomology, the latter a ring automorphism, and the module $H_*(M;k)$ over $k[\mathbb{Z}/2]$ splits into the fixed part and the anti-fixed part; over a ring in which two is invertible, the fixed part is the homology of the quotient and the anti-fixed part is its complement, the sign-isotypic component of the module. On a closed orientable $2m$-manifold the intersection form is multiplied by the degree of the involution: an orientation-preserving involution leaves it invariant, so the two parts are orthogonal and the form restricts nondegenerately to each, and the signature of the manifold is the sum of the signatures of the two parts; an orientation-reversing involution negates the form, so the two parts are isotropic and placed in perfect duality by the form, and the signature of the manifold vanishes. Poincaré duality is an isomorphism of equivariant modules and preserves the parts for an orientation-preserving involution and exchanges them for an orientation-reversing one. The form twisted by the involution, $\langle x,y\rangle = Q(x,T_*y)$, is $\varepsilon$-Hermitian with $\varepsilon = (-1)^m\deg(T)$ and compatible with the involution up to the degree sign; its classification is the algebraic input to the equivariant signature, and the vanishing of the signature under an orientation-reversing involution is its simplest geometric consequence.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $T_*$, $T^{*}$ | the induced involution on the homology and on the cohomology |
| $H_*^{+} = \ker(T_*-\mathrm{id})$ | the fixed part; $H_*^{+}\cong H_*(M/T;k)$ over a ring with $2$ invertible |
| $H_*^{-} = \ker(T_*+\mathrm{id})$ | the anti-fixed part; the sign-isotypic component of the module |
| $P_\pm = \tfrac12(1\pm T_*)$ | the projections onto the two parts |
| $\deg(T) = \pm1$ | the orientation character; $T_*[M] = \deg(T)[M]$ |
| $Q(x,y) = \langle x\smile y,[M]\rangle$ | the intersection form of a closed orientable $2m$-manifold |
| $Q(T_*x,T_*y) = \deg(T)Q(x,y)$ | the compatibility of the form with the involution |
| $Q = Q^{+}\oplus Q^{-}$, $\sigma(M) = \sigma(M^{+})+\sigma(M^{-})$ | the orientation-preserving case |
| $Q(H_m^{\pm},H_m^{\pm}) = 0$, $\sigma(M) = 0$ | the orientation-reversing case |
| $\langle x,y\rangle = Q(x,T_*y)$ | the Hermitian (or anti-Hermitian) form twisted by the involution |
| $k_{\mathrm{sgn}}$ | the coefficient module on which $\mathbb{Z}/2$ acts by $-1$ |

## Further Reading

- Allen Hatcher, *Algebraic Topology* (Cambridge University Press, 2002), for the cup and cap products, Poincaré duality and the intersection form.
- Glen E. Bredon, *Topology and Geometry* (Springer, 1993), for the intersection form, the signature and their behaviour under finite group actions.
- Friedrich Hirzebruch and Dietrich Zagier, *The Atiyah–Singer Theorem and Elementary Number Theory* (Publish or Perish, 1974), for the equivariant signature and the fixed-point data.
- Michael F. Atiyah and Isadore M. Singer, "The Index of Elliptic Operators: III", *Annals of Mathematics* 87 (1968), 546–604, for the $G$-signature theorem, whose statement is the subject of *Hermitian Pairings and the Equivariant Signature*.
- C. T. C. Wall, *Surgery on Compact Manifolds* (Academic Press, 1970), for the elementary operations on forms induced by surgery and the Hermitian-form classification.
- Winfried Scharlau, *Quadratic and Hermitian Forms* (Springer, 1985), for the Hermitian and anti-Hermitian forms over a ring with involution and their Witt groups.
