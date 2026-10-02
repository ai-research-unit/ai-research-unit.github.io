
# __The Involution and the Dual Pairing__

## Introduction

An involution of a space is measured against the dual pairing by its **transposed involution**: given a dual pair $\langle E, F\rangle$ and a $\varsigma$-semilinear involution $\theta$ of $E$, there is a unique $\varsigma$-semilinear involution $\theta^{t}$ of $F$ such that

$$
\langle \theta x, y\rangle = \varsigma\bigl(\langle x, \theta^{t} y\rangle\bigr) \qquad (x \in E, \ y \in F),
$$

and the pairing is then invariant up to the scalar involution, $\langle \theta x, \theta^{t} y\rangle = \varsigma(\langle x, y\rangle)$. When the second space is the dual and the pairing is the evaluation, the transposed involution is the transpose of the earlier articles, and the fixed and negated parts are the annihilators of the negated and fixed parts. A form on $E$ is compatible with $\theta$ exactly when the operator it induces between $E$ and $F$ intertwines $\theta$ with $\theta^{t}$, so the compatibility of a form is a statement about the transposed involution and is read off from it.

This article develops the transposed involution of a dual pairing and the compatible forms. The dual pairs, the polar calculus, the weak topologies and the reflexivity are *Duality Theory*; the transposed involution on the dual is *Locally Convex Spaces with an Involution*; the topological involution itself is *Involutive Topological Linear Spaces*; the non-degenerate forms, their polarisation and their Hermitian property belong to the form theory of Part III and are named where they occur, not developed. The formulas of the sesquilinear case are those of *Involutive Linear Spaces* in Part I, transported to a pairing.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$, $\varsigma$ is the involution of $\mathbb{K}$ (the identity or the complex conjugation), $(E, F)$ is a dual pair over $\mathbb{K}$ with pairing $\langle\cdot, \cdot\rangle$, and $\theta$ is a $\varsigma$-semilinear involution of $E$ with $\theta^{2} = \mathrm{id}$; the linear case is $\varsigma = \mathrm{id}$ and is written $T$. The fixed and negated subspaces are $E^{\theta}$ and $E^{-}$.

## The Transposed Involution

**Theorem (existence and uniqueness).** Let $\theta$ be a $\varsigma$-semilinear involution of $E$. Then there is a unique $\varsigma$-semilinear involution $\theta^{t}$ of $F$ with

$$
\langle \theta x, y\rangle = \varsigma\bigl(\langle x, \theta^{t} y\rangle\bigr) \qquad (x \in E, \ y \in F) ,
$$

and $(\theta^{t})^{2} = \mathrm{id}$. It is called the **transposed involution**, and it is linear exactly when $\theta$ is linear.

**Proof.** For fixed $y \in F$ the map $x \mapsto \varsigma(\langle \theta x, y\rangle)$ is linear (the composition of the $\varsigma$-semilinear $\theta$ with the linear functional $\langle\cdot, y\rangle$ and the involution $\varsigma$), so by the non-degeneracy of the pairing it is $\langle x, y^{t}\rangle$ for a unique $y^{t} \in F$; set $\theta^{t}y = y^{t}$. Linearity of $y \mapsto \theta^{t}y$ is the bilinearity of the pairing, and semilinearity follows from $\varsigma^{2} = \mathrm{id}$. Applying the defining relation twice, $\langle\theta^{2}x, y\rangle = \varsigma(\langle\theta x, \theta^{t}y\rangle) = \varsigma^{2}(\langle x, (\theta^{t})^{2}y\rangle) = \langle x, (\theta^{t})^{2}y\rangle$, and $\theta^{2} = \mathrm{id}$ with non-degeneracy gives $(\theta^{t})^{2} = \mathrm{id}$.

**Proposition (invariance of the pairing up to $\varsigma$).** For all $x \in E$ and $y \in F$,

$$
\langle \theta x, \theta^{t} y\rangle = \varsigma\bigl(\langle x, y\rangle\bigr) ,
$$

so the pairing is invariant when $\theta$ is linear and conjugate-invariant in the antilinear case; the same relation with the roles exchanged holds for the transposed involution of $F$.

**Proof.** Apply the defining relation with $y$ replaced by $\theta^{t}y$: $\langle\theta x, \theta^{t}y\rangle = \varsigma(\langle x, \theta^{t}\theta^{t}y\rangle) = \varsigma(\langle x, y\rangle)$.

**Proposition (annihilators).** The fixed and negated subspaces of $\theta^{t}$ are the annihilators of the negated and fixed subspaces of $\theta$,

$$
F^{\theta^{t}} = (E^{-})^{\circ}, \qquad F^{-} = (E^{\theta})^{\circ} ,
$$

and the bipolar theorem of *Duality Theory* recovers the summands; in particular the transposed involution is injective on $F$ exactly when the summands of $E$ are the whole space.

**Proof.** $y$ is fixed under $\theta^{t}$ exactly when $\langle\theta x, y\rangle = \langle x, y\rangle$ for all $x$, which on $E^{-}$ reads $\langle -x, y\rangle = \langle x, y\rangle$ and forces $\langle x, y\rangle = 0$, and on $E^{\theta}$ is automatic; hence $F^{\theta^{t}}$ is the set of $y$ annihilating $E^{-}$. The rest is the annihilator calculus of *Duality Theory*.

## Compatible Forms

**Definition.** A bilinear form $B : E \times E \to \mathbb{K}$ is **$\theta$-compatible** (or **$\theta$-invariant**) when

$$
B(\theta x, \theta y) = B(x, y) \qquad (x, y \in E).
$$

When $B$ is non-degenerate it induces the operator $\Phi : E \to F$ by

$$
B(x, y) = \langle x, \Phi y\rangle ,
$$

and compatibility is the intertwining of the two involutions.

**Theorem (compatibility is intertwining, linear case).** Let $\theta = T$ be linear and let $B$ be a non-degenerate bilinear form on $E$ with induced isomorphism $\Phi : E \to F$, $B(x,y) = \langle x, \Phi y\rangle$. Then

$$
B(Tx, Ty) = B(x, y) \ \text{for all } x, y \iff \Phi\,T = T^{t}\,\Phi ,
$$

so a bilinear form is $T$-compatible exactly when its induced operator intertwines $T$ with the transposed involution.

**Proof.** $B(Tx, Ty) = \langle Tx, \Phi Ty\rangle = \langle x, T^{t}\Phi Ty\rangle$ by the defining relation of the transposed involution, and $B(x,y) = \langle x, \Phi y\rangle$; non-degeneracy of the pairing gives $T^{t}\Phi T = \Phi$, which, multiplied on the right by $T$ and using $T^{2} = \mathrm{id}$, is $\Phi T = T^{t}\Phi$.

**Remark (the antilinear case and Hermitian forms).** If $\theta$ is antilinear then $\theta^{t}$ is antilinear, and a bilinear form cannot be expressed by the intertwining above, because the relation would equate a linear and a conjugate-linear functional in each slot. The correct object in that case is a **sesquilinear** form $h$ on $E$, linear in the first argument and $\varsigma$-semilinear in the second, for which compatibility $h(\theta x, \theta y) = h(x, y)$ is equivalent to the induced semilinear map intertwining $\theta$ with $\theta^{t}$ up to the scalar involution. The sesquilinear and Hermitian forms are the subject of Part III and are named here, not developed.

## The Pairing of an Involutive Space with its Dual

**Proposition (the evaluation pairing).** For $F = E'$ with the evaluation pairing $\langle x, \varphi\rangle = \varphi(x)$, the transposed involution is the transpose $\theta'(\varphi) = \varphi \circ \theta$ of *Locally Convex Spaces with an Involution*, of the same kind as $\theta$; it is continuous for the weak-star, weak and strong topologies, and its fixed and negated parts are the annihilators of $E^{-}$ and $E^{\theta}$.

**Proof.** The defining relation $\langle\theta x, \varphi\rangle = \varsigma(\langle x, \theta'\varphi\rangle)$ is $(\theta'\varphi)(\theta x) = \varsigma(\varphi(x))$, which is the transpose; continuity and the annihilator calculus are *Locally Convex Spaces with an Involution*.

**Proposition (involutive reflexivity).** If $E$ is reflexive then the transposed involution of $\theta^{t}$ on $E'' = E$ is $\theta$; the formation $(\theta, \theta^{t})$ is symmetric and the pair $(E, F)$ with the two involutions is a dual pair of involutive spaces, with the canonical identification carrying one involution to the other.

**Proof.** The double transpose $(\theta^{t})^{t}$ acts on $E'' = E$ by the naturality of the transpose, and equals $\theta$ because $((\theta^{t})^{t}\varphi)(x) = \varphi(\theta x)$ under the identification $E'' = E$; the symmetry is the identity $(\theta^{t})^{t} = \theta$.

## Examples

**Example (the standard pairing over $\mathbb{C}$).** On $E = F = \mathbb{C}^{n}$ with the bilinear pairing $\langle z, w\rangle = \sum_i z_iw_i$ and the componentwise conjugation $\theta(z) = \bar z$, the transposed involution is again the conjugation, $\theta^{t} = \theta$, and the pairing satisfies $\langle\theta z, \theta w\rangle = \overline{\langle z, w\rangle}$; the compatible forms are the real-bilinear forms whose induced operator commutes with the conjugation.

**Example (the $\ell^{p}$-$\ell^{q}$ pairing).** On $E = \ell^{p}$ and $F = \ell^{q}$ with $1/p + 1/q = 1$ and the standard pairing, the transposed involution of the coordinatewise conjugation is the coordinatewise conjugation; the shift $R$ on $E$ has transpose $L$ on $F$, and the conjugation intertwines them, the pair being an involutive dual pair.

**Example (the evaluation pairing and the shift).** On $E = \ell^{p}$ with the coordinatewise conjugation and $F = \ell^{q}$, the transposed involution is the same conjugation, its fixed part is the real sequences and its negated part is the purely imaginary sequences, the annihilator calculus giving the real sequences as the annihilator of the imaginary ones.

## Summary

For a dual pair $\langle E, F\rangle$ and a $\varsigma$-semilinear involution $\theta$ of $E$ there is a unique $\varsigma$-semilinear involution $\theta^{t}$ of $F$ with $\langle\theta x, y\rangle = \varsigma(\langle x, \theta^{t} y\rangle)$, the transposed involution, of the same kind as $\theta$; the pairing satisfies $\langle\theta x, \theta^{t} y\rangle = \varsigma(\langle x, y\rangle)$, so it is invariant in the linear case and conjugate-invariant in the antilinear one. The fixed and negated parts of $\theta^{t}$ are the annihilators of the negated and fixed parts of $\theta$, and the bipolar theorem recovers the summands. A non-degenerate bilinear form is $\theta$-compatible exactly when the operator it induces between $E$ and $F$ intertwines $\theta$ with $\theta^{t}$, so compatibility of a form is a statement about the transposed involution; in the Hermitian case the intertwiner is of Hermitian type and the fixed subspace is isotropic in the antilinear case. When $F$ is the dual with the evaluation pairing the transposed involution is the transpose, continuous for the weak-star, weak and strong topologies, and in the reflexive case the operation is symmetric, $(\theta^{t})^{t} = \theta$. The standard pairing of $\mathbb{C}^{n}$ and the $\ell^{p}$-$\ell^{q}$ pairing are the models.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\langle E, F\rangle$ | Dual pair over $\mathbb{K}$ |
| $\varsigma$ | Involution of the scalars |
| $\theta$, $T$ | $\varsigma$-semilinear involution; the linear case |
| $\theta^{t}$ | Transposed involution of $F$ |
| $\langle\theta x, \theta^{t} y\rangle = \varsigma\langle x, y\rangle$ | Invariance of the pairing |
| $E^{\theta}$, $E^{-}$ | Fixed and negated parts |
| $(E^{-})^{\circ}$, $(E^{\theta})^{\circ}$ | Annihilators, the summands of $F$ |
| $B$, $\Phi$ | Compatible form and its induced operator |
| $\Phi T = T^{t}\Phi$ | Intertwining, compatibility of a bilinear form (linear case) |
| $(\theta^{t})^{t} = \theta$ | Symmetry in the reflexive case |

## Further Reading

- Nicolas Bourbaki, *Topological Vector Spaces, Chapters 1–5* (Springer, 1987), for the dual pairs, the polar calculus and the transposed maps.
- Gottfried Köthe, *Topological Vector Spaces I* and *II* (Springer, 1969 and 1979), for the duality of involutive spaces.
- Helmut H. Schaefer and Manfred P. Wolff, *Topological Vector Spaces* (Springer, second edition, 1999), for the dual pairs, the weak topologies and the compatible forms.
- Serge Lang, *Algebra* (Springer, third edition, 2002), for the sesquilinear forms, the Hermitian forms and the semilinear maps.
- John B. Conway, *A Course in Functional Analysis* (Springer, second edition, 1990), for the dual pairings and the transposed involutions.
