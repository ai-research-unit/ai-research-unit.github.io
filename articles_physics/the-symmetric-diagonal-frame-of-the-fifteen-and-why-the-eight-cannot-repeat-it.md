# __The Symmetric Diagonal Frame of the Fifteen: Three Generators Permuted by $S_3$, and Why the Eight Cannot Repeat It__

## Introduction

Three of the fifteen generators are diagonal. Up to this point they have been written as one trace direction and two differences, $iD$, $d_2$ and $d_3$. That choice singles out one colour line and then chains the other two, so it is not symmetric in the three vector units.

A different triple is available above $M_C$, and it is symmetric. It is written

$$
M_x=E_{xx}-E_{tt},\qquad M_y=E_{yy}-E_{tt},\qquad M_z=E_{zz}-E_{tt},
$$

and the group $S_3$ that permutes $\vec e_x$, $\vec e_y$ and $\vec e_z$ permutes the three of them. The trace direction is not one of them. It is their sum:

$$
M_x+M_y+M_z=\operatorname{diag}(-3,1,1,1)=D .
$$

So the basis element that carries the broken direction is a recombination of the frame, not a member of it. That is the point of the change: above the breaking the frame does not name the lepton line, and below the breaking the lepton line appears as a sum.

This article proves that such a frame exists in $\mathfrak{su}(4)$ and cannot exist in $\mathfrak{su}(3)$, states exactly what is and is not broken, and records the one cost of the choice. Three qualifications belong in the introduction because they are easy to overstate.

The object is a basis of the Cartan, three of the fifteen generators. It is not a basis of the full algebra, which needs the twelve off-diagonal arrays as well.

The permutation is spatial. The labels $x$, $y$ and $z$ are the three vector units of the algebra, so $S_3$ here is a relabelling of three directions in space, not an internal symmetry. It is not gauged and nothing is spontaneously broken by it.

The symmetry that is lost is a symmetry of the frame, not of the representation. The eight-dimensional adjoint of $\mathfrak{su}(3)$ is a perfectly good $S_3$-module. What fails is the existence of a basis adapted to it. Section *The Eight* proves this in two independent ways.

## The Permutation Is Spatial

The fifteen generators are indexed by the six unordered pairs of four lines, $(\epsilon_t,\epsilon_x,\epsilon_y,\epsilon_z)$. One of the four lines is the scalar direction, $\epsilon_t$, and three are the vector directions of the algebra, $\epsilon_x,\epsilon_y,\epsilon_z$, which the corpus elsewhere calls the colours.

The group $S_3$ acts by permuting the three vector labels and fixing $\epsilon_t$. On the arrays it acts by conjugation with the corresponding permutation matrix, and the twelve off-diagonal arrays are permuted among themselves. On the diagonal it acts on the three colour entries and leaves the $t$ entry alone.

The reason $\epsilon_t$ sits outside the permutation is not aesthetic. It is structural, and Section *What Makes the Triple Traceless* shows that the symmetric frame is possible in $\mathfrak{su}(4)$ and not in $\mathfrak{su}(3)$ for exactly this reason.

## The Symmetric Triple

The three arrays are two-cell arrays with entries $\pm1$:

$$
M_x=\operatorname{diag}(-1,1,0,0),\qquad M_y=\operatorname{diag}(-1,0,1,0),\qquad M_z=\operatorname{diag}(-1,0,0,1),
$$

in the order $(t,x,y,z)$. Each is traceless, each is anti-Hermitian after multiplication by $i$, so

$$
G_j=iM_j,\qquad j=x,y,z,\qquad \operatorname{tr}\bigl(G_j^{\dagger}G_j\bigr)=2,
$$

lies in $\mathfrak{su}(4)$. **The $G_j$ are the printed generators; the canonical Hermitian $t_j$ of §*The Normalisation* are a further step and carry a different normalisation.**

The set is closed under the six permutations of the three vector labels. A transposition of two vector labels exchanges the corresponding two arrays and fixes the third, so every image of every element is again an element. Verified by conjugation with all six permutation matrices.

The three are independent. In the order written the matrix of rows is unit lower triangular, so its rank is $3$: verified exactly, rank $3$.

Their Gram matrix is

$$
\operatorname{tr}\bigl(M_jM_k\bigr)=2\delta_{jk}+\bigl(1-\delta_{jk}\bigr),
$$

that is $2$ on the diagonal and $1$ off it. The three directions are at $60^\circ$ to each other, all of the same length. This obliqueness is the one cost of the frame, and Section *The Normalisation* deals with it.

The sum is the trace direction:

$$
M_x+M_y+M_z=D=\operatorname{diag}(-3,1,1,1),\qquad |D|^2=12 .
$$

Verified exactly. The coefficient is $+1$, not $-\tfrac13$: the sum of the frame is the vacuum direction itself, written with the same integers as the twelve arrays.

## What Makes the Triple Traceless

Look at one element, $M_x=\operatorname{diag}(-1,1,0,0)$. Its three colour entries are $+1$, $0$ and $0$. The entry on $\epsilon_t$ is $-1$. Nothing in the colour block forces the total to vanish; the $-1$ on the fourth line does.

This is the whole mechanism, and it is easiest to see by removing the fourth line. In $\mathfrak{su}(3)$ the analogous object is the democratic triple

$$
\operatorname{diag}(1,1,-2),\qquad \operatorname{diag}(1,-2,1),\qquad \operatorname{diag}(-2,1,1),
$$

obtained by putting the odd entry on each of the three lines in turn. Its three elements are permuted by $S_3$, they are traceless, and each has the same length. But they sum to zero:

$$
\operatorname{diag}(1,1,-2)+\operatorname{diag}(1,-2,1)+\operatorname{diag}(-2,1,1)=0 .
$$

So the three are dependent, and their span is two-dimensional. Verified: the rank is $2$, while the $\mathfrak{su}(3)$ Cartan has dimension $2$, so a spanning set of this shape exists and a basis does not.

The general statement is this. Let $v=(v_t,\alpha,\beta,\beta)$ be a traceless diagonal in the fifteen, with the odd entry $\alpha$ on one vector line and $\beta$ on the other two. Its orbit under $S_3$ has size three, because its stabiliser is the transposition of the two equal lines, of order two. The orbit is $\{v_x,v_y,v_z\}$ with $v_x=v$, and

$$
\langle v_x,v_y\rangle=v_t^2+2\alpha\beta+\beta^2 .
$$

Tracelessness gives $\alpha+v_t+2\beta=0$, and substituting,

$$
v_t^2-2\beta v_t-3\beta^2=(v_t-3\beta)(v_t+\beta)=0 .
$$

So a size-three orbit is orthogonal exactly in two families, $v_t=-\beta$ and $v_t=3\beta$. Delete the fourth line, as in $\mathfrak{su}(3)$, and $v_t$ has nowhere to live: the constraint becomes $\alpha+2\beta=0$, the sum of the orbit vanishes and the rank drops to $2$. **The fourth line is not a decoration. It is what makes the symmetric triple a basis.**

## The Orthogonal Sibling

Two integer triples come out of the factorisation. With $v_t=-\beta$ and $\beta=1$,

$$
A_x=(-1,-1,1,1),\qquad A_y=(-1,1,-1,1),\qquad A_z=(-1,1,1,-1),
$$

which is the three colour words $W_{jj}=\mathbb 1-2E_{tt}-2E_{jj}$ already used in the corpus. With $v_t=3\beta$ and $\beta=1$,

$$
(3,-5,1,1),\qquad (3,1,-5,1),\qquad (3,1,1,-5),
$$

whose sum is $-3D$ and whose elements have norm $36$.

Both are orthogonal, $4\,\mathbb 1$ and $36\,\mathbb 1$ respectively. So the symmetric triple comes in two shapes, and only the first has unit entries and a sum equal to $D$ with coefficient $+1$. Verified:

$$
\operatorname{tr}\bigl(A_jA_k\bigr)=4\delta_{jk},\qquad \sum_j A_j=D,\qquad |A_j|^2=4 .
$$

The two frames are integer images of one another. Multiplying out,

$$
A_j=\sum_k M_k-2M_j ,
$$

that is, $A$ is obtained from $M$ by the integer matrix $J-2\mathbb 1$, which is invertible with eigenvalue $-1$ on the sum direction and $+1$ on the other two. Verified for all three $j$.

So the corpus has a choice of two pictures of the same three-dimensional space, and the choice is worth stating once:

| frame | elements | norm² | Gram | sum | $\operatorname{tr}(t_at_b)$ |
| --- | --- | --- | --- | --- | --- |
| $M$ | $E_{jj}-E_{tt}$ | $2$ | $2\,\mathbb 1$ with $1$ off | $D$ | $\tfrac12\delta_{jk}+\tfrac14(1-\delta_{jk})$ |
| $A$ | $W_{jj}$ | $4$ | $4\,\mathbb 1$ | $D$ | $\tfrac12\delta_{jk}$ |

The frame adopted for the fifteen is $M$, because its arrays have the same width and the same norm as the twelve off-diagonal arrays: two cells, unit entries, norm $2$. The orthogonal form is $A$, related by the integer matrix above, and it is the form in which the trace form is diagonal.

## The Eight

The claim is that no basis of the eight generators of $\mathfrak{su}(3)$ can be permuted by $S_3$ acting on the three lines. The proof does not use the diagonal at all in its first form, and uses only the diagonal in its second.

First form, by characters. The trace of the permutation matrix on three lines is $3$ for the identity, $1$ for a three-cycle and $2$ for a transposition, because the cycle has no fixed point and the transposition fixes one line. On the adjoint of $\mathfrak{su}(n)$ the character is $|\operatorname{tr}g|^2-1$. Verified:

| group | identity | three-cycle | transposition |
| --- | --- | --- | --- |
| $S_3$ on $\mathfrak{su}(3)$ | $8$ | $0$ | $-1$ |
| $S_3$ on $\mathfrak{su}(4)$, $t$ fixed | $15$ | $3$ | $0$ |

With the three irreducible representations of $S_3$ of dimensions $1$, $1$ and $2$, characters $(1,1,1)$, $(1,-1,1)$ and $(2,0,-1)$, the multiplicities solve

$$
\mathfrak{su}(3):\quad a+b+2c=8,\quad a-b=0,\quad a+b-c=-1,
$$

giving $(a,b,c)=(1,1,3)$ and

$$
\mathbf 8=\mathbf 1\oplus\mathbf 1'\oplus 3\cdot\mathbf 2 ;
$$

and

$$
\mathfrak{su}(4):\quad a+b+2c=15,\quad a-b=3,\quad a+b-c=0,
$$

giving $(a,b,c)=(4,1,5)$ and

$$
\mathbf{15}=4\cdot\mathbf 1\oplus\mathbf 1'\oplus 5\cdot\mathbf 2 .
$$

Now suppose a set of eight elements of $\mathfrak{su}(3)$ is permuted by $S_3$. It spans a permutation module, whose trivial multiplicity equals the number of orbits. That multiplicity is $1$, so there is exactly one orbit, of size $8$. But $S_3$ has orbits of size $1$, $2$, $3$ and $6$ only. Contradiction.

The same computation explains why the fifteen is not affected. Its trivial multiplicity is $4$, so at most four orbits are allowed, and

$$
6+3+3+3=15
$$

is exactly achievable: one six-element orbit and three three-element orbits. The module arithmetic checks, since a six-element orbit spans $\mathbf 1\oplus\mathbf 1'\oplus 2\cdot\mathbf 2$ and a three-element orbit spans $\mathbf 1\oplus\mathbf 2$, and

$$
\bigl(\mathbf 1\oplus\mathbf 1'\oplus 2\cdot\mathbf 2\bigr)\oplus 3\cdot\bigl(\mathbf 1\oplus\mathbf 2\bigr)
=4\cdot\mathbf 1\oplus\mathbf 1'\oplus 5\cdot\mathbf 2 .
$$

So fifteen elements can be permuted and eight cannot, and the reason is the multiplicity of the trivial representation: four against one.

Second form, by the diagonal alone. The $\mathfrak{su}(3)$ Cartan has dimension $2$. A symmetric basis of it would be a two-element set closed under $S_3$, hence a single orbit of size two, hence a stabiliser of order three, hence a vector invariant under the three-cycle, hence three equal entries, hence zero by tracelessness. No such pair exists.

The stable sets that do exist all have rank two:

| representative | orbit size | stabiliser | rank |
| --- | --- | --- | --- |
| $(1,1,-2)$ | $3$ | transposition | $2$ |
| $(1,-1,0)$ | $6$ | trivial | $2$ |
| $(1,2,-3)$ | $6$ | trivial | $2$ |

Verified. So a stable set either spans the Cartan with three elements or more, never with two. **The eight cannot carry a symmetric diagonal frame, and the reason is that the traceless condition has already spent one dimension.** In $\mathfrak{su}(4)$ the Cartan has dimension three, the fourth line supplies the $-1$ that tracelessness needs, and the symmetric triple fits.

The invariant subspace makes the same point without orbits. The commutant of $S_3$ in $M_3$ is $\operatorname{span}\{\mathbb 1,J\}$, of dimension two, so tracelessness leaves one invariant direction. In $M_4$ with $t$ fixed the commutant has dimension five, so the fifteen carry four. Verified by solving the commutation conditions exactly.

## What Is Broken and What Is Not

The statements that follow from the two sections above are narrower than the phrase symmetry breaking suggests, and it is worth being precise about each.

The adjoint representation is not broken by the permutation. $\mathbf 8=\mathbf 1\oplus\mathbf 1'\oplus 3\cdot\mathbf 2$ is a decomposition into genuine submodules, and the relabelling of lines is a symmetry of the algebra throughout. Nothing forbids it and nothing removes it.

The frame is what changes, and it changes in two steps. Above $M_C$ the frame is $M$, symmetric in $x,y,z$, and the permutation acts on it without a fixed element: no member names the lepton line. Below $M_C$ the vacuum is the direction $D$, which lies on the invariant line, so it is fixed by the whole permutation. The frame adapted to the broken phase is $\{D,T^c_3,T^c_8\}$, symmetric only under the transposition of two colour lines, that is under $S_2$. The passage from $S_3$ to $S_2$ is therefore the frame's motion, and it is the content of the breaking in the diagonal sector.

No Goldstone boson follows. $S_3$ is not gauged, so its loss removes no continuous symmetry and produces no massless mode. The eleven massless generators of the broken phase come from $\operatorname{ad}(D)$ and its kernel, not from this discussion.

The eight cannot repeat the construction because a symmetric frame needs one line outside the permutation, and $\mathfrak{su}(3)$ has no fourth line. This is why the symmetric frame is a property of the four-line theory and not of its three-colour part.

## The Twelve and Their Recombination

The diagonal triple is symmetric with no recombination. The twelve off-diagonal arrays are not, and the reason is a sign.

Write $A_{bc}=E_{bc}-E_{cb}$ for a colour pair. Under the transposition of $b$ and $c$ it maps to $-A_{bc}$. Verified by conjugation:

$$
\text{swap}(x,y):\quad A_{xy}\longmapsto-A_{xy}.
$$

A set containing both $A_{xy}$ and $-A_{xy}$ is dependent over $\mathbb R$, so no real array can sit in a permuted set of twelve. Over $\mathbb C$ the repair costs nothing. The pair

$$
X=(1+i)E_{bc}-(1-i)E_{cb},\qquad -Y=-(1-i)E_{bc}+(1+i)E_{cb}
$$

is stable, with $X\mapsto-Y$ and $-Y\mapsto X$ under the transposition. Both are anti-Hermitian and traceless, and both are independent. Verified.

So a fully symmetric fifteen exists, but its off-diagonal part is the twelve recombined in complex pairs, not the twelve as printed. The diagonal part needs nothing of the kind, and that asymmetry between the two parts is worth remembering when the frame is used.

## The Normalisation

The corpus fixes the generators by

$$
t_a=\frac{iG_a}{\sqrt{2n_a}},\qquad n_a=\operatorname{tr}\bigl(G_a^{\dagger}G_a\bigr),
$$

so that the kinetic term is canonical, which requires $\operatorname{tr}(t_at_b)=\tfrac12\delta_{ab}$ and therefore requires the $G_a$ to be mutually orthogonal.

The twelve off-diagonal arrays have $n_a=2$ and are orthogonal. The frame has $n_j=2$ as well, so all fifteen printed arrays share one norm, and the canonical generators $t_j=iG_j/2=-\tfrac12M_j$ are Hermitian. But the three are not orthogonal:

$$
\operatorname{tr}\bigl(t_jt_k\bigr)=\tfrac12\delta_{jk}+\tfrac14\bigl(1-\delta_{jk}\bigr).
$$

The kinetic term is therefore not diagonal in the frame, and one rotation is needed to reach canonical form. It is the integer rotation to the orthogonal sibling:

$$
A_j=\sum_kM_k-2M_j,\qquad t^{(A)}_j=-\frac{A_j}{\sqrt{8}},\qquad \operatorname{tr}\bigl(t^{(A)}_jt^{(A)}_k\bigr)=\tfrac12\delta_{jk}.
$$

With the orthogonal form the three diagonal generators have $n_a=4$ and the twelve have $n_a=2$, so the rescaling of the structure constants $F^{c}{}_{ab}=\sqrt{n_c/2n_an_b}\,f^{c}{}_{ab}$ is not uniform across the fifteen, exactly as before the change.

The trace direction is a combination, and its coefficient is not one:

$$
t_{15}=\frac{1}{\sqrt6}\sum_{j=x,y,z}t_j,\qquad \operatorname{tr}\bigl(t_{15}t_{15}\bigr)=\tfrac12 .
$$

Verified. Every statement about $D$ survives unchanged, because those statements concern $\operatorname{ad}(D)$ and not the frame: $|D|^2=12$, the eigenvalues $0$ nine times and $\pm4i$ three times each, $32v^2=2(1-(-3))^2v^2$ and $M_X^2=16g_4^2v_C^2$. The frame is bookkeeping; the direction is physics.

## The Checks

Every number in this article was recomputed exactly, in integer and rational arithmetic. What was checked, and the outcome:

| statement | check | outcome |
| --- | --- | --- |
| $M$ closed under $S_3$ | conjugation with six permutation matrices | closed |
| $M$ independent | exact rank of the $3\times4$ row matrix | rank $3$ |
| $\sum_jM_j=D$ | exact sum | $(-3,1,1,1)$ |
| Gram of $M$ | exact | $2\delta_{jk}+(1-\delta_{jk})$ |
| $A_j=\sum_kM_k-2M_j$ | exact, three cases | holds |
| Gram of $A$ | exact | $4\delta_{jk}$ |
| orthogonal triple, both families | factorisation $(v_t-3\beta)(v_t+\beta)=0$ | holds |
| traceless minus fourth line, rank | exact | $2$ |
| characters on the eight and the fifteen | $|\operatorname{tr}g|^2-1$ | $(8,0,-1)$, $(15,3,0)$ |
| multiplicities | exact linear system | $(1,1,3)$, $(4,1,5)$ |
| invariant subspace dims | exact nullspace of commutator conditions | $1$, $4$ |
| $A_{bc}\mapsto-A_{bc}$ under transposition | conjugation | holds |
| $X\mapsto-Y$, $-Y\mapsto X$ | conjugation | holds |
| $\operatorname{tr}(t_{15}t_{15})=\tfrac12$ | exact | holds |

## Summary

Three of the fifteen generators are diagonal, and above $M_C$ they can be chosen symmetric in the three vector units:

$$
M_j=E_{jj}-E_{tt},\qquad G_j=iM_j,\qquad \sum_jM_j=D .
$$

The trace direction is not a member of the frame. It is the sum, with coefficient $+1$, so the element that carries the broken direction appears below $M_C$ as a recombination of the three and not as a distinguished member. The frame is independent, of rank three, and its Gram is $2$ on the diagonal and $1$ off it; the orthogonal sibling is the integer image $A_j=\sum_kM_k-2M_j$, with Gram $4\,\mathbb 1$ and the same sum.

The construction needs a line outside the permutation. In $\mathfrak{su}(4)$ the fourth line supplies the $-1$ that tracelessness requires, and the triple is a basis. In $\mathfrak{su}(3)$ there is no fourth line, the democratic triple sums to zero, and its rank is two. This is not an accident of one choice: the eight has one invariant direction, so a permuted set of eight would be a single orbit, and $S_3$ has no orbit of size eight. The fifteen has four invariant directions and splits as $6+3+3+3$, which is why it can be permuted and the eight cannot.

The symmetry that is lost is the frame's, not the representation's, and it is lost in two steps, from $S_3$ to $S_2$, when the vacuum direction $D$ takes its place on the invariant line. No Goldstone boson follows.

The cost of the choice is one rotation: the frame's three directions are not orthogonal, so the trace form is not diagonal on them until $A$ is used. Nothing else changes. The norm of $D$, its eigenvalues, and the two relations that fix the scales, $32v^2=2(1-(-3))^2v^2$ and $M_X^2=16g_4^2v_C^2$, are properties of the direction and survive untouched.

## Summary of Notation

| symbol | meaning |
| --- | --- |
| $E_{\mu\nu}$ | matrix unit, one at $(\mu,\nu)$, zero elsewhere |
| $\epsilon_t,\epsilon_x,\epsilon_y,\epsilon_z$ | the four lines; $t$ the scalar direction, $x,y,z$ the three vector units |
| $S_3$ | permutations of the three vector labels, fixing $t$ |
| $M_j$ | $E_{jj}-E_{tt}$, the symmetric frame, $j=x,y,z$ |
| $A_j$ | $W_{jj}=\mathbb 1-2E_{tt}-2E_{jj}$, the orthogonal sibling |
| $D$ | $\operatorname{diag}(-3,1,1,1)$, the trace direction, equal to $\sum_jM_j$ |
| $t_a$ | generators, $t_a=iG_a/\sqrt{2n_a}$ |
| $n_a$ | $\operatorname{tr}(G_a^{\dagger}G_a)$, the norm of the array |
| $\mathbf 1,\mathbf 1',\mathbf 2$ | trivial, sign and standard irreducible representations of $S_3$ |

## Further Reading

- `construction-of-the-axf-matrices-of-the-fifteen-generators.md`
- `the-counts-of-the-fifteen-sixteen-cells-six-pairs-twelve-arrays-fifteen-generators.md`
- `the-commutation-table-of-the-fifteen-generators-225-entries-105-independent-80-nonzero-and-five-rules.md`
- `the-colours-in-su4-a-coordinate-label-on-the-fifteen-not-a-charge.md`
- `the-breaking-of-the-primordial-force-and-the-mass-of-the-six-leptoquarks.md`
- `charge-quantisation-from-the-fourth-colour-one-trace-one-third.md`
- `the-lagrangian-and-the-primordial-force.md`
- `classification-of-the-bosons-in-the-su4-model-one-grid-fifteen-generators-nine-massless-six-heavy.md`
