
# __Reflections as Signed Two-Sided Operators on a Banach Algebra__

## Introduction

An order-two symmetry of an algebra is an involutive automorphism, and the symmetries that a Banach algebra carries with respect to a grade involution $\alpha$ are the automorphisms of order two of the form

$$
\rho_u(x) = u\,\alpha(x)\,u^{-1} ,
$$

one for each unit $u$ whose product $u\,\alpha(u)$ with its twist is central. Each such $\rho_u$ is a **signed two-sided operator**, the signed sandwich $S_{u,u^{-1}}$, and it is an involutive automorphism of the algebra. This article studies the reflections of a Banach algebra: the reflector condition that makes a signed conjugation an involution, the square and the eigenvalue decomposition, the correspondence between the reflectors and the reflections with its kernel the central units, and the degenerate cases in which the family collapses. The topology contributes the norm of the reflection and the closedness of its fixed set, and it contributes nothing else, because a reflection is an automorphism and the algebraic statements already hold.

The article assumes the signed sandwich, its decomposition, its multiplication table and its inverse from *The Signed Sandwich on a Banach Algebra*, the article immediately preceding; the Banach algebra, its norm, the unit group and the centre from *Topological Algebras and Banach Algebras*; the bounded operators and the operator norm from *Operators on a Banach Algebra*; the involutive automorphism, the grading and the inner automorphisms from *Involutive Topological Bilinear Algebras* and *Reflections as Signed Two-Sided Operators on an Algebra*; and the completeness and closed subalgebras of the operator algebra from *The Operator Algebra of a Banach Space*. The anti-automorphism involution $\sigma$ is the `- * Theory` structure and is not used; the adjoint and the self-adjointness of the reflection are *The Signed Adjoint of the Reflection on a Banach Algebra*, later still.

Throughout, $\mathbb{K}$ is $\mathbb{R}$ or $\mathbb{C}$; $A$ is a unital Banach algebra over $\mathbb{K}$ with submultiplicative norm $\lVert\cdot\rVert$, centre $Z(A)$ and unit group $A^\times$; $\alpha$ is a continuous involutive automorphism; $c_t(x) = txt^{-1}$ is the inner automorphism by a unit $t$; the **reflection** determined by a unit $u$ is $\rho_u = c_u\alpha = S_{u,u^{-1}}$, $\rho_u(x) = u\alpha(x)u^{-1}$; and $A^\pm_\rho$ are the $\pm1$-eigenspaces of $\rho$ when $2$ is invertible.

## The Reflector

**Definition.** A **reflector** of $A$ with respect to $\alpha$ is a unit $u \in A^\times$ with $u\alpha(u) \in Z(A)$. The **reflection** determined by a reflector $u$ is the signed conjugation $\rho_u = c_u\alpha = S_{u,u^{-1}}$. The reflectors are written $R^\times(A,\alpha)$ and the reflections $\mathrm{Ref}(A,\alpha)$.

**Theorem (the reflection is an involutive automorphism).** For every unit $u$ the signed conjugation $\rho_u$ is a bounded algebra automorphism with $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$, and

$$
\rho_u^2 = c_{u\alpha(u)} ,
$$

so that $\rho_u$ is an involutive automorphism, $\rho_u^2 = \mathrm{id}$, exactly when $u$ is a reflector. Conversely every signed conjugation that is an involution has a reflector parameter.

**Proof.** The signed conjugation is a composite of the automorphisms $c_u$ and $\alpha$, hence an automorphism; it is bounded because $c_u$, $\alpha$ and $c_u^{-1} = c_{u^{-1}}$ are. The square is $\rho_u^2(x) = u\alpha(u\alpha(x)u^{-1})u^{-1} = u\alpha(u)x\alpha(u)^{-1}u^{-1} = c_{u\alpha(u)}(x)$, using that $\alpha$ is an automorphism and $\alpha^2 = \mathrm{id}$. An inner automorphism is the identity exactly when its conjugating element is central, so $\rho_u^2 = \mathrm{id}$ exactly for a reflector, and the converse is the same computation read backwards. $\square$

**Corollary (the identity and the grade involution).** The unit $1$ is a reflector with $\rho_1 = \alpha$, so the grade involution is always a reflection of the family; the family is nonempty as soon as $\alpha$ is defined, and it contains $\mathrm{id}$ only when $\alpha = \mathrm{id}$.

**Proof.** $1\cdot\alpha(1) = 1$ is central and $\rho_1 = c_1\alpha = \alpha$. The reflection $\rho_u$ equals the identity exactly when $c_u\alpha = \mathrm{id}$, that is $\alpha = c_{u^{-1}}$, which forces $\alpha = \mathrm{id}$ on a unital algebra when $u = 1$; in general $\mathrm{id}$ is a reflection only for the inner realisation of the identity. $\square$

## The Eigenvalue Decomposition

**Proposition (fixed subalgebra and negated part).** Let $u$ be a reflector and $\rho = \rho_u$. Then, when $2$ is invertible,

$$
A = A^+_\rho \oplus A^-_\rho , \qquad A^+_\rho = \{x : \rho(x) = x\} , \qquad A^-_\rho = \{x : \rho(x) = -x\} ,
$$

the fixed set $A^+_\rho$ is a closed subalgebra, the negated part $A^-_\rho$ is a closed subspace, and the multiplication table of the grading holds:

$$
A^+_\rho A^+_\rho \subseteq A^+_\rho , \quad A^+_\rho A^-_\rho \subseteq A^-_\rho , \quad A^-_\rho A^+_\rho \subseteq A^-_\rho , \quad A^-_\rho A^-_\rho \subseteq A^+_\rho .
$$

**Proof.** The map $\rho$ is a continuous involutive automorphism, so its eigenspaces for $\pm1$ are its fixed set and its negated part, they sum directly to $A$ by the averaging $x = \tfrac12(x + \rho(x)) + \tfrac12(x - \rho(x))$, and the multiplication table is the multiplicativity of $\rho$. Closedness is the closedness of the fixed set of a continuous map and of the equalizer of $\rho$ with $-\mathrm{id}$. $\square$

**Corollary (determination by the fixed subalgebra).** A reflection is determined by its fixed subalgebra and by its negated part; two reflections with the same fixed subalgebra are equal.

**Proof.** An automorphism of order two is determined by its action on the $\pm1$-eigenspaces, and the eigenspaces determine each other by the direct sum. $\square$

**Remark (the topology adds closedness).** The algebraic content of the decomposition is that of the involutive automorphism; the topology adds that both parts are closed, because $\rho$ is continuous, and that the averaging maps are continuous. No norm, no form and no measure enters the algebra of the reflection beyond that.

## The Correspondence

**Theorem (the kernel of the parametrisation).** The assignment $u \mapsto \rho_u$ is a surjection of the reflectors onto the reflections, and

$$
\rho_u = \rho_v \quad\Longleftrightarrow\quad v^{-1}u \in Z(A)^\times ,
$$

so the reflections are parametrised by the reflectors modulo the central units,

$$
\mathrm{Ref}(A,\alpha) \cong R^\times(A,\alpha)\big/ Z(A)^\times .
$$

**Proof.** If $\rho_u = \rho_v$ then $u\alpha(x)u^{-1} = v\alpha(x)v^{-1}$ for all $x$, so $(v^{-1}u)\alpha(x) = \alpha(x)(v^{-1}u)$ for all $x$; since $\alpha$ is onto, $v^{-1}u$ commutes with every element and lies in $Z(A)^\times$. Conversely a central unit is absorbed by the inner conjugation. The image of the central units is $\alpha$, since a central unit commutes with everything. $\square$

**Corollary (the reflector as the correcting element).** For a reflector $u$, $\rho_u(u) = \alpha(u)$, and the reflection is the composite $\rho_u = c_u\alpha$ of the inner automorphism by $u$ with the twist; the reflector is the element whose inner automorphism corrects $\alpha$ to the desired reflection.

**Proof.** $u\alpha(u)$ is central, so $u$ commutes with it and $\rho_u(u) = u\alpha(u)u^{-1} = \alpha(u)$; the composite form is the definition. $\square$

**Proposition (the coset of the inner automorphisms).** The reflections relative to $\alpha$ are exactly the involutive automorphisms lying in the coset $\mathrm{Inn}(A)\alpha$ of the inner automorphism group, and the map $[u] \mapsto [c_u]$ sends the reflectors to the classes of the reflections in $\mathrm{Out}(A) = \mathrm{Aut}(A)/\mathrm{Inn}(A)$. If every automorphism of $A$ is inner then every involutive automorphism is a reflection for a suitable $\alpha$.

**Proof.** The reflection is $c_u\alpha$ by the corollary, so it lies in the coset; conversely an element of the coset is $c_u\alpha$, and it is an involution exactly when $u$ is a reflector. The map $[u]\mapsto[c_u]$ is the standard isomorphism $A^\times/Z(A)^\times \to \mathrm{Inn}(A)$. $\square$

## The Degenerate Cases

**Theorem (the inner grade involution).** Suppose $\alpha = c_z$ for a unit $z$. Then

$$
\rho_u = c_{uz} , \qquad \mathrm{Ref}(A,\alpha) = \{\,\text{involutive inner automorphisms}\,\} ,
$$

and the reflections are exactly the inner automorphisms of $A$ of order two, with reflector condition $u\alpha(u) = uzuz^{-1} = u z u z^{-1}\in Z(A)$.

**Proof.** $\rho_u = c_u\alpha = c_uc_z = c_{uz}$, an inner automorphism; it is an involution exactly when $(uz)x(uz)^{-1} = x$ for all $x$, that is when $uz \in Z(A)$, the reflector condition read for $\alpha = c_z$. $\square$

**Theorem (the commutative case).** If $A$ is commutative then every unit is a reflector and $\rho_u = \alpha$ for every unit $u$; the reflection family collapses to the two-element group $\{\mathrm{id},\alpha\}$ and the correspondence $u \mapsto \rho_u$ is constant.

**Proof.** In a commutative algebra every element is central, so every unit is a reflector and $\rho_u = c_u\alpha = \alpha$. The reflections are therefore only $\alpha$, together with $\mathrm{id}$ when $\alpha = \mathrm{id}$. $\square$

**Remark (the failure of the correspondence).** The map $u \mapsto \rho_u$ is neither injective nor, when $\alpha$ is not inner, surjective onto all involutive automorphisms: only the signed conjugations are reflections, and the involutive automorphisms outside the coset $\mathrm{Inn}(A)\alpha$ are not. The parametrisation is also not a group homomorphism in general, because the product of two reflections is an unsigned sandwich rather than a reflection; each reflection is individually of order two, and the reflections are a coset of the inner automorphisms, not a subgroup.

## The Banach Reading and Examples

**Proposition (norm and isometry).** Every reflection $\rho_u$ is a bounded invertible operator with $\lVert\rho_u\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$ and $\lVert\rho_u^{-1}\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$; when $\alpha$ is isometric and $u$ is a unitary with $\lVert u\rVert = \lVert u^{-1}\rVert = 1$, the reflection is isometric, $\lVert\rho_u\rVert = 1$. The fixed subalgebra $A^+_\rho$ is closed, and $\rho_u$ extends to the completion of $A$.

**Proof.** The norm bound is submultiplicativity in the composite $c_u\alpha$; the isometry case is $\lVert u\alpha(x)u^{-1}\rVert \leq \lVert x\rVert$ with equality by applying $\rho_u^{-1}$. The fixed set is closed as the fixed set of a continuous map, and a bounded automorphism of a normed algebra extends uniquely to a bounded automorphism of its completion. $\square$

**Example (the matrix algebra).** Let $A = M_n(\mathbb{K})$ and $\alpha(X) = DXD^{-1}$ with $D$ an invertible diagonal matrix of order two, $D^2 = I$, so that $\alpha$ is a continuous involutive automorphism. Since $\alpha$ is inner, every reflection is an inner automorphism: $\rho_u = c_{u}\alpha = c_{uD}$, and it is an involution exactly when $uDuD^{-1}$ is central, that is a scalar matrix. For $D = I$ the grade involution is trivial and the reflections are the involutions $X \mapsto UXU^{-1}$ with $U^2$ central, the classical involutive inner automorphisms of $M_n$.

**Example (the graded function algebra).** Let $A = C(X,\mathbb{K})$ and $\alpha(f) = (2\chi - 1)f$ for a clopen subset $E \subseteq X$ with indicator $\chi$. Every unit (a nowhere-zero function) is a reflector, since $A$ is commutative, and every reflection equals $\alpha$: the reflection family is $\{\mathrm{id}, \alpha\}$, the sign functions on the two parts.

## Summary

A reflection of a Banach algebra $A$ with respect to a continuous involutive automorphism $\alpha$ is the signed conjugation $\rho_u(x) = u\alpha(x)u^{-1}$, the signed sandwich $S_{u,u^{-1}}$; it is a bounded algebra automorphism with $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$ and square $c_{u\alpha(u)}$, and it is an involutive automorphism exactly when $u$ is a **reflector**, $u\alpha(u) \in Z(A)$. An involutive reflection splits $A = A^+_\rho\oplus A^-_\rho$ into a closed fixed subalgebra and a closed negated part, with the multiplication table of a grading, and it is determined by its fixed subalgebra. The map $u \mapsto \rho_u$ is a surjection of the reflectors onto the reflections with kernel the central units, so the reflections are parametrised by $R^\times(A,\alpha)/Z(A)^\times$, and they are exactly the involutive automorphisms in the coset $\mathrm{Inn}(A)\alpha$. When $\alpha$ is inner every reflection is an inner automorphism, and when $A$ is commutative every unit is a reflector and the family collapses to $\{\mathrm{id},\alpha\}$; the correspondence is neither injective nor, in general, surjective onto all involutive automorphisms, and the reflections form a coset of the inner automorphisms rather than a subgroup. The reflection is bounded with $\lVert\rho_u\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$, isometric when $\alpha$ and $u$ are, and it extends to the completion. Its adjoint and self-adjointness are *The Signed Adjoint of the Reflection on a Banach Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $A$, $\lVert\cdot\rVert$, $A^\times$, $Z(A)$ | Banach algebra, norm, units, centre |
| $\alpha$, $c_t(x)=txt^{-1}$ | Continuous involutive automorphism; inner automorphism |
| $\rho_u = c_u\alpha = S_{u,u^{-1}}$ | Reflection by the unit $u$, $\rho_u(x)=u\alpha(x)u^{-1}$ |
| $R^\times(A,\alpha)$ | Reflectors: units with $u\alpha(u)\in Z(A)$ |
| $\mathrm{Ref}(A,\alpha)$ | Reflections, $\cong R^\times(A,\alpha)/Z(A)^\times$ |
| $\rho_u^2 = c_{u\alpha(u)}$ | Square; involution iff $u$ is a reflector |
| $A^+_\rho$, $A^-_\rho$ | Fixed subalgebra and negated part of $\rho$ |
| $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$ | The two readings of the reflection |
| $\rho_1 = \alpha$ | The grade involution is a reflection |
| $\lVert\rho_u\rVert \leq \lVert u\rVert\lVert u^{-1}\rVert\lVert\alpha\rVert$ | Norm bound; isometric when $\alpha,u$ are |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for the involutive automorphisms, the signed conjugations and the correspondences with the units.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for the inner automorphisms, the cosets in the automorphism group and the reflections.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for the bounded automorphisms of a Banach algebra and the closed fixed subalgebras.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for the graded Banach algebras, the automorphisms of order two and the reflections.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the classical reflections and the signed conjugations that model them.
