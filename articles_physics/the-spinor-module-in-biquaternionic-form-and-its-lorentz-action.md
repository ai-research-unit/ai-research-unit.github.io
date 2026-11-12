# __The Spinor Module in Biquaternionic Form and Its Lorentz Action__

## Introduction

The biquaternion algebra $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ is simple, and it has one simple module. The Lorentz group acts on that module by multiplication on one side. Those two facts are the subject of this article.

Two actions are compared throughout. The article [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) reads the four-vector as an element of the anti-Hermitian sector $\mathbb{B}_{\Phi}$ and the Lorentz group as acting on it by the **Hermitian pair**,

$$
\tilde Q\;\longmapsto\;\tilde U_{\mathrm{lor}}\,\tilde Q\,\tilde U_{\mathrm{lor}}{}^{*}.
$$

The action of this article is **one-sided**: the group multiplies the field on the left,

$$
\tilde X\;\longmapsto\;\tilde U_{\mathrm{lor}}\,\tilde X .
$$

The difference is not a matter of notation. The element $-e_t$ acts trivially by the two-sided operator on $\mathbb{B}_{\Phi}$ and as minus the identity by the one-sided action, so the four-vector action descends to the Lorentz group and the one-sided action does not. The one-sided action is a representation of the double cover.

**The field is an element of the algebra.** An element multiplies an element, and the module structure is the multiplication of the algebra; no array and no list of components enters the statement. The field carries four complex numbers, and they are the coefficients of one element.

**The conventions are cited, not restated.** The algebra, its units and its conjugations are *Algebra and Element Conventions*; the twelve products and the four forms are *Product and Form Conventions*; the values of the subscript, the frame and its metric are *Matrix Representations Conventions* and *Frame and Metric Conventions*; the group of unit-norm elements, written $SL(2,\mathbb{C})$, is *Norm and Pairing Conventions*; the derivative is *Operator and Calculus Conventions*. No formula of theirs is printed below. What the article adds is the module: its two values, the action on it, the forms it carries, and the map to the Hermitian sector.

Two words are used in one sense each. **The module** is the module of the algebra, and the field is an element on which the algebra acts by left multiplication. **The value** is what the test returns, $L$ or $R$, fixed in *Matrix Representations Conventions*, §*The Subscript on an Element*.

## The Algebra and Its Module

### The Algebra Is Simple

**One simple module.** The algebra is isomorphic to $M_2(\mathbb{C})$ (*Matrix Representations Conventions*, §*The Isomorphism*), so it is simple: no two-sided subspace of it is carried into itself by every product except zero and the whole. A finite-dimensional module of a simple algebra is a direct sum of copies of one simple module, and that module is of complex dimension two.

The isomorphism is named once, for those two facts, and it is not used. This article computes no array, and every statement below is a statement about elements and their products.

**The invariants come from the element.** The quaternionic norm of an element is the determinant of its image, and its scalar part is half the trace (*Matrix Representations Conventions*, §*The Isomorphism*). The article quotes neither; it uses the group of elements of norm one, which is defined in *Norm and Pairing Conventions*, §*The Unitary Convention*.

### The Algebra as Its Own Module

**The regular module.** The algebra acts on itself by left multiplication: the product $\tilde a\tilde X$ is linear in $\tilde X$, and $\tilde a(\tilde b\tilde X)=(\tilde a\tilde b)\tilde X$ by associativity. The algebra read this way is the **regular module**, and it is a direct sum of two copies of the simple module. It is the carrier of this article, and the field is an element of it.

**The two copies are the two values.** Every element is the sum of one part of each value, each part is of complex dimension two, and only the zero element is both. A product takes the value of its right factor, and a left multiplication keeps the value. Those four facts are those of *Matrix Representations Conventions*, §*The Subscript on an Element*; they are used here and not proved.

**The values are subspaces.** Each value is a subspace of complex dimension two which every left multiplication carries into itself. That is all the article needs: the action of the group is well defined on each value, and no decomposition beyond the two values is made. No basis of either value is chosen below.

**The action written out.** For an element $\tilde a$ and a field $\tilde X$, the action is the product $\tilde a\tilde X$. Its two properties are $\mathbb{C}$-linearity in the field and $(\tilde a\tilde b)\tilde X=\tilde a(\tilde b\tilde X)$; both are the bilinearity and the associativity of the product. No basis and no array enter either line.

## The Two Halves

**The two modules of the group.** The group of unit-norm elements has two inequivalent two-dimensional complex modules. The first is the simple module of the algebra, of label $(\tfrac12,0)$ in the classification of [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html). The second is its conjugate, of label $(0,\tfrac12)$. Both are of complex dimension two, and both are carried by the same complex vector space.

**The conjugate action.** On the conjugate module the group acts through the coefficient bar,

$$
\tilde X\;\longmapsto\;\bar{\tilde U}_{\mathrm{lor}}\,\tilde X .
$$

The bar is an automorphism of the algebra, it conjugates the norm, and on an element of norm one its value is again of norm one; the assignment $\tilde U_{\mathrm{lor}}\mapsto\bar{\tilde U}_{\mathrm{lor}}$ is therefore an automorphism of the group, and the action is a genuine representation. The bar is the coefficient conjugation of *Algebra and Element Conventions*, and it is not the Hermitian conjugation: the star composes the bar with the quaternion sign.

**The two halves are not the two values.** The field is one element $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}$, and its two parts are the two values. Both parts carry the same action of the group: a left multiplication multiplies both by $\tilde U_{\mathrm{lor}}$, so the two parts are two copies of one module. The inequivalence of the two labels belongs to the pair of modules $(S,\bar S)$ and not to the two values of one element.

**The algebra cannot see the difference.** The algebra is simple and has one simple module, so both values are copies of it; a difference between the two halves is not a property of the algebra and no subspace of the algebra carries it. The conjugate module is not a module for the algebra at all: the assignment $\tilde U_{\mathrm{lor}}\mapsto\bar{\tilde U}_{\mathrm{lor}}$ conjugates the scalar $i$, so it is not $\mathbb{C}$-linear in the algebra element, and the action is not the restriction of a $\mathbb{C}$-linear action of the algebra.

**The four-dimensional module of the group.** The direct sum $S\oplus\bar S$ is a module for the group, of complex dimension four, and its two summands carry the two labels. It is not a module for the algebra. The field of this article also carries four complex numbers, but it carries them as one element of $\mathbb{B}$; the two objects have the same dimension and different structure.

**The value is a label.** The value is the subscript, read from the frame, and it takes the two values fixed in *Matrix Representations Conventions*, §*The Subscript on an Element*. The article introduces no operator and no second element to carry it.

**The two halves are exchanged by parity.** Parity is a transformation of the full Lorentz group and not of its restricted component, and it carries each label to the other (*The Reflection and the Rotation in Biquaternionic Form*, §*The Two Parts and the Reflection*). The two labels are therefore two, and no transformation of the restricted group exchanges them.

## The Unit-Norm Elements and the Double Cover

The group that acts is $SL(2,\mathbb{C})$, the group of elements of norm one, defined in *Norm and Pairing Conventions*, §*The Unitary Convention*. The article uses the group and prints no defining formula of it.

The subgroups relevant to the series sit inside it as follows.

| Element | Characterization | Sector |
|---|---|---|
| Pure boost $\tilde U_{\Psi,\mathrm b}=\cosh\frac{\zeta}{2}\,e_t+i\sinh\frac{\zeta}{2}\vec u_{\mathrm b}$ | Hermitian, norm one | $\mathbb{B}_{\Psi}$ |
| Pure rotation $\tilde u_{\mathrm r}=\cos\frac{\theta}{2}\,e_t+\sin\frac{\theta}{2}\vec u_{\mathrm r}$ | Real quaternion, norm one | $\mathbb{B}_{H}$ |
| General $\tilde U_{\mathrm{lor}}=\tilde U_{\Psi,\mathrm b}\tilde u_{\mathrm r}$ | Norm one | $\mathbb{B}$ |

A boost is Hermitian and satisfies $\tilde U_{\Psi,\mathrm b}^{*}=\tilde U_{\Psi,\mathrm b}$; boosts do not form a subgroup, because the product of two non-collinear boosts is a boost and a rotation. A rotation is a real quaternion, and the rotations form the subgroup $SU(2)=SL(2,\mathbb{C})\cap U(2)$.

**The two-sided operator.** The action on the four-vector sector is

$$
\pi:\;SL(2,\mathbb{C})\longrightarrow SO^{+}(1,3),\qquad
\pi(\tilde U_{\mathrm{lor}}):\;\tilde Q\longmapsto\tilde U_{\mathrm{lor}}\,\tilde Q\,\tilde U_{\mathrm{lor}}{}^{*},\qquad \tilde Q\in\mathbb{B}_{\Phi} .
$$

It is well defined, because the Hermitian conjugate of an anti-Hermitian element is anti-Hermitian; it preserves the quaternionic norm; and it is a homomorphism, because the star reverses the order. Its kernel is

$$
\ker\pi=\{\pm e_t\}\cong\mathbb{Z}/2\mathbb{Z},
$$

since $-e_t$ is central and the two signs cancel in the two-sided operator, $(-\tilde U_{\mathrm{lor}})\tilde Q(-\tilde U_{\mathrm{lor}})^{*}=\tilde U_{\mathrm{lor}}\tilde Q\tilde U_{\mathrm{lor}}{}^{*}$ for every $\tilde Q$. Hence $\pi$ is two-to-one onto the proper orthochronous Lorentz group, and $SL(2,\mathbb{C})$ is its double cover.

**The one-sided action is faithful.** On the module the same element acts by

$$
(-e_t)\tilde X=-\tilde X ,
$$

so $\tilde U_{\mathrm{lor}}$ and $-\tilde U_{\mathrm{lor}}$ act differently on every field. The defining representation therefore does not descend to $SO^{+}(1,3)$: it is a genuine representation of the double cover. That is the exact sense in which the one-sided action and the two-sided operator differ by the double cover.

## The Lorentz Action on the Module

### The Action

The group acts on the module by left multiplication:

$$
\boxed{\;\tilde X\;\longmapsto\;\tilde U_{\mathrm{lor}}\,\tilde X,\qquad \tilde U_{\mathrm{lor}}\in SL(2,\mathbb{C}),\quad \tilde X\in\mathbb{B}\;}
$$

The action is $\mathbb{C}$-linear in the field, it preserves each value, and it is a group action:

$$
\tilde U_{\mathrm{lor},2}\bigl(\tilde U_{\mathrm{lor},1}\tilde X\bigr)=\bigl(\tilde U_{\mathrm{lor},2}\tilde U_{\mathrm{lor},1}\bigr)\tilde X .
$$

No two-sided action appears. That is the defining feature of the module: one factor of the group element multiplies the field, and it multiplies it on the left. On the conjugate module the same group acts through the bar, and the two actions are the two labels of §*The Two Halves*.

### Boosts and Rotations as Exponentials

A boost along the direction $\vec u_{\mathrm b}$ with rapidity $\zeta$ is the exponential of its generator, because the generator squares to the unit:

$$
\tilde U_{\Psi,\mathrm b}=\exp\Bigl(\frac{\zeta}{2}\,i\vec u_{\mathrm b}\Bigr),
\qquad (i\vec u_{\mathrm b})^2=e_t .
$$

A rotation about $\vec u_{\mathrm r}$ by the angle $\theta$ is the exponential of its generator, because that generator squares to minus the unit:

$$
\tilde u_{\mathrm r}=\exp\Bigl(\frac{\theta}{2}\,\vec u_{\mathrm r}\Bigr),
\qquad \vec u_{\mathrm r}^{\,2}=-e_t .
$$

The two displays are the two signs of the square, and neither needs an array. A rotation by $2\pi$ gives $\tilde u_{\mathrm r}=-e_t$: it is the identity by the two-sided operator and minus the identity on the module. A rotation by $4\pi$ is the identity on both.

### The Generators

The Lie algebra $\mathfrak{sl}(2,\mathbb{C})$ consists of the traceless elements, and in the units of the algebra it is

$$
\mathfrak{sl}(2,\mathbb{C})=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}\;\oplus\;\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}.
$$

The first summand is the compact part, the pure quaternions, and its three elements square to $-e_t$; the second is the non-compact part, in $\mathbb{B}_{\Psi}$, and its three elements square to $+e_t$. The two summands are the rotations and the boosts. On the module the six generators act by left multiplication, and that action is the defining action of the group: the module is of complex dimension two, the algebra acts on it as all its $\mathbb{C}$-linear endomorphisms, and the representation is the fundamental one. No further object is needed to say so.

### The Compact Subgroup

The compact subgroup $SU(2)\subset SL(2,\mathbb{C})$ consists of the elements of norm one that are also $*$-unitary, that is, the unit quaternions (*Norm and Pairing Conventions*, §*The Unitary Convention*). Its action on the module preserves the Hermitian form of §*The Invariant Forms*, and it is the double cover of the spatial rotation group $SO(3)$. A boost is not $*$-unitary and does not preserve that form; the non-compactness of the group is exactly that failure.

## The Invariant Forms

### The Quaternionic Form

The quaternionic form $\langle\cdot,\cdot\rangle_{\natural}$ of *Product and Form Conventions* is the invariant bilinear form of the module. For an element $\tilde U$ of norm one,

$$
\bigl\langle\tilde U\tilde X,\tilde U\tilde Y\bigr\rangle_{\natural}=\bigl\langle\tilde X,\tilde Y\bigr\rangle_{\natural},
$$

because the quaternion sign reverses the order of a product and $\tilde U^{\natural}\tilde U=e_t$. The form is therefore invariant under the whole group, and none of the other three forms of *Product and Form Conventions* is.

**It vanishes on one value.** Two elements of the same value are never paired by it: the form is identically zero on each value. It pairs one value with the other, and on that pair it is nondegenerate. The dual of one value is therefore the other value; since the two values are isomorphic as modules, each value is self-dual.

**Self-duality is not self-conjugacy.** The dual of a value is a value, and the conjugate module is not: the first is a module for the algebra, the second is a module for the group alone. The two statements are often written as one, and they are two.

### The Hermitian Form

The value carries a positive definite Hermitian form, and the conventions do not own it, so it is defined here as a derived form of this article. For two elements of one value,

$$
h(\tilde X,\tilde Y)=2\,\mathrm{Sc}\bigl(\tilde X^{*}\tilde Y\bigr),
\qquad h(\tilde X,\tilde X)>0\ \text{for}\ \tilde X\neq0 .
$$

It is $\mathbb{C}$-linear in the second argument and conjugate-linear in the first, and it is positive definite on each value. Its invariance is the compact one:

$$
h\bigl(\tilde U\tilde X,\tilde U\tilde Y\bigr)=h(\tilde X,\tilde Y)
\quad\Longleftrightarrow\quad
\tilde U^{*}\tilde U=e_t .
$$

The warrant is one line: the star reverses the order, so the product carries $\tilde U^{*}\tilde U$ between the two fields, and the scalar part is unchanged only when that factor is the unit. The form is therefore invariant exactly on the compact subgroup $SU(2)$ and on no boost. It selects the maximal compact subgroup of the group; it does not define an invariant structure on the module under the whole group.

### The Indefinite Form

A second Hermitian form is obtained by twisting the first by a fixed direction. Let $\tilde U_{\mathrm{ax}}$ be a fixed Hermitian element squaring to the unit, taken here as $\tilde U_{\mathrm{ax}}=i\vec e_z$; the direction is the declared one of the frame, and any other direction gives a conjugate form. Define, for two elements of one value,

$$
[X\,|\,Y]=2\,\mathrm{Sc}\bigl(\tilde X^{*}\tilde U_{\mathrm{ax}}\tilde Y\bigr).
$$

The form is Hermitian, and on a value it has signature $(1,1)$: one direction is positive and one is negative. It is invariant under the elements that fix the direction,

$$
[X\,|\,Y]\ \text{invariant}
\quad\Longleftrightarrow\quad
\tilde U^{*}\tilde U_{\mathrm{ax}}\tilde U=\tilde U_{\mathrm{ax}} ,
$$

and that stabiliser is of real dimension three: it contains the rotations about the direction and the two boosts transverse to it, those three elements span its Lie algebra, and it is the group $SU(1,1)$ of the companion articles. The definite form and the indefinite one therefore select the two real forms of the same complex group, the compact one and the non-compact one, and neither is a change of basis of the other.

### The Mixed Pairing

One expression serves the two labels. Read $h(\tilde X,\tilde Y)$ with the first factor carrying the action of $\tilde U$ and the second the action of $\bar{\tilde U}$:

$$
h\bigl(\tilde U\tilde X,\;\bar{\tilde U}\tilde Y\bigr)=h(\tilde X,\tilde Y).
$$

The warrant is the identity $\tilde U^{*}\bar{\tilde U}=e_t$, which holds for every element of norm one because the bar is an automorphism and $\tilde U^{*}=\overline{\tilde U^{\natural}}$. The pairing is therefore invariant between the defining module and its conjugate, and it is the scalar bilinear that pairs the two labels. Read with the same action on both factors it is not invariant, and that difference is what separates the two labels.

| Form | Arguments | Invariance group | Role |
|---|---|---|---|
| $\langle\tilde X,\tilde Y\rangle_{\natural}$ | one value with the other | the whole group | the invariant bilinear form; self-duality |
| $h(\tilde X,\tilde Y)$ | one value | the compact $SU(2)$ | positive definite; the compact real form |
| $[X\,\vert\,Y]$ | one value | the stabiliser of $\tilde U_{\mathrm{ax}}$, $SU(1,1)$ | indefinite; the non-compact real form |
| $h(\tilde X,\tilde Y)$ with $\bar{\tilde U}$ on the second factor | a value, and the conjugate action on the second factor | the whole group | the pairing of the two labels |

### The Map to the Hermitian Sector

For two elements of one value, the Hermitian part of their product lands in the Hermitian sector:

$$
\tilde H_\Psi=\tfrac12\bigl(\tilde X\tilde Y^{*}+\tilde Y\tilde X^{*}\bigr)\in\mathbb{B}_{\Psi},
\qquad
\tilde H_\Psi\longmapsto\tilde U_{\mathrm{lor}}\tilde H_\Psi\tilde U_{\mathrm{lor}}{}^{*}.
$$

The element $\tilde H_\Psi$ is Hermitian for every pair, and the two-sided operator carries it to the two-sided operator of the transformed pair, so the map is equivariant under the whole group. It is the algebraic form of the map from a pair of fields to a four-vector, and the four-vector is the element $i\tilde H_\Psi$ of $\mathbb{B}_{\Phi}$.

**The single field gives a null element.** For $\tilde Y=\tilde X$ the element is $\tilde X\tilde X^{*}$, it is Hermitian, and it is null: its quaternionic norm vanishes, because a product of two zero divisors is a zero divisor. Its scalar part is half the Hermitian norm of the field,

$$
\mathrm{Sc}\bigl(\tilde X\tilde X^{*}\bigr)=\tfrac12\,h(\tilde X,\tilde X),
$$

and its three spatial coefficients are purely imaginary with squares summing to minus the square of the scalar part. The four coefficients therefore satisfy

$$
\bigl(\mathrm{Sc}\,\tilde X\tilde X^{*}\bigr)^2+\bigl(\tilde X\tilde X^{*}\bigr)_x^2+\bigl(\tilde X\tilde X^{*}\bigr)_y^2+\bigl(\tilde X\tilde X^{*}\bigr)_z^2=0,
$$

which is the statement that the four-vector of one field lies on the light cone. The level set $h(\tilde X,\tilde X)=2r$ is the set of fields whose Hermitian image has scalar part $r$, and the spatial coefficients of that image form the sphere of radius $r$ about the origin. With the indefinite form in place of the definite one the same construction gives the two-sheeted hyperboloid, and those are the two models of the source.

**The three surfaces of the source.** The sphere, the two-sheeted hyperboloid and the single-sheeted one are the images of the level sets of the three forms under this map, read with the three signatures. The source models them with its own arrays, and that modelling is recorded in J. D. Simão's article cited in §*Further Reading*; the three forms above are the invariant objects behind the three models.

## One-Sided Action Versus the Two-Sided Operator

The preceding sections separate two actions that are often conflated. The comparison is worth stating once in a table.

| Question | One-sided action | Hermitian pair |
|---|---|---|
| Object acted on | $\tilde X\in\mathbb{B}$ | $\tilde Q\in\mathbb{B}_{\Phi}$ |
| Action | $\tilde X\mapsto\tilde U_{\mathrm{lor}}\tilde X$ | $\tilde Q\mapsto\tilde U_{\mathrm{lor}}\tilde Q\tilde U_{\mathrm{lor}}{}^{*}$ |
| Factors of $\tilde U_{\mathrm{lor}}$ | one | two |
| Action of $-e_t$ | $-\mathrm{id}$ | $+\mathrm{id}$ |
| Kernel | $\{e_t\}$ | $\{\pm e_t\}$ |
| Image group | $SL(2,\mathbb{C})$ | $SO^{+}(1,3)$ |
| Descends to $SO^{+}(1,3)$ | no | yes |

The entries are not a list of conventions; they are the content of the double cover. The elements $\tilde U_{\mathrm{lor}}$ and $-\tilde U_{\mathrm{lor}}$ describe the same Lorentz transformation of every four-vector, and opposite transformations of every field. A representation of $SO^{+}(1,3)$ cannot see the sign; a representation of $SL(2,\mathbb{C})$ can.

A common mistake is to "fix" the one-sided action by composing it with the two-sided operator, in the hope of making it two-sided. That composition changes the representation: it multiplies the number of factors by two, and it carries the field into the algebra. The field transforms in $(\tfrac12,0)$; an element $\tilde U_{\mathrm{lor}}\tilde Q\tilde U_{\mathrm{lor}}{}^{*}$ transforms in $(\tfrac12,0)\otimes(0,\tfrac12)=(\tfrac12,\tfrac12)$, which is the complexified vector representation, and the four-vector is its Hermitian slice. The one-sided action is therefore not a vector action in disguise; it is the fundamental action from which the vector action is built by tensor product.

The composition laws make the same point. For elements of norm one,

$$
\tilde U_{\mathrm{lor},2}\bigl(\tilde U_{\mathrm{lor},1}\tilde X\bigr)=\bigl(\tilde U_{\mathrm{lor},2}\tilde U_{\mathrm{lor},1}\bigr)\tilde X,
\qquad
\tilde U_{\mathrm{lor},2}\bigl(\tilde U_{\mathrm{lor},1}\tilde Q\tilde U_{\mathrm{lor},1}{}^{*}\bigr)\tilde U_{\mathrm{lor},2}{}^{*}
=\bigl(\tilde U_{\mathrm{lor},2}\tilde U_{\mathrm{lor},1}\bigr)\tilde Q\bigl(\tilde U_{\mathrm{lor},2}\tilde U_{\mathrm{lor},1}\bigr)^{*}.
$$

Both are group actions; they are actions on different objects, and neither reduces to the other.

## Why the Action Is One-Sided

The one-sided action is not a device of this article. It is the multiplication of the algebra, and the algebra acts on itself on the left whatever else is written.

**A two-sided operator has three factors and a module action has two.** A two-sided operator is a product of three: one factor on each side of the field. A module action is a product of two: one factor on one side. The difference is the difference between an endomorphism of a module and an endomorphism of the algebra, and the two are not the same object. That is why the two-sided operator acts on $\mathbb{B}_{\Phi}$ and the one-sided action acts on the module, and why neither can be read as the other.

**Each action has its own invariant subspace.** The two-sided operator carries $\mathbb{B}_{\Phi}$ into itself, because the Hermitian conjugate of an anti-Hermitian element is anti-Hermitian and the star reverses the order. The one-sided action carries each value into itself, because a left multiplication keeps the value. Each action has the invariant subspace it deserves, and the two invariant subspaces are different.

**Equal real dimension, different kind.** Both actions are of four real dimensions, and they differ in kind. The vector action is a real form: it is real four-dimensional, and its complexification is $S\otimes\bar S=(\tfrac12,\tfrac12)$, of complex dimension four. The one-sided action is genuinely complex two-dimensional, and it carries no invariant real structure, because such a structure would be an isomorphism $S\cong\bar S$ and the two labels are inequivalent. Equal real dimension, different kind.

**The origin of the value.** The value is read from the frame, and it is a property of the element and of the frame (*Matrix Representations Conventions*, §*The Subscript on an Element*). It is not an operator of the algebra, and no element of the algebra carries it.

## Open Questions

1. **The informational sector.** The companion article [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) identifies $\mathbb{B}_{\Psi}$ with the Hermitian observables of a two-state system. The module constructed here is the carrier on which those observables act, but the identification of a **state** with an element of the module is not made in this article. A pure state is an element of the form $\tilde X\tilde X^{*}$ up to a positive factor, and the field $\tilde X$ is a square root of it, defined up to a phase. Whether the phase is physical, and whether the informational sector requires the double cover or only its image in $SO^{+}(1,3)$, is left open.

2. **The covariance of the biquaternion Dirac equation.** The companion article [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) carries two equations, and they are not the same operator. The corpus's own equation is the **one-sided chiral pair**

    $$
    \tilde\nabla_\Phi\tilde{Ξ}_{R}=k_m\tilde{Ξ}_{L},
    \qquad
    (\tilde\nabla_\Phi)^{\natural}\tilde{Ξ}_{L}=k_m\tilde{Ξ}_{R},
    $$

    in which the gradient acts by left multiplication on the field $\tilde{Ξ}=\tilde{Ξ}_{L}+\tilde{Ξ}_{R}\in\mathbb{B}$ and the mass is the term that carries one value to the other. Kravchenko's equation is the **two-sided** single equation on $\mathbb{B}$,

    $$
    \mathcal{N}F=\left(i\frac{\partial}{\partial r'_t}+D_3\right)F-k_mi\,\overline{F}\,\vec e_z=0,
    $$

    in which the derivative acts on the left, the mass acts on the right through $\vec e_z$, and the conjugation supplies the antilinear part. The two are related by the dictionary, but the transformation law of the biquaternion-valued field $\tilde{Ξ}$ is still open. A natural candidate is the one-sided action defined here; its compatibility with the mass term requires the relation between that action and the conjugate module to be fixed by a convention. The one-sided pair is the definition; the two-sided form is a representation in which the mass is a right multiplication. Here $k_m=mc/\hbar$ is the mass wave number, the inverse of the mass length.

3. **The alternating pairing within a value.** The quaternionic form vanishes on each value and pairs the two values; an alternating scalar built from two fields of one value, the $\varepsilon$ of the older display, is not among the four forms of *Product and Form Conventions* and is not constructed here. Its expression in elements of the algebra is a matter of convention.

4. **Majorana fields and the real structure.** A Majorana field is fixed by a real structure commuting with the action. The module has such a structure only after a choice of conjugation, and the choice is not unique. The companion article [The Neutrino and Majorana Fermions in Biquaternionic Form](the-neutrino-and-majorana-fermions-in-biquaternionic-form.html) treats the physical case; the representation-theoretic classification of the possible real structures is not attempted here.

5. **Curved spacetime.** The construction is flat-spacetime representation theory. The soldering of the module to a curved manifold — a spin structure, a covariant derivative, and the conversion of the constant action into local frames — is the subject of the companion articles on the Einstein equation and on gravity, and is not repeated here.

6. **The indefinite form and the physical signature.** The forms $\langle\cdot,\cdot\rangle_{\natural}$, $h$ and $[\,\cdot\,|\,\cdot\,]$ are three different invariant forms on the same two-dimensional complex space. Only the last has an indefinite signature, and the indefinite signature is the one that matches the Lorentzian geometry of $\mathbb{R}^{1,2}$. Which of the three is the "physical" one is a question about the interpretation of the module, not about its representation theory; the article records all three and leaves the choice to the applications.

## The Legacy Pauli Gamma Formulation

The Pauli and gamma formulation is legacy: the reasons are explained in the article *Why AXF Matrices instead of Pauli and Gamma Matrices*. The generators carry no frame label: $\gamma_\mu$ is one set of matrices, and the frame is named on the coordinate.

The gamma matrices are a **frame** of the same basis operator algebra, written as $4\times4$ matrices on the regular module. They are displayed once, here, so that the body of the article can be read without them.

The gammas are a frame of $\mathrm{Cl}_{1,3}(\mathbb{C})\cong M_4(\mathbb{C})$, not a different algebra. In basis operator notation,

$$
\gamma_0=iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{pau},\vec e_y}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{pau},\vec e_z}R_{\mathrm{pau},\vec e_y},\qquad
\gamma_5=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}.
$$

The same in the axis-free display:

$$
\gamma_0=iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_x},\qquad
\gamma_1=iL_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_2=iL_{\mathrm{axf},\vec e_y}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_3=iL_{\mathrm{axf},\vec e_z}R_{\mathrm{axf},\vec e_y},\qquad
\gamma_5=-iL_{\mathrm{axf},e_t}R_{\mathrm{axf},\vec e_z}.
$$

Each is a one-basis operator product, and each satisfies the anticommutation relations appropriate to the signature: $\gamma_0^2=I_4$, $\gamma_\eta^2=-I_4$ for $\eta=1,2,3$, and $\gamma_\mu\gamma_\nu+\gamma_\nu\gamma_\mu=2\varepsilon_\mu\delta_{\mu\nu}I_4$ with $\varepsilon=(1,-1,-1,-1)$. The fifth is the product of the other four, $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$, and it satisfies $\gamma_5^2=I_4$. As an operator, $\gamma_5$ **is** the chirality basis operator $\Gamma=-iL_{\mathrm{pau},e_t}R_{\mathrm{pau},\vec e_z}$ of §*The Two Chiral Halves* — one operator, written once as a basis operator and once as a matrix of the frame. The algebra element behind the basis operator is the central grading $\xi$ of the complexification, which is not a gamma matrix; the body of the article uses $\xi$ and never needs a gamma symbol.

A single basis operator $L_aR_b$ is a pure tensor of $\mathbb{B}\otimes\mathbb{B}_{\mathrm{opp}}$, of tensor rank one; as an operator on $\mathcal{S}_{\mathrm{rep}}$ its rank is four whenever $a$ and $b$ are invertible, so the two ranks must not be confused. The pure basis operators form the seven-dimensional cone of rank at most one, and a general element is a sum of at most four of them. Two basis operators multiply by $L_aR_b\,L_cR_d=L_{ac}R_{db}$, the right factors in reverse order, and the products of the four frame basis operators $\gamma_0,\dots,\gamma_3$ give the usual sixteen-element Clifford basis. Every sign among them comes from $i^2=-1$ together with $\vec e_\eta^2=-e_t$: for instance

$$
\gamma_0\gamma_1=i^2L_{\mathrm{pau},e_t\vec e_x}R_{\mathrm{pau},\vec e_y\vec e_x}=-L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_y\vec e_x}=L_{\mathrm{pau},\vec e_x}R_{\mathrm{pau},\vec e_z},
$$

In the axis-free display:

$$
\gamma_0\gamma_1=i^2L_{\mathrm{axf},e_t\vec e_x}R_{\mathrm{axf},\vec e_y\vec e_x}=-L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_y\vec e_x}=L_{\mathrm{axf},\vec e_x}R_{\mathrm{axf},\vec e_z},
$$

and the same four steps give $\gamma_0\gamma_1\gamma_2\gamma_3=-i\Gamma$, that is $\gamma_5=i\gamma_0\gamma_1\gamma_2\gamma_3$ with $\Gamma$ the chirality basis operator.

The dictionary is complex-linear: the five basis operators are a complex frame, and their sixteen products are the sixteen-element Clifford basis. What the frame does **not** fix is the real slice. Both $\mathrm{Cl}_{1,3}(\mathbb{R})\cong M_2(\mathbb{H})$ and $\mathrm{Cl}_{3,1}(\mathbb{R})\cong M_4(\mathbb{R})$ are real forms of the same complex algebra $\mathrm{Cl}_{4}(\mathbb{C})\cong M_4(\mathbb{C})$, and they are not isomorphic to one another. The signs in the display above are the ones that make $\vec e_x,\vec e_y,\vec e_z$ spacelike bivectors, that is the signature $(1,3)$; the other choice of signs describes the other real form, and the complex frame cannot tell the two apart. The choice is made once, in [Matrix Representations: Conventions](matrix-representations-conventions.html), and it is held throughout the series.

**The display.** Every array printed in this section is given twice: in the Peirce display first, labelled $\mathrm{pau}$, whose arrays are the ones the literature prints, and in the axis-free display after it, labelled $\mathrm{axf}$, which is the display of the body and of the corpus. The two are carried into one another by $L_{\mathrm{axf},e_\mu}=C_{\Pi}L_{\mathrm{pau},e_\mu}C_{\Pi}^{-1}$, and a conjugation by $C_{\Pi}$ changes no product, no anticommutator, no trace and no determinant, so every identity of the section holds in both. An array is a statement about one display; a basis operator named in the running text keeps the Peirce label, and its axis-free array is the conjugate. The label names the array and not the operator.

## Summary

The module is the unique simple module of $\mathbb{B}\cong M_2(\mathbb{C})$. It is the carrier of the defining action of $SL(2,\mathbb{C})$ and of its conjugate, and it is the object on which the group acts by left multiplication. The main results are:

- **The algebra is simple.** It has one simple module, of complex dimension two, and the regular module is the direct sum of two copies of it. The field of the article is an element of the algebra, and the algebra acts on it by the product $\tilde a\tilde X$.
- **The two copies are the two values.** Every element is the sum of one part of each value, each part is of complex dimension two, and only the zero element is both. A product takes the value of its right factor, and a left multiplication keeps the value.
- **The action is one-sided.** $\tilde X\mapsto\tilde U_{\mathrm{lor}}\tilde X$; the four-vector action is the two-sided operator $\tilde Q\mapsto\tilde U_{\mathrm{lor}}\tilde Q\tilde U_{\mathrm{lor}}{}^{*}$.
- **The double cover is the kernel.** $\ker\pi=\{\pm e_t\}$ acts trivially on $\mathbb{B}_{\Phi}$ and as $-\mathrm{id}$ on the module; the one-sided action is faithful, the vector action is not.
- **The two halves are $S$ and $\bar S$.** They are the two labels $(\tfrac12,0)$ and $(0,\tfrac12)$, the second carrying the action of $\bar{\tilde U}_{\mathrm{lor}}$. They are not the two values of one element: the algebra is simple, both values are copies of $S$, and the conjugate module is not a module for the algebra.
- **The module carries four invariant forms.** The quaternionic form is invariant under the whole group and pairs one value with the other; the Hermitian form $h$ is positive definite and invariant exactly on the compact $SU(2)$; the indefinite form $[\,\cdot\,|\,\cdot\,]$ is invariant exactly on the stabiliser of a direction, the group $SU(1,1)$; and $h$ with the conjugate action on the second factor pairs the two labels.
- **The map to the Hermitian sector.** A pair of fields gives the Hermitian element $\tfrac12(\tilde X\tilde Y^{*}+\tilde Y\tilde X^{*})$, equivariant under the two-sided operator, and a single field gives a null Hermitian element whose scalar part is half its Hermitian norm. The vector action is the tensor square of the one-sided action.

What the article does **not** supply is a dynamics. It supplies the carrier, the action, the invariant forms and the map to four-vectors; the Dirac equation, the mass terms and the gauge couplings are the subjects of the companion articles.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $\mathbb{B}=\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$ | Biquaternion algebra, $\cong M_2(\mathbb{C})$ |
| $e_t=1,\vec e_x,\vec e_y,\vec e_z$ | Quaternion basis, $\vec e_\eta^2=-e_t$, $\vec e_x\vec e_y=\vec e_z$ |
| $i$ | Scalar imaginary, $i^2=-1$ |
| $\bar{\tilde{Q}}$, $\tilde{Q}^{\natural}$, $\tilde{Q}^{*}$ | Coefficientwise complex, quaternion, and Hermitian conjugates; $\tilde{Q}^{*}=\overline{\tilde{Q}^{\natural}}$ |
| $\mathbb{B}_{\Phi}$, $\mathbb{B}_{\Psi}$ | Anti-Hermitian and Hermitian sectors; material and informational |
| $\tilde X_L,\tilde X_R$ | The two parts named by the subscript; a product takes the value of its right factor, and a left multiplication keeps the value |
| $S$, $\bar S$ | The defining module $(\tfrac12,0)$ and its conjugate $(0,\tfrac12)$ |
| $\tilde U_{\mathrm{lor}}$ | Element of norm one, $SL(2,\mathbb{C})$ |
| $\tilde X\mapsto\tilde U_{\mathrm{lor}}\tilde X$ | The one-sided action on the module |
| $\tilde X\mapsto\bar{\tilde U}_{\mathrm{lor}}\tilde X$ | The conjugate action on $\bar S$ |
| $\tilde Q\mapsto\tilde U_{\mathrm{lor}}\tilde Q\tilde U_{\mathrm{lor}}{}^{*}$ | The Hermitian pair on $\mathbb{B}_{\Phi}$ |
| $\langle\tilde X,\tilde Y\rangle_{\natural}$ | The quaternionic form; the invariant bilinear form of the module |
| $h(\tilde X,\tilde Y)=2\,\mathrm{Sc}(\tilde X^{*}\tilde Y)$ | The positive definite Hermitian form of a value; invariant on $SU(2)$ |
| $[X\,\vert\,Y]=2\,\mathrm{Sc}(\tilde X^{*}\tilde U_{\mathrm{ax}}\tilde Y)$, $\tilde U_{\mathrm{ax}}=i\vec e_z$ | The indefinite Hermitian form of a value; invariant on the stabiliser of $\tilde U_{\mathrm{ax}}$, $SU(1,1)$ |
| $\tfrac12(\tilde X\tilde Y^{*}+\tilde Y\tilde X^{*})$ | The map to $\mathbb{B}_{\Psi}$; the four-vector is $i$ times it |

## Further Reading

- [Why AXF Matrices instead of Pauli and Gamma Matrices](why-axf-matrices-instead-of-pauli-and-gamma-matrices.html), for the reasons the AXF matrices replace the Pauli and gamma matrices.

**Companion articles.**

- [The Material Sector: Four-Vectors, Interval and Lorentz Action](the-material-sector-four-vectors-interval-and-lorentz-action.html) — the two-sided action on $\mathbb{B}_{\Phi}$ and the identification of the four-vector.
- [The Informational Sector: States, Observables and Probability](the-informational-sector-states-observables-and-probability.html) — the Hermitian observables and the two-state system.
- [The Lorentz Group in Biquaternionic Form — Structure and Representations](the-lorentz-group-in-biquaternionic-form-structure-and-representations.html) — the classification $(\tfrac12,0)$ and $(0,\tfrac12)$ used here.
- [The Dirac Equation in Biquaternionic Form](the-dirac-equation-in-biquaternionic-form.html) — the one-sided chiral pair and its two-sided Kravchenko form.
- [The Unpolarized Module of the Biquaternion Algebra](../articles_maths/the-unpolarized-module-of-the-biquaternion-algebra.html) — the central sign of the complexification and the two halves.
- [The Reflection and the Rotation in Biquaternionic Form](the-reflection-and-the-rotation-in-biquaternionic-form.html) — the discrete symmetries that exchange the two halves.
- [Matrix Representations: Conventions](matrix-representations-conventions.html) — the two frames, the two displays, and the subscript on an element.

**External references.**

- Roger Penrose and Wolfgang Rindler, *Spinors and Space-Time*, Vol. 1 (Cambridge, 1984), for the standard two-component calculus, the invariant $\epsilon$-form, and the two Weyl modules.
- Pertti Lounesto, *Clifford Algebras and Spinors* (Cambridge, 2001), for the construction of the module and the double cover of the Lorentz group.
- Chris Doran and Anthony Lasenby, *Geometric Algebra for Physicists* (Cambridge, 2003), for the rotor formulation of the Lorentz group and the relation between fields and four-vectors.
- David Hestenes, *Space-Time Algebra* (Gordon and Breach, 1966), for the original formulation of the Lorentz transformations in the even subalgebra.
- P. A. M. Dirac, "The quantum theory of the electron," *Proceedings of the Royal Society A* **117** (1928) 610–624, for the original representation of the electron.
- Steven Weinberg, *The Quantum Theory of Fields*, Vol. 1 (Cambridge, 1995), for the representation theory of the Lorentz group and the construction of the Dirac field from two Weyl fields.
- Julius Wess and Jonathan Bagger, *Supersymmetry and Supergravity* (Princeton, 1992), for the two-component conventions.
- William Fulton and Joe Harris, *Representation Theory: A First Course* (Springer, 1991), for the modules of $M_2(\mathbb{C})$, the highest-weight classification, and the Clebsch–Gordan rule.
- T. Y. Lam, *A First Course in Noncommutative Rings* (Springer, 2001), for simple modules, Schur's lemma, and the structure of matrix algebras.
- J. D. Simão, "Biquaternions, Majorana spinors and time-like spin-foams," arXiv:2401.10324 [gr-qc] (2024), for the indefinite form, the triple of elements behind the vector maps, the three models of $S^2$, $H^\pm$ and $H^{sl}$, and the closure of the bilinears. External; cited for the forms and the models only.
