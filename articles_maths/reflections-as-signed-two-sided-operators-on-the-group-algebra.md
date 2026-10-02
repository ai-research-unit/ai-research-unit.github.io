
# __Reflections as Signed Two-Sided Operators on the Group Algebra__

## Introduction

A reflection of the group algebra is a signed two-sided operator of the form $f\mapsto u\,\alpha(f)\,u^{-1}$ that is its own inverse: it is an involution produced by the convolution product, the grade involution and the inverse of a unit. This article reads the reflections of a graded group algebra as operators, identifies the units that carry them, computes the closed subalgebra they fix, and records the two ways the correspondence between reflections and carriers can degenerate — the grade involution inner, or the group algebra commutative. It is the two-sided operator theory of the signed conjugations of which the signed sandwich is the general form.

The article assumes the group, its Haar measure and the modular function from *Locally Compact Groups and Haar Measure*; the algebra $L^1(G)$ and its norm from *The Convolution Algebra $L^1(G)$*; the convolution operators and the group algebra as an algebra of operators from *Convolution on a Group* and *The Group Algebra as an Algebra of Operators*; the grade involution, the signed and unsigned sandwiches, their composition laws, the coset, the inverse and the signed conjugation from *The Signed Sandwich on the Group Algebra*, the immediately preceding article; the general reflections of an algebra and their degenerate cases from *Reflections as Signed Two-Sided Operators on an Algebra* and *Reflections as Signed Two-Sided Operators on a Banach Algebra* (Topology on Linear Algebras); the topological-group reflections, fixed subgroups and carriers from *Reflections as Signed Two-Sided Operators on a Topological Group* and *Involutive Topological Groups*; and the bounded operators, the operator norm and the closed subalgebras from *Operator Algebras* and *Topological Algebras and Banach Algebras*. The adjoint of a reflection is *The Signed Adjoint of the Reflection on the Group Algebra*, in the `- * Operator Theory` group of this category; the measure algebra is *The Involution on the Measure Algebra*, later. A reflection in the geometric sense — in a hyperplane, preserving a form — needs a form and belongs to the later categories; a reflection here is only a bounded operator of order two on the group algebra, and no adjoint is used.

Throughout, $G$ is a locally compact Hausdorff group with identity $e$ and left Haar measure $dx$; $\mathcal{A} = L^1(G)$ is the group algebra with convolution $f*g$, norm $\|f\|_1$, centre $Z(\mathcal{A})$ and unit group $\mathcal{A}^\times$; $\alpha$ is a continuous involutive automorphism, $\mathrm{A}f = \alpha(f)$, and $c_t(f) = t*f*t^{-1}$ is the inner automorphism by a unit $t$; the **reflector** set and the **reflection** family are

$$
R^\times(\mathcal{A},\alpha) = \{u \in \mathcal{A}^\times : u*\alpha(u) \in Z(\mathcal{A})\}, \qquad \rho_u = c_u\alpha = S_{u,u^{-1}} , \quad \rho_u(f) = u*\alpha(f)*u^{-1} ,
$$

and $\mathcal{A}^\pm_\rho$ are the $\pm1$-eigenspaces of a reflection $\rho$ when $2$ is invertible.

## The Reflector and the Reflection

**Definition.** A **reflector** of $\mathcal{A}$ with respect to $\alpha$ is a unit $u$ with $u*\alpha(u) \in Z(\mathcal{A})$, and the **reflection** determined by a reflector $u$ is $\rho_u = c_u\alpha$. The set of reflections is written $\mathrm{Ref}(\mathcal{A},\alpha)$.

**Theorem (the reflection is an involutive automorphism).** For every unit $u$ the signed conjugation $\rho_u = c_u\alpha$ is a bounded algebra automorphism of $\mathcal{A}$ with $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$ and

$$
\rho_u^2 = c_{u*\alpha(u)} ,
$$

so $\rho_u$ is an involutive automorphism, $\rho_u^2 = \mathrm{id}$, exactly when $u$ is a reflector; conversely every signed conjugation that is an involution has a reflector parameter.

**Proof.** The signed conjugation is the composite of the automorphisms $c_u$ and $\alpha$, hence an automorphism, and it is bounded because $c_u$, $\alpha$ and $c_{u^{-1}}$ are. The square is $\rho_u^2(f) = u*\alpha(u*\alpha(f)*u^{-1})*u^{-1} = (u*\alpha(u))*f*(u*\alpha(u))^{-1} = c_{u*\alpha(u)}(f)$, using that $\alpha$ is an automorphism and $\alpha^2 = \mathrm{id}$. An inner automorphism is the identity exactly when its element is central, which gives the involution criterion; reading the computation backwards gives the converse. $\square$

**Corollary (the identity and the grade involution).** When $\mathcal{A}$ has a unit, $1$ is a reflector with $\rho_1 = \alpha$, so the grade involution is always a reflection of the family; and $\rho_u = \mathrm{id}$ exactly when $u$ is a central unit and $\alpha = c_{u^{-1}}$, which for $\alpha = \mathrm{id}$ means exactly $u \in Z(\mathcal{A})^\times$.

**Proof.** $1*\alpha(1) = 1$ is central and $\rho_1 = c_1\alpha = \alpha$; $\rho_u = \mathrm{id}$ is $c_u\alpha = \mathrm{id}$, that is $\alpha = c_{u^{-1}}$. $\square$

**Proposition (the reflection is an operator of the sandwich family).** The reflection is the signed sandwich whose second factor is the inverse of the first, $\rho_u = S_{u,u^{-1}}$; conversely the signed sandwich is recovered from the reflections and the one-sided operators by

$$
S_{a,b} = \rho_a\,R_{\alpha(b)*\alpha(a)} \qquad (a \in \mathcal{A}^\times),
$$

so the reflections together with the right convolutions generate the whole signed family.

**Proof.** $S_{u,u^{-1}}(f) = u*\alpha(f)*u^{-1} = \rho_u(f)$. For the reconstruction, $\rho_aR_{\alpha(b)*\alpha(a)}(f) = \rho_a(f*\alpha(b)*\alpha(a)) = a*\alpha(f)*\alpha(\alpha(b)*\alpha(a))*a^{-1} = a*\alpha(f)*(b*a)*a^{-1} = a*\alpha(f)*b = S_{a,b}(f)$, using $\alpha^2 = \mathrm{id}$ and the associativity of convolution. $\square$

## The Eigenvalue Decomposition

**Proposition (fixed subalgebra and negated part).** Let $u$ be a reflector and $\rho = \rho_u$. When $2$ is invertible,

$$
\mathcal{A} = \mathcal{A}^+_\rho\oplus\mathcal{A}^-_\rho, \qquad \mathcal{A}^+_\rho = \{f : \rho(f) = f\}, \qquad \mathcal{A}^-_\rho = \{f : \rho(f) = -f\},
$$

the fixed set $\mathcal{A}^+_\rho$ is a closed subalgebra, the negated part $\mathcal{A}^-_\rho$ is a closed subspace, and the multiplication table of the grading holds:

$$
\mathcal{A}^+_\rho\mathcal{A}^+_\rho\subseteq\mathcal{A}^+_\rho, \quad \mathcal{A}^+_\rho\mathcal{A}^-_\rho\subseteq\mathcal{A}^-_\rho, \quad \mathcal{A}^-_\rho\mathcal{A}^+_\rho\subseteq\mathcal{A}^-_\rho, \quad \mathcal{A}^-_\rho\mathcal{A}^-_\rho\subseteq\mathcal{A}^+_\rho .
$$

**Proof.** $\rho$ is a continuous involutive automorphism, so its $\pm1$-eigenspaces decompose $\mathcal{A}$ by the averaging $f = \tfrac12(f+\rho(f)) + \tfrac12(f-\rho(f))$; the multiplication table is the multiplicativity of $\rho$, $\rho(fg) = \rho(f)\rho(g)$. The fixed set is the kernel of the continuous map $\rho - \mathrm{id}$ and the negated part the kernel of $\rho + \mathrm{id}$, hence both closed. $\square$

**Corollary (determination by the fixed subalgebra).** A reflection is determined by its fixed subalgebra and by its negated part; two reflections with the same fixed subalgebra are equal.

**Proof.** An automorphism of order two is determined by its action on the $\pm1$-eigenspaces, and the two eigenspaces determine each other by the direct sum. $\square$

**Remark (the topology adds closedness).** The algebraic content of the decomposition is that of any involutive automorphism; the topology adds that the two parts are closed, because $\rho$ is continuous, and that the averaging maps are continuous. No norm, no form and no measure enters the algebra of the reflection beyond that.

## The Correspondence

**Theorem (the kernel of the parametrisation).** The assignment $u\mapsto\rho_u$ is a surjection of the reflectors onto the reflections, and

$$
\rho_u = \rho_v \quad\Longleftrightarrow\quad v^{-1}*u \in Z(\mathcal{A})^\times ,
$$

so the reflections are parametrised by the reflectors modulo the central units, $\mathrm{Ref}(\mathcal{A},\alpha)\cong R^\times(\mathcal{A},\alpha)/Z(\mathcal{A})^\times$.

**Proof.** If $\rho_u = \rho_v$ then $u*\alpha(f)*u^{-1} = v*\alpha(f)*v^{-1}$ for all $f$, so $(v^{-1}*u)*\alpha(f) = \alpha(f)*(v^{-1}*u)$ for all $f$; since $\alpha$ is onto, $v^{-1}*u$ commutes with every element and lies in $Z(\mathcal{A})^\times$. Conversely a central unit is absorbed by the inner conjugation, and every reflector is in the image by definition. $\square$

**Corollary (the reflector as the correcting element).** For a reflector $u$, $\rho_u(u) = \alpha(u)$, and $\rho_u$ is the composite of the inner automorphism by $u$ with the twist; the reflector is the element whose inner automorphism corrects $\alpha$ to the desired reflection.

**Proof.** $u*\alpha(u)$ is central, so $u$ commutes with it and $\rho_u(u) = u*\alpha(u)*u^{-1} = \alpha(u)$. $\square$

**Proposition (the coset of the inner automorphisms).** The reflections relative to $\alpha$ are exactly the involutive automorphisms lying in the coset $\mathrm{Inn}(\mathcal{A})\alpha$ of the inner automorphism group, and the map $[u]\mapsto[c_u]$ sends the reflectors to the classes of the reflections in $\mathrm{Out}(\mathcal{A}) = \mathrm{Aut}(\mathcal{A})/\mathrm{Inn}(\mathcal{A})$. If every automorphism of $\mathcal{A}$ is inner then every involutive automorphism is a reflection for a suitable $\alpha$.

**Proof.** The reflection is $c_u\alpha$ by the corollary, so it lies in the coset; conversely an element of the coset is $c_u\alpha$, and it is an involution exactly when $u$ is a reflector. The map $[u]\mapsto[c_u]$ is the standard isomorphism $\mathcal{A}^\times/Z(\mathcal{A})^\times\to\mathrm{Inn}(\mathcal{A})$. $\square$

## The Degenerate Cases

**Theorem (the inner grade involution).** Suppose $\alpha = c_z$ for a unit $z$. Then

$$
\rho_u = c_{u*z}, \qquad \mathrm{Ref}(\mathcal{A},\alpha) = \{\text{involutive inner automorphisms}\},
$$

so the reflections are exactly the inner automorphisms of $\mathcal{A}$ of order two, with reflector condition $u*z*u*z^{-1} \in Z(\mathcal{A})$.

**Proof.** $\rho_u = c_u\alpha = c_uc_z = c_{u*z}$, an inner automorphism; it is an involution exactly when $(u*z)*f*(u*z)^{-1} = f$ for all $f$, that is when $u*z\in Z(\mathcal{A})$. $\square$

**Theorem (the commutative case).** If $G$ is abelian then every unit is a reflector and $\rho_u = \alpha$ for every unit $u$; the reflection family collapses to the two-element group $\{\mathrm{id},\alpha\}$ and the correspondence $u\mapsto\rho_u$ is constant on the units.

**Proof.** In a commutative algebra every element is central, so every unit is a reflector and $\rho_u = c_u\alpha = \alpha$; the reflections are therefore only $\alpha$, together with $\mathrm{id}$ when $\alpha = \mathrm{id}$. $\square$

**Remark (the failure of the correspondence).** The map $u\mapsto\rho_u$ is neither injective nor, when $\alpha$ is not inner, surjective onto all involutive automorphisms: only the signed conjugations are reflections, and the involutive automorphisms outside the coset $\mathrm{Inn}(\mathcal{A})\alpha$ are not. The parametrisation is also not a group homomorphism in general, because the product of two reflections is an unsigned sandwich rather than a reflection; each reflection is individually of order two, and the reflections are a coset of the inner automorphisms, not a subgroup.

## The Group Instance

**Example (the discrete group).** Let $G$ be discrete and $\alpha = \alpha_\theta$ induced by an involutive automorphism of $G$. The reflectors among the point masses are the elements $h$ with $h\theta(h) \in Z(G)$, and

$$
\rho_{\delta_h}(\delta_g) = \delta_{h\theta(g)h^{-1}} ,
$$

so that the restriction of $\rho_{\delta_h}$ to the point masses is exactly the signed conjugation $\rho_h$ of *Reflections as Signed Two-Sided Operators on a Topological Group*; the fixed subalgebra $\mathcal{A}^+_\rho$ is the linear span of the fixed subgroup $\{g : \alpha(g) = h^{-1}gh\}$ together with the topological closedness inherited from $\ell^1(G)$.

**Example (the sign character and the two-element group).** Let $\alpha = \alpha_\varepsilon$ for a sign character and let $G$ be abelian. Then $\varepsilon$ is the only nontrivial reflection, the family is $\{\mathrm{id},\alpha_\varepsilon\}$, and the reflector condition is $h^2 \in Z(G) = G$, automatically satisfied by every unit: the correspondence is constant, in accordance with the commutative degeneracy. On a finite abelian group the two reflections are the identity and the sign, which is the group-algebra reading of the Fourier sign symmetry.

**Remark (the group-level dictionary).** The reflector condition $u*\alpha(u)\in Z(\mathcal{A})$, the square $\rho_u^2 = c_{u*\alpha(u)}$, the parametrisation by $Z(\mathcal{A})^\times$ and the two degenerate cases are the group-algebra form of the dictionary of *Involutive Topological Groups* and *Reflections as Signed Two-Sided Operators on a Topological Group*; on the point masses of a discrete group the latter theory is recovered exactly, and on a non-discrete group only the integrable reflections survive.

## Summary

A reflection of the group algebra $\mathcal{A} = L^1(G)$ with respect to the invertible twist $\alpha$ is the signed conjugation $\rho_u(f) = u*\alpha(f)*u^{-1} = S_{u,u^{-1}}$, a bounded algebra automorphism with $\rho_u = c_u\alpha = \alpha c_{\alpha(u)}$ and square $c_{u*\alpha(u)}$; it is an involutive automorphism exactly when $u$ is a **reflector**, $u*\alpha(u)\in Z(\mathcal{A})$. An involutive reflection splits $\mathcal{A} = \mathcal{A}^+_\rho\oplus\mathcal{A}^-_\rho$ into a closed fixed subalgebra and a closed negated part with the multiplication table of a grading, and it is determined by its fixed subalgebra. The map $u\mapsto\rho_u$ is a surjection of the reflectors onto the reflections with kernel the central units, so the reflections are parametrised by $R^\times(\mathcal{A},\alpha)/Z(\mathcal{A})^\times$, and they are exactly the involutive automorphisms in the coset $\mathrm{Inn}(\mathcal{A})\alpha$, mapping to $\mathrm{Out}(\mathcal{A})$ by the class of the inner part. When $\alpha$ is inner every reflection is an inner automorphism, $c_{u*z}$; when $G$ is abelian every unit is a reflector, every reflection equals $\alpha$, and the family collapses to $\{\mathrm{id},\alpha\}$. The correspondence is neither injective nor, for a non-inner $\alpha$, surjective onto all involutive automorphisms, and the reflections form a coset of the inner automorphisms rather than a subgroup. On a discrete group the point masses reproduce the signed conjugations of the topological-group theory; the adjoint and the measure algebra are the `- * Operator Theory` group and *The Involution on the Measure Algebra*.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathcal{A} = L^1(G)$, $Z(\mathcal{A})$, $\mathcal{A}^\times$ | Group algebra, centre, unit group |
| $\alpha$, $\mathrm{A}f = \alpha(f)$, $c_t(f) = t*f*t^{-1}$ | Grade involution; inner automorphism |
| $\rho_u = c_u\alpha = S_{u,u^{-1}}$ | Reflection by the unit $u$, $\rho_u(f) = u*\alpha(f)*u^{-1}$ |
| $R^\times(\mathcal{A},\alpha)$ | Reflectors: units with $u*\alpha(u)\in Z(\mathcal{A})$ |
| $\mathrm{Ref}(\mathcal{A},\alpha)\cong R^\times(\mathcal{A},\alpha)/Z(\mathcal{A})^\times$ | Reflections and their parametrisation |
| $\rho_u^2 = c_{u*\alpha(u)}$ | Square; involution iff $u$ is a reflector |
| $\mathcal{A}^+_\rho$, $\mathcal{A}^-_\rho$ | Fixed subalgebra and negated part of $\rho$ |
| $\rho_1 = \alpha$ | The grade involution is a reflection |
| $\mathrm{Inn}(\mathcal{A})\alpha$, $\mathrm{Out}(\mathcal{A})$ | The coset of the reflections; the outer quotient |
| $\rho_{\delta_h}(\delta_g) = \delta_{h\theta(g)h^{-1}}$ | Group instance on a discrete group |

## Further Reading

- Richard S. Pierce, *Associative Algebras*, Graduate Texts in Mathematics 88 (Springer, 1982), for involutive automorphisms, signed conjugations and the correspondence with the units.
- Nathan Jacobson, *Structure of Rings*, American Mathematical Society Colloquium Publications 37 (1964), for inner automorphisms, the cosets of the automorphism group and the reflections.
- Charles E. Rickart, *General Theory of Banach Algebras* (Van Nostrand, 1960), for bounded automorphisms of a Banach algebra and their closed fixed subalgebras.
- Theodore W. Palmer, *Banach Algebras and the General Theory of ${}^*$-Algebras, Volume I* (Cambridge University Press, 1994), for graded Banach algebras, automorphisms of order two and reflections.
- Ian R. Porteous, *Clifford Algebras and the Classical Groups* (Cambridge University Press, 1995), for the sandwich action and the reflections it generates.
