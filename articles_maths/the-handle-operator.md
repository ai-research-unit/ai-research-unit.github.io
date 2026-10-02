
# __The Handle Operator__

## Introduction

A **handle** is a product of two discs glued to the boundary of a manifold along half of its own boundary. Attaching a $k$-handle is the elementary operation that changes the manifold — and its boundary — by one cell, and it is the operator that generates every compact manifold and every bordism. This article treats the handle attachment as an operator: its effect on the homology, its chain-level form, the cancellation of two handles, and the reading of a handle decomposition as a sequence of critical points.

The handle is the local companion of *The Surgery Operator*: a surgery is what a handle attachment does to the boundary, and every cobordism is a sequence of handle attachments. The proof that a compact manifold with boundary has a handle decomposition — and the inequalities that count the handles — is the Morse theory of a smooth function, and needs the smooth structure of Part III; this article establishes the topological operation and its homological effect, and names the differential-topological reading.

**The article assumes** the homology of a manifold and of a pair, the boundary operator, the fundamental group and cell attachments, and the intersection form, that is, *Simplicial and Singular Homology*, *CW Complexes and Cellular Approximation*, *The Fundamental Group and Covering Spaces* and *Poincaré Duality* of this Part, together with *The Surgery Operator*.

**The boundaries of the article.** The surgery classification, the $h$- and $s$-cobordism theorems and the group of homotopy spheres are *Cobordism and Surgery Theory*. The Morse-theoretic reading — the correspondence between handles and the critical points of a smooth function, the Morse inequalities and the cancellation theorems — is the differential topology of *Smooth Manifolds and Differential Topology* in Part III, and is stated here as a forward reference; the topological handle decomposition is what the article proves. The equivariant handle attachments are *Involutions on Manifolds and Equivariant Surgery*. No smooth function, no derivative and no analysis is used.

## The Handle Operator

**Definition.** Let $W$ be a compact $n$-manifold with boundary and let $0 \leq k \leq n$. A **$k$-handle attachment** to $W$ is the operation of forming
$$
W' = W \cup_{\varphi} \bigl(D^k\times D^{n-k}\bigr), \qquad \varphi : S^{k-1}\times D^{n-k}\longrightarrow \partial W,
$$
where $\varphi$ is an embedding of the **attaching region** into the boundary; the disc $D^k\times D^{n-k}$ is the **handle** $h^k$, its core is $D^k\times\{0\}$, its **attaching sphere** is $\varphi(S^{k-1}\times\{0\})$, and its **belt sphere** is $\{0\}\times S^{n-k-1}\subseteq \partial W'$. The **handle operator** is the assignment $H^k_\varphi : [W]\mapsto[W']$.

**Proposition (the result is a manifold and the boundary is surgered).** The space $W'$ is a compact $n$-manifold with boundary, and its boundary is obtained from $\partial W$ by the surgery that removes the attaching region $S^{k-1}\times D^{n-k}$ and glues in $D^k\times S^{n-k-1}$:
$$
\partial W' = \bigl(\partial W \setminus \varphi(S^{k-1}\times\operatorname{int}D^{n-k})\bigr)\cup_{\varphi} \bigl(D^k\times S^{n-k-1}\bigr).
$$
Consequently the handle operator on a bordism induces the surgery operator on its boundary, and conversely every surgery of a boundary is realised by a handle attachment.

**Proof.** The handle $D^k\times D^{n-k}$ has boundary $S^{k-1}\times D^{n-k}\cup D^k\times S^{n-k-1}$; the first piece is glued to the boundary of $W$ by the embedding $\varphi$, and the gluing theorem for manifolds with boundary applies because $\varphi$ is an embedding of a codimension-zero submanifold of the boundary. The boundary computation is then the definition of the surgered boundary, which is exactly the operation of *The Surgery Operator*.

**Corollary (the Euler characteristic).** The Euler characteristic changes by the sign of the index,
$$
\chi(W') = \chi(W) + (-1)^k ,
$$
because the handle is attached along a cell of dimension $k$.

## The Effect on the Homology

**Proposition (the relative homology of a handle).** For the pair $(W',W)$ one has
$$
H_i(W',W;\mathbb{Z}) \;\cong\; \begin{cases}\mathbb{Z}, & i = k,\\ 0, & i\neq k,\end{cases}
$$
with generator the core of the handle, whose boundary is the attaching sphere.

**Proof.** The pair $(W',W)$ is homotopy equivalent to the pair obtained from $W$ by attaching a single $k$-cell along the attaching sphere, by the cellular approximation of the handle; the homology of a pair with one cell is the stated group.

**Theorem (the change of the homology).** In the long exact sequence of the pair,
$$
\cdots \longrightarrow H_k(W) \longrightarrow H_k(W') \longrightarrow \mathbb{Z} \xrightarrow{\ \partial\ } H_{k-1}(W) \longrightarrow H_{k-1}(W') \longrightarrow 0 ,
$$
the connecting map sends the generator to the class $A = [\varphi(S^{k-1})]\in H_{k-1}(W)$ of the attaching sphere. Hence
$$
H_i(W')\cong H_i(W)\quad (i \leq k-2,\ i\geq k+1), \qquad H_{k-1}(W')\cong H_{k-1}(W)\big/\langle A\rangle ,
$$
and $H_k(W')\cong H_k(W)\oplus\mathbb{Z}$ when $A = 0$, while $H_k(W')\cong H_k(W)$ when $A\neq0$.

**Proof.** The exact sequence comes from the pair $(W',W)$ and the identification of the relative group; the connecting homomorphism is the boundary of the core cell, which is the attaching sphere. Reading the sequence: the terms outside degrees $k-1$ and $k$ are unchanged, the cokernel of the map $\mathbb{Z}\to H_{k-1}(W)$ is $H_{k-1}(W)/\langle A\rangle$, and the kernel of that map is $\mathbb{Z}$ or $0$ according as $A = 0$ or not, which is the statement about $H_k(W')$.

**Corollary (the handle operator on the chain complex).** The chain complex of $W'$ is the **elementary expansion** of the chain complex of $W$ by generators $e_k,e_{k-1}$ with $\partial e_k = e_{k-1} + c_A$, where $c_A$ is a chain representing the attaching class; the inverse operation is the **elementary collapse**. Two manifolds are related by handle attachments and cancellations exactly when their chain complexes are related by elementary expansions and collapses.

**Proof.** The cellular chain complex of the handle relative to $W$ is $\mathbb{Z}\langle e_k\rangle$ with $\partial e_k = c_A$, and the statement is the algebraic shadow of the geometric operation; it is the same algebra as the elementary expansion of *The Surgery Operator*, shifted by one degree.

**Example (attaching a $0$-handle).** A $0$-handle is a disc $D^n$ attached along the empty set; attaching it to $W$ enlarges $W$ by a disc and changes $H_0$ by $\mathbb{Z}$, the statement that a $0$-handle creates a component. The boundary gains the belt sphere $\{0\}\times S^{n-1} = S^{n-1}$, so a $0$-handle adds a spherical boundary component.

**Example (attaching a $1$-handle and a $2$-handle).** A $1$-handle $D^1\times D^{n-1}$ is attached along two discs $S^0\times D^{n-1}$, and on the boundary it removes the two discs and glues in the band $D^1\times S^{n-2} = [-1,1]\times S^{n-2}$, joining the two boundary spheres and reducing the number of boundary components by one. A $2$-handle $D^2\times D^{n-2}$ attached along a framed circle is the elementary operation of the Kirby calculus: on the boundary it is the surgery on a circle, and it changes $H_1$ of the boundary by killing the class of the attaching curve and creating the dual class. The handle decomposition of a closed surface by one $0$-handle, $2g$ $1$-handles and one $2$-handle is the standard example.

## Cancellation and Decomposition

**Definition.** A handle decomposition of a compact manifold $W$ is a filtration
$$
\emptyset = W_{-1}\subseteq W_0\subseteq W_1\subseteq\cdots\subseteq W_n = W
$$
in which $W_k$ is obtained from $W_{k-1}$ by attaching $k$-handles. The **number of handles of index $k$** is written $c_k$.

**Theorem (existence of a handle decomposition).** Every compact piecewise-linear or smooth manifold with boundary, and every cobordism between closed manifolds, admits a handle decomposition; the decomposition can be chosen in increasing order of the indices, and each handle of index $k$ is attached to the boundary of the union of the handles of index at most $k-1$.

**Proof sketch.** The topological input is the existence of a triangulation or a "handlebody structure" for a compact manifold with boundary; the standard proof constructs the handles by thickening a cell decomposition of the manifold, dual to a triangulation. The statement in the smooth category is equivalent to the existence of a Morse function, and its proof is Part III; the topological existence is the one used here.

**Theorem (cancellation of handles).** Let $h^k$ and $h^{k+1}$ be handles of consecutive indices, with $h^{k+1}$ attached after $h^k$. Then $h^k$ and $h^{k+1}$ cancel — the union can be replaced, up to homeomorphism fixing the rest, by a smaller union with neither handle — if the attaching sphere of $h^{k+1}$ meets the belt sphere of $h^k$ transversely in exactly one point.

**Proof sketch.** If the two spheres meet once, one can slide the attaching sphere of the higher handle over the lower one until it becomes a standard sphere in the boundary sphere of $h^k$ and cancel; the slide is realised by an isotopy of the attaching map. The condition is also necessary for the cancellation of a pair in the simplest form. The full treatment is in *Cobordism and Surgery Theory*.

**Corollary (the number of handles).** A compact manifold with a handle decomposition with $c_k$ handles of index $k$ satisfies
$$
c_k \;\geq\; b_k(W) \quad \text{and} \quad c_k - c_{k-1} + c_{k-2} - \cdots \pm c_0 = \chi(W)
$$
for every $k$, since the handle decomposition is a CW structure and its chain complex computes the homology; the inequalities are the **Morse inequalities** of the topological decomposition.

## The Morse-Theoretic Reading (Forward Reference)

The correspondence between the handle operator and the critical points of a function is what makes the handle decomposition computable, and it belongs to the differential topology of Part III.

**Statement (Part III).** Let $f : W\to\mathbb{R}$ be a smooth function on a compact manifold with boundary whose critical points are nondegenerate and whose boundary values are regular. Then $f$ determines a handle decomposition of $W$ in which each critical point of index $k$ corresponds to one $k$-handle, and conversely. In particular the number of handles of index $k$ is the number of critical points of index $k$, the Morse inequalities of *Smooth Manifolds and Differential Topology* bound those numbers by the Betti numbers, and the cancellation of a handle pair corresponds to the elimination of a critical pair. The existence of the handle decomposition and the inequalities stated above are the topological shadow.

**Remark (why the reading is deferred).** The statement uses a smooth function, its derivative and its Hessian, none of which is available in this Part; what is available is the topological handlebody, and the two agree because a handle decomposition can be "smoothed" once a smooth structure exists. The present article therefore states the handle operator and its homological effect without the calculus, and names the reading as the source of the Morse inequalities in Part III.

## Examples and Applications

**Example (the sphere and the ball).** The sphere $S^n$ has the handle decomposition with one $0$-handle and one $n$-handle, obtained by attaching $D^n$ to a point; the belt sphere of the $n$-handle is a point and the attaching sphere of the $0$-handle is empty. The ball $D^n$ is a single $0$-handle, and its boundary is the empty result of a $0$-handle, consistent with the boundary formula.

**Example (the genus-$g$ surface).** The genus-$g$ surface has a handle decomposition with one $0$-handle, $2g$ $1$-handles and one $2$-handle; the $1$-handles give the $2g$ generators of $H_1$ and the $2$-handle kills their sum, so $H_1\cong\mathbb{Z}^{2g}$, $H_0\cong H_2\cong\mathbb{Z}$, and $\chi = 1-2g+1 = 2-2g$, the correct Euler characteristic. The example shows the handle count and the homology together.

**Example (a $3$-dimensional surgery and the Kirby calculus).** In the Kirby calculus a closed $3$-manifold is described by a framed link in $S^3$, and the calculus is generated by two moves: the handle slide and the blow-up; both are handle-operations on a $4$-dimensional handlebody whose boundary is the $3$-manifold. The moves are the handle operator in the ambient four-manifold, and their effect on the boundary homology is the surgery formula; the application to lens spaces and to the classification is *Low-Dimensional Topology* and *Lens Spaces*.

**Example (the $h$-cobordism theorem, named).** A cobordism between closed manifolds of dimension at least five which is an $h$-cobordism — both inclusions are homotopy equivalences — admits a handle decomposition with only handles that can be cancelled, and the cancellation uses the Whitney trick in the middle dimension; the conclusion that the cobordism is a product is the $s$-cobordism theorem, and it is *Cobordism and Surgery Theory*. The handle operator is the elementary input, and the Whitney trick is the differential-topological input of Part III.

## Summary

A $k$-handle is the disc $D^k\times D^{n-k}$ attached to the boundary of a compact manifold along the attaching region $S^{k-1}\times D^{n-k}$; the handle operator carries a manifold to the manifold with the handle attached, changes the boundary by the surgery on the attaching sphere, and increases the Euler characteristic by $(-1)^k$. Its relative homology is $\mathbb{Z}$ in degree $k$ and zero elsewhere, so the long exact sequence of the pair shows that the homology is unchanged except in degrees $k-1$ and $k$, where the attaching class $A$ is killed or a free $\mathbb{Z}$ is created; on the chain complex the operator is an elementary expansion with a collapse as its inverse. Every compact manifold and every cobordism has a handle decomposition, two consecutive handles cancel when the attaching sphere of the higher meets the belt sphere of the lower once, and the handle counts satisfy the Morse inequalities and compute the Euler characteristic. The correspondence between handles and the critical points of a smooth function, and the analytic content of the cancellation, is the differential topology of Part III and is named as the Morse-theoretic reading.

## Summary of Notation

| Symbol | Meaning |
|---|---|
| $W$, $W' = W\cup_\varphi(D^k\times D^{n-k})$ | a compact manifold with boundary and its handle attachment |
| $h^k = D^k\times D^{n-k}$ | the $k$-handle, an index-$k$ handle |
| $\varphi : S^{k-1}\times D^{n-k}\to\partial W$ | the attaching map onto the attaching region |
| attaching sphere, belt sphere | $\varphi(S^{k-1}\times\{0\})\subseteq\partial W$ and $\{0\}\times S^{n-k-1}\subseteq\partial W'$ |
| $H^k_\varphi$ | the handle operator, $[W]\mapsto[W']$ |
| $\partial W'$ | the boundary of $W'$, the surgery of $\partial W$ along the attaching sphere |
| $H_i(W',W)\cong\mathbb{Z}$ at $i=k$ | the relative homology of the handle |
| $A = [\varphi(S^{k-1})]\in H_{k-1}(W)$ | the class killed in degree $k-1$; the free $\mathbb{Z}$ in degree $k$ if $A=0$ |
| $\chi(W') = \chi(W)+(-1)^k$ | the change of the Euler characteristic |
| elementary expansion / collapse | the chain-level form of the handle operator |
| $c_k$, Morse inequalities | the number of $k$-handles and the bounds $c_k\geq b_k$, $\sum(-1)^kc_k = \chi$ |

## Further Reading

- John Milnor, *Lectures on the $h$-Cobordism Theorem* (Princeton University Press, 1965), for the handle decomposition, the cancellation and the Whitney trick.
- Stephen Smale, "On the Structure of Manifolds", *American Journal of Mathematics* 84 (1962), 387–399, for the handlebody theory and the $h$-cobordism theorem.
- Morris Hirsch, *Differential Topology* (Springer, 1976), for the Morse-theoretic reading and the equivalence with handle decompositions.
- John Milnor, *Morse Theory* (Princeton University Press, 1963), for the critical points, the index and the Morse inequalities of Part III's reading.
- Robion Kirby, "A Calculus for Framed Links in $S^3$", *Inventiones Mathematicae* 45 (1978), 35–56, for the handle moves of the Kirby calculus.
- Andrew Ranicki, *Algebraic and Geometric Surgery* (Oxford University Press, 2002), for the elementary expansion and collapse and the algebraic handle theory.
- C. T. C. Wall, *Surgery on Compact Manifolds* (Academic Press, 1970), for the handle operators in the surgery classification and the middle-dimensional cancellations.
