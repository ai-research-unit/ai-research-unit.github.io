
# __Involutive Nuclear Spaces__

## Introduction

A nuclear space is a locally convex space whose finite-dimensional-like behaviour makes the projective and the injective tensor product coincide, and an involution respects this behaviour: the fixed and negated subspaces of a continuous involution of a nuclear space are themselves nuclear, the topology and the completed tensor product are unambiguous, and the involution of a tensor product is well defined for the completed product without the choice between the two completions. On the tensor product the involution $\theta \otimes \omega$ has fixed and negated subspaces computed from the four pieces of the two factors, so that the signature of the product involution is the sum of the signatures of the factors; on the strong dual of a nuclear Fréchet space the transposed involution is again continuous, the dual being nuclear.

This article develops the theory of an involution on a nuclear space. The nuclear operators, the approximation numbers, the nuclear norm and the nuclearity of a space are *Nuclear Spaces*; the projective and the injective topologies, their completions and the coincidence theorem are *Topological Tensor Products*; the continuous involution, the closedness, the splitting and the extension to the completion are *Involutive Topological Linear Spaces* and *Locally Convex Spaces with an Involution*; the Banach and the Fréchet cases are the two preceding articles of this group. The forms, the kernels and the adjoints of the nuclear operators are Part III. No form and no Hilbert structure is used.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is the involution of $\mathbb{K}$, $E$ and $F$ are Hausdorff locally convex spaces over $\mathbb{K}$, $\theta$ and $\omega$ are continuous $\varsigma$-semilinear involutions of $E$ and $F$ with $\theta^{2} = \omega^{2} = \mathrm{id}$, the linear case is written $T$ and $S$, the summands are $E^{\theta} = E_{+}$, $E^{-}$ and $F^{\omega} = F_{+}$, $F^{-}$, and $E\widehat{\otimes} F$ is the completed tensor product, which is unambiguous when one factor is nuclear.

## Nuclearity and the Summands

**Theorem (the summands of a nuclear space are nuclear).** Let $E$ be a nuclear locally convex space and let $\theta$ be a continuous involution of $E$. Then the fixed subspace $E^{\theta}$ and the negated subspace $E^{-}$ are closed nuclear subspaces of $E$; each carries the induced locally convex structure and is nuclear, and when $2$ is invertible the topological direct sum $E^{\theta} \oplus E^{-}$ is nuclear.

**Proof.** A subspace of a nuclear space is nuclear, by *Nuclear Spaces*; the summands are closed by *Involutive Topological Linear Spaces*, and the direct sum of two nuclear spaces is nuclear. The direct-sum topology is the induced one by the splitting of *Locally Convex Spaces with an Involution*.

**Proposition (continuity of the involution on a nuclear space).** If $E$ is a nuclear Fréchet space, a $\varsigma$-semilinear involution is continuous exactly when it is bounded, exactly when it has closed graph, and exactly when the four criteria of *Involutive Fréchet Spaces* hold; nuclearity does not dispense with the continuity hypothesis, and the equivalent invariant seminorms are available as there.

**Proof.** A nuclear Fréchet space is a Fréchet space, so the criteria of *Involutive Fréchet Spaces* apply; the nuclearity adds the behaviour of the tensor product below but not automatic continuity of an arbitrary involution.

**Proposition (nuclear representations and the involution).** Let $\theta$ be continuous and let $T : E \to F$ be a nuclear map between involutive spaces. Then the composition with the involutions preserves nuclearity, $\theta_{F} \circ T \circ \theta_{E}$ is nuclear with the same nuclear norm, and the transposed map on the strong duals is nuclear.

**Proof.** A composite of a nuclear map with continuous linear maps is nuclear, with the nuclear norm bounded by the product of the operator norms by *Nuclear Spaces*; the involutions are topological isomorphisms of norm one in the isometric case, and semilinear in the antilinear case, where the composition is understood over the fixed field.

## The Involution on the Tensor Product

**Definition.** For continuous linear involutions $T$ of $E$ and $S$ of $F$, the **tensor product involution** is the map $T \otimes S$ on $E \otimes F$ determined by $(T \otimes S)(x \otimes y) = Tx \otimes Sy$; it is a linear involution, and it is continuous for the projective topology, its completion being written $T \widehat{\otimes} S$ on $E \widehat{\otimes} F$. For semilinear involutions the same formula defines a $\varsigma$-semilinear involution, with $\varsigma$ acting on the scalars.

**Theorem (the signature of the product).** Let $T$ and $S$ be linear involutions of $E$ and $F$. Then $T \otimes S$ is a linear involution of $E \otimes F$ with

$$
(E \otimes F)^{+} = (E_{+} \otimes F_{+}) \oplus (E_{-} \otimes F_{-}), \qquad
(E \otimes F)^{-} = (E_{+} \otimes F_{-}) \oplus (E_{-} \otimes F_{+}) ,
$$

so the fixed part of the product involution is the direct sum of the products of like signs and the negated part the direct sum of the products of opposite signs; in terms of the types $(p, q)$ and $(r, s)$ of $T$ and $S$ the product has type $(pr + qs,\, ps + qr)$.

**Proof.** On a decomposable tensor $x \otimes y$ the involution acts by $Tx \otimes Sy$; with $x = x_{+} + x_{-}$ and $y = y_{+} + y_{-}$ this is $x_{+}\otimes y_{+} + x_{-}\otimes y_{-}$ in the fixed part and $-(x_{+}\otimes y_{-} + x_{-}\otimes y_{+})$ in the negated part, and the four products span the tensor product. The type formula is the dimension count $pr + qs$ for the fixed part and $ps + qr$ for the negated part.

**Theorem (the completed tensor product).** Let one of $E$, $F$ be nuclear. Then the projective and the injective completions coincide, $E \widehat{\otimes}_\pi F = E \widehat{\otimes}_\varepsilon F = E \widehat{\otimes} F$, the tensor product involution extends uniquely to a continuous involution $T \widehat{\otimes} S$ of this completed tensor product, of the same kind, and its fixed and negated subspaces are the completions of those of the algebraic tensor product,

$$
(E \widehat{\otimes} F)^{+} = \overline{(E_{+} \otimes F_{+}) \oplus (E_{-} \otimes F_{-})}, \qquad
(E \widehat{\otimes} F)^{-} = \overline{(E_{+} \otimes F_{-}) \oplus (E_{-} \otimes F_{+})} .
$$

**Proof.** The coincidence of the two completions when a factor is nuclear is the theorem of *Topological Tensor Products*; the involution $T \otimes S$ is continuous for the projective topology because $T$ and $S$ are, so it extends to the completion $E\widehat{\otimes}_\pi F$ by *Involutive Topological Linear Spaces*, and the injective completion carries the same involution because the two completions are equal; the fixed and negated subspaces of the extension are the closures of the corresponding subspaces of the dense algebraic tensor product, by the extension theorem of *Involutive Banach Spaces*.

**Corollary (the antilinear case).** If $\theta$ and $\omega$ are antilinear then $\theta \otimes \omega$ is antilinear, of the same kind as the factors, with

$$
\ker\bigl((\theta\otimes\omega) - \mathrm{id}\bigr) = E_{+} \otimes F_{+} , \qquad
\ker\bigl((\theta\otimes\omega) + \mathrm{id}\bigr) = i\,(E_{+} \otimes F_{+}) ,
$$

read over $\mathbb{R}$; the two pieces $E_{+}\otimes F_{+}$ and $E_{-}\otimes F_{-}$ of the linear formula coincide here because $E_{-} = iE_{+}$ and $F_{-} = iF_{+}$. The completed tensor product of two involutive nuclear spaces is again an involutive nuclear space.

**Proof.** The tensor product of two $\varsigma$-semilinear maps is $\varsigma$-semilinear, so $\theta\otimes\omega$ is antilinear, and $(\theta\otimes\omega)^{2} = \theta^{2}\otimes\omega^{2} = \mathrm{id}$. A fixed decomposable tensor satisfies $\theta x\otimes\omega y = x\otimes y$, which holds for $x\in E_{+}$, $y\in F_{+}$ and, on a negated-negated product, because $(-x_{-})\otimes(-y_{-}) = x_{-}\otimes y_{-}$, but the two real subspaces coincide since $E_{-} = iE_{+}$ and $F_{-} = iF_{+}$. The completed tensor product of nuclear spaces is nuclear by *Nuclear Spaces*, and its involution is the extension theorem.

## The Dual

**Proposition (the dual of an involutive nuclear space).** Let $E$ be a nuclear Fréchet space with a continuous involution $\theta$. Then the strong dual $E'_{b}$ is nuclear, the transposed involution $\theta'$ is continuous for the strong topology, and

$$
(E'_{b})^{\theta'} = (E^{-})^{\circ}, \qquad (E'_{b})^{-} = (E^{\theta})^{\circ} ;
$$

the dual pair $(E, E'_{b})$ with the two involutions is a dual pair of involutive nuclear spaces, and when $E$ is reflexive the operation is an involution, $(\theta')' = \theta$.

**Proof.** The strong dual of a nuclear Fréchet space is nuclear, by *Nuclear Spaces*; the continuity of the transposed involution and the annihilator identification are *Involutive Fréchet Spaces* and *The Involution and the Dual Pairing*, and the reflexive statement is *Duality Theory*.

## Examples

**Example (the Schwartz space).** On $\mathcal{S}(\mathbb{R}^{n})$ the conjugation $f \mapsto \overline{f}$ is an antilinear isometric involution and the reflection $f(x) \mapsto f(-x)$ a linear isometric involution; both are continuous for the nuclear topology, the fixed subspaces are the real and the even Schwartz spaces, and these are nuclear. The completed tensor product $\mathcal{S}(\mathbb{R}^{m}) \widehat{\otimes} \mathcal{S}(\mathbb{R}^{n}) = \mathcal{S}(\mathbb{R}^{m+n})$ carries the tensor product of the reflections, whose fixed subspace consists of the sums of products of even functions and of odd functions paired by the same parity.

**Example (the rapidly decreasing sequences).** On $s$ the coordinatewise conjugation is an antilinear isometric involution with fixed subspace the real rapidly decreasing sequences; on the completed tensor product $s \widehat{\otimes} s$ the tensor product of the conjugations is the coordinatewise conjugation on the double sequence, with fixed subspace the real double sequences.

**Example (distributions).** The strong dual $\mathcal{S}'(\mathbb{R}^{n})$ of the Schwartz space is nuclear, and the transposed involution of the conjugation is given by $\langle\theta' u, f\rangle = \varsigma(\langle u, \theta f\rangle)$; the fixed distributions are the real ones, $\overline{u} = u$, and the annihilator calculus identifies them with the distributions annihilating the odd test functions.

## Summary

On a nuclear space a continuous involution has nuclear fixed and negated subspaces, closed and carrying the induced nuclear structure, and their direct sum is nuclear; a nuclear Fréchet space is a Fréchet space, so the four criteria of continuity of the preceding article continue to hold, and nuclearity adds no automatic continuity but makes the tensor product behave finitely. For linear involutions the tensor product involution $T \otimes S$ has fixed part $(E_{+}\otimes F_{+})\oplus(E_{-}\otimes F_{-})$ and negated part $(E_{+}\otimes F_{-})\oplus(E_{-}\otimes F_{+})$, so the product has type $(pr+qs, ps+qr)$ in the types of the factors; the antilinear case composes to a linear involution up to the scalar involution, with the same signature over the real scalars. When one factor is nuclear the projective and injective completions coincide, the involution extends uniquely to the completed tensor product, and its summands are the closures of those of the algebraic tensor product. The strong dual of an involutive nuclear Fréchet space is nuclear and carries the transposed involution with the summands given by the annihilators, and reflexive nuclear spaces have the symmetry $(\theta')' = \theta$. The Schwartz space, the space of rapidly decreasing sequences and the space of tempered distributions are the standard examples. The completed tensor product with an involution in the general locally convex case is *The Involution on a Topological Tensor Product*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $E$, $F$ | Nuclear or locally convex spaces over $\mathbb{K}$ |
| $\theta$, $\omega$, $T$, $S$ | Continuous involutions of $E$ and $F$ |
| $E_{+} = E^{\theta}$, $E_{-} = E^{-}$ | Fixed and negated summands |
| $T \otimes S$ | Tensor product involution on $E \otimes F$ |
| $(E \otimes F)^{+} = (E_{+}\otimes F_{+}) \oplus (E_{-}\otimes F_{-})$ | Fixed part of the product |
| $(E \otimes F)^{-} = (E_{+}\otimes F_{-}) \oplus (E_{-}\otimes F_{+})$ | Negated part of the product |
| $(pr + qs,\, ps + qr)$ | Type of the product from the types of the factors |
| $E \widehat{\otimes} F = E \widehat{\otimes}_\pi F = E \widehat{\otimes}_\varepsilon F$ | Completed tensor product, unambiguous for a nuclear factor |
| $E'_{b}$, $\theta'$ | Strong dual and transposed involution, nuclear |

## Further Reading

- Alexander Grothendieck, "Produits tensoriels topologiques et espaces nucléaires", *Memoirs of the AMS* **16** (1955), for the nuclear spaces, the completed tensor products and their involutions.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the nuclear spaces, their subspaces and their duals.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the nuclear spaces and the tensor product topologies.
- François Trèves, *Topological Vector Spaces, Distributions and Kernels* (Academic Press, 1967), for the nuclear spaces and the tensor products with involutions.
- Albrecht Pietsch, *Nuclear Locally Convex Spaces* (Springer, 1972), for the nuclear operators, the nuclear norms and the tensor product representation.
