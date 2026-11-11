# __Mirror Biquaternions of the Biquaternion Algebra__

## Introduction

The biquaternion algebra splits into a Hermitian and an anti-Hermitian subspace, $\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$, and an element of either
subspace carries four real numbers. Multiplication by the central unit $i$ carries such an element to the other subspace and keeps its four numbers. One further
multiplication, by $1+i$ instead of by $i$, carries it to a mixed element of the whole algebra, and the two parts of that mixed element are exactly the element and
its image. The product is one element, it is built in one multiplication, and this article names it the **mirror biquaternion** of the element.

The construction answers a question the sector split leaves open. A sector element carries its four numbers in one sector only, so a reader who wants the same four
numbers in the other sector has, in the split alone, only a pair of elements, which is two objects. The mirror biquaternion is one object that carries the
pair, and the four real numbers are not duplicated in it: it has eight real components and four independent ones.

The article states three results about the object and its class, which is the set of the mirror biquaternions.

The class is a real four-dimensional subspace of the eight-dimensional algebra. It is the graph of the map $\tilde Q\mapsto i\tilde Q$ from one sector to the
other, it is complementary to each sector, and it is complementary to its own image under the same map. So it is a real form of the complex vector space
$\mathbb{B}$ carried by $J:\tilde Q\mapsto i\tilde Q$.

The class is not a subalgebra, and the failure is total: the product of two of its members is again a member only when that product is zero. The products are not
small, and the criterion that decides the case reduces to a pair of real equations whose only solutions over nonzero factors are the zero divisors of the algebra.

The class is not one of the six remarkable subspaces and not a sum of coordinate blocks. It meets the four four-dimensional remarkable subspaces only at zero, the
centre in a line and the vector subspace in a three-plane, and it is a diagonal of the block decomposition rather than a block.

The whole of the article is algebra. It uses the product, the four conjugations, the trace, the quaternionic norm and the Hermitian form, all as the conventions
fix them, and it introduces no further structure, no form and no topology. The two sectors and their decompositions are *Subspaces and Decompositions of the
Biquaternion Algebra*; the conjugations are *The Group of Involutions*; the zero divisors are *Zero Divisors and Units*. The same construction read as a statement
about two physical readings, with the operators, the equations and the fields it carries there, is the physics article *Mirror Biquaternions and the Phy–Psy
Switch*, and nothing of that article is needed here.

## The Two Sectors

**The star and its two eigenspaces.** The Hermitian conjugation is the map

$$
\tilde Q^{*}=\bar Q_t\,e_t-\bar Q_x\,\vec e_x-\bar Q_y\,\vec e_y-\bar Q_z\,\vec e_z ,
$$

conjugate-linear and reversing the order of a product, $\bigl(\tilde Q_1\tilde Q_2\bigr)^{*}=\tilde Q_2^{*}\tilde Q_1^{*}$. It is an involution, so it cuts the
algebra into its fixed and its anti-fixed space, and the two are the two sectors.

| subspace | defining condition | coefficient condition | real basis | $\dim_{\mathbb{R}}$ |
| --- | --- | --- | --- | --- |
| $\mathbb{B}_{\Psi}$ | $\tilde Q^{*}=\tilde Q$ | $Q_t$ real, $Q_x,Q_y,Q_z$ purely imaginary | $e_t, i\vec e_x, i\vec e_y, i\vec e_z$ | $4$ |
| $\mathbb{B}_{\Phi}$ | $\tilde Q^{*}=-\tilde Q$ | $Q_t$ purely imaginary, $Q_x,Q_y,Q_z$ real | $ie_t, \vec e_x, \vec e_y, \vec e_z$ | $4$ |

The two are the Hermitian and the anti-Hermitian subspace of the corpus, and they are written with the signs of their condition: $\mathbb{B}_{\Psi}$ for the fixed
space and $\mathbb{B}_{\Phi}$ for the anti-fixed one. Neither is a subalgebra. Both are real four-dimensional, and the algebra is their direct sum,
$\mathbb{B}=\mathbb{B}_{\Psi}\oplus\mathbb{B}_{\Phi}$.

**The two projections.** The parts of an element are its two projections,

$$
\tilde Q_\Psi=\tfrac12\bigl(\tilde Q+\tilde Q^{*}\bigr),
\qquad
\tilde Q_\Phi=\tfrac12\bigl(\tilde Q-\tilde Q^{*}\bigr),
$$

and each projection is idempotent, since the star fixes an element of $\mathbb{B}_{\Psi}$ and reverses an element of $\mathbb{B}_{\Phi}$. A sector element is
therefore its own part: $\tilde Q_\Phi$ is the whole of $\tilde Q$ when $\tilde Q$ lies in $\mathbb{B}_{\Phi}$, and zero when it lies in $\mathbb{B}_{\Psi}$.

**The four numbers of a sector element.** In the coordinates of its own sector an element of $\mathbb{B}_{\Phi}$ is written with one real scalar and one real
vector,

$$
\tilde Q_\Phi=i a\,e_t+u_x\vec e_x+u_y\vec e_y+u_z\vec e_z=i a\,e_t+\vec u ,
\qquad a\in\mathbb{R},\quad \vec u\in\mathbb{R}^{3},
$$

and an element of $\mathbb{B}_{\Psi}$ with one real scalar and one real vector of the other kind,

$$
\tilde Q_\Psi=b\,e_t+i\bigl(v_x\vec e_x+v_y\vec e_y+v_z\vec e_z\bigr)=b\,e_t+i\vec v ,
\qquad b\in\mathbb{R},\quad \vec v\in\mathbb{R}^{3}.
$$

Four real numbers in each case, and no more. The letters $a$, $b$ and the vectors $\vec u$, $\vec v$ are real throughout the article, and every formula below is
read in these coordinates.

## The Mirror Map

### Multiplication by the Central Unit

The unit $i$ is central and anti-Hermitian, $i^{*}=-i$. The two facts together give the conjugation of a product by $i$ in one line,

$$
\bigl(i\tilde Q\bigr)^{*}=\tilde Q^{*}i^{*}=-i\,\tilde Q^{*},
$$

and the sign changes the sector of a sector element. If $\tilde Q^{*}=-\tilde Q$ then $\bigl(i\tilde Q\bigr)^{*}=+i\tilde Q$, and if $\tilde Q^{*}=+\tilde Q$ then
$\bigl(i\tilde Q\bigr)^{*}=-i\tilde Q$. Hence

$$
\boxed{\;\tilde Q\in\mathbb{B}_{\Phi}\ \Longrightarrow\ i\tilde Q\in\mathbb{B}_{\Psi},
\qquad\qquad
\tilde Q\in\mathbb{B}_{\Psi}\ \Longrightarrow\ i\tilde Q\in\mathbb{B}_{\Phi}\;}.
$$

The map is a bijection in each direction, with inverse multiplication by $-i$, and it is real-linear: it carries a real combination to the real combination of the
images. It is not complex-linear, and the next paragraph says which scalars keep an element in its sector.

**Which scalars move an element between the sectors.** A central scalar $c$ carries $\mathbb{B}_{\Phi}$ into itself when $c$ is real, and out of it when $c$ has a
nonzero imaginary part. For $c=a+bi$ with $a$ and $b$ real and not both zero, the image $c\tilde Q_\Phi=a\tilde Q_\Phi+bi\tilde Q_\Phi$ has a part in
$\mathbb{B}_{\Phi}$ and a part in $\mathbb{B}_{\Psi}$, and it is a sector element only when one of $a$ and $b$ vanishes. The mirror map is the imaginary case, and
the real scalars are the scalars that keep an element at home.

### The Coordinate Form

On an anti-Hermitian element the map has one sentence: **it negates the scalar coefficient and moves the $i$ onto the three vector slots.** In the coordinates of
the sector,

$$
i\tilde Q_\Phi=i\bigl(i a\,e_t+\vec u\bigr)=-a\,e_t+i\bigl(u_x\vec e_x+u_y\vec e_y+u_z\vec e_z\bigr),
$$

and the four real parameters pass through unchanged in magnitude. Read backwards, the same line gives the reverse map on a Hermitian element,

$$
i\tilde Q_\Psi=i\bigl(b\,e_t+i\vec v\bigr)=i b\,e_t-\vec v ,
$$

which negates the vector part and moves the $i$ onto the scalar slot. The two lines are one operation on the two sectors, and no coordinate is created or destroyed.

### Order Four, and the Pair

Two applications of the map are minus the identity, and four are the identity, since $i^{2}=-1$. The orbit of a sector element is therefore the quadruple

$$
\tilde Q_\Phi\ \xrightarrow{\ i\ }\ i\tilde Q_\Phi\ \xrightarrow{\ i\ }\ -\tilde Q_\Phi \xrightarrow{\ i\ }\ -i\tilde Q_\Phi \xrightarrow{\ i\ }\ \tilde Q_\Phi ,
$$

and the object the article builds out of it is the pair $\{\tilde Q_\Phi,i\tilde Q_\Phi\}$, which is the orbit read up to the overall sign. Two applications do not
return the element but its negative, so the mirror of an element is not an involution on the algebra; the involution is the composite of the mirror with the
central sign. The pair is what the construction uses, and no further application produces a third element.

## The Mirror Biquaternion

### The Construction

**Definition.** The **mirror biquaternion** of a sector element is the product by $1+i$:

$$
\boxed{\;\tilde Q_{\mathrm{mir}}:=(1+i)\tilde Q_\Phi\;}.
$$

One multiplication, one element of the whole algebra, and the definition names no part and takes no projection. In the coordinates of the sector the product is

$$
\tilde Q_{\mathrm{mir}}=(1+i)\bigl(i a\,e_t+\vec u\bigr)=(i-1)a\,e_t+(1+i)\vec u ,
$$

that is, coefficient $(i-1)a$ on the scalar slot and coefficient $(1+i)u_k$ on the three vector slots. The scalar coefficient of the product is the negative of its
own imaginary part, and each vector coefficient equals its own imaginary part; that fingerprint is a test, and it is the coordinate test of the next section.

**The two parts of the product.** The product is the sum of the element and its mirror,

$$
\tilde Q_{\mathrm{mir}}=\tilde Q_\Phi+i\tilde Q_\Phi ,
$$

and that sum is a theorem about the product and not the way the product is defined. The definition is one multiplication of one element; the decomposition into two
parts is read off the result.

### The Construction from the Hermitian Side

The same set of elements is reached from the other sector, with the conjugate factor. For a Hermitian element,

$$
(1-i)\tilde Q_\Psi=(1+i)\bigl(-i\tilde Q_\Psi\bigr),
$$

and $-i\tilde Q_\Psi$ is anti-Hermitian, so the right side is a mirror biquaternion. Hence

$$
\boxed{\;\mathbb{B}_{\mathrm{mir}}:=(1+i)\mathbb{B}_{\Phi}=(1-i)\mathbb{B}_{\Psi}\;},
$$

and the class does not know from which sector it was built. The two factors differ by a central unit, $1-i=-i(1+i)$, and the two inputs differ by the same unit,
which is the statement that the construction is one construction.

The sign carries a warning. The element $(1+i)e_t$ is not a mirror biquaternion, because $e_t$ is Hermitian and not anti-Hermitian; the element
$(1-i)e_t=(1+i)(-ie_t)$ is one. A reader who multiplies an element by $1+i$ without checking the sector gets an element of the algebra and not a member of the
class, and the star test of the next section says so in one line.

### The Eight Components and the Four Parameters

**Components.** The mirror biquaternion has four complex coefficients, hence eight real components. In the coordinates of its sector,

$$
Q_t=(i-1)a=-a+ia,
\qquad
Q_x=(1+i)u_x=u_x+iu_x,
\qquad
Q_y=u_y+iu_y,
\qquad
Q_z=u_z+iu_z .
$$

| slot | coefficient | real part | imaginary part |
| --- | --- | --- | --- |
| $e_t$ | $(i-1)a$ | $-a$ | $+a$ |
| $\vec e_x$ | $(1+i)u_x$ | $u_x$ | $u_x$ |
| $\vec e_y$ | $(1+i)u_y$ | $u_y$ | $u_y$ |
| $\vec e_z$ | $(1+i)u_z$ | $u_z$ | $u_z$ |

**Four parameters, not eight.** The eight real components are functions of the four numbers $a,u_x,u_y,u_z$, so the class is four-dimensional in the real sense and
the map from the sector to the class is injective. It is also surjective onto the class by the definition. The component table shows the injectivity at sight: the
real part of $Q_x$ is $u_x$ and gives the parameter back, and once the four parameters are known every component is known. A member of the class is therefore one
sector element carrying eight numbers in a fixed pattern, and the pattern is the whole constraint.

**The third test.** The table reads as a condition: an element lies in the class exactly when its scalar coefficient has opposite real and imaginary parts and its
three vector coefficients have equal real and imaginary parts,

$$
\operatorname{Re}Q_t=-\operatorname{Im}Q_t,
\qquad
\operatorname{Re}Q_x=\operatorname{Im}Q_x,
\qquad
\operatorname{Re}Q_y=\operatorname{Im}Q_y,
\qquad
\operatorname{Re}Q_z=\operatorname{Im}Q_z .
$$

Four real equations on eight real unknowns, of rank four, and the solutions are the class. The next section gives the same class in a form that uses no coordinates.

### The Two Projections

The projections of the product return the pair, and the two identities are one line each:

$$
\boxed{\;\tfrac{1-i}{2}\,\tilde Q_{\mathrm{mir}}=\tilde Q_\Phi,
\qquad\qquad
\tfrac{1+i}{2}\,\tilde Q_{\mathrm{mir}}=i\tilde Q_\Phi\;},
$$

since $\tfrac{1-i}{2}(1+i)=1$ and $\tfrac{1+i}{2}(1+i)=i$. The two scalars are applied after the inverse of the construction, and the results are exactly the
projections onto the two sectors. So the class is the set of elements whose second sector projection is $i$ times the first, and the construction
and the projection are inverse to each other between the sector and the class.

## The Class

### Two Tests

**The star test.** An element is a mirror biquaternion exactly when

$$
\boxed{\;\tilde Q^{*}=i\tilde Q\;}.
$$

*Proof.* If $\tilde Q=(1+i)\tilde Q_\Phi$ then $\tilde Q^{*}=(1-i)\tilde Q_\Phi^{*}=-(1-i)\tilde Q_\Phi=(i-1)\tilde Q_\Phi=i(1+i)\tilde Q_\Phi=i\tilde Q$, using
$\tilde Q_\Phi^{*}=-\tilde Q_\Phi$ and $(1-i)i=(i-1)$. Conversely, if $\tilde Q^{*}=i\tilde Q$ then the two projections read
$\tilde Q_\Phi=\tfrac12(\tilde Q-\tilde Q^{*})=\tfrac12(1-i)\tilde Q$ and $\tilde Q_\Psi=\tfrac12(\tilde Q+\tilde Q^{*})=\tfrac12(1+i)\tilde Q$, and
$i\tilde Q_\Phi=\tfrac12(i+1)\tilde Q=\tilde Q_\Psi$; the second projection is $i$ times the first, and by the projection formulas of the construction
$\tilde Q=(1+i)\tilde Q_\Phi$.

**The three tests together.** The class is one set in three descriptions, and each description is the short one for a different argument.

| test | form | what it uses |
| --- | --- | --- |
| sector test | $\tilde Q_\Psi=i\tilde Q_\Phi$ | the projections and the split |
| star test | $\tilde Q^{*}=i\tilde Q$ | the conjugation alone, no projection |
| coordinate test | $\operatorname{Re}Q_t=-\operatorname{Im}Q_t$ and $\operatorname{Re}Q_k=\operatorname{Im}Q_k$ | the coefficients alone |

### The Class Is a Real Four-Dimensional Subspace

The class is closed under real linear combinations, since
$(1+i)(\alpha\tilde Q_\Phi+\beta\tilde Q_\Phi')=\alpha(1+i)\tilde Q_\Phi+\beta(1+i)\tilde Q_\Phi'$ for real $\alpha$ and $\beta$, and it is the image of the
four-dimensional real space $\mathbb{B}_{\Phi}$ under the real-linear map $\tilde Q\mapsto(1+i)\tilde Q$. That map is injective, because multiplication by
$\tfrac{1-i}{2}$ is a left inverse. Hence the class is a real subspace of dimension four, isomorphic to the sector as a real vector space, inside an algebra of
dimension eight.

It is not a complex subspace. Multiplication by $i$ carries the class out of itself, as the section on the partner class shows, so the class is not stable under the
complex structure of the algebra. The isomorphism with the sector is an isomorphism of real vector spaces and of nothing more, since the sector is not a complex
space either.

### The Class Is a Graph

The projection of the class onto either sector is an isomorphism. The kernel of the projection onto $\mathbb{B}_{\Phi}$ is the intersection
$\mathbb{B}_{\mathrm{mir}}\cap\mathbb{B}_{\Phi}$, and that intersection is zero: an anti-Hermitian element that is also a member would satisfy both
$\tilde Q^{*}=-\tilde Q$ and $\tilde Q^{*}=i\tilde Q$, hence $\tilde Q=-i\tilde Q$ and $\tilde Q=0$. The kernel of
the projection onto $\mathbb{B}_{\Psi}$ vanishes for the same reason, with the signs exchanged, and both projections have rank four because the class has dimension
four. So

$$
\boxed{\;\mathbb{B}=\mathbb{B}_{\mathrm{mir}}\oplus\mathbb{B}_{\Phi}=\mathbb{B}_{\mathrm{mir}}\oplus\mathbb{B}_{\Psi}\;},
$$

and the class is the graph of the map $\tilde Q\mapsto i\tilde Q$ from $\mathbb{B}_{\Phi}$ to $\mathbb{B}_{\Psi}$: one element of the first sector for each point of
the graph, and one element of the second by the map. That is the precise sense in which a member of the class is one sector element known twice.

### The Partner Class and the Decomposition of the Whole Algebra

**The partner class.** The star image of the class is the set of elements satisfying the test with the other sign,

$$
\mathbb{B}_{\mathrm{mir}}^{\mathrm{c}}:=\mathbb{B}_{\mathrm{mir}}^{*}=\{\tilde Q:\tilde Q^{*}=-i\tilde Q\},
$$

and it is also the image of the class under the mirror, since for a member $\tilde Q$ the element $i\tilde Q$ has conjugate
$(i\tilde Q)^{*}=-i\tilde Q^{*}=-i\,(i\tilde Q)$, which is $-i$ times itself. In coordinates the partner class is $(1-i)\mathbb{B}_{\Phi}$, and the two classes are
exchanged by the star, by the coefficient conjugation, by the reversal $\flat=-{}^{*}$ and by the mirror.

**The two classes are complementary.** The intersection is zero, since an element of both satisfies $\tilde Q^{*}=i\tilde Q$ and $\tilde Q^{*}=-i\tilde Q$, hence
$2i\tilde Q=0$. Both have dimension four, so their sum has dimension eight:

$$
\boxed{\;\mathbb{B}=\mathbb{B}_{\mathrm{mir}}\oplus\mathbb{B}_{\mathrm{mir}}^{\mathrm{c}}=\mathbb{B}_{\mathrm{mir}}\oplus i\,\mathbb{B}_{\mathrm{mir}}\;}.
$$

The second equality holds because the partner class is the image of the class under the mirror, and it is the interesting one: the complex structure $J$ carries the
class onto its complement, so the class contains no complex line of the algebra and no two of its elements are complex multiples of one another.

**The two senses of real form.** A real form of a complex vector space $V$ with complex structure $J$ is a real subspace $W$ with $V=W\oplus JW$; a real form of a
complex algebra is a real subalgebra with the same property. The class is a real form in the first sense and not in the second, since it has dimension four and is
not a subalgebra, as the next section shows. The real form of the algebra that the corpus names is $\mathbb{B}_{H}$, the quaternion subspace, and the class is a
different object: $\mathbb{B}_{H}$ is closed under the product, and the class is as far from closed as a subspace can be.

### The Unique Decomposition of an Element

Since the class and its mirror image are complementary, every element of the algebra is a member plus $i$ times a member, and the writing is unique. In the parts of
the element the two members are

$$
\tilde Q=\tilde Q_{\mathrm{mir}}+i\tilde Q_{\mathrm{mir}}',
\qquad
\tilde Q_{\mathrm{mir}}=(1+i)\tfrac12\bigl(\tilde Q_\Phi-i\tilde Q_\Psi\bigr),
\qquad
\tilde Q_{\mathrm{mir}}'=-(1+i)\tfrac12\bigl(\tilde Q_\Phi+i\tilde Q_\Psi\bigr),
$$

and the verification is one expansion: the sum is
$\tfrac12(\tilde Q_\Phi-i\tilde Q_\Psi)-\tfrac12(\tilde Q_\Phi+i\tilde Q_\Psi)+i\tfrac12(\tilde Q_\Phi-i\tilde Q_\Psi)+i\tfrac12(\tilde Q_\Phi+i\tilde Q_\Psi)$, whose
part in $\mathbb{B}_{\Phi}$ is $\tilde Q_\Phi$ and whose part in $\mathbb{B}_{\Psi}$ is $\tilde Q_\Psi$. So every element of the algebra is two sector elements
packed as two mirror biquaternions, and the packing is the decomposition of the algebra into the class and its mirror image.

## The Product: The Class Is Not a Subalgebra

### The Criterion

The factor squares to $2i$, so the product of two mirror biquaternions is a central multiple of the product of their members:

$$
(1+i)\tilde Q_\Phi\cdot(1+i)\tilde Q_\Phi'=(1+i)^{2}\tilde Q_\Phi\tilde Q_\Phi'=2i\,\tilde Q_\Phi\tilde Q_\Phi' .
$$

The product is a member of the class exactly when it passes the star test, $\tilde Q^{*}=i\tilde Q$. Its conjugate is
$(2i\tilde Q_\Phi\tilde Q_\Phi')^{*}=-2i\,\tilde Q_\Phi'^{*}\tilde Q_\Phi^{*}=-2i\,\tilde Q_\Phi'\tilde Q_\Phi$, using the anti-Hermiticity of both factors, so the
test reads

$$
-2i\,\tilde Q_\Phi'\tilde Q_\Phi=i\cdot2i\,\tilde Q_\Phi\tilde Q_\Phi'=-2\,\tilde Q_\Phi\tilde Q_\Phi'
\qquad\Longleftrightarrow\qquad
\tilde Q_\Phi\tilde Q_\Phi'=i\,\tilde Q_\Phi'\tilde Q_\Phi .
$$

The criterion is a twisted commutation of the two members. It is not the anti-Hermiticity of their product, but a condition on the two members, and the factor
$2i$ is what puts the condition there.

### The Solutions of the Criterion

**The two products.** Write the members in the coordinates of the sector,
$\tilde Q_\Phi=i a+\vec u$ and $\tilde Q_\Phi'=i b+\vec v$, with $a$, $b$ real and $\vec u$, $\vec v$ real vectors. Then

$$
\tilde Q_\Phi\tilde Q_\Phi'=-\bigl(ab+\vec u\cdot\vec v\bigr)+\vec u\times\vec v+i\bigl(a\vec v+b\vec u\bigr),
$$

$$
\tilde Q_\Phi'\tilde Q_\Phi=-\bigl(ab+\vec u\cdot\vec v\bigr)-\vec u\times\vec v+i\bigl(a\vec v+b\vec u\bigr),
$$

which differ only in the sign of the cross product. The criterion equates the first with $i$ times the second, and the two sides split into a scalar slot and a
vector slot. The scalar slot gives one equation and the vector slot gives one:

$$
ab+\vec u\cdot\vec v=0,
\qquad\qquad
\vec u\times\vec v=-\bigl(a\vec v+b\vec u\bigr).
$$

**The three cases.** The equations are solved by cases on the two scalars.

If $a=b=0$, the first equation gives $\vec u\cdot\vec v=0$ and the second gives $\vec u\times\vec v=0$, so the two vectors are parallel and orthogonal, one of them
vanishes, and with it one of the two mirror biquaternions.

If $a=0$ and $b\neq0$, the first equation gives $\vec u\cdot\vec v=0$ and the second reads $b\vec u=-\vec u\times\vec v$. Crossing the second with $\vec u$ and using
the first gives $\lvert\vec u\rvert^{2}\vec v=0$, so $\vec v=0$, and then the second gives $b\vec u=0$, so $\vec u=0$; the member $\tilde Q_\Phi$ vanishes. The case
$b=0$, $a\neq0$ is the same under the exchange of the two members.

If $a$ and $b$ are both nonzero, cross the vector equation with $\vec u$:

$$
\vec u\times(\vec u\times\vec v)=\vec u\,(\vec u\cdot\vec v)-\vec v\,\lvert\vec u\rvert^{2}
=-ab\,\vec u-\lvert\vec u\rvert^{2}\vec v ,
$$

using the first equation, while the same cross product read from the vector equation gives
$\vec u\times\bigl(-\vec u\times\vec v\bigr)=a^{2}\vec v+ab\,\vec u$. Equating the two, $\vec v$ is a real multiple of $\vec u$. Then $\vec u\times\vec v=0$ and the
vector equation reads $a\vec v+b\vec u=0$, whose solution is $\vec v=-(b/a)\vec u$. Substituting that multiple in the relation just obtained gives the condition
$\lvert\vec u\rvert^{2}=a^{2}$, which is consistent, and the first equation is then automatic.

### A Product Is a Member Only When It Vanishes

In the last case the three quantities $\vec u\times\vec v$, $a\vec v+b\vec u$ and $ab+\vec u\cdot\vec v$ all vanish, so the product $\tilde Q_\Phi\tilde Q_\Phi'$ is
zero. In the other two cases one of the members is zero. Hence

$$
\boxed{\;(1+i)\tilde Q_\Phi\cdot(1+i)\tilde Q_\Phi'\in\mathbb{B}_{\mathrm{mir}}
\qquad\Longleftrightarrow\qquad
\tilde Q_\Phi\tilde Q_\Phi'=0\;},
$$

and the class satisfies $\mathbb{B}_{\mathrm{mir}}\cdot\mathbb{B}_{\mathrm{mir}}\cap\mathbb{B}_{\mathrm{mir}}=\{0\}$: no nonzero product of two of its members is a
member. Solutions with nonzero factors exist, because the algebra has zero divisors, and they are the pairs $\tilde Q_\Phi=i a+\vec u$ and
$\tilde Q_\Phi'=i b-(b/a)\vec u$ with $\lvert\vec u\rvert=\lvert a\rvert$ and $a$, $b$ nonzero. The smallest instance is the pair $ie_t+\vec e_x$ and
$ie_t-\vec e_x$, which is worked below.

Two consequences follow at once. The square of a member is a member only when it vanishes, since a square is a product of two members. And a member is a zero divisor
exactly when the sector element it comes from is one, since the factor $1+i$ is invertible, so the family above is the family of the
members of vanishing quaternionic norm, which the section on the invariants computes.

### The Witness

The smallest nonzero product of two members leaves the class, and it uses the two pure vector units, which are anti-Hermitian:

$$
\tilde Q_\Phi=\vec e_x,\qquad \tilde Q_\Phi'=\vec e_y,\qquad
(1+i)\vec e_x\cdot(1+i)\vec e_y=2i\,\vec e_x\vec e_y=2i\,\vec e_z .
$$

The product lies wholly in $\mathbb{B}_{\Psi}$ and it is not zero, so it fails the star test: the test would require it to equal $i$ times itself. The product is
therefore a central multiple of a member and not a member, since $(1+i)\vec e_z$ is a member and $(1+i)\,(1+i)\vec e_z=2i\vec e_z$. The class is not closed under
the product.

The identity cannot serve as a witness, and the reason is worth stating. The identity is Hermitian, $e_t^{*}=e_t$, so $(1+i)e_t$ is not a member, and a product
built from it tests nothing about the class. The pair of vector units above is a pair of members.

### The Commutator Also Leaves the Class

The same pair shows that the class is not closed under the commutator either, since

$$
\bigl[(1+i)\vec e_x,(1+i)\vec e_y\bigr]=2i\,\bigl(\vec e_x\vec e_y-\vec e_y\vec e_x\bigr)=2i\,(2\vec e_z)=4i\,\vec e_z ,
$$

and $4i\vec e_z$ passes neither test: its star image is $4i\vec e_z$ itself, while $i$ times it is $-4\vec e_z$. So the class carries neither the product nor the
commutator of its members, and it is a subspace and nothing more.

## The Conjugations on the Class

The four conjugations act on the class in a pattern that separates it from the six remarkable subspaces, because a remarkable subspace is by definition the fixed or
the anti-fixed space of one of them.

| map | image of the class | one-line reason |
| --- | --- | --- |
| ${}^{\natural}$ | the class | $\mathbb{C}$-linear, so it commutes with $1+i$, and it preserves $\mathbb{B}_{\Phi}$ |
| $\bar{\cdot}$ | the partner class | it conjugates the factor, $(1+i)\mapsto(1-i)$, and preserves $\mathbb{B}_{\Phi}$ |
| ${}^{*}$ | the partner class | the defining test turns into the test with the other sign |
| $\flat=-{}^{*}$ | the partner class | it is the star followed by the central sign |
| $J:\tilde Q\mapsto i\tilde Q$ | the partner class | $i$ times a member satisfies the test with the other sign |

Only the quaternion conjugation preserves the class, and it does not fix it: an element of the class fixed by ${}^{\natural}$ has a real scalar coefficient, and no
nonzero member has one, since $Q_t=(i-1)a$ is not real for $a\neq0$. So the class is stable under one conjugation and neither fixed nor anti-fixed by it, and it is
the fixed space of none of the four.

**The eigenspaces inside the class.** The fixed elements of the class are the members with $\vec u=0$, a real line,
$\mathbb{B}_{\mathrm{mir}}\cap\mathbb{B}_{C}=\mathbb{R}(1-i)e_t$, and the anti-fixed ones are the members with $a=0$, a real three-plane,
$\mathbb{B}_{\mathrm{mir}}\cap\mathbb{B}_{V}=(1+i)\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$. The two are the intersections of the class with
the centre and with the vector subspace, and their dimensions add to four, so the class is the direct sum of its fixed and its anti-fixed part under
${}^{\natural}$.

**The scalars.** A real scalar preserves the class, a purely imaginary scalar carries it to the partner class, and a scalar with both parts nonzero carries it into
neither. The class is therefore a module over $\mathbb{R}$ and not over $\mathbb{C}$, and its four dimensions are real ones.

## The Invariants

The invariants of the algebra take fixed factors on a mirror biquaternion, one factor per invariant, and each factor is read from the one multiplication that defines
the object.

| invariant | on the member $\tilde Q_\Phi$ | on the member $\tilde Q_{\mathrm{mir}}$ | factor |
| --- | --- | --- | --- |
| trace $\operatorname{Tr}=2\operatorname{Sc}$ | $2ia$ | $(1+i)\,2ia=2ia-2a$ | $1+i$ |
| quaternionic norm, $=\det\mathsf{M}_2$ | $\lvert\vec u\rvert^{2}-a^{2}$ | $2i\bigl(\lvert\vec u\rvert^{2}-a^{2}\bigr)$ | $2i$ |
| spectrum | $ia\pm i\lvert\vec u\rvert$ | $(1+i)\bigl(ia\pm i\lvert\vec u\rvert\bigr)$ | $1+i$ |
| Hermitian form $\langle\cdot\rangle_{*}$ | $a^{2}+\lvert\vec u\rvert^{2}$ | $2\bigl(a^{2}+\lvert\vec u\rvert^{2}\bigr)$ | $2$ |

**The trace.** The trace is linear and a central scalar passes through it, so $\operatorname{Tr}\tilde Q_{\mathrm{mir}}=(1+i)\operatorname{Tr}\tilde Q_\Phi$. On the
member the trace is $2ia$, purely imaginary; on the mirror biquaternion it is $2ia-2a$, which keeps the imaginary part and adds a real one.

**The quadratic invariant.** The quaternionic norm is multiplicative, so
$\langle\tilde Q_{\mathrm{mir}}\rangle_{\natural}=(1+i)^{2}\langle\tilde Q_\Phi\rangle_{\natural}=2i\langle\tilde Q_\Phi\rangle_{\natural}$. On the member the norm
is $\lvert\vec u\rvert^{2}-a^{2}$, real, the difference of the vector square and the scalar square, so on the mirror biquaternion it is purely imaginary and
proportional to that difference. The determinant of the $2\times2$ image is the same value, since the two are equal on the algebra, so the row carries both names.

**The spectrum.** The spectrum of an element is the pair $Q_t\pm iB$ with $B$ the square root of the sum of the three squared vector coefficients. Multiplication by
the central scalar multiplies the scalar coefficient and every vector coefficient, hence multiplies each root of the characteristic equation, and the spectrum of
the mirror biquaternion is the spectrum of the member times $1+i$. The multiplication turns the complex plane by $\pi/4$ and scales it by $\sqrt{2}$, so a pair
of imaginary eigenvalues becomes a pair whose real and imaginary parts have the same magnitude, and the pair stays a pair: the sum is still the trace and the
product is still the norm.

**The Hermitian form.** The form is $\langle\tilde Q\rangle_{*}=\operatorname{Sc}(\tilde Q\tilde Q^{*})$, and on the member it is
$\operatorname{Sc}(\tilde Q_\Phi\tilde Q_\Phi^{*})=-\operatorname{Sc}(\tilde Q_\Phi^{2})=a^{2}+\lvert\vec u\rvert^{2}$, using the anti-Hermiticity of the member. On
the mirror biquaternion, $\tilde Q_{\mathrm{mir}}\tilde Q_{\mathrm{mir}}^{*}=(1+i)(1-i)\tilde Q_\Phi\tilde Q_\Phi^{*}=2\tilde Q_\Phi\tilde Q_\Phi^{*}$, so the
form doubles and stays real and non-negative. Every mirror biquaternion has a real non-negative Hermitian form, and the form vanishes only at the origin.

**The zero norm.** The quaternionic norm vanishes exactly when $\lvert\vec u\rvert=\lvert a\rvert$, which is the family of the criterion above. A mirror biquaternion
is a zero divisor exactly when the sector element it comes from is one, and the members of that family are the ones whose products with one another vanish. The two
sections are one computation read twice.

## The Class Among the Remarkable Subspaces

**The intersections.** The class meets the six remarkable subspaces in dimensions that follow from the coordinates, and the table collects them.

| subspace | intersection with the class | $\dim_{\mathbb{R}}$ | why |
| --- | --- | --- | --- |
| the centre $\mathbb{B}_{C}$ | $\mathbb{R}(1-i)e_t$ | $1$ | $\vec u=0$ |
| the vector subspace $\mathbb{B}_{V}$ | $(1+i)\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec e_y,\vec e_z\}$ | $3$ | $a=0$ |
| the quaternion subspace $\mathbb{B}_{H}$ | $0$ | $0$ | $(i-1)a$ is not real and $(1+i)u_k$ is not real |
| the anti-quaternion subspace $\mathbb{B}_{iH}$ | $0$ | $0$ | $(i-1)a$ is not imaginary and $(1+i)u_k$ is not imaginary |
| the Hermitian subspace $\mathbb{B}_{\Psi}$ | $0$ | $0$ | the scalar coefficient is not real and the vector coefficients are not imaginary |
| the anti-Hermitian subspace $\mathbb{B}_{\Phi}$ | $0$ | $0$ | the scalar coefficient is not imaginary and the vector coefficients are not real |

The two nonzero intersections are one line and one three-plane, and they are the eigenspaces of the quaternion conjugation inside the class. In particular the class
meets each sector only at zero, which is the direct-sum statement of the section on the graph, and it meets the two four-dimensional subspaces that are not sectors
only at zero as well.

**The sums.** With either sector the class sums to the whole algebra, $\mathbb{B}_{\mathrm{mir}}+\mathbb{B}_{\Phi}=\mathbb{B}$ and
$\mathbb{B}_{\mathrm{mir}}+\mathbb{B}_{\Psi}=\mathbb{B}$, both of dimension eight. With the centre it sums to a subspace of dimension five, since the intersection has
dimension one. With the vector subspace it sums to the class itself, of dimension four, because the three-plane of the intersection is the whole vector part of the
class: the class is the sum of that three-plane and the line of the centre.

**It is not a sum of blocks.** The four coordinate blocks are $A_1=\mathbb{R}e_t$, $A_2=\mathbb{R}(ie_t)$, $B_1=\operatorname{span}_{\mathbb{R}}\{\vec e_x,\vec
e_y,\vec e_z\}$ and $B_2=\operatorname{span}_{\mathbb{R}}\{i\vec e_x,i\vec e_y,i\vec e_z\}$. The class meets each of the four only at zero, because the scalar
coefficient $(i-1)a$ mixes the two scalar slots in a fixed proportion and the vector coefficient $(1+i)u$ mixes the two vector blocks in a fixed proportion. So the
class is a diagonal of the block decomposition and not a block: it is the image of the block pair $(A_2,B_1)$, which is the sector $\mathbb{B}_{\Phi}$, under a map
that tilts each block into the sum of the two blocks of its kind.

**Why it is not one of the six.** Each of the six is the fixed or the anti-fixed space of one of the four conjugations. The class is the fixed space of no
conjugation, since only ${}^{\natural}$ preserves it and ${}^{\natural}$ does not fix it; it is the anti-fixed space of none, since its anti-fixed part under
${}^{\natural}$ is a three-plane and not the class; and the other three conjugations carry it to the partner class. So the class is a new subspace, and it is new
in the only way a subspace of this algebra can be new: it is defined by a relation between the two sectors and not by a symmetry of the algebra.

## Worked Examples

**A member and its mirror biquaternion.** Take $a=0.7$ and $\vec u=(0.3,-0.5,1.1)$, so that

$$
\tilde Q_\Phi=0.7i\,e_t+0.3\vec e_x-0.5\vec e_y+1.1\vec e_z .
$$

Its mirror biquaternion has the coefficients of the component table,

$$
\tilde Q_{\mathrm{mir}}=(-0.7+0.7i)e_t+(0.3+0.3i)\vec e_x+(-0.5-0.5i)\vec e_y+(1.1+1.1i)\vec e_z .
$$

The star test holds on this element, $\tilde Q_{\mathrm{mir}}^{*}=i\tilde Q_{\mathrm{mir}}$, and the projections return the pair, since
$\tfrac{1-i}{2}\tilde Q_{\mathrm{mir}}=\tilde Q_\Phi$ and $\tfrac{1+i}{2}\tilde Q_{\mathrm{mir}}=i\tilde Q_\Phi$. The invariants run as follows.

| invariant | $\tilde Q_\Phi$ | $\tilde Q_{\mathrm{mir}}$ |
| --- | --- | --- |
| trace | $1.4i$ | $-1.4+1.4i$ |
| quaternionic norm | $1.06$ | $2.12i$ |
| Hermitian form | $2.04$ | $4.08$ |
| spectrum | $1.9450i$, $-0.5450i$ | $0.5450-0.5450i$, $-1.9450+1.9450i$ |

The spectrum of the mirror biquaternion is the spectrum of the member multiplied by $1+i$, and the checksum is the same on both sides: the sum of the spectrum is the
trace, $1.4i$ on the left and $-1.4+1.4i$ on the right, and the product of the spectrum is the quaternionic norm, $1.06$ on the left and $2.12i$ on the right.
Nothing has been relabelled; two different elements have been computed.

**A member from the Hermitian side.** Take $\tilde Q_\Psi=1.3e_t+0.8i\vec e_y$, in $\mathbb{B}_{\Psi}$. Its image under the mirror is $1.3i\,e_t-0.8\vec e_y$,
which is anti-Hermitian, and the construction from that side is

$$
(1-i)\tilde Q_\Psi=(1.3-1.3i)e_t+(0.8+0.8i)\vec e_y ,
$$

which is a member of the class and equals $(1+i)\bigl(-i\tilde Q_\Psi\bigr)$. The two constructions of the article are one construction read from the two sides.

**Two members whose product vanishes.** Take $\tilde Q_\Phi=ie_t+\vec e_x$ and $\tilde Q_\Phi'=ie_t-\vec e_x$, with $a=b=1$ and $\vec v=-\vec u$, so that
$\lvert\vec u\rvert=\lvert a\rvert=1$. The two members of the class are

$$
(1+i)(ie_t+\vec e_x)=(-1+i)e_t+(1+i)\vec e_x,
\qquad
(1+i)(ie_t-\vec e_x)=(-1+i)e_t+(-1-i)\vec e_x ,
$$

and their product is exactly zero. The pair is a pair of zero divisors, and the product is a member because it vanishes: zero is the only product of two members that
stays inside the class, and the criterion is satisfied by the family that the section solved.

## Summary

The biquaternion algebra splits into the Hermitian and the anti-Hermitian subspace, each of real dimension four, and the central unit $i$ carries one sector onto
the other, being central and anti-Hermitian. One multiplication by $1+i$ instead of by $i$ carries a sector element to a mixed element whose two parts are the
element and its mirror, and the article names that element the **mirror biquaternion** of the sector element,
$\tilde Q_{\mathrm{mir}}=(1+i)\tilde Q_\Phi=(i-1)a\,e_t+(1+i)\vec u$. It has eight real components and four independent ones, its scalar coefficient has opposite
real and imaginary parts and its three vector coefficients have equal ones, and its two projections return the pair. The class $\mathbb{B}_{\mathrm{mir}}$ is also
$(1-i)\mathbb{B}_{\Psi}$, so it is built from either sector, and the three tests $\tilde Q_\Psi=i\tilde Q_\Phi$, $\tilde Q^{*}=i\tilde Q$ and the four coefficient
equalities name it in the three available languages.

The class is a real four-dimensional subspace, the image of the anti-Hermitian sector under the real-linear injection $\tilde Q\mapsto(1+i)\tilde Q$, and it is the
graph of the mirror map between the two sectors. It is complementary to each sector and to its own mirror image, so the algebra is the direct sum of the class and
of $i$ times the class, and every element is a member plus $i$ times a member, uniquely. The class is a real form of the complex vector space carried by
$J:\tilde Q\mapsto i\tilde Q$ and not a real form of the algebra, since it is not closed under the product.

The failure of closure is total. The product of two members is $2i$ times the product of their members, it is a member exactly when the two members satisfy the
twisted commutation $\tilde Q_\Phi\tilde Q_\Phi'=i\tilde Q_\Phi'\tilde Q_\Phi$, and the solutions of that condition with nonzero factors are exactly the pairs whose
product vanishes. So $\mathbb{B}_{\mathrm{mir}}\cdot\mathbb{B}_{\mathrm{mir}}\cap\mathbb{B}_{\mathrm{mir}}=\{0\}$: no nonzero product of two members is a member, the square of a
member lies outside the class unless it vanishes, and the witness $(1+i)\vec e_x\cdot(1+i)\vec e_y=2i\vec e_z$ leaves the class. The commutator leaves it on the
same pair.

Only the quaternion conjugation preserves the class; the coefficient conjugation and the star, the reversal and the mirror carry it to the partner class
$\mathbb{B}_{\mathrm{mir}}^{\mathrm{c}}=\{\tilde Q:\tilde Q^{*}=-i\tilde Q\}$. Inside the class the quaternion conjugation has a fixed line, the intersection with
the centre, and an anti-fixed three-plane, the intersection with the vector subspace, and those are the only nonzero intersections of the class with the six
remarkable subspaces. The class meets the four four-dimensional remarkable subspaces only at zero, it is a diagonal of the block decomposition and not a block, and
it is the fixed space of no conjugation, which is why it is not one of the six.

The invariants take fixed factors: the trace by $1+i$, the quaternionic norm, which is the determinant of the $2\times2$ image, by $2i$, the spectrum by $1+i$, and
the Hermitian form by $2$. The Hermitian form of a mirror biquaternion is real and non-negative, $2(a^{2}+\lvert\vec u\rvert^{2})$, and the quaternionic norm
vanishes on the family $\lvert\vec u\rvert=\lvert a\rvert$, which is the family of zero divisors on which two members multiply to zero. The worked example runs the
numbers on one element and its mirror biquaternion, and they check against the trace and against the norm.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $\mathbb{B}$ | the biquaternion algebra, $\mathbb{C}\otimes_{\mathbb{R}}\mathbb{H}$, of real dimension eight |
| $e_t,\vec e_x,\vec e_y,\vec e_z$ | the basis, with $e_t$ the unit and $\vec e_k^{2}=-e_t$ |
| $i$ | the central imaginary unit, $i^{2}=-1$, commuting with every element |
| ${}^{\natural}$ | the quaternion conjugation, $\mathbb{C}$-linear: the scalar coefficient kept and the vector coefficients negated |
| $\bar{\cdot}$ | the coefficient conjugation, acting on the four coefficients |
| ${}^{*}$ | the Hermitian conjugation, $\bar{\cdot}\circ{}^{\natural}$, conjugate-linear and reversing the product |
| $\flat$ | the reversal $-{}^{*}$ |
| $\mathbb{B}_{\Psi}$ | the Hermitian subspace, fixed space of ${}^{*}$; $Q_t$ real, $Q_k$ imaginary; dimension $4$ |
| $\mathbb{B}_{\Phi}$ | the anti-Hermitian subspace, anti-fixed space of ${}^{*}$; $Q_t$ imaginary, $Q_k$ real; dimension $4$ |
| $\tilde Q_\Phi,\tilde Q_\Psi$ | the two parts of an element, $\tfrac12(\tilde Q\mp\tilde Q^{*})$, in $\mathbb{B}_{\Phi}$ and in $\mathbb{B}_{\Psi}$ |
| $\tilde Q_\Phi=i a\,e_t+\vec u$ | a sector element in the coordinates of its sector, with $a$ real and $\vec u$ a real vector |
| the mirror | the map $\tilde Q\mapsto i\tilde Q$, of order four, exchanging the two sectors |
| $\tilde Q_{\mathrm{mir}}$ | the mirror biquaternion, $(1+i)\tilde Q_\Phi$; its two parts are $\tilde Q_\Phi$ and $i\tilde Q_\Phi$ |
| $\mathbb{B}_{\mathrm{mir}}$ | the class of the mirror biquaternions, $(1+i)\mathbb{B}_{\Phi}=(1-i)\mathbb{B}_{\Psi}$, a real subspace of dimension $4$ |
| $\mathbb{B}_{\mathrm{mir}}^{\mathrm{c}}$ | the partner class, $\{\tilde Q:\tilde Q^{*}=-i\tilde Q\}=i\mathbb{B}_{\mathrm{mir}}=\mathbb{B}_{\mathrm{mir}}^{*}$ |
| $J$ | the complex structure $\tilde Q\mapsto i\tilde Q$, $J^{2}=-\mathrm{id}$ |
| $\operatorname{Tr}\tilde Q$ | the trace, $2\operatorname{Sc}\tilde Q$ |
| $\langle\tilde Q\rangle_{\natural}$ | the quaternionic norm $\tilde Q\tilde Q^{\natural}$, the determinant of the $2\times2$ image |
| $\langle\tilde Q\rangle_{*}$ | the Hermitian form $\operatorname{Sc}(\tilde Q\tilde Q^{*})$ |
| $\mathbb{B}_{C},\mathbb{B}_{V},\mathbb{B}_{H},\mathbb{B}_{iH}$ | the centre, the vector subspace, the quaternion and the anti-quaternion subspace |
| $A_1,A_2,B_1,B_2$ | the coordinate blocks $\mathbb{R}e_t$, $\mathbb{R}(ie_t)$, the real vectors and the imaginary vectors |
| twisted commutation | the condition $\tilde Q_\Phi\tilde Q_\Phi'=i\tilde Q_\Phi'\tilde Q_\Phi$, under which a product of two members is a member |

## Further Reading

- [Subspaces and Decompositions of the Biquaternion Algebra](subspaces-and-decompositions-of-the-biquaternion-algebra.html), for the six remarkable subspaces, the
four coordinate blocks and the three decompositions, and for the complex structure as the map that exchanges the two sectors
- [The Group of Involutions of the Biquaternion Algebra](the-group-of-involutions.html), for the four conjugations as a Klein four-group and for their fixed and
anti-fixed spaces
- [The Element, the Coordinates and the Conjugations in the Biquaternion Algebra](the-element-the-coordinates-and-the-conjugations.html), for the formulas of the
conjugations, their linear or antilinear character and the real reading of the algebra
- [Zero Divisors and Units in the Biquaternion Algebra](zero-divisors-and-units.html), for the zero divisors that the criterion of the product needs and for the
annihilators of an element
- [The Square of an Element in the Biquaternion Algebra](the-square-of-an-element.html), for the square of a sector element and the isotropic cone
- [N-Regularity and N-Degeneracy in the Biquaternion Algebra](n-regularity-and-n-degeneracy-in-the-biquaternion-algebra.html), for the norm, the inverse formula
and the unit group
- [The Four Forms and the Four Algebraic Norms over the Biquaternion Algebra](the-four-forms-and-the-four-algebraic-norms-over-the-biquaternion-algebra.html),
for the invariants that take factors on the class
- [Remarkable Subspaces and the Four General Products, Forms and Norms](remarkable-subspaces-and-the-four-general-products-forms-and-norms.html), for what the six
subspaces carry under each of the four general products
- [Mirror Biquaternions and the Phy–Psy Switch](../articles_physics/mirror-biquaternions-and-the-phy-psy-switch.html), the physics article of the same
construction, where the two sectors are read as a material and an informational reading, and where the class carries operators, equations and fields
- Nicolas Bourbaki, *Algebra I* (Springer, 1998), for the fixed and the reversed parts of an involution and for the real forms of a complex vector space
- William Kingdon Clifford, "Preliminary Sketch of Biquaternions" (1873), for the first systematic treatment of the biquaternions
